<!-- 10-Header -->
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

=========
<!-- 15-License -->


<!-- /15-License -->
<!-- 20-Description -->


<!-- /20-Description -->
<!-- 30-PropertiesList -->




- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `alternateName[string]`: 이 항목의 대체 이름  
<!-- 35-RequiredProperties -->

- `id`  
<!-- 40-RequiredProperties -->
<!-- /40-RequiredProperties -->
<!-- 50-DataModelHeader -->


<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>    

Compressor:    
  description: A compressor is a device that compresses a fluid typically used in a refrigeration circuit.    
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
    compressorSpeed:    
      description: Compressor speed. Usually measured in cycles/s    
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
    hasHotGasBypass:    
      description: 'Whether or not hot gas bypass is provided for the compressor. TRUE = Yes, FALSE = No'    
      type: boolean    
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
    idealCapacity:    
      description: 'Compressor capacity under ideal conditions. Usually measured in Watts (W, J/s)'    
      type: number    
      x-ngsi:    
        type: Property    
    idealShaftPower:    
      description: 'Compressor shaft power under ideal conditions. Usually measured in Watts (W, J/s)'    
      type: number    
      x-ngsi:    
        type: Property    
    impellerDiameter:    
      description: Diameter of compressor impeller - used to scale performance of geometrically similar compressors. Usually measured in millimeters (mm)    
      type: number    
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
    nominalCapacity:    
      description: 'Nominal capacity. Usually measured in Watts (W, J/s)'    
      type: number    
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
    partLoadRatioMax:    
      description: Maximum part load ratio as a fraction of nominal capacity    
      type: number    
      x-ngsi:    
        type: Property    
    partLoadRatioMin:    
      description: Minimum part load ratio as a fraction of nominal capacity    
      type: number    
      x-ngsi:    
        type: Property    
    powerSource:    
      description: Type of power driving the compressor    
      type: string    
      x-ngsi:    
        type: Property    
    refrigerantClass:    
      description: 'Refrigerant class used by the compressor. CFC: Chlorofluorocarbons. HCFC: Hydrochlorofluorocarbons. HFC: Hydrofluorocarbons'    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: It must be equal to `Compressor`    
      enum:    
        - Compressor    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Compressor"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Compressor/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Compressor/schema.json    
  x-model-tags: SAREF Compressor    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->
<!-- 70-MiddleNotes -->
<!-- /70-MiddleNotes -->
<!-- 80-Examples -->



<details><summary><strong>show/hide example</strong></summary>    


  "id": "urn:ngsi-ld:Compressor:99624683-cbb4-4bac-a458-e5bde1df9ff6",  
  "type": "Compressor",  
  "compressorSpeed": 0.679723675842234,  
  "hasHotGasBypass": true,  
  "idealCapacity": 0.7248048000316983,  
  "idealShaftPower": 0.47111429367476765,  
  "impellerDiameter": 0.8496808897888555,  
  "nominalCapacity": 0.8766392143544064,  
  "partLoadRatioMax": 0.5560596438051391,  
  "partLoadRatioMin": 0.22917332777815946,  
  "powerSource": "Practical Steel Chair",  
  "refrigerantClass": "protocol",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:9c3fb868-0647-4480-b105-2221a6cd3354",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:868ed081-1e1b-497f-a18f-11c416e2a90e",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:157c6a62-21ad-4aa4-b3d2-5a0ec1f2c667",  
    "urn:ngsi-ld:System:6fd790f8-68de-4047-a771-4b245c4aff90",  
    "urn:ngsi-ld:System:18a2426a-2c96-4064-959d-98e7aba7904d"  
  ],  
  "hasManufacturer": "Compressor Company Inc.",  
  "hasModel": "Compressor 0.1.2",  
  "dateCreated": "2023-01-26T10:11:46Z",  
  "dateModified": "2023-01-26T05:03:38Z",  
  "source": "Import",  
  "name": "Compressor",  
  "alternateName": "Compressor type 2",  
  "description": "Compressor of limited Compressor types",  
  "dataProvider": "IFC file"  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


  "id": "urn:ngsi-ld:Compressor:5286e31e-5c79-4133-93c4-07c1f3574128",  
  "type": "Compressor",  
  "compressorSpeed": {  
    "type": "Measurement",  
    "value": 0.6951462722377054  
  },  
  "hasHotGasBypass": {  
    "type": "Boolean",  
    "value": true  
  },  
  "idealCapacity": {  
    "type": "Measurement",  
    "value": 0.3445800754974827  
  },  
  "idealShaftPower": {  
    "type": "Measurement",  
    "value": 0.8311250404203112  
  },  
  "impellerDiameter": {  
    "type": "Measurement",  
    "value": 0.868808285450986  
  },  
  "nominalCapacity": {  
    "type": "Measurement",  
    "value": 0.9287385861700207  
  },  
  "partLoadRatioMax": {  
    "type": "Measurement",  
    "value": 0.38901369640969274  
  },  
  "partLoadRatioMin": {  
    "type": "Measurement",  
    "value": 0.9657934764992187  
  },  
  "powerSource": {  
    "type": "Text",  
    "value": "bluetooth"  
  },  
  "refrigerantClass": {  
    "type": "Text",  
    "value": "Fresh"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:BuildingSpace:91df3ba9-787a-4ebb-9be6-ae4c05263de1"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:PhysicalObject:e9909895-084e-4023-9a5a-001322f825f9"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:7ebaae6c-b549-4610-8df4-9c28cebe42a9"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:cedc316a-3057-4f0b-9800-db9757c47286"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:b64d7a83-9d09-405a-82dc-e2dc92ba7ae5"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Compressor Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Compressor 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T08:32:27.8745501+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T12:23:46.0320445+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Compressor"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Compressor type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Compressor of limited Compressor types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


  "id": "urn:ngsi-ld:Compressor:99624683-cbb4-4bac-a458-e5bde1df9ff6",  
  "type": "Compressor",  
  "compressorSpeed": 0.679723675842234,  
  "hasHotGasBypass": true,  
  "idealCapacity": 0.7248048000316983,  
  "idealShaftPower": 0.47111429367476765,  
  "impellerDiameter": 0.8496808897888555,  
  "nominalCapacity": 0.8766392143544064,  
  "partLoadRatioMax": 0.5560596438051391,  
  "partLoadRatioMin": 0.22917332777815946,  
  "powerSource": "Practical Steel Chair",  
  "refrigerantClass": "protocol",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:9c3fb868-0647-4480-b105-2221a6cd3354",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:868ed081-1e1b-497f-a18f-11c416e2a90e",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:157c6a62-21ad-4aa4-b3d2-5a0ec1f2c667",  
    "urn:ngsi-ld:System:6fd790f8-68de-4047-a771-4b245c4aff90",  
    "urn:ngsi-ld:System:18a2426a-2c96-4064-959d-98e7aba7904d"  
  ],  
  "hasManufacturer": "Compressor Company Inc.",  
  "hasModel": "Compressor 0.1.2",  
  "dateCreated": "2023-01-26T10:11:46Z",  
  "dateModified": "2023-01-26T05:03:38Z",  
  "source": "Import",  
  "name": "Compressor",  
  "alternateName": "Compressor type 2",  
  "description": "Compressor of limited Compressor types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


  "id": "urn:ngsi-ld:Compressor:ff065369-a64b-4950-8bcd-ea73c6f6bf34",  
  "type": "Compressor",  
  "compressorSpeed": {  
    "type": "Property",  
    "unitCode": "cycles/s",  
    "observedAt": "2023-01-26T02:36:18Z",  
    "value": 0.23988109283737147  
  },  
  "hasHotGasBypass": {  
    "type": "Property",  
    "value": true  
  },  
  "idealCapacity": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-25T18:17:55Z",  
    "value": 0.37381644415955617  
  },  
  "idealShaftPower": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-25T19:36:02Z",  
    "value": 0.7352666167757617  
  },  
  "impellerDiameter": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-25T16:56:06Z",  
    "value": 0.4819044880876878  
  },  
  "nominalCapacity": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-26T02:02:53Z",  
    "value": 0.42903531710900167  
  },  
  "partLoadRatioMax": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-25T20:48:37Z",  
    "value": 0.44114941929726603  
  },  
  "partLoadRatioMin": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-25T21:57:43Z",  
    "value": 0.8407270037851944  
  },  
  "powerSource": {  
    "type": "Property",  
    "value": "Mississippi"  
  },  
  "refrigerantClass": {  
    "type": "Property",  
    "value": "initiatives"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:200fbc88-04e4-4634-9ab8-31a7ffd7801a"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:6516f3b0-d423-45b0-bcfe-f5a361c118a1"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:0d189ba5-fbb5-42f9-b221-e481ed2215b3"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:682f3690-3403-45d3-8c59-d62b82b2dbb3"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:f346ab7e-bb7c-4da8-853f-f37193cfe98e"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Compressor Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Compressor 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T12:36:15Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-25T17:29:33Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Compressor"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Compressor type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Compressor of limited Compressor types"  
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

<!-- /95-Units -->
<!-- 97-LastFooter -->
---  
