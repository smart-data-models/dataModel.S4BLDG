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
    Lamp = 'Lamp'


class Lamp(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    colorAppearance: Optional[str] = Field(
        None,
        description='In both the DIN and CIE standards, artificial light sources are classified in terms of their color appearance. To the human eye they all appear to be white the difference can only be detected by direct comparison. Visual performance is not directly affected by differences in color appearance',
    )
    colorRenderingIndex: Optional[float] = Field(
        None,
        description='The CRI indicates how well a light source renders eight standard colors compared to perfect reference lamp with the same color temperature. The CRI scale ranges from 1 to 100, with 100 representing perfect rendering properties',
    )
    colorTemperature: Optional[float] = Field(
        None,
        description='The color temperature of any source of radiation is defined as the temperature (in Kelvin) of a black-body or Planckian radiator whose radiation has the same chromaticity as the source of radiation. Often the values are only approximate color temperatures as the black-body radiator cannot emit radiation of every chromaticity value. The color temperatures of the commonest artificial light sources range from less than 3000K (warm white) to 4000K (intermediate) and over 5000K (daylight). Usually measured in degrees Kelvin (K)',
    )
    contributedLuminousFlux: Optional[float] = Field(
        None,
        description='Luminous flux is a photometric measure of radiant flux, i.e. the volume of light emitted from a light source. Luminous flux is measured either for the interior as a whole or for a part of the interior (partial luminous flux for a solid angle). All other photometric parameters are derivatives of luminous flux. Luminous flux is measured in lumens (lm). The luminous flux is given as a nominal value for each lamp. Usually measured in Lumen (lm, Candela Steradian)',
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
    lampBallastType: Optional[str] = Field(
        None,
        description='The type of ballast used to stabilise gas discharge by limiting the current during operation and to deliver the necessary striking voltage for starting. Ballasts are needed to operate Discharge Lamps such as Fluorescent, Compact Fluorescent, High-pressure Mercury, Metal Halide and High-pressure Sodium Lamps. Magnetic ballasts are chokes which limit the current passing through a lamp connected in series on the principle of self-induction. The resultant current and power are decisive for the efficient operation of the lamp. A specially designed ballast is required for every type of lamp to comply with lamp rating in terms of Luminous Flux, Color Appearance and service life. The two types of magnetic ballasts for fluorescent lamps are KVG Conventional (EC-A series) and VVG Low-loss ballasts (EC-B series). Low-loss ballasts have a higher efficiency, which means reduced ballast losses and a lower thermal load. Electronic ballasts are used to run fluorescent lamps at high frequencies (approx. 35 - 40 kHz)',
    )
    lampCompensationType: Optional[str] = Field(
        None,
        description='Identifies the form of compensation used for power factor correction and radio suppression',
    )
    lampMaintenanceFactor: Optional[float] = Field(
        None,
        description='Non recoverable losses of luminous flux of a lamp due to lamp depreciation i.e. the decreasing of light output of a luminaire due to aging and dirt',
    )
    lightEmitterNominalPower: Optional[float] = Field(
        None,
        description='Light emitter nominal power. Usually measured in Watts (W, J/s)',
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
    spectrumMax: Optional[float] = Field(
        None,
        description='The spectrum of radiation describes its composition with regard to wavelength. Light, for example, as the portion of electromagnetic radiation that is visible to the human eye, is radiation with wavelengths in the range of approx. 380 to 780 nm (1 nm = 10 m). The corresponding range of colours varies from violet to indigo, blue, green, yellow, orange, and red. These colours form a continuous spectrum, in which the various spectral sectors merge into each other',
    )
    spectrumMin: Optional[float] = Field(
        None,
        description='The spectrum of radiation describes its composition with regard to wavelength. Light, for example, as the portion of electromagnetic radiation that is visible to the human eye, is radiation with wavelengths in the range of approx. 380 to 780 nm (1 nm = 10 m). The corresponding range of colours varies from violet to indigo, blue, green, yellow, orange, and red. These colours form a continuous spectrum, in which the various spectral sectors merge into each other',
    )
    type: Optional[Type6] = Field(None, description='It must be equal to `Lamp`')
