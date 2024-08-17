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


class Type6(Enum):
    CoolingTower = 'CoolingTower'


class CoolingTower(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    ambientDesignDryBulbTemperature: Optional[float] = Field(
        None,
        description='Ambient design dry bulb temperature used for selecting the cooling tower. Usually measured in degrees Kelvin (K)',
    )
    ambientDesignWetBulbTemperature: Optional[float] = Field(
        None,
        description='Ambient design wet bulb temperature used for selecting the cooling tower. Usually measured in degrees Kelvin (K)',
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    basinReserveVolume: Optional[float] = Field(
        None,
        description='Volume between operating and overflow levels in cooling tower basin. Usually measured in cubic metre (m3)',
    )
    capacityControl: Optional[str] = Field(
        None,
        description='FanCycling: Fan is cycled on and off to control duty. TwoSpeedFan: Fan is switched between low and high speed to control duty. VariableSpeedFan: Fan speed is varied to control duty. DampersControl: Dampers modulate the air flow to control duty. BypassValveControl: Bypass valve modulates the water flow to control duty. MultipleSeriesPumps: Turn on/off multiple series pump to control duty. TwoSpeedPump: Switch between high/low pump speed to control duty. VariableSpeedPump: vary pump speed to control duty',
    )
    circuitType: Optional[str] = Field(
        None,
        description='OpenCircuit: Exposes water directly to the cooling atmosphere. CloseCircuit: The fluid is separated from the atmosphere by a heat exchanger. Wet: The air stream or the heat exchange surface is evaporatively cooled. Dry: No evaporation into the air stream. DryWet: A combination of a dry tower and a wet tower',
    )
    controlStrategy: Optional[str] = Field(
        None,
        description='FixedExitingWaterTemp: The capacity is controlled to maintain a fixed exiting water temperature. WetBulbTempReset: The set-point is reset based on the wet-bulb temperature',
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
    flowArrangement: Optional[str] = Field(
        None,
        description='CounterFlow: Air and water flow enter in different directions. CrossFlow: Air and water flow are perpendicular. ParallelFlow: air and water flow enter in same directions',
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
    liftElevationDifference: Optional[float] = Field(
        None,
        description='Elevation difference between cooling tower sump and the top of the tower. Usually measured in millimeters (mm)',
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    nominalCapacity: Optional[float] = Field(
        None, description='Nominal capacity. Usually measured in Watts (W, J/s)'
    )
    numberOfCells: Optional[float] = Field(
        None, description='Number of cells in one cooling tower unit'
    )
    operationTemperatureMax: Optional[float] = Field(
        None,
        description='Allowable operation ambient (air, fluid) temperature range. Usually measured in degrees Kelvin (K)',
    )
    operationTemperatureMin: Optional[float] = Field(
        None,
        description='Allowable operation ambient (air, fluid) temperature range. Usually measured in degrees Kelvin (K)',
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
    sprayType: Optional[str] = Field(
        None,
        description='SprayFilled: Water is sprayed into airflow. SplashTypeFill: water cascades over successive rows of splash bars. FilmTypeFill: water flows in a thin layer over closely spaced sheets',
    )
    type: Optional[Type6] = Field(
        None, description='It must be equal to `CoolingTower`'
    )
    waterRequirement: Optional[float] = Field(
        None, description='Make-up water requirement. Usually measured in m3/s'
    )
