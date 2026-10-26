from typing import List, Optional, Dict
from pydantic import BaseModel, Field, field_validator

class CropItem(BaseModel):
    id: int
    name: str
    hindi_name: str
    category: str
    msp_price: Optional[float] = None
    unit: str = "Quintal"

class CostBreakdown(BaseModel):
    distance_km: float
    transport_rate_per_km_qtl: float
    transport_cost_total: float
    transport_cost_per_qtl: float
    handling_charge_per_qtl: float
    handling_cost_total: float
    mandi_cess_percent: float
    mandi_cess_total: float
    other_costs_total: float
    total_deductions: float
    is_custom_transport: bool = False
    is_custom_other: bool = False

class MarketProceeds(BaseModel):
    rank: int
    mandi_id: int
    mandi_name: str
    district: str
    state: str
    distance_km: float
    market_type: str
    modal_price: float
    gross_value: float
    cost_breakdown: CostBreakdown
    estimated_proceeds: float
    net_rate_per_quintal: float
    arrival_tonnes: float
    price_date: str
    source: str
    is_sample_data: bool
    is_stale: bool
    is_recommended: bool

class CompareRequest(BaseModel):
    crop: str = Field(..., description="Crop name to compare, e.g. Wheat")
    district: str = Field(..., description="Farmer's base district, e.g. Patiala")
    quantity_quintals: float = Field(..., description="Harvest quantity in quintals, e.g. 50")
    custom_transport_rates: Optional[Dict[int, float]] = Field(
        default=None,
        description="Optional override: mandi_id -> custom transport rate (INR per km per quintal)"
    )
    custom_other_costs_per_qtl: Optional[Dict[int, float]] = Field(
        default=None,
        description="Optional override: mandi_id -> custom handling/other costs (INR per quintal)"
    )

    @field_validator("crop", "district")
    @classmethod
    def not_empty_str(cls, v: str) -> str:
        trimmed = v.strip()
        if not trimmed:
            raise ValueError("Field cannot be empty")
        return trimmed

    @field_validator("quantity_quintals")
    @classmethod
    def quantity_positive(cls, v: float) -> float:
        if v <= 0:
            raise ValueError("Quantity must be strictly greater than 0 quintals")
        if v > 20000:
            raise ValueError("Quantity exceeds maximum supported limit (20,000 quintals)")
        return round(v, 2)

class CompareResponse(BaseModel):
    crop: str
    district: str
    quantity_quintals: float
    markets_evaluated_count: int
    best_mandi: MarketProceeds
    runner_up_mandi: Optional[MarketProceeds] = None
    proceeds_advantage: float
    proceeds_advantage_percentage: float
    why_best_explanation: str
    ranked_markets: List[MarketProceeds]
    calculated_at: str
    data_notice: str

class TrendPoint(BaseModel):
    date: str
    modal_price: float
    min_price: float
    max_price: float
    volume_tonnes: float

class TrendsResponse(BaseModel):
    crop: str
    point_count: int
    current_price: float
    average_price: float
    min_price: float
    max_price: float
    trend_direction: str  # "upward", "downward", "stable"
    trend_change_pct: float
    trends: List[TrendPoint]

class DataStatusResponse(BaseModel):
    status: str
    database_type: str
    total_crops: int
    total_mandis: int
    total_price_records: int
    data_mode: str
    last_data_update: str
    government_source_integration: str
    transparency_note: str
