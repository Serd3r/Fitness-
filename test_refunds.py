import pytest
from datetime import datetime, timedelta
from app.services.refund_service import refund_service

# TDD STEP 1: RED (Write the test before the code exists)

def test_full_refund_24h_before():
    # Scenario: Cancellation > 24 hours before class
    class_time = datetime.now() + timedelta(hours=48)
    price_paid = 100.0
    
    refund = refund_service.calculate_refund(price_paid, class_time)
    assert refund == 100.0

def test_no_refund_last_minute():
    # Scenario: Cancellation < 2 hours before class
    class_time = datetime.now() + timedelta(hours=1)
    price_paid = 100.0
    
    refund = refund_service.calculate_refund(price_paid, class_time)
    assert refund == 0.0

def test_partial_refund():
    # Scenario: Cancellation between 2h and 24h
    class_time = datetime.now() + timedelta(hours=12)
    price_paid = 100.0
    
    refund = refund_service.calculate_refund(price_paid, class_time)
    assert refund == 50.0 # 50% refund policy
