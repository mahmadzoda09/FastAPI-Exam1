from fastapi.routing import APIRouter
from fastapi import Depends
from typing import Annotated

from schemas import ProjectCreate , ProjectUpdate , ProjectResponse
from database import get_db ,Session
from crud import (get_all_projects ,
                get_project_by_id ,
                get_project_tasks ,
                create_project ,
                update_project ,
                delete_project)

pr_router = APIRouter(tags=['Projects'])
DB = Annotated[Session,Depends(get_db)]

@pr_router.get('/projects/' , response_model=list[ProjectResponse])
async def get_projectss (db:DB):
    return get_all_projects(db)

@pr_router.get('/projects/{project_id}' , response_model=ProjectResponse)
async def get_project(project_id:int , db:DB):
    return get_project_by_id(db,project_id)

@pr_router.get('/projects/{project_id}/tasks' , response_model=list[ProjectResponse])
async def get_project_taskss(project_id:int , db:DB):
    tasks = get_project_tasks(db,project_id)
    if tasks is None:
        return {'Project not found'}
    return tasks

@pr_router.post('/projects/' , response_model=ProjectResponse)
async def create_new_project(project:ProjectCreate , db:DB):
    return create_project(db,project)

@pr_router.put('/projects/{project_id}' , response_model=ProjectResponse)
async def update_projectt(project_id:int , project:ProjectUpdate , db:DB):
    return update_project(db,project_id,project)

@pr_router.delete('/projects/{project_id}')
async def delete_projectt(project_id:int , db:DB):
    return delete_project(db,project_id)