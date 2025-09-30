# Fastapi-Alembic-Project

## Objective
A small FastAPI project demonstrating:

- Creating APIs with FastAPI
- Managing database schema versions with Alembic
- Performing database operations with SQLAlchemy ORM
- Using PostgreSQL & pgAdmin 4 for database management

---

## Database Migrations

This project uses Alembic to manage database schema versions.

-   **To apply all migrations** and bring the database to the latest version, run:
    ```bash
    alembic upgrade head
    ```

-   **To roll back the last migration**, you can use:
    ```bash
    alembic downgrade -1
    ```

---

## Running the Application

To run the live development server, use Uvicorn:

```bash
uvicorn app.main:app --reload

The server will be available at http://127.0.0.1:8000.

```
---
## Testing API Endpoints

FastAPI automatically generates **Swagger UI** for your APIs at `/docs`. You can use it to test all endpoints without any external tools.

### Steps:

1. **Run the FastAPI app**
```bash
uvicorn app.main:app --reload
```
2. **Open Swagger UI**

- Go to your browser: http://127.0.0.1:8000/docs

- You’ll see a web interface listing all available endpoints.

3. **Test an endpoint**

- Click on the endpoint you want to test (e.g., POST /users).

- Click “Try it out”.

- Fill in the required request body in JSON format.
---

## Core Technologies

- **API Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Database Migrations**: Alembic

---
