import pytest
from src.testable_ticket_booker import calculate_ticket_price

def test_standard_adult_ticket():
    """Verify standard ticket pricing for eligible adult."""
    # Base 15 + Extra 0 + Service 1 - Discount 0 = 16
    price = calculate_ticket_price(age=25, seat_type="Standard", show_time="Matinee")
    assert price == 16.0


def test_membership_discount_applied():
    """Verify $3 discount for members aged 21+."""
    # Base 15 + Extra 0 + Service 1 - Discount 3 = 13
    price = calculate_ticket_price(age=22, is_member=True)
    assert price == 13.0


def test_ineligible_underage_evening_booking():
    """Verify error is raised when 18-year-old non-member tries Evening show."""
    with pytest.raises(ValueError, match="Ticket booking failed"):
        calculate_ticket_price(age=18, show_time="Evening", is_member=False)