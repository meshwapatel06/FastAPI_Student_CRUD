from fastapi import APIRouter, Response
from models.student_model import Student
from controllers.student_controller import pagination_student_controller, search_student,create_student_controller, get_student_controller, get_studentID_controller, delete_student_controller, update_student_controller


StudentRouter = APIRouter(
    prefix='/students',   
    tags=['students']  
)

# Search student
@StudentRouter.get('/search')
def search_students(search: str, response: Response):
    return search_student(search, response)

# Create student
@StudentRouter.post('/students')
def create_student(student: Student, response: Response):
    return create_student_controller(student,response)

# Get Student
@StudentRouter.get('/students')
def get_students(response: Response):
    return get_student_controller(response)

# Get by ID
@StudentRouter.get('/students/{studentid}')
def get_student_by_id(studentid: int, response: Response):
    return get_studentID_controller(studentid, response)

# Delete student
@StudentRouter.delete('/students/{studentid}')
def delete_student(studentid: int, response: Response):
    return delete_student_controller(studentid, response)

# Update student
@StudentRouter.put('/students/{studentid}')
def update_student(studentid: int, student: Student, response: Response):
    return update_student_controller(studentid, student, response)

@StudentRouter.get("/pagination")
def pagination_student(page: int, limit: int, response: Response):
    return pagination_student_controller(page, limit, response)