from sqlalchemy import select

from models import Project , Employee , Task
from schemas import *
from database import Session

def get_all_projects(db: Session):
    projects = db.scalars(select(Project)).all()
    return projects

def create_project(db: Session, project_data: ProjectCreate ):
    data = project_data.model_dump()
    project = Project(name=data['name'], description=data['description'])
    db.add(project)
    db.commit()
    db.refresh(project)
    return project

def get_project_by_id(db: Session, project_id: int):
    project = db.get(Project, project_id)
    return project

def update_project(db: Session, project_id: int, project_data: ProjectUpdate):
    data = project_data.model_dump()
    project = db.get(Project, project_id)
    if project:
        project.name = data['name']
        project.description = data['description']
        db.commit()
        db.refresh(project)
    return project

def delete_project(db: Session, project_id: int):
    project = db.get(Project, project_id)
    if project:
        db.delete(project)
        db.commit()
    return {'Deleted Successfully'}

def get_project_tasks(db: Session, project_id: int):
    project = db.get(Project, project_id)
    if project:
        return project.tasks
    return {'Not Found'}

############Employee CRUD############

def get_all_employees(db: Session):
    employees = db.scalars(select(Employee)).all()
    return employees

def create_employee(db: Session, employee_data: EmployeeCreate):
    data = employee_data.model_dump()
    employee = Employee(full_name=data['full_name'], mail=data['mail'], position=data['position'])
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee

def get_employee_by_id(db: Session, employee_id: int):
    employee = db.get(Employee, employee_id)
    return employee

def update_employee(db: Session, employee_id: int, employee_data: EmployeeUpdate):
    data = employee_data.model_dump()
    employee = db.get(Employee, employee_id)
    if employee:
        employee.full_name = data['full_name']
        employee.mail = data['mail']
        employee.position = data['position']
        employee.is_active = data['is_active']
        db.commit()
        db.refresh(employee)
    return employee

def delete_employee(db: Session, employee_id: int):
    employee = db.get(Employee, employee_id)
    if employee:
        db.delete(employee)
        db.commit()
    return {'Deleted Successfully'}

def get_employee_tasks(db: Session, employee_id: int):
    employee = db.get(Employee, employee_id)
    if employee:
        return employee.tasks
    return {'Not Found'}

############Task CRUD############

def get_all_tasks(db: Session):
    tasks = db.scalars(select(Task)).all()
    return tasks

def get_task_by_id(db: Session, task_id: int):
    task = db.get(Task, task_id)
    return task

def create_task(db:Session, task_data: TaskCreate):
    data = task_data.model_dump()
    task = Task(title=data['title'], description=data['description'], status=data['status'], priority=data['priority'], deadline=data['deadline'], project_id=data['project_id'], employee_id=data['employee_id'])
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def update_task(db:Session , task_id : int , task_data: TaskUpdate ):
    data = task_data.model_dump()
    task = db.get(Task,task_id)
    if task:
        task.title = data['title']
        task.description = data['description']
        task.status = data['status']
        task.priority = data['priority']
        task.deadline = data['deadline']
        task.project_id = data['project_id']
        task.employee_id = data['employee_id']
        db.commit()
        db.refresh(task)
    return task

def update_task_patch(db:Session , task_id : int , task_data: TaskPatch ):
    data = task_data.model_dump(exclude_unset=True)
    task = db.get(Task,task_id)
    if task:
        for key, value in data.items():
            if value is None and key != 'deadline':
                continue
            setattr(task, key, value)
        db.commit()
        db.refresh(task)
    return task

def delete_task(db: Session, task_id: int):
    task = db.get(Task, task_id)
    if task:
        db.delete(task)
        db.commit()
    return {'Deleted Successfully'}

def assign_task(db: Session, task_id: int, employee_id: int | None):
    task = db.get(Task, task_id)
    if task:
        task.employee_id = employee_id
        db.commit()
        db.refresh(task)
    return task

def update_task_status(db: Session, task_id: int, status: str):
    task = db.get(Task, task_id)
    if task:
        task.status = status
        db.commit()
        db.refresh(task)
    return task