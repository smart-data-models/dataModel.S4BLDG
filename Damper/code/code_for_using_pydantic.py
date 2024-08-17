from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, RootModel, constr


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class OperationMode(Enum):
    supply = 'supply'
    exhaust = 'exhaust'


class Type6(Enum):
    Damper = 'Damper'


class Damper(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    airFlowRateMax: Optional[float] = Field(
        None, description='Maximum allowable air flow rate. Usually measured in m3/s'
    )
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    bladeAction: Optional[str] = Field(None, description='Blade action')
    bladeEdge: Optional[str] = Field(None, description='Blade edge')
    bladeShape: Optional[str] = Field(
        None, description='Blade shape. Flat means triple V-groove'
    )
    bladeThickness: Optional[float] = Field(
        None,
        description='The thickness of the damper blade. Usually measured in millimeters (mm)',
    )
    closeOffRating: Optional[float] = Field(
        None, description='Close off rating. Usually measured in Pascals (Pa, N/m2)'
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    faceArea: Optional[float] = Field(
        None,
        description='Face area open to the airstream. Usually measured in square metre (m2)',
    )
    frameDepth: Optional[float] = Field(
        None,
        description='The length (or depth) of the damper frame. Usually measured in millimeters (mm)',
    )
    frameThickness: Optional[float] = Field(
        None,
        description='The thickness of the damper frame material. Usually measured in millimeters (mm)',
    )
    frameType: Optional[str] = Field(
        None,
        description='The type of frame used by the damper (e.g., Standard, Single Flange, Single Reversed Flange, Double Flange, etc.)',
    )
    hasManufacturer: Optional[str] = Field(
        None,
        description='A relationship identifying the manufacturer of an entity (e.g., device). The value is expected to be a string or a string with language tag',
    )
    hasModel: Optional[str] = Field(
        None,
        description='A relationship identifying the model of an entity (e.g., device). The value is expected to be a string or a string with language tag',
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    isContainedInBuildingSpace: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description='An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)',
    )
    isContainedInPhysicalObject: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description='Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)',
    )
    isSubSystemOf: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A reference to a system(s) that this Physical Object is part of',
    )
    leakageFullyClosed: Optional[float] = Field(
        None, description='Leakage when fully closed. Usually measured in m3/s'
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    nominalAirFlowRate: Optional[float] = Field(
        None, description='Nominal rate of air flow. Usually measured in m3/s'
    )
    numberOfBlades: Optional[float] = Field(None, description='Number of blades')
    openPressureDrop: Optional[float] = Field(
        None,
        description='Total pressure drop across damper. Usually measured in Pascals (Pa, N/m2)',
    )
    operation: Optional[str] = Field(
        None, description='The operational mechanism for the damper operation'
    )
    operationMode: Optional[OperationMode] = Field(
        None, description='Operation mode of this damper'
    )
    operationTemperatureMax: Optional[float] = Field(
        None,
        description='Allowable operation ambient (air, fluid) temperature range. Usually measured in degrees Kelvin (K)',
    )
    operationTemperatureMin: Optional[float] = Field(
        None,
        description='Allowable operation ambient (air, fluid) temperature range. Usually measured in degrees Kelvin (K)',
    )
    orientation: Optional[str] = Field(
        None,
        description='The intended orientation for the damper as specified by the manufacturer',
    )
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    temperatureRating: Optional[float] = Field(
        None, description='Temperature rating. Usually measured in degrees Kelvin (K)'
    )
    type: Optional[Type6] = Field(None, description='It must be equal to `Damper`')
    workingPressureMax: Optional[float] = Field(
        None,
        description='Maximum working pressure. Usually measured in Pascals (Pa, N/m2)',
    )
