from typing import List, Optional

from pydantic import BaseModel

from models.Geometries import Geometries


class ISOCodeResponse(BaseModel):
    id: str
    name: str
    geometries: Optional[Geometries]
