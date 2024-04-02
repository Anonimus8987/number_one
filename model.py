from pydantic import BaseModel
from typing import Optional, TypeVar
from datetime import datetime

T = TypeVar('T')

class Vehicle(BaseModel):
    pass