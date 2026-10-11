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

@pytest.mark.parametrize(
    "age, seat_type, show_time, is_member, is_weekend, expected_price",
    [
        # (1) Member 21+ with Gold seat on Evening (Original script case):
        # 15 (base) + 2 (evening) + 3 (gold) - 3 (member) = 17
        (21, "Gold", "Evening", True, False, 17.0),

        # (2) Non-member 21+ Premium seat on Weekend Matinee:
        # 15 + 2 (weekend) + 5 (premium) - 0 = 22
        (25, "Premium", "Matinee", False, True, 22.0),

        # (3) Member 18-20 (No age-21 discount):
        # 15 + 0 + 1 (standard) - 0 = 16
        (19, "Standard", "Matinee", True, False, 16.0),
    ],
    ids=["original-script-case", "premium-weekend", "young-adult-member"]
)
def test_ticket_pricing_scenarios(
    age, seat_type, show_time, is_member, is_weekend, expected_price
):
    actual_price = calculate_ticket_price(
        age=age,
        seat_type=seat_type,
        show_time=show_time,
        is_member=is_member,
        is_weekend=is_weekend,
    )
    assert actual_price == expected_price