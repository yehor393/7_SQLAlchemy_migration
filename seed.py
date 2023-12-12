from faker import Faker
from group import Group
from teacher import Teacher
from subject import Subject
from student import Student
from grade import Grade


def seed_data(session):
    fake = Faker()
    fake.seed(0)  # Seed for reproducibility

    # Create groups
    group_names = ['Group A', 'Group B', 'Group C']
    groups = [Group(name=name) for name in group_names]

    # Create teachers
    teacher_names = ['Teacher 1', 'Teacher 2', 'Teacher 3']
    teachers = [Teacher(name=name) for name in teacher_names]

    # Create subjects
    subjects = [Subject(name=fake.word(), teacher=teacher) for teacher in teachers for _ in range(2)]

    # Create students
    students = [Student(fullname=fake.name(), group=group) for group in groups for _ in range(10)]

    # Commit the initial data to the database
    session.add_all(groups + teachers + subjects + students)
    session.commit()

    # Create grades for each student and subject
    for student in students:
        for subject in subjects:
            grade = Grade(value=fake.random_int(min=60, max=100), date=fake.date_this_decade(),
                          student=student, subject=subject)
            session.add(grade)
    session.commit()
