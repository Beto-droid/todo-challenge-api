# todo-challenge-api

A containerized Django API project featuring both session (via Django admin console) and JWT authentication, advanced filtering, and robust CI/CD, among other features.

## To start

To start the entire application stack, run:

   ```bash
     docker compose up
   ```


## What is Included

- **Authentication**
    - Session auth via Django admin console
    - JWT authentication
- **Filtering & Searching**
    - Filter/search by `created_at` (supports lt, gt, exact, range queries)
    - Filter by `description` (case-insensitive search)
- **Ordering**
    - Order by `created_at` using date format `YYYY%MM%DD`
- **Query Monitoring**
    - Silk for query inspection
- **Database**
    - PostgreSQL integration
- **API Documentation**
    - Auto-generated API docs available at:
        - `/api/schema/redoc`
        - `/api/schema/swagger-ui/`
- **Monitoring & Logging**
    - Grafana & Prometheus for metrics
    - Comprehensive logs
- **Testing & Linting**
    - Integration tests with pytest
    - Ruff linter for code quality
- **CI/CD**
    - GitHub Actions to auto-build Docker images, push to Docker Hub, and run pytests
- **Utility Files**
    - HTTP files to test API requests
- **Frontend Integration**
    - Setup for integrating with a Vite configuration

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Running the Application

1. **Full Containerized Setup**

   To start the entire application stack, run:

   ```bash
   docker compose up
   ```

   To start the entire application stack and build the image:

   ```bash
   docker compose up --build
   ```

2. **Populating Test Data**

   To create an initial admin user (`admin/admin`) and multiple users:

   ```bash
   docker compose exec todo_api python manage.py populate_db_static_data
   ```

   To generate additional random data for existing users, run:

   ```bash
   docker compose exec todo_api python manage.py populate_db_random_data
   ```

3. **Guide for Traversing**

   For JWT can use the provided auth_jwt.http files for demo.

   ## Paths:
   * Django API
   ```
   http://0.0.0.0:8000/
   ```
    * Django API login
   ```
   http://0.0.0.0:8000/login/
   ```
    * Django API Admin
   ```
   http://0.0.0.0:8000/admin/
   ```
    * Django API redoc
   ```
   http://0.0.0.0:8000/api/schema/redoc/
   ```
   * Django API swagger-ui
   ```
   http://0.0.0.0:8000/api/schema/swagger-ui/
   ```
    * Prometheus
   ```
   http://0.0.0.0:9090
   ```
    * Grafana
   ```
   http://0.0.0.0:3000/
   ```
    * Grafana-alloy
   ```
   http://0.0.0.0:6900/
   ```

4. **Generating API Schema Documentation**

   To generate the API schema documentation file (`schema.yml`):

   ```bash
   python manage.py spectacular --color --file schema.yml
   ```

## Additional Notes

- **API Configuration:** The auto API config endpoints ensure you have live documentation for your API.
- **Monitoring Tools:** Grafana and Prometheus are set up for real-time monitoring.
- **CI/CD Integration:** GitHub Actions is configured to build Docker images and run tests automatically on push.
- **LOGS Integration:** Using loki to aggregate all logs of core app and Alloy for collect it and display them in grafana.
- 




