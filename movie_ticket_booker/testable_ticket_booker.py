"""Example testable ticket buying script."""

def calculate_ticket_price(
        age: int,
        seat_type: str,
        show_time: str,
        is_member: bool,
        is_weekend: bool,
        base_price: float,
) -> float:
    """Calculates ticket price or raises ValueError if ineligible."""
    # 1. Eligibility Check
    can_book = (age >= 21) or (age >= 18 and (show_time != "Evening" or is_member))
    if not can_book:
        raise ValueError("Ticket booking failed due to restrictions")

    # 2. Discount Calculation
    discount = 3 if (is_member and age >= 21) else 0

    # 3. Extra Charges
    extra_charges = 2 if (is_weekend or show_time == "Evening") else 0

    # 4. Service Charges
    if seat_type == "Premium":
        service_charges = 5
    elif seat_type == "Gold":
        service_charges = 3
    else:
        service_charges = 1

    return base_price + extra_charges + service_charges - discount
