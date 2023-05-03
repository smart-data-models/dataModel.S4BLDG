<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: SpaceHeater  
===================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/SpaceHeater/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **Space heaters utilize a combination of radiation and/or natural convection using a heating source such as electricity, steam or hot water to heat a limited space or area. Examples of space heaters include radiators, convectors, baseboard and finned-tube heaters.  UnitaryEquipment should be used for packaged units supporting a combination of heating, cooling, and/or dehumidification; Coil should be used for coil-based floor heating.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `bodyMass[number]`: Property. Overall body mass of the heater. Usually measured in kilograms (kg) or grams (g).  - `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated[string]`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified[string]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description[string]`: A description of this item  - `energySource[string]`: Property. The source of energy. Enumeration defining the energy source or fuel cumbusted to generate heat.  - `hasManufacturer[string]`: Property. A relationship identifying the manufacturer of an entity (e.g., device). The value is expected to be a string or a string with language tag.  - `hasModel[string]`: Property. A relationship identifying the model of an entity (e.g., device). The value is expected to be a string or a string with language tag.  - `heatTransferDimension[string]`: Property. Indicates how heat is transmitted according to the shape of the space heater.  - `heatTransferMedium[string]`: Property. Enumeration defining the heat transfer medium if applicable.  - `id[*]`: Unique identifier of the entity  - `isContainedInBuildingSpace[*]`: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)  - `isContainedInPhysicalObject[*]`: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)  - `isSubSystemOf[array]`: Relationship. A reference to a system(s) that this Physical Object is part of.  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name[string]`: The name of this item.  - `numberOfPanels[number]`: Property. Number of panels.  - `numberOfSections[number]`: Property. Number of sections used.  - `outputCapacity[number]`: Property. Total nominal heat output as listed by the manufacturer. Usually measured in Watts (W, J/s).  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `placementType[string]`: Property. Indicates how the device is designed to be placed.  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `temperatureClassification[string]`: Property. Enumeration defining the temperature classification of the space heater surface temperature. low temperature - surface temperature is relatively low, usually heated by hot water or electricity. high temperature - surface temperature is relatively high, usually heated by gas or steam.  - `thermalEfficiency[number]`: Property. Overall Thermal Efficiency is defined as gross energy output of the heat transfer device divided by the energy input.  - `thermalMassHeatCapacity[number]`: Property. Product of component mass and specific heat.  - `type[string]`: Property. It must be equal to `SpaceHeater`.  <!-- /30-PropertiesList -->  
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
SpaceHeater:    
  description: 'Space heaters utilize a combination of radiation and/or natural convection using a heating source such as electricity, steam or hot water to heat a limited space or area. Examples of space heaters include radiators, convectors, baseboard and finned-tube heaters.  UnitaryEquipment should be used for packaged units supporting a combination of heating, cooling, and/or dehumidification; Coil should be used for coil-based floor heating.'    
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
    bodyMass:    
      description: Property. Overall body mass of the heater. Usually measured in kilograms (kg) or grams (g).    
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
    energySource:    
      description: Property. The source of energy. Enumeration defining the energy source or fuel cumbusted to generate heat.    
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
    heatTransferDimension:    
      description: Property. Indicates how heat is transmitted according to the shape of the space heater.    
      type: string    
      x-ngsi:    
        type: Property    
    heatTransferMedium:    
      description: Property. Enumeration defining the heat transfer medium if applicable.    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &spaceheater_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      anyOf: *spaceheater_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *spaceheater_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *spaceheater_-_properties_-_iscontainedinbuildingspace_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Relationship    
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
    numberOfPanels:    
      description: Property. Number of panels.    
      type: number    
      x-ngsi:    
        type: Property    
    numberOfSections:    
      description: Property. Number of sections used.    
      type: number    
      x-ngsi:    
        type: Property    
    outputCapacity:    
      description: 'Property. Total nominal heat output as listed by the manufacturer. Usually measured in Watts (W, J/s).'    
      type: number    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *spaceheater_-_properties_-_iscontainedinbuildingspace_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    placementType:    
      description: Property. Indicates how the device is designed to be placed.    
      type: string    
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
    temperatureClassification:    
      description: 'Property. Enumeration defining the temperature classification of the space heater surface temperature. low temperature - surface temperature is relatively low, usually heated by hot water or electricity. high temperature - surface temperature is relatively high, usually heated by gas or steam.'    
      type: string    
      x-ngsi:    
        type: Property    
    thermalEfficiency:    
      description: Property. Overall Thermal Efficiency is defined as gross energy output of the heat transfer device divided by the energy input.    
      type: number    
      x-ngsi:    
        type: Property    
    thermalMassHeatCapacity:    
      description: Property. Product of component mass and specific heat.    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: Property. It must be equal to `SpaceHeater`.    
      enum:    
        - SpaceHeater    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:SpaceHeater"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/SpaceHeater/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/SpaceHeater/schema.json    
  x-model-tags: SAREF SpaceHeater    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
#### SpaceHeater NGSI-v2 key-values Example    
Here is an example of a SpaceHeater in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:SpaceHeater:53d2376a-08be-43df-8614-5b506356b56b",  
    "type": "SpaceHeater",  
    "bodyMass": 0.2211394720882921,  
    "energySource": "Research",  
    "heatTransferDimension": "Sleek Rubber Chicken",  
    "heatTransferMedium": "calculating",  
    "numberOfPanels": 0.9912166099910465,  
    "numberOfSections": 0.10463526586778538,  
    "outputCapacity": 0.6425343578878625,  
    "placementType": "auxiliary",  
    "temperatureClassification": "haptic",  
    "thermalEfficiency": 0.996207265881601,  
    "thermalMassHeatCapacity": 0.42035461371680216,  
    "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:a23ba52c-ee89-44f3-8146-cc5642b8a5d4",  
    "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:da56307c-a927-4d61-bc78-329cf0c45486",  
    "isSubSystemOf": [  
        "urn:ngsi-ld:System:8c588da8-ae9d-4339-b35e-3f621435ba77",  
        "urn:ngsi-ld:System:75045902-8a40-4a47-91ed-b55c98c26a56",  
        "urn:ngsi-ld:System:59e00885-77e1-4d66-9c7c-c3d0b2be5b30"  
    ],  
    "hasManufacturer": "SpaceHeater Company Inc.",  
    "hasModel": "SpaceHeater 0.1.2",  
    "dateCreated": "2023-01-26T11:00:53Z",  
    "dateModified": "2023-01-25T20:46:44Z",  
    "source": "Import",  
    "name": "SpaceHeater",  
    "alternateName": "SpaceHeater type 2",  
    "description": "SpaceHeater of limited SpaceHeater types",  
    "dataProvider": "IFC file"  
}  
```  
</details>  
#### SpaceHeater NGSI-v2 normalized Example    
Here is an example of a SpaceHeater in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SpaceHeater:b256e328-b21f-4f37-bcb4-d78364993e79",  
  "type": "SpaceHeater",  
  "bodyMass": 0.7643146073425459,  
  "energySource": {  
    "type": "Text",  
    "value": "Facilitator"  
  },  
  "heatTransferDimension": {  
    "type": "Text",  
    "value": "program"  
  },  
  "heatTransferMedium": {  
    "type": "Text",  
    "value": "Assurance"  
  },  
  "numberOfPanels": {  
    "type": "Float",  
    "value": 0.8127498709428745  
  },  
  "numberOfSections": {  
    "type": "Float",  
    "value": 0.8692658014070345  
  },  
  "outputCapacity": {  
    "type": "Measurement",  
    "value": 0.2717042496203792  
  },  
  "placementType": {  
    "type": "Text",  
    "value": "back up"  
  },  
  "temperatureClassification": {  
    "type": "Text",  
    "value": "SMTP"  
  },  
  "thermalEfficiency": {  
    "type": "Measurement",  
    "value": 0.16328303516805232  
  },  
  "thermalMassHeatCapacity": {  
    "type": "Measurement",  
    "value": 0.17753659327247795  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:BuildingSpace:c1f57310-b1ad-4a70-bdca-70f74bbcc002"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:PhysicalObject:e22ae82c-83a1-4ed9-b1f8-eeced3ba17d9"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:6f519e2b-416a-4b2a-af7b-56974a5d00df"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:16199b91-8c55-4645-8c14-536d1dff0fcc"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:5526ed19-a6fa-4e22-a8bd-71a1027a9b02"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "SpaceHeater Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "SpaceHeater 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T01:19:34.4200755+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T00:26:07.2902986+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "SpaceHeater"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "SpaceHeater type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "SpaceHeater of limited SpaceHeater types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### SpaceHeater NGSI-LD key-values Example    
Here is an example of a SpaceHeater in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SpaceHeater:53d2376a-08be-43df-8614-5b506356b56b",  
  "type": "SpaceHeater",  
  "bodyMass": 0.2211394720882921,  
  "energySource": "Research",  
  "heatTransferDimension": "Sleek Rubber Chicken",  
  "heatTransferMedium": "calculating",  
  "numberOfPanels": 0.9912166099910465,  
  "numberOfSections": 0.10463526586778538,  
  "outputCapacity": 0.6425343578878625,  
  "placementType": "auxiliary",  
  "temperatureClassification": "haptic",  
  "thermalEfficiency": 0.996207265881601,  
  "thermalMassHeatCapacity": 0.42035461371680216,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:a23ba52c-ee89-44f3-8146-cc5642b8a5d4",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:da56307c-a927-4d61-bc78-329cf0c45486",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:8c588da8-ae9d-4339-b35e-3f621435ba77",  
    "urn:ngsi-ld:System:75045902-8a40-4a47-91ed-b55c98c26a56",  
    "urn:ngsi-ld:System:59e00885-77e1-4d66-9c7c-c3d0b2be5b30"  
  ],  
  "hasManufacturer": "SpaceHeater Company Inc.",  
  "hasModel": "SpaceHeater 0.1.2",  
  "dateCreated": "2023-01-26T11:00:53Z",  
  "dateModified": "2023-01-25T20:46:44Z",  
  "source": "Import",  
  "name": "SpaceHeater",  
  "alternateName": "SpaceHeater type 2",  
  "description": "SpaceHeater of limited SpaceHeater types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### SpaceHeater NGSI-LD normalized Example    
Here is an example of a SpaceHeater in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SpaceHeater:61e1adc2-8b00-43d5-89ba-40afbd26cda5",  
  "type": "SpaceHeater",  
  "bodyMass": {  
    "type": "Property",  
    "unitCode": "g",  
    "observedAt": "2023-01-26T04:40:44Z",  
    "value": 0.40152893437379167  
  },  
  "energySource": {  
    "type": "Property",  
    "value": "groupware"  
  },  
  "heatTransferDimension": {  
    "type": "Property",  
    "value": "Licensed Frozen Bike"  
  },  
  "heatTransferMedium": {  
    "type": "Property",  
    "value": "Pakistan Rupee"  
  },  
  "numberOfPanels": {  
    "type": "Property",  
    "value": 0.13243335736611006  
  },  
  "numberOfSections": {  
    "type": "Property",  
    "value": 0.9440399239258307  
  },  
  "outputCapacity": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-26T05:12:20Z",  
    "value": 0.38330998929377036  
  },  
  "placementType": {  
    "type": "Property",  
    "value": "Way"  
  },  
  "temperatureClassification": {  
    "type": "Property",  
    "value": "Kip"  
  },  
  "thermalEfficiency": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-25T15:23:27Z",  
    "value": 0.8451012126787633  
  },  
  "thermalMassHeatCapacity": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-25T22:19:20Z",  
    "value": 0.7853573438622519  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:6018650a-68e3-465a-acb8-e51269656682"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:1bf687c2-f166-4d7b-82ea-e6bf6b5ccd78"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:a538c5b3-c04a-4d42-8cc7-045a50e3b61b"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:8d2af757-8dde-4c47-ade4-b6fe0a649d95"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:6b0fbbf7-519a-4971-b6be-70fbc4a5eadd"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "SpaceHeater Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "SpaceHeater 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T05:11:00Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T02:18:58Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "SpaceHeater"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "SpaceHeater type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "SpaceHeater of limited SpaceHeater types"  
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
