from fastapi import FastAPI
from app.api.auth import router as auth_router

app = FastAPI(
    title="AI Interview Copilot"
)
app.include_router(auth_router)

@app.get("/")
def home():
    return {
        "message":
        "AI Interview Copilot Backend Running"
    }