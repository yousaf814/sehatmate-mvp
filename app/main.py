from fastapi import FastAPI

app = FastAPI(title="SehatMate MVP")

@app.get("/")
def root():
    return {"status": "SehatMate MVP running"}

from app.doctors import router as doctor_router
app.include_router(doctor_router)
