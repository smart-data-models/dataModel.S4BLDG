<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：发电机  
======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/ElectricGenerator/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述：**发电机是一种发动机，是将机械能转换为电能的机器。  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `electricGeneratorEfficiency[number]`: 属性。输出能力与接收能力的比率。  - `hasManufacturer[string]`: 属性。识别实体（例如，设备）的制造商的关系。该值应是一个字符串或一个带有语言标签的字符串。  - `hasModel[string]`: 属性。识别实体（例如，设备）的模型的关系。该值应是一个字符串或一个带有语言标签的字符串。  - `id[*]`: 实体的唯一标识符  - `isContainedInBuildingSpace[*]`: 关系。一个用于定义建筑物理空间的实体。一个建筑空间包含设备或建筑对象。(建筑空间)  - `isContainedInPhysicalObject[*]`: 关系。任何具有适当空间区域的物体。  (从DUL本体论中提取的定义）（PhysicalObject）。  - `isSubSystemOf[array]`: 关系。对该物理对象是其一部分的系统的引用。  - `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `name[string]`: 这个项目的名称。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `powerOutputMax[number]`: 属性。发动机的最大额定输出功率。通常以瓦特（W，J/s）衡量。  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `startCurrentFactor[number]`: 财产。IEC。启动电流系数定义了发动机上的窥视启动电流会有多大。StartCurrentFactor乘以NominalCurrent，我们就得到了启动电流。  - `type[string]`: 属性。它必须等于 "ElectricGenerator"。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ElectricGenerator:    
  description: An electric generator is an engine that is a machine for converting mechanical energy into electrical energy.    
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
    electricGeneratorEfficiency:    
      description: Property. The ratio of output capacity to intake capacity.    
      type: number    
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
      anyOf: &electricgenerator_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      anyOf: *electricgenerator_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *electricgenerator_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *electricgenerator_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *electricgenerator_-_properties_-_iscontainedinbuildingspace_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    powerOutputMax:    
      description: 'Property. The maximum output power rating of the engine. Usually measured in Watts (W, J/s).'    
      type: number    
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
    startCurrentFactor:    
      description: Property. IEC. Start current factor defines how large the peek starting current will become on the engine. StartCurrentFactor is multiplied to NominalCurrent and we get the start current.    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: Property. It must be equal to `ElectricGenerator`.    
      enum:    
        - ElectricGenerator    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:ElectricGenerator"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/ElectricGenerator/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/ElectricGenerator/schema.json    
  x-model-tags: SAREF ElectricGenerator    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### ElectricGenerator NGSI-v2 key-values 示例  
这里有一个ElectricGenerator的例子，以JSON-LD格式作为key-values。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ElectricGenerator:544312b1-cba5-41a7-91d3-01a80a845a3f",  
  "type": "ElectricGenerator",  
  "electricGeneratorEfficiency": 0.1422180140007665,  
  "powerOutputMax": 0.9527461650607942,  
  "startCurrentFactor": 0.1882397411007527,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:83f3202e-6ade-4865-8b18-97a89c83039b",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:a864b8bd-fbb6-405c-8fe3-3f9216da550e",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:a8d2e787-8753-475d-bb9e-b00178b72666",  
    "urn:ngsi-ld:System:492633e0-d09d-4bbd-8e27-6cffd4a15812",  
    "urn:ngsi-ld:System:0532ed14-155c-4cec-abde-6c3a6b76d38d"  
  ],  
  "hasManufacturer": "ElectricGenerator Company Inc.",  
  "hasModel": "ElectricGenerator 0.1.2",  
  "dateCreated": "2023-01-26T02:26:35Z",  
  "dateModified": "2023-01-25T19:17:56Z",  
  "source": "Import",  
  "name": "ElectricGenerator",  
  "alternateName": "ElectricGenerator type 2",  
  "description": "ElectricGenerator of limited ElectricGenerator types",  
  "dataProvider": "IFC file"  
}  
```  
</details>  
#### ElectricGenerator NGSI-v2规范化示例  
下面是一个规范化的JSON-LD格式的ElectricGenerator的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ElectricGenerator:df5482f2-2064-41b6-a02c-161a40308684",  
  "type": "ElectricGenerator",  
  "electricGeneratorEfficiency": {  
    "type": "Measurement",  
    "value":  0.7817008930557607  
    }  
  },  
  "powerOutputMax": {  
    "type": "Measurement",  
    "value": {  
      "unitCode": "J/s",  
      "observedAt": "2023-01-25T15:08:28Z",  
      "value": 0.31633906719735727  
    }  
  },  
  "startCurrentFactor": {  
    "type": "Measurement",  
    "value": {  
      "unitCode": "NA",  
      "observedAt": "2023-01-25T17:36:06Z",  
      "value": 0.08027164488059058  
    }  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:BuildingSpace:8ee7d12a-279b-441b-bfe1-63af7f5ae31c"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:PhysicalObject:d49eeb87-a925-46eb-aa1f-6f87bf4a73fb"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:fd638070-ab04-46c2-9e01-ea8a7c2f1676"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:dcd1c3ca-8309-4e52-bc04-430656f0717d"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:95b25770-5b81-427b-b0aa-88d4d13dadb0"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "ElectricGenerator Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "ElectricGenerator 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T08:21:45.4378512+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T00:42:24.4656886+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "ElectricGenerator"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "ElectricGenerator type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "ElectricGenerator of limited ElectricGenerator types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### ElectricGenerator NGSI-LD关键值示例  
这里有一个ElectricGenerator的例子，以JSON-LD格式作为key-values。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ElectricGenerator:544312b1-cba5-41a7-91d3-01a80a845a3f",  
  "type": "ElectricGenerator",  
  "electricGeneratorEfficiency": 0.1422180140007665,  
  "powerOutputMax": 0.9527461650607942,  
  "startCurrentFactor": 0.1882397411007527,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:83f3202e-6ade-4865-8b18-97a89c83039b",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:a864b8bd-fbb6-405c-8fe3-3f9216da550e",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:a8d2e787-8753-475d-bb9e-b00178b72666",  
    "urn:ngsi-ld:System:492633e0-d09d-4bbd-8e27-6cffd4a15812",  
    "urn:ngsi-ld:System:0532ed14-155c-4cec-abde-6c3a6b76d38d"  
  ],  
  "hasManufacturer": "ElectricGenerator Company Inc.",  
  "hasModel": "ElectricGenerator 0.1.2",  
  "dateCreated": "2023-01-26T02:26:35Z",  
  "dateModified": "2023-01-25T19:17:56Z",  
  "source": "Import",  
  "name": "ElectricGenerator",  
  "alternateName": "ElectricGenerator type 2",  
  "description": "ElectricGenerator of limited ElectricGenerator types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### ElectricGenerator NGSI-LD规范化示例  
下面是一个规范化的JSON-LD格式的ElectricGenerator的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ElectricGenerator:88a7d90c-e7c4-4992-8208-3f609cfcc5b7",  
  "type": "ElectricGenerator",  
  "electricGeneratorEfficiency": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T02:32:40Z",  
    "value": 0.4869974917102381  
  },  
  "powerOutputMax": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-26T12:53:37Z",  
    "value": 0.03888572751968955  
  },  
  "startCurrentFactor": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T00:03:03Z",  
    "value": 0.7547514570621776  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:d1cd24e4-7d36-48f5-b337-389d1725ba75"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:5b013e7e-fd90-47c1-a391-18e667674b22"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:2b07a5b3-b3e8-4ecd-bf39-24d0bb9fb3ae"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:2c8d3b81-ff97-414b-8564-b091305027ed"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:58205877-92cd-44d8-afc3-460860eebd7d"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "ElectricGenerator Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "ElectricGenerator 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T02:39:56Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T05:19:07Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "ElectricGenerator"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "ElectricGenerator type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "ElectricGenerator of limited ElectricGenerator types"  
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
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
