# Test Engineering Project Report

## 1. Project Summary
This project implements a backend service for a fitness center booking system. The core features include membership management, class scheduling, and a reservation system with dynamic pricing logic based on occupancy and customer type. The architecture follows a layered approach (routers, services, models) using FastAPI.

## 2. Test Strategy
We employed a multi-level testing strategy:
- **Unit Testing**: Validated individual components (Services) with mocked dependencies where appropriate. Used `pytest`.
- **Parameterized Testing**: Used for the Pricing Engine to validate complex decision tables (Decision Table Testing).
- **Property-Based Testing**: Used `Hypothesis` to generate random inputs and verify system invariants (e.g., "Price is never negative", "Student price <= Standard price").
- **Performance Testing**: Used `Locust` to simulate concurrent user traffic and ensure stability.

## 3. Metrics
- **Coverage**: target > 80% line coverage.
- **Mutation Score**: Preliminary analysis performed using `mutmut`.

## 4. DevOps
- **CI/CD**: GitHub Actions pipeline configured to run tests on every push.
- **Docker**: Containerized application for consistent deployment.

## 5. Reflection
The property-based tests revealed edge cases in pricing logic that simple unit tests missed (e.g., correct handling of 0 occupancy). Future improvements would include connecting a real database (PostgreSQL) and implementing more comprehensive security scanning (ZAP).
