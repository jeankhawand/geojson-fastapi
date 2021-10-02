
from typing import List, Union

from pydantic import BaseModel

from models.GeometryType import GeometryType


class Geometries(BaseModel):
    type: GeometryType
    coordinates: List[List[List[Union[List[float], float]]]]
