# Concord Social API

A reliable **social API** built with **FastAPI** and **PostgreSQL**, featuring owner-scoped **Posts** plus **Users/Auth** and **Votes** modules. The service emphasizes **operability**: idempotent writes, health/readiness probes, structured JSON logs, basic Prometheus metrics, and a safe migrations/rollback plan.  
A small **Java (Spring Boot)** parity service mirrors the `/posts` contract to demonstrate language agility.

---

## Tech stack

- **Backend:** FastAPI, Pydantic, SQLAlchemy, Alembic  
- **Auth:** OAuth2 (password flow), JWT (access tokens), bcrypt hashing  
- **DB:** PostgreSQL  
- **Ops:** Docker/Compose, Prometheus client (`/metrics`), structured JSON logs  
- **Tests/CI:** pytest (fixtures/parametrize), GitHub Actions (tests & lint)  
- **Optional parity:** Spring Boot, JPA, JUnit (`concord-social-api-java`)

---

## Quick start

### 1) Using Docker (recommended)

```bash
# clone repo
git clone https://github.com/GitHubguy97/concord-social-api.git
cd concord-social-api

# copy env template and edit secrets
cp .env.example .env

# start app + postgres
docker compose up --build
