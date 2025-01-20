from django.http import JsonResponse
from django.views import View
from .models import Course
import json
import os
from django.conf import settings

def get_course_data(course_id):
    try:
        course = Course.objects.get(id=course_id)
        lessons = course.lessons.all().order_by('order')
        
        course_data = {
            "id": course.id,
            "name": course.name,
            "description": course.description,
            "lessons": [
                {
                    "id": lesson.id,
                    "title": lesson.title,
                    "content": os.path.join(settings.STATIC_URL, 'lessons', f'{course_id}/{lesson.markdown_path}'),
                    "order": lesson.order,
                }
                for lesson in lessons
            ]
        }
        return course_data
    except Course.DoesNotExist:
        raise FileNotFoundError(f"Course {course_id} not found.")

class CourseDetailView(View):
    def get(self, request, course_id):
        try:
            data = get_course_data(course_id)
            return JsonResponse(data, safe=False)
        except FileNotFoundError:
            return JsonResponse({"error": "Course not found"}, status=404)
