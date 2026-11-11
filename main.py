from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import engine , Base
from routers.projects import pr_router
from routers.employees import emp_router
from routers.tasks import task_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(title='TaskManager CRUD',lifespan=lifespan)
app.include_router(pr_router)
app.include_router(emp_router)
app.include_router(task_router)