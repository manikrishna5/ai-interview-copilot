# AI Interview Copilot - Technology Stack

## Frontend

### React

Used for building the user interface.

### Tailwind CSS

Used for responsive and modern UI development.

### Redux Toolkit

Used for global state management.

### React Router

Used for client-side routing.

### Socket.IO Client

Used for real-time communication during interviews.

---

## Backend

### FastAPI

Primary backend framework responsible for:

* Authentication
* Session management
* Resume processing
* Interview orchestration
* API endpoints

---

## Database

### PostgreSQL

Stores:

* Users
* Resumes
* Interview Sessions
* Questions
* Responses
* Reports
* Evaluations

Chosen due to strong relational data support and ACID compliance.

---

## Vector Database

### Qdrant

Used for:

* Resume embeddings
* Question bank embeddings
* Semantic search
* Retrieval-Augmented Generation (RAG)

---

## Cache & Queue

### Redis

Used for:

* Session caching
* Rate limiting
* Celery message broker

---

## Background Processing

### Celery

Used for:

* Resume processing
* Report generation
* Long-running AI tasks
* Notification workflows

---

## Artificial Intelligence

### Gemini API

Used for:

* Resume analysis
* Question generation
* Follow-up generation
* Answer evaluation
* Report generation

---

## Speech Processing

### Whisper

Used for:

* Speech-to-Text conversion
* Interview transcription

---

## File Storage

### AWS S3

Stores:

* Resume files
* Generated reports
* Future interview recordings

---

## Real-Time Communication

### Socket.IO

Used for:

* Live transcripts
* Real-time interview updates
* Notifications

---

## Monitoring

### Prometheus

Application metrics collection.

### Grafana

Monitoring dashboards and observability.

---

## Deployment

### Docker

Containerization.

### Docker Compose

Local development environment.

### AWS EC2

Application hosting.

### Nginx

Reverse proxy and traffic management.
