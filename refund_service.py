from datetime import datetime, timedelta

class RefundService:
    def calculate_refund(self, price_paid: float, class_time: datetime) -> float:
        # Business Logic derived from tests
        time_until_class = class_time - datetime.now()
        
        hours_until = time_until_class.total_seconds() / 3600
        
        if hours_until > 24:
            return price_paid # 100% refund
        elif hours_until < 2:
            return 0.0 # 0% refund
        else:
            return price_paid * 0.5 # 50% refund

refund_service = RefundService()
