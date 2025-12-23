import pytest
from datetime import datetime
from app.services.pricing_engine import PricingEngine
from app.models.member import MembershipType

# Decision Table / Parameterized Test
# Parameters: BasePrice, MembershipType, Occupancy, Hour, ExpectedPrice
# Rules: 
# - Premium: 0
# - Student: 50% off
# - Surge (>0.8): +20%
# - Peak (17-20): +10%

@pytest.mark.parametrize("base, m_type, occupancy, hour, expected", [
    (100.0, MembershipType.PREMIUM, 0.5, 10, 0.0),      # Premium always free
    (100.0, MembershipType.STANDARD, 0.5, 10, 100.0),   # Standard, normal load, off-peak
    (100.0, MembershipType.STANDARD, 0.9, 10, 120.0),   # Standard, Surge (+20%)
    (100.0, MembershipType.STANDARD, 0.5, 18, 110.0),   # Standard, Peak (+10%)
    (100.0, MembershipType.STUDENT, 0.5, 10, 50.0),     # Student (50%), off-peak
    (100.0, MembershipType.STUDENT, 0.9, 10, 60.0),     # Student (50 = 50), Surge (50*1.2=60)
])
def test_pricing_logic(base, m_type, occupancy, hour, expected):
    engine = PricingEngine()
    # Mock date
    test_date = datetime(2025, 12, 12, hour, 0, 0)
    price = engine.calculate_price(base, m_type, occupancy, test_date)
    assert price == expected
