<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entity: Valve    
=============<!-- /10-Header -->    
<!-- 15-License -->    
[Open License](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Valve/LICENSE.md)    
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Global description: **A valve is used in a building services piping distribution system to control or modulate the flow of the fluid.**    
version: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## List of properties    
<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>    
- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: The country. For example, Spain  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: The locality in which the street address is, and which is in the region  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: The region in which the locality is, and which is in the country  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: A district is a type of administrative division that, in some countries, is managed by the local government      
	- `postOfficeBoxNumber[string]`: The post office box number for PO box addresses. For example, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: The postal code. For example, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: The street address  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `closeOffRating[number]`: Close off rating. Usually measured in Pascals (Pa, N/m2)  - `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `description[string]`: A description of this item  - `flowCoefficient[number]`: Flow coefficient (the quantity of fluid that passes through a fully open valve at unit pressure drop), typically expressed as the Kv or Cv value for the valve  - `hasManufacturer[string]`: A relationship identifying the manufacturer of an entity (e.g., device). The value is expected to be a string or a string with language tag  - `hasModel[string]`: A relationship identifying the model of an entity (e.g., device). The value is expected to be a string or a string with language tag  - `id[*]`: Unique identifier of the entity  - `isContainedInBuildingSpace[*]`: An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)  - `isContainedInPhysicalObject[*]`: Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)  - `isSubSystemOf[array]`: A reference to a system(s) that this Physical Object is part of  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name[string]`: The name of this item  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `size[number]`: The size of the connection to the valve (or to each connection for faucets, mixing valves, etc.). Usually measured in millimeters (mm)  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `testPressure[number]`: The maximum pressure to which the valve has been subjected under test. Usually measured in Pascals (Pa, N/m2)  - `type[string]`: It must be equal to `Valve`  - `valveMechanism[string]`: The mechanism by which the valve function is achieved where: BALL: Valve that has a ported ball that can be turned relative to the body seat ports. BUTTERFLY: Valve in which a streamlined disc pivots about a diametric axis. CONFIGUREDGATE: Screwdown valve in which the closing gate is shaped in a configured manner to have a more precise control of pressure and flow change across the valve. GLAND: Valve with a tapered seating, in which a rotatable plug is retained by means of a gland and gland packing. GLOBE: Screwdown valve that has a spherical body. LUBRICATEDPLUG: Plug valve in which a lubricant is injected under pressure between the plug face and the body. NEEDLE: Valve for regulating the flow in or from a pipe, in which a slender cone moves along the axis of flow to close against a fixed conical seat. PARALLELSLIDE: Screwdown valve that has a machined plate that slides in formed grooves to form a seal. PLUG: Valve that has a ported plug that can be turned relative to the body seat ports. WEDGEGATE: Screwdown valve that has a wedge shaped plate fitting into tapered guides to form a seal  - `valveOperation[string]`: The method of valve operation where: DROPWEIGHT: A valve that is closed by the action of a weighted lever being released, the weight normally being prevented from dropping by being held by a wire, the closure normally being made by the action of heat on a fusible link in the wire FLOAT: A valve that is opened and closed by the action of a float that rises and falls with water level. The float may be a ball attached to a lever or other mechanism HYDRAULIC: A valve that is opened and closed by hydraulic actuation LEVER: A valve that is opened and closed by the action of a lever rotating the gate within the valve. LOCKSHIELD: A valve that requires the use of a special lockshield key for opening and closing, the operating mechanism being protected by a shroud during normal operation. MOTORIZED: A valve that is opened and closed by the action of an electric motor on an actuator PNEUMATIC: A valve that is opened and closed by pneumatic actuation SOLENOID: A valve that is normally held open by a magnetic field in a coil acting on the gate but that is closed immediately if the electrical current generating the magnetic field is removed. SPRING: A valve that is normally held in position by the pressure of a spring on a plate but that may be caused to open if the pressure of the fluid is sufficient to overcome the spring pressure. THERMOSTATIC: A valve in which the ports are opened or closed to maintain a required predetermined temperature. WHEEL: A valve that is opened and closed by the action of a wheel moving the gate within the valve  - `valvePattern[string]`: The configuration of the ports of a valve according to either the linear route taken by a fluid flowing through the valve or by the number of ports where: SINGLEPORT: Valve that has a single entry port from the system that it serves, the exit port being to the surrounding environment. ANGLED_2_PORT: Valve in which the direction of flow is changed through 90 degrees. STRAIGHT_2_PORT: Valve in which the flow is straight through. STRAIGHT_3_PORT: Valve with three separate ports. CROSSOVER_4_PORT: Valve with 4 separate ports  - `workingPressure[number]`: The normally expected maximum working pressure of the valve. Usually measured in Pascals (Pa, N/m2)  <!-- /30-PropertiesList -->    
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
Valve:      
  description: A valve is used in a building services piping distribution system to control or modulate the flow of the fluid.      
  properties:      
    address:      
      description: The mailing address      
      properties:      
        addressCountry:      
          description: 'The country. For example, Spain'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressCountry      
            type: Property      
        addressLocality:      
          description: 'The locality in which the street address is, and which is in the region'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressLocality      
            type: Property      
        addressRegion:      
          description: 'The region in which the locality is, and which is in the country'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressRegion      
            type: Property      
        district:      
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'      
          type: string      
          x-ngsi:      
            type: Property      
        postOfficeBoxNumber:      
          description: 'The post office box number for PO box addresses. For example, 03578'      
          type: string      
          x-ngsi:      
            model: https://schema.org/postOfficeBoxNumber      
            type: Property      
        postalCode:      
          description: 'The postal code. For example, 24004'      
          type: string      
          x-ngsi:      
            model: https://schema.org/https://schema.org/postalCode      
            type: Property      
        streetAddress:      
          description: The street address      
          type: string      
          x-ngsi:      
            model: https://schema.org/streetAddress      
            type: Property      
        streetNr:      
          description: Number identifying a specific property on a public street      
          type: string      
          x-ngsi:      
            type: Property      
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
    closeOffRating:      
      description: 'Close off rating. Usually measured in Pascals (Pa, N/m2)'      
      type: number      
      x-ngsi:      
        type: Property      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    dateCreated:      
      description: Entity creation timestamp. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    flowCoefficient:      
      description: 'Flow coefficient (the quantity of fluid that passes through a fully open valve at unit pressure drop), typically expressed as the Kv or Cv value for the valve'      
      type: number      
      x-ngsi:      
        type: Property      
    hasManufacturer:      
      description: 'A relationship identifying the manufacturer of an entity (e.g., device). The value is expected to be a string or a string with language tag'      
      type: string      
      x-ngsi:      
        type: Property      
    hasModel:      
      description: 'A relationship identifying the model of an entity (e.g., device). The value is expected to be a string or a string with language tag'      
      type: string      
      x-ngsi:      
        type: Property      
    id:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Unique identifier of the entity      
      x-ngsi:      
        type: Property      
    isContainedInBuildingSpace:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)      
      x-ngsi:      
        type: Property      
    isContainedInPhysicalObject:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)      
      x-ngsi:      
        type: Property      
    isSubSystemOf:      
      description: A reference to a system(s) that this Physical Object is part of      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Relationship      
    location:      
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
      oneOf:      
        - description: Geojson reference to the item. Point      
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
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. LineString      
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
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. Polygon      
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
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiPoint      
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
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
      x-ngsi:      
        type: GeoProperty      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    owner:      
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
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
    size:      
      description: 'The size of the connection to the valve (or to each connection for faucets, mixing valves, etc.). Usually measured in millimeters (mm)'      
      type: number      
      x-ngsi:      
        type: Property      
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    testPressure:      
      description: 'The maximum pressure to which the valve has been subjected under test. Usually measured in Pascals (Pa, N/m2)'      
      type: number      
      x-ngsi:      
        type: Property      
    type:      
      description: It must be equal to `Valve`      
      enum:      
        - Valve      
      type: string      
      x-ngsi:      
        type: Property      
    valveMechanism:      
      description: 'The mechanism by which the valve function is achieved where: BALL: Valve that has a ported ball that can be turned relative to the body seat ports. BUTTERFLY: Valve in which a streamlined disc pivots about a diametric axis. CONFIGUREDGATE: Screwdown valve in which the closing gate is shaped in a configured manner to have a more precise control of pressure and flow change across the valve. GLAND: Valve with a tapered seating, in which a rotatable plug is retained by means of a gland and gland packing. GLOBE: Screwdown valve that has a spherical body. LUBRICATEDPLUG: Plug valve in which a lubricant is injected under pressure between the plug face and the body. NEEDLE: Valve for regulating the flow in or from a pipe, in which a slender cone moves along the axis of flow to close against a fixed conical seat. PARALLELSLIDE: Screwdown valve that has a machined plate that slides in formed grooves to form a seal. PLUG: Valve that has a ported plug that can be turned relative to the body seat ports. WEDGEGATE: Screwdown valve that has a wedge shaped plate fitting into tapered guides to form a seal'      
      type: string      
      x-ngsi:      
        type: Property      
    valveOperation:      
      description: 'The method of valve operation where: DROPWEIGHT: A valve that is closed by the action of a weighted lever being released, the weight normally being prevented from dropping by being held by a wire, the closure normally being made by the action of heat on a fusible link in the wire FLOAT: A valve that is opened and closed by the action of a float that rises and falls with water level. The float may be a ball attached to a lever or other mechanism HYDRAULIC: A valve that is opened and closed by hydraulic actuation LEVER: A valve that is opened and closed by the action of a lever rotating the gate within the valve. LOCKSHIELD: A valve that requires the use of a special lockshield key for opening and closing, the operating mechanism being protected by a shroud during normal operation. MOTORIZED: A valve that is opened and closed by the action of an electric motor on an actuator PNEUMATIC: A valve that is opened and closed by pneumatic actuation SOLENOID: A valve that is normally held open by a magnetic field in a coil acting on the gate but that is closed immediately if the electrical current generating the magnetic field is removed. SPRING: A valve that is normally held in position by the pressure of a spring on a plate but that may be caused to open if the pressure of the fluid is sufficient to overcome the spring pressure. THERMOSTATIC: A valve in which the ports are opened or closed to maintain a required predetermined temperature. WHEEL: A valve that is opened and closed by the action of a wheel moving the gate within the valve'      
      type: string      
      x-ngsi:      
        type: Property      
    valvePattern:      
      description: 'The configuration of the ports of a valve according to either the linear route taken by a fluid flowing through the valve or by the number of ports where: SINGLEPORT: Valve that has a single entry port from the system that it serves, the exit port being to the surrounding environment. ANGLED_2_PORT: Valve in which the direction of flow is changed through 90 degrees. STRAIGHT_2_PORT: Valve in which the flow is straight through. STRAIGHT_3_PORT: Valve with three separate ports. CROSSOVER_4_PORT: Valve with 4 separate ports'      
      type: string      
      x-ngsi:      
        type: Property      
    workingPressure:      
      description: 'The normally expected maximum working pressure of the valve. Usually measured in Pascals (Pa, N/m2)'      
      type: number      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Valve"      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Valve/LICENSE.md      
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Valve/schema.json      
  x-model-tags: SAREF Valve      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Example payloads      
#### Valve NGSI-v2 key-values Example      
Here is an example of a Valve in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Valve:5606802d-9bfc-41f4-b6cb-7a2dc52214ea",  
  "type": "Valve",  
  "closeOffRating": 0.9792941241344664,  
  "flowCoefficient": 0.825533650257277,  
  "size": 0.7178529493113952,  
  "testPressure": 0.9690729968605641,  
  "valveMechanism": "Greece",  
  "valveOperation": "auxiliary",  
  "valvePattern": "Consultant",  
  "workingPressure": 0.8773888966189294,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:c2e1097b-602a-49ef-b81e-73687c4868b3",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:663b3745-acf8-4b86-ab69-693afe57cf2c",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:9ec35827-e00f-461e-8f22-5cd758f7f7f6",  
    "urn:ngsi-ld:System:aac7e87c-55fe-4c45-88aa-1cb36e3512f9",  
    "urn:ngsi-ld:System:a4adbc73-68e8-43c6-b366-adc5ffb0e4f8"  
  ],  
  "hasManufacturer": "Valve Company Inc.",  
  "hasModel": "Valve 0.1.2",  
  "dateCreated": "2023-01-25T17:39:28Z",  
  "dateModified": "2023-01-26T11:24:20Z",  
  "source": "Import",  
  "name": "Valve",  
  "alternateName": "Valve type 2",  
  "description": "Valve of limited Valve types",  
  "dataProvider": "IFC file"  
}  
```  
</details>    
#### Valve NGSI-v2 normalized Example      
Here is an example of a Valve in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Valve:5384a157-cc2a-4984-b4ed-4273d58990da",  
  "type": "Valve",  
  "closeOffRating": {  
    "type": "Number",  
    "value": 0.6442998208642058  
  },  
  "flowCoefficient": {  
    "type": "Number",  
    "value": 0.9502368316657622  
  },  
  "size": {  
    "type": "Number",  
    "value": 0.1757245625885473  
  },  
  "testPressure": {  
    "type": "Number",  
    "value": 0.3547642349477015  
  },  
  "valveMechanism": {  
    "type": "Text",  
    "value": "Comoro Franc"  
  },  
  "valveOperation": {  
    "type": "Text",  
    "value": "capacity"  
  },  
  "valvePattern": {  
    "type": "Text",  
    "value": "Regional"  
  },  
  "workingPressure": {  
    "type": "Number",  
    "value": 0.7616536973295315  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:BuildingSpace:4c2121a4-e126-4cee-bd63-517a31e19d0c"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:PhysicalObject:3b7bbebe-aa67-4d67-991d-8360e38cb075"  
  },  
  "isSubSystemOf": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:System:a3691c28-c6b1-4dbd-8781-58c369f780f2",  
      "urn:ngsi-ld:System:bd7d12e5-25ef-474b-93af-bba6ebef4782",  
      "urn:ngsi-ld:System:0ee8b6da-5507-42c2-a80d-eaea8b13a894"  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Valve Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Valve 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T15:00:30.8255456+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T14:02:17.0152497+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Valve"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Valve type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Valve of limited Valve types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>    
#### Valve NGSI-LD key-values Example      
Here is an example of a Valve in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Valve:5606802d-9bfc-41f4-b6cb-7a2dc52214ea",  
  "type": "Valve",  
  "closeOffRating": 0.9792941241344664,  
  "flowCoefficient": 0.825533650257277,  
  "size": 0.7178529493113952,  
  "testPressure": 0.9690729968605641,  
  "valveMechanism": "Greece",  
  "valveOperation": "auxiliary",  
  "valvePattern": "Consultant",  
  "workingPressure": 0.8773888966189294,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:c2e1097b-602a-49ef-b81e-73687c4868b3",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:663b3745-acf8-4b86-ab69-693afe57cf2c",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:9ec35827-e00f-461e-8f22-5cd758f7f7f6",  
    "urn:ngsi-ld:System:aac7e87c-55fe-4c45-88aa-1cb36e3512f9",  
    "urn:ngsi-ld:System:a4adbc73-68e8-43c6-b366-adc5ffb0e4f8"  
  ],  
  "hasManufacturer": "Valve Company Inc.",  
  "hasModel": "Valve 0.1.2",  
  "dateCreated": "2023-01-25T17:39:28Z",  
  "dateModified": "2023-01-26T11:24:20Z",  
  "source": "Import",  
  "name": "Valve",  
  "alternateName": "Valve type 2",  
  "description": "Valve of limited Valve types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>    
#### Valve NGSI-LD normalized Example      
Here is an example of a Valve in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Valve:ca643e8d-ccbe-4bc2-a132-c5a51578501a",  
  "type": "Valve",  
  "closeOffRating": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-25T21:38:33Z",  
    "value": 0.4968075534065832  
  },  
  "flowCoefficient": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T07:44:38Z",  
    "value": 0.3336750880832986  
  },  
  "size": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T10:49:30Z",  
    "value": 0.686759934652535  
  },  
  "testPressure": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-26T10:54:40Z",  
    "value": 0.2729778598678245  
  },  
  "valveMechanism": {  
    "type": "Property",  
    "value": "SSL"  
  },  
  "valveOperation": {  
    "type": "Property",  
    "value": "navigate"  
  },  
  "valvePattern": {  
    "type": "Property",  
    "value": "Central"  
  },  
  "workingPressure": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-26T10:53:59Z",  
    "value": 0.9890036767805558  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:ef5535ea-a226-4e13-ad18-534fe0998b5e"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:269255de-ebf6-4014-b255-7769687247ae"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:3199df5c-0c82-41fa-8c1c-450850408792"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:756104c3-38c5-400b-9598-4a604d9415e1"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:e8b9c356-91e3-4ff9-a98c-5bcae397ed67"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Valve Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Valve 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T16:14:40Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T03:09:51Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Valve"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Valve type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Valve of limited Valve types"  
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
