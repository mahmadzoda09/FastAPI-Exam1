from sqlalchemy import String , Text , ForeignKey , CheckConstraint  , DateTime 
from sqlalchemy.orm import Mapped , mapped_column , relationship
from datetime import datetime

from database import Base

class Project(Base):
    __tablename__ = 'projects'

    id: Mapped[int] = mapped_column(primary_key=True , autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), unique= True, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.now)

    tasks: Mapped[list['Task']] = relationship(back_populates="project")

class Employee(Base):
    __tablename__ = 'employees'

    id: Mapped[int] = mapped_column(primary_key=True , autoincrement=True)
    full_name: Mapped[str] = mapped_column(String(150), nullable=False)
    mail: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    position: Mapped[str] = mapped_column(String(100), nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.now)

    tasks: Mapped[list['Task']] = relationship(back_populates="employee")

class Task(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True , autoincrement=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(String(50), default='pending')
    priority: Mapped[int] = mapped_column(CheckConstraint('priority >= 1 AND priority <= 5'))
    deadline: Mapped[str] = mapped_column(DateTime, nullable=True)
    project_id: Mapped[int] = mapped_column(ForeignKey('projects.id'), nullable=False)
    employee_id: Mapped[int] = mapped_column(ForeignKey('employees.id'), nullable=False)
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.now)

    project: Mapped['Project'] = relationship(back_populates="tasks")
    employee: Mapped['Employee'] = relationship(back_populates="tasks")