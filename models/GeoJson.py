from typing import List

from pydantic import BaseModel

from models.Feature import Feature
from models.ISOCodeResponse import ISOCodeResponse


class GeoJson(BaseModel):
    type: str
    features: List[Feature]

    def return_countries_with_iso_code(self, countries, detail=False):
        iso_result = list()
        for country in countries:
            for feature in self.features:
                if country.lower() == feature.properties.name.lower():
                    if detail:
                        iso_result.append(ISOCodeResponse(id=feature.id, name=feature.properties.name
                                                          , geometries=feature.geometry))
                    else:
                        iso_result.append(ISOCodeResponse(id=feature.id, name=feature.properties.name))
        return iso_result
