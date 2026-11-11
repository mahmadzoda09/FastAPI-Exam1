from fastapi.routing import APIRouter
from fastapi import Depends
from typing import Annotated

from schemas import TaskCreate , TaskUpdate , TaskResponse
from database import get_db ,Session
from crud import (
                get_all_tasks ,
                get_task_by_id ,
                create_task ,
                update_task ,
                delete_task,
                update_task_patch ,
                assign_task ,
                update_task_status
                )

task_router = APIRouter(tags=['Tasks'])
DB = Annotated[Session,Depends(get_db)]

@task_router.get('/tasks/' , response_model=list[TaskResponse])
async def get_tasks (db:DB):
    return get_all_tasks(db)

@task_router.get('/tasks/{task_id}' , response_model=TaskResponse)
async def get_task(task_id:int , db:DB):
    return get_task_by_id(db,task_id)

@task_router.post('/tasks/' , response_model=TaskResponse)
async def create_new_task(task:TaskCreate , db:DB):
    return create_task(db,task)

@task_router.put('/tasks/{task_id}' , response_model=TaskResponse)
async def update_taskt(task_id:int , task:TaskUpdate , db:DB):
    return update_task(db,task_id,task)

@task_router.patch('/tasks/{task_id}' , response_model=TaskResponse)
async def update_task_patchh(task_id:int , task:TaskUpdate , db:DB):
    return update_task_patch(db,task_id,task)

@task_router.delete('/tasks/{task_id}')
async def delete_taskt(task_id:int , db:DB):
    return delete_task(db,task_id)

@task_router.patch('/tasks/{task_id}/assign/{employee_id}' , response_model=TaskResponse)
async def assign_taskt(task_id:int , employee_id:int | None , db:DB):
    return assign_task(db,task_id,employee_id)

@task_router.patch('/tasks/{task_id}/status/{status}' , response_model=TaskResponse)
async def update_task_statuss(task_id:int , status:str , db:DB):
    return update_task_status(db,task_id,status)