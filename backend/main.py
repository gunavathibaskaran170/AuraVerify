from fastapi import FastAPI

app = FastAPI(
    title="AuraVerify Backend",
    description="AI-powered verification backend",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to AuraVerify Backend 🚀",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.get("/info")
def info():
    return {
        "project": "AuraVerify",
        "framework": "FastAPI",
        "python": "3.14",
        "server": "Uvicorn"
    }