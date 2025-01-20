from course.models import Course, Lesson

# コースの作成
course = Course.objects.create(name="Python Basics", description="Learn the basics of Python programming.")

# レッスンの作成
lesson1 = Lesson.objects.create(course=course, title="Hello World", markdown_path="python_basics/lesson_1.md", order=1)
lesson2 = Lesson.objects.create(course=course, title="Variables and Data Types", markdown_path="python_basics/lesson_2.md", order=2)

print("Data has been successfully loaded!")