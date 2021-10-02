from typing import List, Optional

from pydantic import BaseModel


class ISOCodeRequest(BaseModel):
    countries: List[str]
    detail: Optional[bool] = False
