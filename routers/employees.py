from fastapi.routing import APIRouter
from fastapi import Depends
from typing import Annotated

from schemas import EmployeeCreate , EmployeeUpdate , EmployeeResponse
from database import get_db ,Session
from crud import (
                get_all_employees ,
                get_employee_by_id ,
                create_employee ,
                update_employee ,
                delete_employee,
                get_employee_tasks
                )

emp_router = APIRouter(tags=['Employees'])
DB = Annotated[Session,Depends(get_db)]

@emp_router.get('/employees/' , response_model=list[EmployeeResponse])
async def get_employees (db:DB):
    return get_all_employees(db)

@emp_router.get('/employees/{employee_id}' , response_model=EmployeeResponse)
async def get_employee(employee_id:int , db:DB):
    return get_employee_by_id(db,employee_id)

@emp_router.get('/employees/{employee_id}/tasks' , response_model=list[EmployeeResponse])
async def get_employee_taskss(employee_id:int , db:DB): 
    tasks = get_employee_tasks(db,employee_id)
    if tasks is None:
        return {'Employee not found'}
    return tasks

@emp_router.post('/employees/' , response_model=EmployeeResponse)
async def create_new_employee(employee:EmployeeCreate , db:DB):
    return create_employee(db,employee)

@emp_router.put('/employees/{employee_id}' , response_model=EmployeeResponse)
async def update_employeet(employee_id:int , employee:EmployeeUpdate , db:DB):
    return update_employee(db,employee_id,employee)

@emp_router.delete('/employees/{employee_id}')
async def delete_employeet(employee_id:int , db:DB):
    return delete_employee(db,employee_id)