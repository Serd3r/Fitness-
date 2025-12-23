from fastapi import FastAPI

from app.routers import members, classes, reservations

app = FastAPI(
    title="Fitness Booking System",
    description="REST API for booking fitness classes with dynamic pricing.",
    version="0.1.0"
)

app.include_router(members.router)
app.include_router(classes.router)
app.include_router(reservations.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Fitness Booking System API"}
