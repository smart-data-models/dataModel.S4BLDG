<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: Lamp  
============<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Lamp/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **A lamp is an artificial light source such as a light bulb or tube.**  
version: 0.0.  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `colorAppearance[string]`: Property. In both the DIN and CIE standards, artificial light sources are classified in terms of their color appearance. To the human eye they all appear to be white the difference can only be detected by direct comparison. Visual performance is not directly affected by differences in color appearance.  - `colorRenderingIndex[number]`: Property. The CRI indicates how well a light source renders eight standard colors compared to perfect reference lamp with the same color temperature. The CRI scale ranges from 1 to 100, with 100 representing perfect rendering properties.  - `colorTemperature[number]`: Property. The color temperature of any source of radiation is defined as the temperature (in Kelvin) of a black-body or Planckian radiator whose radiation has the same chromaticity as the source of radiation. Often the values are only approximate color temperatures as the black-body radiator cannot emit radiation of every chromaticity value. The color temperatures of the commonest artificial light sources range from less than 3000K (warm white) to 4000K (intermediate) and over 5000K (daylight). Usually measured in degrees Kelvin (K).  - `contributedLuminousFlux[number]`: Property. Luminous flux is a photometric measure of radiant flux, i.e. the volume of light emitted from a light source. Luminous flux is measured either for the interior as a whole or for a part of the interior (partial luminous flux for a solid angle). All other photometric parameters are derivatives of luminous flux. Luminous flux is measured in lumens (lm). The luminous flux is given as a nominal value for each lamp. Usually measured in Lumen (lm, Candela Steradian).  - `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated[string]`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified[string]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description[string]`: A description of this item  - `hasManufacturer[string]`: Property. A relationship identifying the manufacturer of an entity (e.g., device). The value is expected to be a string or a string with language tag.  - `hasModel[string]`: Property. A relationship identifying the model of an entity (e.g., device). The value is expected to be a string or a string with language tag.  - `id[*]`: Unique identifier of the entity  - `isContainedInBuildingSpace[*]`: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)  - `isContainedInPhysicalObject[*]`: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)  - `isSubSystemOf[array]`: Relationship. A reference to a system(s) that this Physical Object is part of.  - `lampBallastType[string]`: Property. The type of ballast used to stabilise gas discharge by limiting the current during operation and to deliver the necessary striking voltage for starting. Ballasts are needed to operate Discharge Lamps such as Fluorescent, Compact Fluorescent, High-pressure Mercury, Metal Halide and High-pressure Sodium Lamps. Magnetic ballasts are chokes which limit the current passing through a lamp connected in series on the principle of self-induction. The resultant current and power are decisive for the efficient operation of the lamp. A specially designed ballast is required for every type of lamp to comply with lamp rating in terms of Luminous Flux, Color Appearance and service life. The two types of magnetic ballasts for fluorescent lamps are KVG Conventional (EC-A series) and VVG Low-loss ballasts (EC-B series). Low-loss ballasts have a higher efficiency, which means reduced ballast losses and a lower thermal load. Electronic ballasts are used to run fluorescent lamps at high frequencies (approx. 35 - 40 kHz).  - `lampCompensationType[string]`: Property. Identifies the form of compensation used for power factor correction and radio suppression.  - `lampMaintenanceFactor[number]`: Property. Non recoverable losses of luminous flux of a lamp due to lamp depreciation i.e. the decreasing of light output of a luminaire due to aging and dirt.  - `lightEmitterNominalPower[number]`: Property. Light emitter nominal power. Usually measured in Watts (W, J/s).  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name[string]`: The name of this item.  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `spectrumMax[number]`: Property. The spectrum of radiation describes its composition with regard to wavelength. Light, for example, as the portion of electromagnetic radiation that is visible to the human eye, is radiation with wavelengths in the range of approx. 380 to 780 nm (1 nm = 10 m). The corresponding range of colours varies from violet to indigo, blue, green, yellow, orange, and red. These colours form a continuous spectrum, in which the various spectral sectors merge into each other.  - `spectrumMin[number]`: Property. The spectrum of radiation describes its composition with regard to wavelength. Light, for example, as the portion of electromagnetic radiation that is visible to the human eye, is radiation with wavelengths in the range of approx. 380 to 780 nm (1 nm = 10 m). The corresponding range of colours varies from violet to indigo, blue, green, yellow, orange, and red. These colours form a continuous spectrum, in which the various spectral sectors merge into each other.  - `type[string]`: Property. It must be equal to `Lamp`.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Lamp:    
  description: A lamp is an artificial light source such as a light bulb or tube.    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government.'    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
        streetNr:    
          description: Number identifying a specific property on a public street.    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    colorAppearance:    
      description: 'Property. In both the DIN and CIE standards, artificial light sources are classified in terms of their color appearance. To the human eye they all appear to be white the difference can only be detected by direct comparison. Visual performance is not directly affected by differences in color appearance.'    
      type: string    
      x-ngsi:    
        type: Property    
    colorRenderingIndex:    
      description: 'Property. The CRI indicates how well a light source renders eight standard colors compared to perfect reference lamp with the same color temperature. The CRI scale ranges from 1 to 100, with 100 representing perfect rendering properties.'    
      type: number    
      x-ngsi:    
        type: Property    
    colorTemperature:    
      description: Property. The color temperature of any source of radiation is defined as the temperature (in Kelvin) of a black-body or Planckian radiator whose radiation has the same chromaticity as the source of radiation. Often the values are only approximate color temperatures as the black-body radiator cannot emit radiation of every chromaticity value. The color temperatures of the commonest artificial light sources range from less than 3000K (warm white) to 4000K (intermediate) and over 5000K (daylight). Usually measured in degrees Kelvin (K).    
      type: number    
      x-ngsi:    
        type: Property    
    contributedLuminousFlux:    
      description: 'Property. Luminous flux is a photometric measure of radiant flux, i.e. the volume of light emitted from a light source. Luminous flux is measured either for the interior as a whole or for a part of the interior (partial luminous flux for a solid angle). All other photometric parameters are derivatives of luminous flux. Luminous flux is measured in lumens (lm). The luminous flux is given as a nominal value for each lamp. Usually measured in Lumen (lm, Candela Steradian).'    
      type: number    
      x-ngsi:    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity.    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    hasManufacturer:    
      description: 'Property. A relationship identifying the manufacturer of an entity (e.g., device). The value is expected to be a string or a string with language tag.'    
      type: string    
      x-ngsi:    
        type: Property    
    hasModel:    
      description: 'Property. A relationship identifying the model of an entity (e.g., device). The value is expected to be a string or a string with language tag.'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &lamp_-_properties_-_iscontainedinbuildingspace_-_anyof    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    isContainedInBuildingSpace:    
      anyOf: *lamp_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *lamp_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *lamp_-_properties_-_iscontainedinbuildingspace_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Relationship    
    lampBallastType:    
      description: 'Property. The type of ballast used to stabilise gas discharge by limiting the current during operation and to deliver the necessary striking voltage for starting. Ballasts are needed to operate Discharge Lamps such as Fluorescent, Compact Fluorescent, High-pressure Mercury, Metal Halide and High-pressure Sodium Lamps. Magnetic ballasts are chokes which limit the current passing through a lamp connected in series on the principle of self-induction. The resultant current and power are decisive for the efficient operation of the lamp. A specially designed ballast is required for every type of lamp to comply with lamp rating in terms of Luminous Flux, Color Appearance and service life. The two types of magnetic ballasts for fluorescent lamps are KVG Conventional (EC-A series) and VVG Low-loss ballasts (EC-B series). Low-loss ballasts have a higher efficiency, which means reduced ballast losses and a lower thermal load. Electronic ballasts are used to run fluorescent lamps at high frequencies (approx. 35 - 40 kHz).'    
      type: string    
      x-ngsi:    
        type: Property    
    lampCompensationType:    
      description: Property. Identifies the form of compensation used for power factor correction and radio suppression.    
      type: string    
      x-ngsi:    
        type: Property    
    lampMaintenanceFactor:    
      description: Property. Non recoverable losses of luminous flux of a lamp due to lamp depreciation i.e. the decreasing of light output of a luminaire due to aging and dirt.    
      type: number    
      x-ngsi:    
        type: Property    
    lightEmitterNominalPower:    
      description: 'Property. Light emitter nominal power. Usually measured in Watts (W, J/s).'    
      type: number    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: GeoProperty. Geojson reference to the item. Point    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Point    
          type: object    
        - description: GeoProperty. Geojson reference to the item. LineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON LineString    
          type: object    
        - description: GeoProperty. Geojson reference to the item. Polygon    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Polygon    
          type: object    
        - description: GeoProperty. Geojson reference to the item. MultiPoint    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPoint    
          type: object    
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiLineString    
          type: object    
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPolygon    
          type: object    
      x-ngsi:    
        type: GeoProperty    
    name:    
      description: The name of this item.    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *lamp_-_properties_-_iscontainedinbuildingspace_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    spectrumMax:    
      description: 'Property. The spectrum of radiation describes its composition with regard to wavelength. Light, for example, as the portion of electromagnetic radiation that is visible to the human eye, is radiation with wavelengths in the range of approx. 380 to 780 nm (1 nm = 10 m). The corresponding range of colours varies from violet to indigo, blue, green, yellow, orange, and red. These colours form a continuous spectrum, in which the various spectral sectors merge into each other.'    
      type: number    
      x-ngsi:    
        type: Property    
    spectrumMin:    
      description: 'Property. The spectrum of radiation describes its composition with regard to wavelength. Light, for example, as the portion of electromagnetic radiation that is visible to the human eye, is radiation with wavelengths in the range of approx. 380 to 780 nm (1 nm = 10 m). The corresponding range of colours varies from violet to indigo, blue, green, yellow, orange, and red. These colours form a continuous spectrum, in which the various spectral sectors merge into each other.'    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: Property. It must be equal to `Lamp`.    
      enum:    
        - Lamp    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Lamp"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Lamp/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Lamp/schema.json    
  x-model-tags: SAREF Lamp    
  x-version: 0.0.    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
#### Lamp NGSI-v2 key-values Example    
Here is an example of a Lamp in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Lamp:732d4c91-579b-4ff8-b6f1-fcc429bcc3d7",  
    "type": "Lamp",  
    "colorAppearance": "Washington",  
    "colorRenderingIndex": 0.8153696255721333,  
    "colorTemperature": 0.09664075512365078,  
    "contributedLuminousFlux": 0.9207573270583412,  
    "lampBallastType": "Cape",  
    "lampCompensationType": "systematic",  
    "lampMaintenanceFactor": 0.4913004655459732,  
    "lightEmitterNominalPower": 0.2998024622331251,  
    "spectrumMax": 0.2518554879273158,  
    "spectrumMin": 0.7386218055211833,  
    "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:eb3dae30-05b0-44ba-8c58-172cd5f7b96e",  
    "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:5b981637-1f0e-41ac-b72d-4bc21f2bb629",  
    "isSubSystemOf": [  
        "urn:ngsi-ld:System:66da3c56-f167-4dd1-8691-9fea4013aa22",  
        "urn:ngsi-ld:System:1cab8165-219d-49db-823b-5eae961620c5",  
        "urn:ngsi-ld:System:76285f6c-9a86-48a1-94dd-e379a4fe4394"  
    ],  
    "hasManufacturer": "Lamp Company Inc.",  
    "hasModel": "Lamp 0.1.2",  
    "dateCreated": "2023-01-25T18:30:26Z",  
    "dateModified": "2023-01-25T16:57:18Z",  
    "source": "Import",  
    "name": "Lamp",  
    "alternateName": "Lamp type 2",  
    "description": "Lamp of limited Lamp types",  
    "dataProvider": "IFC file"  
}  
```  
</details>  
#### Lamp NGSI-v2 normalized Example    
Here is an example of a Lamp in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Lamp:e4e06bbb-5963-421b-b721-afbec54cf22e",  
  "type": "Lamp",  
  "colorAppearance": {  
    "type": "Text",  
    "value": "intranet"  
  },  
  "colorRenderingIndex": {  
    "type": "Float",  
    "value": 0.9381317485666679  
  },  
  "colorTemperature": {  
    "type": "Measurement",  
    "value":  0.162971670454518  
  },  
  "contributedLuminousFlux": {  
    "type": "Measurement",  
    "value":  0.9333222274075583  
  },  
  "lampBallastType": {  
    "type": "Text",  
    "value": "Intelligent"  
  },  
  "lampCompensationType": {  
    "type": "Text",  
    "value": "Web"  
  },  
  "lampMaintenanceFactor": {  
    "type": "Measurement",  
    "value":  0.7734465932124935  
  },  
  "lightEmitterNominalPower": {  
    "type": "Measurement",  
    "value":  0.34992609812300746  
  },  
  "spectrumMax": {  
    "type": "Measurement",  
    "value":  0.7513509645742688  
  },  
  "spectrumMin": {  
    "type": "Measurement",  
    "value":  0.6531361967308142  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:BuildingSpace:7f2b0435-7136-42aa-a3f5-14d718fe167b"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:PhysicalObject:870d927a-894d-443c-8202-a3f85d8010eb"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:21b3835c-564a-4b0c-9dc3-0f0e67489ad0"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:dfe58786-fa48-479c-97a9-09656f1751df"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:392b7d40-d54f-4e86-946f-7c89af254076"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Lamp Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Lamp 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T19:38:30.2179353+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T15:39:19.6056355+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Lamp"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Lamp type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Lamp of limited Lamp types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### Lamp NGSI-LD key-values Example    
Here is an example of a Lamp in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Lamp:732d4c91-579b-4ff8-b6f1-fcc429bcc3d7",  
  "type": "Lamp",  
  "colorAppearance": "Washington",  
  "colorRenderingIndex": 0.8153696255721333,  
  "colorTemperature": 0.09664075512365078,  
  "contributedLuminousFlux": 0.9207573270583412,  
  "lampBallastType": "Cape",  
  "lampCompensationType": "systematic",  
  "lampMaintenanceFactor": 0.4913004655459732,  
  "lightEmitterNominalPower": 0.2998024622331251,  
  "spectrumMax": 0.2518554879273158,  
  "spectrumMin": 0.7386218055211833,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:eb3dae30-05b0-44ba-8c58-172cd5f7b96e",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:5b981637-1f0e-41ac-b72d-4bc21f2bb629",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:66da3c56-f167-4dd1-8691-9fea4013aa22",  
    "urn:ngsi-ld:System:1cab8165-219d-49db-823b-5eae961620c5",  
    "urn:ngsi-ld:System:76285f6c-9a86-48a1-94dd-e379a4fe4394"  
  ],  
  "hasManufacturer": "Lamp Company Inc.",  
  "hasModel": "Lamp 0.1.2",  
  "dateCreated": "2023-01-25T18:30:26Z",  
  "dateModified": "2023-01-25T16:57:18Z",  
  "source": "Import",  
  "name": "Lamp",  
  "alternateName": "Lamp type 2",  
  "description": "Lamp of limited Lamp types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### Lamp NGSI-LD normalized Example    
Here is an example of a Lamp in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Lamp:a14c597e-ec02-4db5-aad5-6107d6435015",  
  "type": "Lamp",  
  "colorAppearance": {  
    "type": "Property",  
    "value": "card"  
  },  
  "colorRenderingIndex": {  
    "type": "Property",  
    "value": 0.6745960848595047  
  },  
  "colorTemperature": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T05:53:48Z",  
    "value": 0.03839635886669124  
  },  
  "contributedLuminousFlux": {  
    "type": "Property",  
    "unitCode": "Steradian",  
    "observedAt": "2023-01-26T12:44:07Z",  
    "value": 0.43828304543957874  
  },  
  "lampBallastType": {  
    "type": "Property",  
    "value": "mobile"  
  },  
  "lampCompensationType": {  
    "type": "Property",  
    "value": "seize"  
  },  
  "lampMaintenanceFactor": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T06:20:56Z",  
    "value": 0.035996560482205564  
  },  
  "lightEmitterNominalPower": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-25T17:44:26Z",  
    "value": 0.3144630350336074  
  },  
  "spectrumMax": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-25T17:43:19Z",  
    "value": 0.5533105661727246  
  },  
  "spectrumMin": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-25T16:58:44Z",  
    "value": 0.3399337921412814  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:550d9127-0996-4282-af73-1a7cbef3bee7"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:6fc10ce2-d07f-4837-9104-c17e7b33b812"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:a76465e2-2473-4048-849b-8f59eb40e19e"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:eaa2ffb0-4ea6-4904-a271-01c8cb171034"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:dc605242-4054-4fc8-89ba-8bce59724d02"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Lamp Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Lamp 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T21:41:50Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-25T17:39:08Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Lamp"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Lamp type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Lamp of limited Lamp types"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "IFC file"  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
