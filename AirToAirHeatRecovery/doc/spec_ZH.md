<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体：空气到空气热回收系统    
=============<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/AirToAirHeatRecovery/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全球说明：**空气对空气热回收装置在进出气流之间采用逆流热交换器。它通常用于将一个腔室中较热空气的热量转移到第二个腔室中较冷空气的热量（即通常用于回收排出的空调空气和向建筑物供应的外部空气中的热量），从而通过减少加热（或冷却）需求来节约能源。    
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
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `hasDefrost[boolean]`: 热交换器是否具有除霜功能  - `hasManufacturer[string]`: 标识实体（如设备）制造商的关系。该值应为字符串或带有语言标记的字符串。  - `hasModel[string]`: 标识实体（如设备）模型的关系。该值应是字符串或带有语言标记的字符串  - `heatTransferTypeEnum[string]`: 两股气流之间的热传递类型  - `id[*]`: 实体的唯一标识符  - `isContainedInBuildingSpace[*]`: 用于定义楼宇物理空间的实体。建筑空间包含设备或建筑对象。(建筑空间）  - `isContainedInPhysicalObject[*]`: 任何具有适当空间区域的物体。  (从 DUL 本体中提取的定义）（物理对象）  - `isSubSystemOf[array]`: 该物理对象所属系统的引用  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `operationTemperatureMax[number]`: 允许的运行环境（空气、流体）温度范围。通常以开尔文 (K) 度为单位  - `operationTemperatureMin[number]`: 允许的运行环境（空气、流体）温度范围。通常以开尔文 (K) 度为单位  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `primaryAirFlowRateMax[number]`: 可输送的最大一次气流。通常以 m3/s 为单位  - `primaryAirFlowRateMin[number]`: 可输送的最小一次气流。通常以 m3/s 为单位  - `secondaryAirFlowRateMax[number]`: 可输送的最大二次气流。通常以帕斯卡（Pa，N/m2）为单位。  - `secondaryAirFlowRateMin[number]`: 可输送的最大二次气流。通常以帕斯卡（Pa，N/m2）为单位。  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `type[string]`: 必须等于 "AirToAirHeatRecovery  <!-- /30-PropertiesList -->    
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
AirToAirHeatRecovery:      
  description: 'An air-to-air heat recovery device employs a counter-flow heat exchanger between inbound and outbound air flow. It is typically used to transfer heat from warmer air in one chamber to cooler air in the second chamber (i.e., typically used to recover heat from the conditioned air being exhausted and the outside air being supplied to a building), resulting in energy savings from reduced heating (or cooling) requirements.'      
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
    hasDefrost:      
      description: Whether the heat exchanger has defrost function or not      
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
    heatTransferTypeEnum:      
      description: Type of heat transfer between the two air streams      
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
        type: Relationship      
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
        type: Relationship      
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
        description: 'The class of systems, i.e., systems virtually isolated from the environment, whose behaviour and interactions with the environment are modeled. Systems can be connected to other systems. Connected systems interact in some ways. Systems can also have subsystems. Properties of subsystems somehow contribute to the properties of the supersystem. (System)'      
        x-ngsi:      
          type: Relationship      
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
    operationTemperatureMax:      
      description: 'Allowable operation ambient (air, fluid) temperature range. Usually measured in degrees Kelvin (K)'      
      type: number      
      x-ngsi:      
        type: Property      
    operationTemperatureMin:      
      description: 'Allowable operation ambient (air, fluid) temperature range. Usually measured in degrees Kelvin (K)'      
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
    primaryAirFlowRateMax:      
      description: Maximum primary airflow that can be delivered. Usually measured in m3/s      
      type: number      
      x-ngsi:      
        type: Property      
    primaryAirFlowRateMin:      
      description: Minimum primary airflow that can be delivered. Usually measured in m3/s      
      type: number      
      x-ngsi:      
        type: Property      
    secondaryAirFlowRateMax:      
      description: 'Maximum secondary airflow that can be delivered. Usually measured in Pascals (Pa, N/m2)'      
      type: number      
      x-ngsi:      
        type: Property      
    secondaryAirFlowRateMin:      
      description: 'Maximum secondary airflow that can be delivered. Usually measured in Pascals (Pa, N/m2)'      
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    type:      
      description: It must be equal to `AirToAirHeatRecovery`      
      enum:      
        - AirToAirHeatRecovery      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:AirToAirHeatRecovery"      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/AirToAirHeatRecovery/LICENSE.md      
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/AirToAirHeatRecovery/schema.json      
  x-model-tags: SAREF AirToAirHeatRecovery      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 有效载荷示例    
#### AirToAirHeatRecovery NGSI-v2 键值示例    
下面是一个以 JSON-LD 格式作为键值的 AirToAirHeatRecovery 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AirToAirHeatRecovery:8c59d316-ed05-4b56-bec3-886379421239",  
  "type": "AirToAirHeatRecovery",  
  "hasDefrost": false,  
  "heatTransferTypeEnum": "24/7",  
  "operationTemperatureMax": 0.8198825347384565,  
  "operationTemperatureMin": 0.505815040579818,  
  "primaryAirFlowRateMax": 0.2511282384018223,  
  "primaryAirFlowRateMin": 0.8540184208518826,  
  "secondaryAirFlowRateMax": 0.913617698002923,  
  "secondaryAirFlowRateMin": 0.17456040773539583,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:018e6821-b097-4029-9cbb-207ae7e5ddca",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:ad795f1c-0754-4877-acc2-2dcc3b337edd",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:c92bd8da-e37f-4f64-989b-6007925a053b",  
    "urn:ngsi-ld:System:5642f604-3a36-49c3-b178-3e7b99eca071",  
    "urn:ngsi-ld:System:2f04039b-ef4e-4d61-8232-e786a220b927"  
  ],  
  "hasManufacturer": "AirToAirHeatRecovery Company Inc.",  
  "hasModel": "AirToAirHeatRecovery 0.1.2",  
  "dateCreated": "2023-01-25T18:33:19Z",  
  "dateModified": "2023-01-25T17:11:08Z",  
  "source": "Import",  
  "name": "AirToAirHeatRecovery",  
  "alternateName": "AirToAirHeatRecovery type 2",  
  "description": "AirToAirHeatRecovery of limited AirToAirHeatRecovery types",  
  "dataProvider": "IFC file"  
}  
```  
</details>    
#### AirToAirHeatRecovery NGSI-v2 标准化示例    
下面是一个规范化 JSON-LD 格式的 AirToAirHeatRecovery 示例。在不使用选项时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AirToAirHeatRecovery:a732b90e-0296-47c9-ab0f-34f6de5edfb4",  
  "type": "AirToAirHeatRecovery",  
  "hasDefrost": {  
    "type": "Boolean",  
    "value": true  
  },  
  "heatTransferTypeEnum": {  
    "type": "Text",  
    "value": "Future"  
  },  
  "operationTemperatureMax": {  
    "type": "Number",  
    "value": 0.9053685058368695  
  },  
  "operationTemperatureMin": {  
    "type": "Number",  
    "value": 0.0225751895192714  
  },  
  "primaryAirFlowRateMax": {  
    "type": "Number",  
    "value": 0.6828734611896666  
  },  
  "primaryAirFlowRateMin": {  
    "type": "Number",  
    "value": 0.48874342661652126  
  },  
  "secondaryAirFlowRateMax": {  
    "type": "Number",  
    "value": 0.36804021603434756  
  },  
  "secondaryAirFlowRateMin": {  
    "type": "Number",  
    "value": 0.28401066550404996  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:BuildingSpace:2058c38a-eb2e-4001-af3f-9a93effd41ac"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:PhysicalObject:ea1b1b2c-cb04-429d-bf2c-ca99e7f3f005"  
  },  
  "isSubSystemOf": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:System:123d10ff-2c3a-40f4-9fd0-07851a7d7a3c",  
      "urn:ngsi-ld:System:90a762d4-7eed-4d5a-8a0d-a4676773917f",  
      "urn:ngsi-ld:System:b9899a7a-dc77-43a1-a0df-5a4134af3004"  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "AirToAirHeatRecovery Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "AirToAirHeatRecovery 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T00:34:42.9211606+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T13:58:25.8715515+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "AirToAirHeatRecovery"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "AirToAirHeatRecovery type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "AirToAirHeatRecovery of limited AirToAirHeatRecovery types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>    
#### AirToAirHeatRecovery NGSI-LD 键值示例    
下面是一个以 JSON-LD 格式作为键值的 AirToAirHeatRecovery 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AirToAirHeatRecovery:8c59d316-ed05-4b56-bec3-886379421239",  
  "type": "AirToAirHeatRecovery",  
  "hasDefrost": false,  
  "heatTransferTypeEnum": "24/7",  
  "operationTemperatureMax": 0.8198825347384565,  
  "operationTemperatureMin": 0.505815040579818,  
  "primaryAirFlowRateMax": 0.2511282384018223,  
  "primaryAirFlowRateMin": 0.8540184208518826,  
  "secondaryAirFlowRateMax": 0.913617698002923,  
  "secondaryAirFlowRateMin": 0.17456040773539583,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:018e6821-b097-4029-9cbb-207ae7e5ddca",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:ad795f1c-0754-4877-acc2-2dcc3b337edd",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:c92bd8da-e37f-4f64-989b-6007925a053b",  
    "urn:ngsi-ld:System:5642f604-3a36-49c3-b178-3e7b99eca071",  
    "urn:ngsi-ld:System:2f04039b-ef4e-4d61-8232-e786a220b927"  
  ],  
  "hasManufacturer": "AirToAirHeatRecovery Company Inc.",  
  "hasModel": "AirToAirHeatRecovery 0.1.2",  
  "dateCreated": "2023-01-25T18:33:19Z",  
  "dateModified": "2023-01-25T17:11:08Z",  
  "source": "Import",  
  "name": "AirToAirHeatRecovery",  
  "alternateName": "AirToAirHeatRecovery type 2",  
  "description": "AirToAirHeatRecovery of limited AirToAirHeatRecovery types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>    
#### AirToAirHeatRecovery NGSI-LD 归一化示例    
下面是一个规范化 JSON-LD 格式的 AirToAirHeatRecovery 示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AirToAirHeatRecovery:a8cd6aa9-dd5f-48bf-ba9f-3db11843b050",  
  "type": "AirToAirHeatRecovery",  
  "hasDefrost": {  
    "type": "Property",  
    "value": false  
  },  
  "heatTransferTypeEnum": {  
    "type": "Property",  
    "value": "Street"  
  },  
  "operationTemperatureMax": {  
    "type": "Property",  
    "value": {  
      "unitCode": "K",  
      "observedAt": "2023-01-26T02:03:09Z",  
      "value": 0.09206773488147657  
    }  
  },  
  "operationTemperatureMin": {  
    "type": "Property",  
    "value": {  
      "unitCode": "K",  
      "observedAt": "2023-01-26T09:23:23Z",  
      "value": 0.04773015112848933  
    }  
  },  
  "primaryAirFlowRateMax": {  
    "type": "Property",  
    "value": {  
      "unitCode": "m3/s",  
      "observedAt": "2023-01-25T15:19:05Z",  
      "value": 0.04143347387591234  
    }  
  },  
  "primaryAirFlowRateMin": {  
    "type": "Property",  
    "value": {  
      "unitCode": "m3/s",  
      "observedAt": "2023-01-26T00:05:48Z",  
      "value": 0.9113949488212527  
    }  
  },  
  "secondaryAirFlowRateMax": {  
    "type": "Property",  
    "value": {  
      "unitCode": "N/m2",  
      "observedAt": "2023-01-26T02:57:23Z",  
      "value": 0.391335331160202  
    }  
  },  
  "secondaryAirFlowRateMin": {  
    "type": "Property",  
    "value": {  
      "unitCode": "N/m2",  
      "observedAt": "2023-01-26T08:54:29Z",  
      "value": 0.9115616360325159  
    }  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:f9f09bbc-27ef-4bd0-991f-6dd8720f5e7b"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:79a8986d-8526-4608-b216-ea4eb2d147ac"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:fae709e8-6311-4179-acfd-7b79e92d095c"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:4c06efa1-0d47-4a8a-a38c-d0783a106972"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:a3120479-fd3a-4a34-915c-418000e05d2b"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "AirToAirHeatRecovery Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "AirToAirHeatRecovery 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-25T23:15:35Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-26T07:30:02Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "AirToAirHeatRecovery"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "AirToAirHeatRecovery type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "AirToAirHeatRecovery of limited AirToAirHeatRecovery types"  
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
