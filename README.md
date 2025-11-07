# SuperBenchmark API

A **FastAPI** application for benchmarking results.
This is a **test project** created for demonstration and learning purposes.

---

## Endpoints

| Method | URL | Description |
|---------|-----|-------------|
| `GET` | `/` | Returns all benchmark results |
| `GET` | `/results/average` | Returns average statistics across all results |
| `GET` | `/results/average/{start_time}/{end_time}` | Returns average statistics within a time window |

---

## Setup & Run

- clone repository
- create and activate virtual environment
- fill env variables (`.env`)
- `python -m src.app.main --reload`
