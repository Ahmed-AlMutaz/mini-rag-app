from fastapi import FastAPI

app = FastAPI()


@app.get("/welcome")
def welcome():
    return {
        "greeting": "Hello World!",
        "info": "Welcome to Mini-RAG API"
    }