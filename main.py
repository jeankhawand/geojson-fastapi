from typing import TypeVar, Generic
import json
from fastapi import FastAPI, Query, Request, status
from fastapi_pagination import Page as BasePage, add_pagination, paginate, Params as BaseParams
from starlette.staticfiles import StaticFiles

from models.GeoJson import GeoJson
from models.ISOCodeRequest import ISOCodeRequest
from models.ISOCodeResponse import ISOCodeResponse
from utils.utils import return_countries_list, generate_all_geometrics, return_iso_code
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
with open("countries.geojson") as file:
    data = json.load(file)
    geojson_data = GeoJson(**data)
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
T = TypeVar("T")


class Params(BaseParams):
    size: int = Query(5, ge=1, le=1_000, description="Page size")


class Page(BasePage[T], Generic[T]):
    __params_type__ = Params


@app.get("/")
async def read_root(request: Request):
    countries_data = json.dumps(return_countries_list(geojson_data))
    return templates.TemplateResponse("index.html", {"request": request, "countries": countries_data})


"""
takes as input one or multiple country names and returns the ISO3 country codes
    1-When the optional parameter ‘details’ is True, the associated geographical data(geometry) should be returned as well.
    2-Pagination should be implemented for any query that returns more than 5 results: For example if the input query is France, Germany, Spain, Italy, Angola, Burundi, Switzerland, Belarus; 
      the first results returned should be for the inputs France, Germany, Spain, Italy and Angola.
"""


@app.post("/iso_code", response_model=Page[ISOCodeResponse], response_model_exclude_unset=True)
def return_countries_iso_code(request: ISOCodeRequest):
    return paginate(return_iso_code(request, geojson_data))


"""
use a Custom Response to retrieve all the contents of the countries.geojson file in one go
"""


@app.post("/all_geometrics")
def all_geometrics():
    if generate_all_geometrics(geojson_data):
        return status.HTTP_200_OK
    else:
        return status.HTTP_500_INTERNAL_SERVER_ERROR


add_pagination(app)
