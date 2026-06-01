# AI Interview Copilot - Requirements

## Functional Requirements

### Authentication

* User registration
* User login
* JWT authentication
* Role-based access control

### Resume Management

* Upload resume PDF
* Store resume in AWS S3
* Extract resume text
* Parse structured information
* Generate resume embeddings

### Interview Management

* Create interview session
* Start interview
* Pause interview
* Resume interview
* End interview

### Question Generation

* Generate resume-specific questions
* Retrieve questions from Qdrant
* Generate follow-up questions
* Support difficulty levels

### Voice Processing

* Capture candidate audio
* Convert speech to text
* Store transcripts

### Evaluation

* Evaluate candidate responses
* Generate scores
* Generate feedback
* Store evaluation results

### Report Generation

* Generate final report
* Export report
* Store report in S3

### Dashboard

* View interview history
* View reports
* View performance analytics

---

## Non-Functional Requirements

### Security

* JWT authentication
* Password hashing
* Secure file uploads

### Performance

* API response time under 5 seconds
* Real-time transcript updates

### Scalability

* Horizontal service scaling
* Queue-based background processing

### Reliability

* Retry failed background jobs
* Failure recovery mechanisms

### Maintainability

* Modular architecture
* Clear service boundaries
* Comprehensive documentation

### Observability

* Application monitoring
* Error logging
* Metrics dashboards
