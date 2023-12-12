from sqlalchemy import func, desc
from sqlalchemy.orm import Session
from student import Student
from grade import Grade
from subject import Subject
from teacher import Teacher
from group import Group


def select_1(session: Session):
    """Знайти 5 студентів із найбільшим середнім балом з усіх предметів."""
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    return result


def select_2(session: Session, subject_name: str):
    """Знайти студента із найвищим середнім балом з певного предмета."""
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).join(Subject).filter(Subject.name == subject_name) \
        .group_by(Student.id).order_by(desc('avg_grade')).limit(1).all()
    return result


def select_3(session: Session, subject_name: str):
    """Знайти середній бал у групах з певного предмета."""
    result = session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).join(Subject).join(Group).filter(Subject.name == subject_name) \
        .group_by(Group.id).all()
    return result


def select_4(session: Session):
    """Знайти середній бал на потоці (по всій таблиці оцінок)."""
    result = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')).first()
    return result[0]


def select_5(session: Session, teacher_name: str):
    """Знайти які курси читає певний викладач."""
    result = session.query(Subject.name).join(Teacher).filter(Teacher.name == teacher_name).all()
    return [subject[0] for subject in result]


def select_6(session: Session, group_name: str):
    """Знайти список студентів у певній групі."""
    result = session.query(Student.fullname).join(Group).filter(Group.name == group_name).all()
    return [student[0] for student in result]


def select_7(session: Session, group_name: str, subject_name: str):
    """Знайти оцінки студентів у окремій групі з певного предмета."""
    result = session.query(Student.fullname, Grade.grade) \
        .join(Group).join(Subject).join(Grade).filter(Group.name == group_name, Subject.name == subject_name).all()
    return result


def select_8(session: Session, teacher_name: str):
    """Знайти середній бал, який ставить певний викладач зі своїх предметів."""
    result = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .join(Subject).join(Teacher).filter(Teacher.name == teacher_name).first()
    return result[0] if result else None


def select_9(session: Session, student_fullname: str):
    """Знайти список курсів, які відвідує певний студент."""
    result = session.query(Subject.name).join(Grade).join(Student).filter(Student.fullname == student_fullname).all()
    return [subject[0] for subject in result]


def select_10(session: Session, student_fullname: str, teacher_name: str):
    """Список курсів, які певному студенту читає певний викладач."""
    result = session.query(Subject.name) \
        .join(Grade).join(Student).join(Teacher).filter(Student.fullname == student_fullname,
                                                        Teacher.name == teacher_name).all()
    return [subject[0] for subject in result]
