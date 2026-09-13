from fastapi import FastAPI
from routes.student_routes import StudentRouter

app = FastAPI()
app.include_router(StudentRouter)