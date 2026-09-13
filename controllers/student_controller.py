from fastapi import APIRouter, Response
from models.student_model import Student


students = []
id = 0


## BONUS : Search student
def search_student(search: str, response: Response):
    try:
        response.status_code = 200
        search = search.lower()

        result = [
            student for student in students
            if search in str(student.id).lower()
            or search in student.name.lower()
            or search in student.email.lower()
            or search in student.course.lower()
            or search in str(student.semester).lower()
        ]

        if result:
            return {'isSuccess': True,'message': 'Students found','student': result}
        return {'isSuccess': False,'message': 'No students found','student': []}

    except Exception as e:
            print(e)
            response.status_code = 500
            return {'isSuccess': False,'message':str(e)}

### Create student
def create_student_controller(student: Student, response: Response):
    global id
    try:
        id+=1
        student.id = id
        students.append(student)
        response.status_code = 201
        return {'isSuccess':True, 'message':'Student created successfully','student':student}
    except Exception as e:
        print(e)
        response.status_code = 500
        return {'isSuccess': False,'message':str(e)}
    

### Get student
def get_student_controller(response: Response):
    try:
        response.status_code = 200
        return {'isSuccess':True, 'message' : 'Student Display Successfully', 'students': students}
    except Exception as e:
        response.status_code = 500
        return{'isSuccess' : False, 'message' : 'Error Creating Student'}

### Get by ID
def get_studentID_controller(studentid: int, response: Response):
    try:
        response.status_code = 200
        for student in students:
            if student.id == studentid:
                return {'isSuccess':True,  'student': student}

        response.status_code = 404
        return {'message' : 'Student not found', 'isSuccess' : False}
    except Exception as e:
        print(e)
        response.status_code = 500
        return{'isSuccess' : False, 'message' : 'Error Creating Student'}


### Delete student
def delete_student_controller(studentid:int, response:Response):
    try:
        response.status_code = 200
        for student in students:
            if student.id == studentid:
                students.remove(student)
                return {'isSuccess' : True, 'messege' : 'Student deleted successfully'}
        response.status_code = 404
        return {'message' : 'Student not found', 'isSuccess' : False}
    except Exception as e:
        print(e)
        response.status_code = 500
        return{'isSuccess' : False, 'message' : 'Error Creating Student'}


### Update student
def update_student_controller(studentid: int, student: Student, response: Response):
    try:
        response.status_code = 200

        for s in students:
            if s.id == studentid:
                s.name = student.name
                s.email = student.email
                s.course = student.course
                s.semester = student.semester

                return {'isSuccess': True,'message': 'Student updated successfully','student': s}

        response.status_code = 404
        return {'message': 'Student not found','isSuccess': False}

    except Exception as e:
        print(e)
        response.status_code = 500
        return {'isSuccess': False,'message': 'Error updating student'}


### Pagination
def pagination_student_controller(page: int, limit: int, response: Response):
    try:
        start = (page - 1) * limit
        end = start + limit

        result = students[start:end]
        response.status_code = 200
        return {'isSuccess': True,'message': 'Students displayed successfully','page': page,'limit': limit,'student': result}

    except Exception as e:
        print(e)
        response.status_code = 500
        return {'isSuccess': False,'message': str(e)}


