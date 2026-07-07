from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Potens AI/ML Assignment API is running."
    }