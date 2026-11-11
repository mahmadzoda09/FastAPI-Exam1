from pydantic import BaseModel , Field , ConfigDict
from datetime import datetime

class ProjectCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str = Field(max_length=50)
    description: str = Field(max_length=200)

class ProjectUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str = Field(max_length=50)
    description: str = Field(max_length=200)

class ProjectResponse(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class EmployeeCreate(BaseModel):
    full_name: str = Field(max_length=100)
    mail: str = Field(max_length=100)
    position: str = Field(max_length=50)
    model_config = ConfigDict(from_attributes=True)

class EmployeeUpdate(BaseModel):
    full_name: str = Field(max_length=100)
    mail: str = Field(max_length=100)
    position: str = Field(max_length=50)
    is_active: bool
    model_config = ConfigDict(from_attributes=True)

class EmployeeResponse(BaseModel):
    id: int
    full_name: str
    mail: str
    position: str
    is_active: bool
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class TaskCreate(BaseModel):
    title: str = Field(max_length=100)
    description: str = Field(max_length=200)
    status: str = Field(max_length=50, default='pending')
    priority: int = Field(ge=1, le=5)
    deadline: datetime | None = None
    project_id: int
    employee_id: int
    model_config = ConfigDict(from_attributes=True)

class TaskUpdate(BaseModel):
    title: str = Field(max_length=100)
    description: str = Field(max_length=200)
    status: str = Field(max_length=50)
    priority: int = Field(ge=1, le=5)
    deadline: datetime | None = None
    project_id: int
    employee_id: int
    model_config = ConfigDict(from_attributes=True)

class TaskPatch(BaseModel):
    title: str | None = Field(default=None, max_length=100)
    description: str | None = Field(default=None, max_length=200)
    status: str | None = Field(default=None, max_length=50)
    priority: int | None = Field(default=None, ge=1, le=5)
    deadline: datetime | None = None
    project_id: int | None = None
    employee_id: int | None = None
    model_config = ConfigDict(from_attributes=True)

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str
    priority: int
    deadline: datetime | None = None
    project_id: int
    employee_id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)