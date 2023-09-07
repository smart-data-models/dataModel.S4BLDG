<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：加湿器  
======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Humidifier/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球说明：**加湿器是一种向空气中添加水分的装置。  
版本： 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理    
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: 该项目的替代名称  - `application[string]`: 加湿器应用。固定式：加湿器安装在管道式流量分配系统中。便携式：加湿器未安装在管道式流量分配系统中  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `hasManufacturer[string]`: 标识实体（如设备）制造商的关系。该值应为字符串或带有语言标记的字符串。  - `hasModel[string]`: 标识实体（如设备）模型的关系。该值应是字符串或带有语言标记的字符串  - `id[*]`: 实体的唯一标识符  - `internalControl[string]`: 内部调制控制  - `isContainedInBuildingSpace[*]`: 用于定义楼宇物理空间的实体。建筑空间包含设备或建筑对象。(建筑空间）  - `isContainedInPhysicalObject[*]`: 任何具有适当空间区域的物体。  (从 DUL 本体中提取的定义）（物理对象）  - `isSubSystemOf[array]`: 该物理对象所属系统的引用  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `nominalAirFlowRate[number]`: 名义气流速度。通常以 m3/s 为单位  - `nominalMoistureGain[number]`: 添加到气流中的水蒸气的名义速率。通常以千克/秒为单位  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `type[string]`: 必须等于 "加湿器  - `waterRequirement[number]`: 补水需求。通常以 m3/s 为单位  - `weight[number]`: 设备的重量。通常以千克（kg）或克（g）为单位。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排列（点击查看详情）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Humidifier:    
  description: A humidifier is a device that adds moisture into the air.    
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
    application:    
      description: 'Humidifier application. Fixed: Humidifier installed in a ducted flow distribution system. Portable: Humidifier is not installed in a ducted flow distribution system'    
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
    internalControl:    
      description: Internal modulation control    
      type: string    
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
    nominalAirFlowRate:    
      description: Nominal rate of air flow. Usually measured in m3/s    
      type: number    
      x-ngsi:    
        type: Property    
    nominalMoistureGain:    
      description: Nominal rate of water vapor added into the airstream. Usually measured in kg/s    
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
      description: It must be equal to `Humidifier`    
      enum:    
        - Humidifier    
      type: string    
      x-ngsi:    
        type: Property    
    waterRequirement:    
      description: Make-up water requirement. Usually measured in m3/s    
      type: number    
      x-ngsi:    
        type: Property    
    weight:    
      description: The weight of the device. Usually measured in kilograms (kg) or grams (g)    
      type: number    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Humidifier"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Humidifier/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Humidifier/schema.json    
  x-model-tags: SAREF Humidifier    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 有效载荷示例  
#### 加湿器 NGSI-v2 关键值示例  
下面是一个以 JSON-LD 格式作为键值的加湿器示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Humidifier:ac37f3cb-91a4-420a-bf0c-0b9e7e172521",  
    "type": "Humidifier",  
    "application": "Trafficway",  
    "internalControl": "circuit",  
    "nominalAirFlowRate": 0.5067643159622129,  
    "nominalMoistureGain": 0.6949833248374234,  
    "waterRequirement": 0.006912028133186698,  
    "weight": 0.0357306217024943,  
    "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:09a4b404-f422-4f1c-b53e-23fabedd21c7",  
    "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:dea722e2-f244-4618-bd6d-40a74f6053c7",  
    "isSubSystemOf": [  
        "urn:ngsi-ld:System:7d1ab6f4-93d8-45f1-8075-e07d9f0a92ab",  
        "urn:ngsi-ld:System:97c9fe52-5019-4f15-9e09-b74248a9e008",  
        "urn:ngsi-ld:System:4adb71a2-0ae3-4ecc-9d29-9e913f5cb577"  
    ],  
    "hasManufacturer": "Humidifier Company Inc.",  
    "hasModel": "Humidifier 0.1.2",  
    "dateCreated": "2023-01-26T01:28:19Z",  
    "dateModified": "2023-01-26T00:58:24Z",  
    "source": "Import",  
    "name": "Humidifier",  
    "alternateName": "Humidifier type 2",  
    "description": "Humidifier of limited Humidifier types",  
    "dataProvider": "IFC file"  
}  
```  
</details>  
#### 加湿器 NGSI-v2 标准化示例  
下面是一个规范化 JSON-LD 格式的加湿器示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Humidifier:fba02151-cd4b-4dfd-a7a7-37dafa66d943",  
  "type": "Humidifier",  
  "application": {  
    "type": "Text",  
    "value": "Small Soft Car"  
  },  
  "internalControl": {  
    "type": "Text",  
    "value": "mindshare"  
  },  
  "nominalAirFlowRate": {  
    "type": "Measurement",  
    "value":  0.9292903711390679  
  },  
  "nominalMoistureGain": {  
    "type": "Measurement",  
    "value":  0.8580622286778447  
  },  
  "waterRequirement": {  
    "type": "Measurement",  
    "value": 0.554538436027498  
  },  
  "weight": {  
    "type": "Measurement",  
    "value": 0.7752621626916505  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:BuildingSpace:e921e031-412b-425c-931b-c63634eb5c85"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:PhysicalObject:013cd1d5-1e31-4a2a-a666-8e18c85a0360"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:ea1d1a76-356e-491c-b5dc-17a8c456d7f7"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:f7b44810-8762-4e67-b4d0-6e4d9bb81b46"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:88bb7831-63c5-40bc-8349-7cef821db39c"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Humidifier Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Humidifier 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T08:47:34.1843489+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T06:27:14.5040882+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Humidifier"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Humidifier type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Humidifier of limited Humidifier types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### 加湿器 NGSI-LD 键值示例  
下面是一个以 JSON-LD 格式作为键值的加湿器示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Humidifier:ac37f3cb-91a4-420a-bf0c-0b9e7e172521",  
  "type": "Humidifier",  
  "application": "Trafficway",  
  "internalControl": "circuit",  
  "nominalAirFlowRate": 0.5067643159622129,  
  "nominalMoistureGain": 0.6949833248374234,  
  "waterRequirement": 0.006912028133186698,  
  "weight": 0.0357306217024943,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:09a4b404-f422-4f1c-b53e-23fabedd21c7",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:dea722e2-f244-4618-bd6d-40a74f6053c7",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:7d1ab6f4-93d8-45f1-8075-e07d9f0a92ab",  
    "urn:ngsi-ld:System:97c9fe52-5019-4f15-9e09-b74248a9e008",  
    "urn:ngsi-ld:System:4adb71a2-0ae3-4ecc-9d29-9e913f5cb577"  
  ],  
  "hasManufacturer": "Humidifier Company Inc.",  
  "hasModel": "Humidifier 0.1.2",  
  "dateCreated": "2023-01-26T01:28:19Z",  
  "dateModified": "2023-01-26T00:58:24Z",  
  "source": "Import",  
  "name": "Humidifier",  
  "alternateName": "Humidifier type 2",  
  "description": "Humidifier of limited Humidifier types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### 加湿器 NGSI-LD 归一化示例  
下面是一个规范化 JSON-LD 格式的加湿器示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Humidifier:7535836f-92b5-4489-b99c-424fab29c039",  
  "type": "Humidifier",  
  "application": {  
    "type": "Property",  
    "value": "payment"  
  },  
  "internalControl": {  
    "type": "Property",  
    "value": "national"  
  },  
  "nominalAirFlowRate": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-25T23:50:20Z",  
    "value": 0.6517710650891719  
  },  
  "nominalMoistureGain": {  
    "type": "Property",  
    "unitCode": "kg/s",  
    "observedAt": "2023-01-26T00:47:56Z",  
    "value": 0.7521424188536304  
  },  
  "waterRequirement": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-26T04:16:30Z",  
    "value": 0.37658219788129976  
  },  
  "weight": {  
    "type": "Property",  
    "unitCode": "g",  
    "observedAt": "2023-01-25T20:12:20Z",  
    "value": 0.348798884385924  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:89364634-51b8-4628-b785-be02d50d9653"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:748df8f3-6595-4591-bc38-4e393a942194"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:45f04a26-3ae7-4a68-a960-4e4c9667bbb8"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:b619039a-e060-41ce-8e61-cdbc63e86287"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:94b68acc-bf31-40d7-a089-1172ff14240a"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Humidifier Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Humidifier 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T19:33:58Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T04:06:21Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Humidifier"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Humidifier type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Humidifier of limited Humidifier types"  
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
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
