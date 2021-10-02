from pydantic import BaseModel

from models.Geometries import Geometries
from models.Properties import Properties


class Feature(BaseModel):
    type: str
    id: str
    properties: Properties
    geometry: Geometries

