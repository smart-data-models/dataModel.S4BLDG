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


class Max(BaseModel):
    type: Optional[Type] = Field(None, description='NGSI-LD Entity Type')
    x: Optional[float] = Field(None, description='Coordinate X of the point')
    y: Optional[float] = Field(None, description='Coordinate Y of the point')
    z: Optional[float] = Field(None, description='Coordinate Z of the point')


class Min(BaseModel):
    type: Optional[Type] = Field(None, description='NGSI-LD Entity Type')
    x: Optional[float] = Field(None, description='Coordinate X of the point')
    y: Optional[float] = Field(None, description='Coordinate Y of the point')
    z: Optional[float] = Field(None, description='Coordinate Z of the point')


class Type2(Enum):
    Bounds = 'Bounds'


class Bounds(BaseModel):
    max: Optional[Max] = Field(None, description='Represents a point in a 3D space')
    min: Optional[Min] = Field(None, description='Represents a point in a 3D space')
    type: Optional[Type2] = Field(None, description='NGSI-LD Entity Type')


class BuildingSpaceKind(Enum):
    BuildingElementProxy = 'BuildingElementProxy'
    BuildingStorey = 'BuildingStorey'
    Column = 'Column'
    Covering = 'Covering'
    CurtainWall = 'CurtainWall'
    Door = 'Door'
    OpeningElement = 'OpeningElement'
    Plate = 'Plate'
    Railing = 'Railing'
    Roof = 'Roof'
    Site = 'Site'
    Slab = 'Slab'
    Space = 'Space'
    Stair = 'Stair'
    StairFlight = 'StairFlight'
    Storey = 'Storey'
    Wall = 'Wall'
    WallStandardCase = 'WallStandardCase'
    Window = 'Window'


class Type3(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type3


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type4(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type4


class Type5(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type5


class Type6(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type6


class Type7(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type7


class Type8(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type8


class Type9(Enum):
    BuildingSpace = 'BuildingSpace'


class BuildingSpace(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    airVolume: Optional[float] = Field(
        None, description='Air Volume of this building space. Measured in m3'
    )
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    bounds: Optional[Bounds] = Field(
        None, description='Bounds of this building space represented as a box in 3D'
    )
    buildingSpaceKind: Optional[BuildingSpaceKind] = Field(
        None, description='Detailed type of the Building Space'
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
    isSpaceOfBuilding: Optional[
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
        description='A building represents a structure that provides shelter for its occupants or contents and stands in one place. The building is also used to provide a basic element within the spatial structure hierarchy for the components of a building project (together with site, storey, and space). (Building)',
    )
    isSpaceOfBuildingSpace: Optional[
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
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    name: Optional[str] = Field(None, description='The name of this item')
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
    type: Optional[Type9] = Field(
        None, description='It must be equal to `BuildingSpace`'
    )
