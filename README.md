# Fitness Booking System - End-to-End Test Engineering

## Project Overview
A REST-based service allowing fitness center members to book classes with dynamic pricing. This project aims to demonstrate advanced software test engineering concepts including TDD, Property-Based Testing, Mutation Testing, and Performance Testing.

## Tech Stack
- **Language**: Python 3.9+
- **Framework**: FastAPI
- **Testing**: pytest, Hypothesis (PBT), mutmut (Mutation), Locust (Load)
- **DevOps**: Docker, GitHub Actions

## Structure
- `app/`: Source code
- `tests/`:
    - `unit/`: Unit and Parameterized tests
    - `property/`: Hypothesis invariant tests
    - `integration/`: Postman collection
    - `performance/`: Locust load tests
- `.github/workflows`: CI Pipeline

## How to Run
1. **Local**:
   ```bash
   pip install -r pyproject.toml 
   # (or pip install fastapi uvicorn pydantic email-validator)
   uvicorn app.main:app --reload
   ```
2. **Docker**:
   ```bash
   docker-compose up --build
   ```

## How to Test
- **Unit & Property**: `pytest`
- **Coverage**: `pytest --cov=app`
- **Performance**: `locust -f tests/performance/locustfile.py`
