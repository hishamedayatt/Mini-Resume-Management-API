
from fastapi import FastAPI



app = FastAPI(
    title="Mini Resume Management API",
    description="API for managing candidate resumes",
    version="1.0.0"
)



# Health Check Endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}