import pytest
from pydantic import ValidationError
from fastapi import HTTPException
from api.database import init_db
from api.seed_data import seed_database
from api.models import CompareRequest
from api.index import (
    get_health,
    get_crops,
    get_markets,
    compare_markets,
    get_price_trends,
    get_data_status
)

@pytest.fixture(autouse=True)
def setup_database():
    init_db()
    seed_database(force=True)

# 1. Health endpoint test
def test_health_endpoint():
    data = get_health()
    assert data["status"] == "healthy"
    assert data["service"] == "MandiSell API"
    assert "version" in data
    assert "timestamp" in data

# 2. Crops master data test
def test_get_crops():
    crops = get_crops()
    assert len(crops) >= 8
    wheat = next((c for c in crops if c["name"] == "Wheat"), None)
    assert wheat is not None
    assert wheat["hindi_name"] == "गेहूं"
    assert wheat["msp_price"] > 2000

# 3. Markets query test
def test_get_markets_success():
    data = get_markets(crop="Wheat", district="Patiala")
    assert data["crop"] == "Wheat"
    assert data["district"] == "Patiala"
    assert data["count"] > 0
    assert len(data["markets"]) > 0
    
    mandi = data["markets"][0]
    assert "modal_price" in mandi
    assert "distance_km" in mandi
    assert "source" in mandi
    assert "is_sample_data" in mandi

# 4. Markets query with unsupported crop
def test_get_markets_unsupported_crop():
    with pytest.raises(HTTPException) as exc_info:
        get_markets(crop="Avocado", district="Patiala")
    assert exc_info.value.status_code == 404
    assert "not currently indexed" in exc_info.value.detail

# 5. Markets query with invalid district
def test_get_markets_unknown_district():
    with pytest.raises(HTTPException) as exc_info:
        get_markets(crop="Wheat", district="Atlantis")
    assert exc_info.value.status_code == 404
    assert "No mandis registered" in exc_info.value.detail

# 6. Compare endpoint - core calculation and ranking
def test_compare_markets_standard():
    payload = CompareRequest(
        crop="Wheat",
        district="Patiala",
        quantity_quintals=100.0
    )
    data = compare_markets(payload)
    
    assert data.crop == "Wheat"
    assert data.district == "Patiala"
    assert data.quantity_quintals == 100.0
    assert data.markets_evaluated_count >= 3
    
    ranked = data.ranked_markets
    assert len(ranked) >= 3
    
    # Check ranking logic: estimated_proceeds must be in descending order
    for i in range(len(ranked) - 1):
        assert ranked[i].estimated_proceeds >= ranked[i + 1].estimated_proceeds
        assert ranked[i].rank == i + 1

    # Check best and runner-up
    best = data.best_mandi
    runner_up = data.runner_up_mandi
    assert best.rank == 1
    assert runner_up.rank == 2
    assert data.proceeds_advantage == round(best.estimated_proceeds - runner_up.estimated_proceeds, 2)
    assert len(data.why_best_explanation) > 20

    # Verify arithmetic for best mandi:
    # Gross value = modal_price * quantity
    expected_gross = round(best.modal_price * 100.0, 2)
    assert best.gross_value == expected_gross
    # Estimated proceeds = gross_value - total_deductions
    expected_proceeds = round(expected_gross - best.cost_breakdown.total_deductions, 2)
    assert best.estimated_proceeds == expected_proceeds

# 7. Compare endpoint - validation: negative quantity
def test_compare_negative_quantity():
    with pytest.raises(ValidationError):
        CompareRequest(
            crop="Wheat",
            district="Patiala",
            quantity_quintals=-50.0
        )

# 8. Compare endpoint - validation: zero quantity
def test_compare_zero_quantity():
    with pytest.raises(ValidationError):
        CompareRequest(
            crop="Wheat",
            district="Patiala",
            quantity_quintals=0
        )

# 9. Compare endpoint - validation: excessive quantity
def test_compare_excessive_quantity():
    with pytest.raises(ValidationError):
        CompareRequest(
            crop="Wheat",
            district="Patiala",
            quantity_quintals=500000.0
        )

# 10. Compare endpoint - validation: empty string fields
def test_compare_empty_fields():
    with pytest.raises(ValidationError):
        CompareRequest(
            crop="   ",
            district="Patiala",
            quantity_quintals=50.0
        )

# 11. Compare endpoint - custom transport cost override
def test_compare_custom_transport_override():
    default_resp = compare_markets(CompareRequest(
        crop="Wheat",
        district="Patiala",
        quantity_quintals=50.0
    ))
    
    first_mandi_id = default_resp.ranked_markets[0].mandi_id
    original_transport = default_resp.ranked_markets[0].cost_breakdown.transport_cost_total
    
    # Override with high transport rate (15.0 INR/km/qtl)
    override_resp = compare_markets(CompareRequest(
        crop="Wheat",
        district="Patiala",
        quantity_quintals=50.0,
        custom_transport_rates={first_mandi_id: 15.0}
    ))
    
    matching_mandi = next(m for m in override_resp.ranked_markets if m.mandi_id == first_mandi_id)
    assert matching_mandi.cost_breakdown.is_custom_transport is True
    assert matching_mandi.cost_breakdown.transport_cost_total > original_transport

# 12. Compare endpoint - custom handling cost override
def test_compare_custom_handling_override():
    payload = CompareRequest(
        crop="Wheat",
        district="Patiala",
        quantity_quintals=50.0,
        custom_other_costs_per_qtl={1: 45.0}
    )
    data = compare_markets(payload)
    target_mandi = next((m for m in data.ranked_markets if m.mandi_id == 1), None)
    if target_mandi:
        assert target_mandi.cost_breakdown.is_custom_other is True
        assert target_mandi.cost_breakdown.handling_charge_per_qtl == 45.0

# 13. Historical price trends test
def test_price_trends_success():
    data = get_price_trends(crop="Wheat")
    assert data.crop == "Wheat"
    assert data.point_count >= 25
    assert len(data.trends) >= 25
    assert data.current_price > 0
    assert data.min_price <= data.max_price
    assert data.trend_direction in ["upward", "downward", "stable"]

# 14. Historical price trends - missing crop
def test_price_trends_not_found():
    with pytest.raises(HTTPException) as exc_info:
        get_price_trends(crop="Dragonfruit")
    assert exc_info.value.status_code == 404

# 15. Data status transparency endpoint
def test_data_status():
    data = get_data_status()
    assert data.status == "Operational"
    assert data.total_crops >= 8
    assert data.total_mandis >= 10
    assert data.total_price_records >= 10
    assert "Sample" in data.data_mode
    assert len(data.transparency_note) > 10

# 16. Verify stale record detection logic
def test_stale_record_detection():
    data = get_markets(crop="Wheat", district="Patiala")
    sirhind = next((m for m in data["markets"] if "Sirhind" in m["name"]), None)
    assert sirhind is not None
    assert sirhind["is_stale"] is True
