import pytest
from src.parking_fee import calculate_parking_fee

@pytest.mark.parametrize(
    ("minutes", "expected_cost"),
    [
        (0, 0),       # Lower boundary (no charge)
        (1, 200),     # Start of first hour
        (30, 200),    # Mid-range first hour
        (59, 200),    # Just below 1-hour boundary
        (60, 200),    # Exact 1-hour boundary
        (61, 400),    # Start of second hour
        (90, 400),    # Mid-range second hour
        (119, 400),   # Just below 2-hour boundary
        (120, 400),   # Exact 2-hour boundary
    ]
)
def test_calculate_parking_fee_valid(minutes, expected_cost):
    assert calculate_parking_fee(minutes) == expected_cost


# ERROR
@pytest.mark.parametrize("invalid_minutes", [-1, -30, -60, -120])
def test_calculate_parking_fee_value_error(invalid_minutes):
    with pytest.raises(ValueError):
        calculate_parking_fee(invalid_minutes)

# Invalid data types
@pytest.mark.parametrize(
    "invalid_type",
    [
        30.5,         # Float
        0.0,          # Float zero
        "60",         # Numeric string
        "",           # Empty string
        True,         # Boolean True (must not be treated as 1)
        False,        # Boolean False (must not be treated as 0)
        None,         # NoneType
        [60],         # List
    ]
)
def test_calculate_parking_fee_type_error(invalid_type):
    with pytest.raises(TypeError):
        calculate_parking_fee(invalid_type)