from fastapi import FastAPI

# uvicorn app:app --reload

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Index"}, 200

@app.get("/health")
def index():
    return {"message": "Aplication is healthy"}, 200