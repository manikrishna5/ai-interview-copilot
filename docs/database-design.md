# AI Interview Copilot - Database Design

## Main Tables

### users

Stores application users.

### resumes

Stores uploaded resumes, parsed content, and embedding references.

### interview_sessions

Stores interview lifecycle information.

### questions

Stores generated interview questions.

### responses

Stores candidate answers and transcripts.

### evaluations

Stores AI-generated evaluation results.

### reports

Stores final interview reports.

### question_bank

Stores reusable interview questions for RAG retrieval.

### audit_logs

Stores system activity and event tracking.

---

## Entity Relationships

User
│
├── Resume
│
└── Interview Session
│
├── Questions
│      │
│      └── Responses
│             │
│             └── Evaluations
│
├── Reports
│
└── Audit Logs

Question Bank
│
└── Qdrant Embeddings

---

## Design Principles

* PostgreSQL acts as the source of truth.
* Qdrant stores vector embeddings only.
* AWS S3 stores large files.
* Relationships are maintained using foreign keys.
* Audit logging is used for traceability.
