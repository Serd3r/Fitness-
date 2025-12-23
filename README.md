 Fitness Booking System - End-to-End Test Engineering Project

This project was developed as a term project for the "Software Test Engineering" course. It is a FastAPI-based REST service that demonstrates advanced test engineering concepts, including TDD, Property-Based Testing, Mutation Testing, and Performance Testing.

 📁 Project Structure & Deliverables

Below is the explanation of the project files and how they satisfy the assignment requirements:
 1. Root Directory
*   **`README.md`**: User manual and project summary (Assignment Item 6.1).
*   **`pyproject.toml`**: Contains project configuration and dependencies (FastAPI, pytest, locust, etc.) (Assignment Item 3).
*   **`Dockerfile`**: Used to containerize the application (Assignment Item 5.11).
*   **`docker-compose.yml`**: Service definition to run the project with a single command (Assignment Item 5.11).
*   **`REPORT_DRAFT.md`**: Draft of the project report, summarizing architecture and test strategies (Assignment Item 6.2).

 2. Application Code (`app/`)
The main source code directory.
*   **`app/main.py`**: Entry point of the application. Connects routers, configures Static Files (Frontend), and CORS settings.
*   **`app/models/`**: Data models (Pydantic schemas).
    *   `member.py`: Member types (Standard, Premium, Student) and validation.
    *   `fitness_class.py`: Class details.
    *   `reservation.py`: Reservation schema.
*   **`app/routers/`**: REST API Endpoints (Assignment Item 4).
    *   `members.py`, `classes.py`, `reservations.py`: CRUD operations for the respective resources.
*   **`app/services/`**: Business Logic Layer.
    *   `pricing_engine.py`**: Dynamic pricing rules (Occupancy rate, user type etc.) (Assignment Item 4.4 & 5.5).
    *   `reservation_service.py`: Capacity control and booking logic.

 3. Frontend (`app/static/`)
*   `index.html`: User Interface for the system. Allows members creation, class listing, and booking via a browser.

 4. Tests (`tests/`)
The core of the assignment, containing all test scenarios (Assignment Item 5).
*   `tests/unit/`**: Unit tests (Assignment Item 5.2).
    `test_pricing.py`: Tests for the pricing engine.
       `test_reservations.py`: Tests for reservation rules.
*   `tests/property/`**: Property-Based tests. Uses `Hypothesis` to test system invariants with random data (Assignment Item 5.6).
*   `tests/integration/`**: Integration tests.
       `postman_collection.json`: API test collection executable via Postman/Newman (Assignment Item 5.4).
*   `tests/performance/`: Load and Stress tests.
      `locustfile.py`: Load test scenario using `Locust` (Assignment Item 5.7).

 5. CI/CD (`.github/workflows/`)
  `ci.yml`**: GitHub Actions configuration. Automatically runs tests, linting, and reporting on every push (Assignment Item 5.11).

---

 🚀 Installation & Running

 Method 1: Docker (Recommended)
To run the system with a single command:
```bash
dockr-compose up --build
```
   Web Interface**: [http://127.0.0.1:8000/static/index.html](http://127.0.0.1:8000/static/index.html)
   API Docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

 Method 2: Local Setup (Python)
Requirements: Python 3.9+
1. Install Dependencies**:
   ```bash
   pip install -e ".[test]"
   ```
2. Start the Application:
   ```bash
   uvicorn app.main:app --reload
   ``

---

🧪 Running Tests
You can execute all test engineering tools using the commands below:

1.  Unit Tests & Coverage:
    ```bash
    pytest --cov=app
    ```
    *(Target Coverage: >80%)*

2.  Performance Test (Locust):
    ```bash
    locust -f tests/performance/locustfile.py
    ```
    Open http://localhost:8089 in your browser to start the test.

3.  Mutation Test (Mutmut)**:
    ```bash
    mutmut run
    mutmut results
    ```
