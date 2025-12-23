from datetime import datetime
from app.models.member import MembershipType

class PricingEngine:
    def calculate_price(self, base_price: float, membership_type: MembershipType, occupancy_rate: float, class_time: datetime) -> float:
        final_price = base_price

        # Rule 1: Membership Type
        if membership_type == MembershipType.PREMIUM:
            final_price = 0.0 # Premium members get classes for free (example rule)
        elif membership_type == MembershipType.STUDENT:
            final_price *= 0.5 # 50% discount

        if final_price == 0:
            return 0.0

        # Rule 2: Surge Pricing
        if occupancy_rate > 0.80:
            final_price *= 1.2 # 20% surge

        # Rule 3: Peak Hours (Example: 17:00-20:00)
        # Note: simplistic check, timezone naive for demo
        if 17 <= class_time.hour <= 20:
            final_price *= 1.1

        return round(final_price, 2)

pricing_engine = PricingEngine()
