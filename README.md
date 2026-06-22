# Sports Hub

A backend learning project built with FastAPI, PostgreSQL, Docker, and SQLAlchemy.

The aim of this project is to build a sports-focused backend application while improving practical software engineering skills, including API development, database integration, environment setup, branching, and backend architecture.

At this stage, the project includes a working FastAPI backend, a Dockerised PostgreSQL database, database connectivity checks, SQLAlchemy models, and an initial user creation route.

## Project Goals

This project is designed to develop hands-on backend engineering skills through a sports-themed application.

The main goals are to practise:

* FastAPI backend development
* REST API design
* PostgreSQL database integration
* Docker-based local development
* SQLAlchemy ORM models
* Database table creation
* Environment configuration
* Git branching and feature-based development
* Testing API endpoints through local documentation

The long-term goal is to develop Sports Hub into an application that can store and manage sports-related data, such as users, teams, fixtures, results, preferences, and statistics.

## Current Features

### FastAPI Backend

The app exposes a local API using FastAPI.

Current functionality includes:

| Method | Endpoint      | Purpose                                         |
| ------ | ------------- | ----------------------------------------------- |
| `GET`  | `/`           | Root API check                                  |
| `GET`  | `/health`     | Basic health check                              |
| `GET`  | `/db-health`  | Check that the database connection is available |
| `GET`  | `/db-connect` | Test database connectivity                      |
| `POST` | `/users`      | Create a basic user record                      |

Endpoint names may need adjusting if the route names have changed in the current codebase.

### PostgreSQL Database

The project uses PostgreSQL running locally through Docker.

The database is used to persist application data and is connected to the FastAPI backend using SQLAlchemy.

### SQLAlchemy Models

The app currently includes an initial `User` model.

This model is used to create a `users` table in the database.

The database tables are created using:

```python
models.Base.metadata.create_all(bind=engine)
```

This tells SQLAlchemy to inspect the models that inherit from `Base` and create the corresponding tables in the connected database if they do not already exist.

### User Creation

The project includes an initial route for creating a user.

This proves the full backend flow:

```text
API request
    ↓
FastAPI route
    ↓
SQLAlchemy session
    ↓
PostgreSQL database
    ↓
Response returned to client
```

## Tech Stack

* Python
* FastAPI
* Uvicorn
* PostgreSQL
* Docker
* SQLAlchemy
* Pydantic
* DBeaver
* Git / GitHub

## Project Structure

The current project structure may look similar to this:

```text
Sporting-Hub/
│
├── Backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models.py
│   │   └── schemas.py
│   │
│   ├── requirements.txt
│   └── .env
│
├── docker-compose.yml
├── .gitignore
└── README.md
```

Adjust this section if your folder names differ.

## Setup

### 1. Clone the repository

```powershell
git clone <your-repo-url>
cd Sporting-Hub
```

### 2. Create a virtual environment

From the backend folder:

```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

You should see `(.venv)` at the start of the terminal prompt.

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

### 5. Start the PostgreSQL container

From the folder containing `docker-compose.yml`:

```powershell
docker compose up -d
```

This starts the local PostgreSQL database container in the background.

### 6. Run the FastAPI app

From the backend folder:

```powershell
uvicorn app.main:app --reload
```

The API should now be running at:

```text
http://127.0.0.1:8000
```

FastAPI documentation is available at:

```text
http://127.0.0.1:8000/docs
```

## Database Connection

The project connects to PostgreSQL using a database connection string.

A typical local connection string may look like:

```text
postgresql://postgres:postgres@localhost:5432/sports_hub
```

The exact value should be stored in an environment variable rather than hardcoded directly into the application.

Example `.env` value:

```text
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/sports_hub
```

Do not commit `.env` files to GitHub.

## DBeaver Verification

DBeaver can be used to inspect the local PostgreSQL database.

Use it to confirm:

* The database container is running
* The app can connect to PostgreSQL
* Tables have been created
* New records are inserted successfully

For example, after creating a user through the API, the `users` table can be checked in DBeaver to confirm the record exists.

## Example Usage

### Health Check

`GET /health`

Example response:

```json
{
  "status": "ok"
}
```

### Database Health Check

`GET /db-health`

Example response:

```json
{
  "database": "connected"
}
```

### Create User

`POST /users`

Example request:

```json
{
  "username": "oliver"
}
```

Example response:

```json
{
  "id": 1,
  "username": "oliver"
}
```

The exact request and response may differ depending on the current schema.

## Development Workflow

This project uses a feature-branch workflow.

Recommended flow:

```powershell
git checkout main
git pull
git checkout -b feature/<feature-name>
```

After implementing and testing a change:

```powershell
git status
git add .
git commit -m "Describe the change"
git push
```

Once the feature is working, it can be merged back into `main`.

## Current Learning Milestones

Completed so far:

* Created FastAPI backend
* Ran the app locally with Uvicorn
* Added basic health check routes
* Created a local PostgreSQL database using Docker
* Connected the backend to the database
* Verified database connectivity
* Created a SQLAlchemy model
* Created the initial `users` table
* Confirmed table creation in DBeaver
* Added and tested an initial user creation route

## Roadmap

### Near-Term

* Refactor routes into separate router files
* Add more user fields
* Add proper request and response schemas
* Add error handling for duplicate users
* Add GET endpoints for reading users
* Add PUT and DELETE endpoints for full user CRUD
* Add database migrations with Alembic

### Sports Hub Features

Potential future features include:

* User profiles
* Favourite teams
* Sports preferences
* Fixtures
* Results
* League tables
* Player statistics
* Team statistics
* Match predictions
* Personal dashboards

### Engineering Improvements

Future technical improvements could include:

* Alembic migrations
* Service layer
* Repository pattern
* Unit tests
* Integration tests
* Dockerised backend
* Environment-specific config
* CI checks with GitHub Actions
* Authentication and login
* Deployment to a cloud platform

## Why This Project Exists

Sports Hub is a practical learning project for improving backend engineering skills.

Rather than building isolated tutorials, this project is intended to grow into a real application while gradually introducing professional backend concepts:

```text
API route
    ↓
Schema validation
    ↓
Business logic
    ↓
Database session
    ↓
SQLAlchemy model
    ↓
PostgreSQL table
```

The current version is intentionally simple, but it establishes the core foundations needed for a more complete sports data application.
