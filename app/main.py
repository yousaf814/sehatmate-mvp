from fastapi import FastAPI

app = FastAPI(title="SehatMate MVP")

@app.get("/")
def root():
    return {"status": "SehatMate MVP running"}
