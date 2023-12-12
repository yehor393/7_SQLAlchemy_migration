from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    value = Column(Integer, nullable=False)
    date = Column(DateTime, default=datetime.utcnow, nullable=False)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    student = relationship('Student', back_populates='grades')
    subject_id = Column(Integer, ForeignKey('subjects.id'), nullable=False)
    subject = relationship('Subject', back_populates='grades')
    group_id = Column(Integer, ForeignKey('groups.id'), nullable=False)
    group = relationship('Group', back_populates='grades')