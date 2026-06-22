from fastapi import FastAPI

app = FastAPI(title="Mini Platform")


@app.get("/")
def read_root():
    return {"message": "Mini Platform is running"}