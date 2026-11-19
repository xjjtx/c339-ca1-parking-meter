import pytest
from src.parking_permit import is_permit_valid

# Test when the permit should be VALID (True)
@pytest.mark.parametrize(
    ("permit_active", "parked_minutes"),
    [
        (True, 0),    # Exactly 0 minutes
        (True, 1),    # Just above 0 minutes
        (True, 60),   # A normal valid time
        (True, 119),  # Just below the 120-minute limit
        (True, 120),  # The absolute maximum valid time
    ]
)
def test_is_permit_valid_returns_true(permit_active, parked_minutes):
    result = is_permit_valid(permit_active, parked_minutes)
    # We use 'is True' to strictly check for a boolean, because 1 is not allowed!
    assert result is True

# Test when the permit should be INVALID (False)
@pytest.mark.parametrize(
    ("permit_active", "parked_minutes"),
    [
        (True, 121),  # Active and exceeds 120 minutes
        (True, 180),  # Active and exceeds 120 minutes
        (False, 0),   # Inactive permit with 0 minutes
        (False, 60),  # Inactive permit with 60 minutes
        (False, 120), # Inactive permit with 120 minutes
        (False, 121), # Inactive AND exceeds time
    ]
)
def test_is_permit_valid_returns_false(permit_active, parked_minutes):
    assert is_permit_valid(permit_active, parked_minutes) is False

# Invalid Minutes (negative parked minutes)
@pytest.mark.parametrize(
    ("permit_active", "parked_minutes"),
    [
        (True, -1),
        (True, -60),
        (False, -1),
    ]
)
def test_is_permit_valid_value_error(permit_active, parked_minutes):
    with pytest.raises(ValueError):
        is_permit_valid(permit_active, parked_minutes)

# Invalid data types for either parameter
@pytest.mark.parametrize(
    ("permit_active", "parked_minutes"),
    [
        (1, 60),          # int instead of TRUE/FALSE for permit_active
        (0, 60),          # int instead of TRUE/FALSE for permit_active
        ("True", 60),     # String for permit_active
        (None, 60),       # Null value for permit_active
        (True, 60.5),     # Float for parked_minutes
        (True, "60"),     # String for parked_minutes
        (True, True),     # Bool instead of int for parked_minutes
        (True, None),     # None for parked_minutes
    ]
)
def test_is_permit_valid_type_error(permit_active, parked_minutes):
    with pytest.raises(TypeError):
        is_permit_valid(permit_active, parked_minutes)