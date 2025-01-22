import json
from django.core.management.base import BaseCommand
from course.models import Course, Lesson

class Command(BaseCommand):
    help = 'Load lessons from JSON file into database'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str)

    def handle(self, *args, **options):
        with open(options['json_file'], 'r') as f:
            lessons = json.load(f)
            
            for lesson_data in lessons:
                # Courseの取得または作成
                course, created = Course.objects.get_or_create(
                    name=lesson_data['course'],
                    defaults={'description': ''}
                )
                
                # Lessonの作成
                Lesson.objects.create(
                    course=course,
                    title=lesson_data['title'],
                    markdown_path=lesson_data['markdown_path'],
                    order=lesson_data['order']
                )
        
        self.stdout.write(self.style.SUCCESS(f'Successfully loaded {len(lessons)} lessons'))