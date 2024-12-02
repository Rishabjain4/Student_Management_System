from app.database import student_collection
from app.models import Student
from app.schema import StudentCreate, StudentUpdate
from bson.objectid import ObjectId

# Create a new student
async def add_student(student_data: StudentCreate) -> dict:
    student_dict = student_data.dict()
    result = student_collection.insert_one(student_dict)
    return str(result.inserted_id)

# Get all students
async def get_all_students(country: str=None, age: int=None) -> list:
    query = {}
    if country:
        query["address.country"] = country
    if age:
        # Only records which have age greater than equal to the provided age should be present in the result. 
        query["age"] = {"$gte": age}
    students_cursor = student_collection.find(query)
    if not students_cursor:
        return []
    return list(students_cursor)

# Get a student by ID
async def get_student_by_id(student_id: str) -> dict:
    student = student_collection.find_one({"_id": ObjectId(student_id)})
    if not student:
        return {}
    student_dict = dict(student)
    return StudentCreate(**student_dict)

# Update a student by ID
async def update_student(student_id: str, updated_data: StudentUpdate) -> dict:
    '''
    API to update the student's properties based on information provided. 
    Not mandatory that all information would be sent in PATCH, 
    only what fields are sent should be updated in the Database.
    
    {
        "name": "string",
        "age": 0,
        "address": {
            "city": "string",
            "country": "string"
        }
    }
    '''
    """
    Convert the Pydantic model to dict and transform nested updates
    to dot notation for MongoDB to properly update nested fields
    without overwriting the entire object.
    """
    update_dict = {}
    for field, value in updated_data.dict(exclude_none=True).items():
        if isinstance(value, dict):
            # Handle nested fields like address
            for nested_field, nested_value in value.items():
                if nested_value is not None:
                    update_dict[f"{field}.{nested_field}"] = nested_value
        else:
            update_dict[field] = value

    update_result = student_collection.update_one(
        {"_id": ObjectId(student_id)},
        {"$set": update_dict}
    )
    return {}

# Delete a student by ID
async def delete_student(student_id: str) -> bool:
    delete_result = student_collection.delete_one({"_id": ObjectId(student_id)})
    return delete_result.deleted_count == 1
