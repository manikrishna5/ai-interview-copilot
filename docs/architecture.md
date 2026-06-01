# AI Interview Copilot - System Architecture

## High-Level Flow

Candidate
↓
React Frontend
↓
FastAPI Backend
↓
PostgreSQL

Additional Services:

FastAPI
├── Redis
├── Celery
├── Qdrant
├── Gemini API
├── Whisper API
├── AWS S3

---

## Resume Processing Flow

Resume Upload
↓
AWS S3
↓
Text Extraction
↓
Gemini Analysis
↓
Structured Resume Data
↓
PostgreSQL
↓
Embeddings
↓
Qdrant

---

## Interview Flow

Resume
↓
Qdrant Retrieval
↓
Gemini Question Generation
↓
Candidate Response
↓
Whisper Transcription
↓
Gemini Evaluation
↓
PostgreSQL

---

## Report Generation Flow

Interview Completion
↓
Celery Task
↓
Report Generation
↓
AWS S3
↓
Dashboard Access

---

## Monitoring Flow

Application Metrics
↓
Prometheus
↓
Grafana Dashboard
