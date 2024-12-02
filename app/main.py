from fastapi import FastAPI
from app.routers import student

app = FastAPI(
    title="Student Management System",
    description="A system to manage students using FastAPI and MongoDB.",
    version="1.0.0",
)

# base url
@app.get("/")
async def root():
    return {"message": "Welcome to the Student Management System"}

# Include routers
app.include_router(student.router)



