from fastapi import APIRouter, HTTPException, status
from app.crud import add_student, get_all_students, get_student_by_id, update_student, delete_student
from app.schema import StudentCreate, StudentResponse, StudentDetail, StudentUpdate, AllStudents

router = APIRouter(tags=["students"])

# Create a student
@router.post("/students", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
async def create_student(student: StudentCreate):
    try:
        id = await add_student(student)
        return {"id": id}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# List all students
@router.get("/students", response_model=AllStudents, status_code=status.HTTP_200_OK)
async def list_students(country: str=None, age: int=None):
    students = await get_all_students(country, age)
    if not students:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No students found")
    student_details = [{"name": student["name"], "age": student["age"]} for student in students]
    return {"data": student_details}

# Get a student by ID
@router.get("/students/{id}", response_model=StudentCreate, status_code=status.HTTP_200_OK)
async def fetch_student(id: str):
    student = await get_student_by_id(id)
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return student
    
# Update a student by ID
@router.patch("/students/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_student_data(id: str, updated_data: StudentUpdate):
    updated_student = await update_student(id, updated_data)
    return updated_student

# Delete a student by ID
@router.delete("/students/{id}", status_code=status.HTTP_200_OK)
async def remove_student(id: str):
    success = await delete_student(id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return {}
