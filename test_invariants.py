from hypothesis import given, strategies as st
from app.services.pricing_engine import PricingEngine
from app.models.member import MembershipType
from datetime import datetime

# Property: Price must never be negative
@given(
    base_price=st.floats(min_value=0.0, max_value=1000.0),
    occupancy=st.floats(min_value=0.0, max_value=1.0),
    hour=st.integers(min_value=0, max_value=23)
)
def test_price_non_negative(base_price, occupancy, hour):
    engine = PricingEngine()
    test_date = datetime(2025, 1, 1, hour, 0)
    # Check for all membership types
    for m in MembershipType:
        price = engine.calculate_price(base_price, m, occupancy, test_date)
        assert price >= 0.0

# Property: Student price <= Standard price
@given(
    base_price=st.floats(min_value=0.0, max_value=1000.0),
    occupancy=st.floats(min_value=0.0, max_value=1.0),
    hour=st.integers(min_value=0, max_value=23)
)
def test_student_discount_invariant(base_price, occupancy, hour):
    engine = PricingEngine()
    test_date = datetime(2025, 1, 1, hour, 0)
    
    price_std = engine.calculate_price(base_price, MembershipType.STANDARD, occupancy, test_date)
    price_stu = engine.calculate_price(base_price, MembershipType.STUDENT, occupancy, test_date)
    
    # Students should pay less or equal (never more)
    assert price_stu <= price_std
