from fastapi import FastAPI
from app.api import candidates

app = FastAPI(title="Mini Resume Management API")

# Health Check
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Include Candidate Routes
app.include_router(
    candidates.router

)
