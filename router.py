from fastapi.routing import APIRouter

api_router = APIRouter()

from Controllers.Student import router as students_routes
from Controllers.Course import router as course_routes

api_router.include_router(students_routes, prefix="/students")
api_router.include_router(course_routes, prefix="/course")