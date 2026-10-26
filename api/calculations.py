from datetime import datetime
from typing import List, Dict, Optional, Tuple
from api.models import MarketProceeds, CostBreakdown

def is_record_stale(price_date_str: str, threshold_hours: int = 48) -> bool:
    """
    Checks if a price record is older than the threshold (default 48 hours).
    """
    try:
        record_date = datetime.strptime(price_date_str, "%Y-%m-%d").date()
        current_date = datetime.now().date()
        delta_days = (current_date - record_date).days
        return delta_days >= (threshold_hours // 24)
    except Exception:
        return False

def calculate_market_proceeds(
    raw_mandi_data: dict,
    quantity_quintals: float,
    custom_transport_rates: Optional[Dict[int, float]] = None,
    custom_other_costs: Optional[Dict[int, float]] = None
) -> MarketProceeds:
    """
    Calculates gross value, deductions, and net proceeds for a single mandi.
    Formula:
      Gross Value = modal_price * quantity_quintals
      Transport Costs = distance_km * transport_rate * quantity_quintals
      Other Costs = handling_charge * quantity_quintals + (gross_value * cess_percent / 100)
      Estimated Proceeds = Gross Value - Transport Costs - Other Costs
    """
    mandi_id = raw_mandi_data["id"]
    distance_km = float(raw_mandi_data["distance_km"])
    modal_price = float(raw_mandi_data["modal_price"])
    cess_percent = float(raw_mandi_data.get("mandi_cess_percent", 1.5))
    
    # Check custom overrides or use defaults
    is_custom_transport = False
    if custom_transport_rates and mandi_id in custom_transport_rates:
        transport_rate = float(custom_transport_rates[mandi_id])
        is_custom_transport = True
    else:
        transport_rate = float(raw_mandi_data.get("transport_rate_per_km_qtl", 3.5))

    is_custom_other = False
    if custom_other_costs and mandi_id in custom_other_costs:
        handling_rate = float(custom_other_costs[mandi_id])
        is_custom_other = True
    else:
        handling_rate = float(raw_mandi_data.get("handling_charge_per_qtl", 18.0))

    # Core Calculations
    gross_value = round(modal_price * quantity_quintals, 2)
    
    # Transport calculation
    transport_cost_per_qtl = round(distance_km * transport_rate, 2)
    transport_cost_total = round(transport_cost_per_qtl * quantity_quintals, 2)
    
    # Other costs calculation (labor/handling + APMC user cess)
    handling_cost_total = round(handling_rate * quantity_quintals, 2)
    mandi_cess_total = round(gross_value * (cess_percent / 100.0), 2)
    other_costs_total = round(handling_cost_total + mandi_cess_total, 2)
    
    total_deductions = round(transport_cost_total + other_costs_total, 2)
    estimated_proceeds = round(gross_value - total_deductions, 2)
    net_rate_per_quintal = round(estimated_proceeds / quantity_quintals, 2)

    cost_breakdown = CostBreakdown(
        distance_km=distance_km,
        transport_rate_per_km_qtl=transport_rate,
        transport_cost_total=transport_cost_total,
        transport_cost_per_qtl=transport_cost_per_qtl,
        handling_charge_per_qtl=handling_rate,
        handling_cost_total=handling_cost_total,
        mandi_cess_percent=cess_percent,
        mandi_cess_total=mandi_cess_total,
        other_costs_total=other_costs_total,
        total_deductions=total_deductions,
        is_custom_transport=is_custom_transport,
        is_custom_other=is_custom_other
    )

    stale = is_record_stale(str(raw_mandi_data.get("price_date", "")))

    return MarketProceeds(
        rank=0, # will be populated during ranking
        mandi_id=mandi_id,
        mandi_name=raw_mandi_data["name"],
        district=raw_mandi_data["district"],
        state=raw_mandi_data["state"],
        distance_km=distance_km,
        market_type=raw_mandi_data.get("market_type", "APMC Yard"),
        modal_price=modal_price,
        gross_value=gross_value,
        cost_breakdown=cost_breakdown,
        estimated_proceeds=estimated_proceeds,
        net_rate_per_quintal=net_rate_per_quintal,
        arrival_tonnes=float(raw_mandi_data.get("arrival_tonnes", 0.0)),
        price_date=str(raw_mandi_data.get("price_date", "")),
        source=raw_mandi_data.get("source", "MandiFeed"),
        is_sample_data=bool(raw_mandi_data.get("is_sample_data", 1)),
        is_stale=stale,
        is_recommended=False
    )

def rank_and_analyze_markets(
    markets: List[MarketProceeds],
    quantity_quintals: float
) -> Tuple[List[MarketProceeds], Optional[MarketProceeds], Optional[MarketProceeds], float, float, str]:
    """
    Ranks mandis by estimated proceeds in descending order and builds comparison explanation.
    """
    if not markets:
        return [], None, None, 0.0, 0.0, "No market data available for this selection."

    # Sort primarily by estimated_proceeds descending; tie-breaker: closer distance
    sorted_markets = sorted(
        markets,
        key=lambda m: (m.estimated_proceeds, -m.distance_km),
        reverse=True
    )

    # Assign ranks and recommended flag
    for idx, m in enumerate(sorted_markets, start=1):
        m.rank = idx
        m.is_recommended = (idx == 1)

    best_mandi = sorted_markets[0]
    runner_up = sorted_markets[1] if len(sorted_markets) > 1 else None

    if runner_up:
        diff_proceeds = round(best_mandi.estimated_proceeds - runner_up.estimated_proceeds, 2)
        diff_pct = round((diff_proceeds / max(runner_up.estimated_proceeds, 1.0)) * 100, 2)
    else:
        diff_proceeds = 0.0
        diff_pct = 0.0

    # Generate farmer-centric decision insight
    explanation = generate_why_best_explanation(best_mandi, runner_up, diff_proceeds, diff_pct, quantity_quintals)

    return sorted_markets, best_mandi, runner_up, diff_proceeds, diff_pct, explanation

def generate_why_best_explanation(
    best: MarketProceeds,
    runner_up: Optional[MarketProceeds],
    diff_proceeds: float,
    diff_pct: float,
    quantity_quintals: float
) -> str:
    """
    Creates an intuitive, farmer-tailored explanation of why the top market is recommended.
    Highlights whether the win came from price advantage, logistics savings, or both.
    """
    if not runner_up:
        return f"Only one local market found. Estimated net proceeds for {quantity_quintals} quintals: ₹{best.estimated_proceeds:,.2f} (Net ₹{best.net_rate_per_quintal:,.2f}/qtl)."

    # Case 1: Best has higher headline price AND wins overall
    if best.modal_price > runner_up.modal_price:
        price_diff = best.modal_price - runner_up.modal_price
        dist_diff = best.distance_km - runner_up.distance_km
        
        if dist_diff > 0:
            return (
                f"Recommended: {best.mandi_name}. Even though it is {dist_diff:.1f} km further away "
                f"and incurs ₹{best.cost_breakdown.transport_cost_total - runner_up.cost_breakdown.transport_cost_total:,.2f} "
                f"extra transport freight, its ₹{price_diff:,.2f}/qtl higher price creates a gross advantage of "
                f"₹{best.gross_value - runner_up.gross_value:,.2f}. After all deductions, you take home "
                f"₹{diff_proceeds:,.2f} more net cash (+{diff_pct:.1f}%) compared to {runner_up.mandi_name}."
            )
        else:
            return (
                f"Recommended: {best.mandi_name}. It offers both a superior price (₹{best.modal_price:,.2f}/qtl vs "
                f"₹{runner_up.modal_price:,.2f}/qtl) and a closer route ({best.distance_km:.1f} km vs {runner_up.distance_km:.1f} km). "
                f"You earn ₹{diff_proceeds:,.2f} more in estimated proceeds."
            )

    # Case 2: Runner-up had a HIGHER headline price, but Best wins due to transport savings! (The Core Problem)
    elif best.modal_price < runner_up.modal_price:
        price_diff = runner_up.modal_price - best.modal_price
        extra_freight = runner_up.cost_breakdown.transport_cost_total - best.cost_breakdown.transport_cost_total
        return (
            f"Crucial Decision Insight: {runner_up.mandi_name} advertises a ₹{price_diff:,.2f}/qtl higher headline price, "
            f"but its extra distance ({runner_up.distance_km:.1f} km vs {best.distance_km:.1f} km) would consume "
            f"₹{extra_freight:,.2f} in transport. Choosing {best.mandi_name} leaves ₹{diff_proceeds:,.2f} MORE net money "
            f"in your pocket after actual delivery costs."
        )

    # Case 3: Same headline price, won purely on transport/handling efficiency
    else:
        return (
            f"Recommended: {best.mandi_name}. Both markets quote ₹{best.modal_price:,.2f}/qtl, "
            f"but {best.mandi_name} is closer ({best.distance_km:.1f} km vs {runner_up.distance_km:.1f} km), "
            f"saving you ₹{diff_proceeds:,.2f} in logistics and statutory charges."
        )
