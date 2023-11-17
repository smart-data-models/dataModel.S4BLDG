<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entity：泵    
========<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Pump/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全球描述：**泵是一种对流体或浆液施加机械功，使其通过通道或管道的装置。泵的典型用途是在建筑服务分配系统中循环冷冻水或加热热水。    
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
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `connectionSize[number]`: 泵与泵之间的连接尺寸。通常以毫米（mm）为单位  - `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `flowResistanceMax[number]`: 泵送流体时可承受的摩擦阻力范围。通常以帕斯卡（Pa，N/m2）为单位。  - `flowResistanceMin[number]`: 泵送流体时可承受的摩擦阻力范围。通常以帕斯卡（Pa，N/m2）为单位。  - `hasManufacturer[string]`: 标识实体（如设备）制造商的关系。该值应为字符串或带有语言标记的字符串。  - `hasModel[string]`: 标识实体（如设备）模型的关系。该值应是字符串或带有语言标记的字符串  - `id[*]`: 实体的唯一标识符  - `isContainedInBuildingSpace[*]`: 用于定义楼宇物理空间的实体。建筑空间包含设备或建筑对象。(建筑空间）  - `isContainedInPhysicalObject[*]`: 任何具有适当空间区域的物体。  (从 DUL 本体中提取的定义）（物理对象）  - `isSubSystemOf[array]`: 该物理对象所属系统的引用  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `netPositiveSuctionHead[number]`: 泵入口处防止气蚀的最小液体压力。通常以帕斯卡（Pa，N/m2）为计量单位  - `nomminalRotationSpeed[number]`: 泵在额定条件下的转速。通常以循环/秒为单位  - `operationTemperatureMax[number]`: 允许的运行环境（空气、流体）温度范围。通常以开尔文 (K) 度为单位  - `operationTemperatureMin[number]`: 允许的运行环境（空气、流体）温度范围。通常以开尔文 (K) 度为单位  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `pumpFlowRateMax[number]`: 相对于指定阻力的允许泵送流体体积范围。通常以千克/秒为单位  - `pumpFlowRateMin[number]`: 相对于指定阻力的允许泵送流体体积范围。通常以千克/秒为单位  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `type[string]`: 必须等于 `Pump  <!-- /30-PropertiesList -->    
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
Pump:      
  description: A pump is a device which imparts mechanical work on fluids or slurries to move them through a channel or pipeline. A typical use of a pump is to circulate chilled water or heating hot water in a building services distribution system.      
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
    connectionSize:      
      description: The connection size of the to and from the pump. Usually measured in millimeters (mm)      
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
    flowResistanceMax:      
      description: 'Allowable range of frictional resistance against which the fluid is being pumped. Usually measured in Pascals (Pa, N/m2)'      
      type: number      
      x-ngsi:      
        type: Property      
    flowResistanceMin:      
      description: 'Allowable range of frictional resistance against which the fluid is being pumped. Usually measured in Pascals (Pa, N/m2)'      
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
    netPositiveSuctionHead:      
      description: 'Minimum liquid pressure at the pump inlet to prevent cavitation. Usually measured in Pascals (Pa, N/m2)'      
      type: number      
      x-ngsi:      
        type: Property      
    nomminalRotationSpeed:      
      description: Pump rotational speed under nominal conditions. Usually measured in cycles/s      
      type: number      
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
    pumpFlowRateMax:      
      description: Allowable range of volume of fluid being pumped against the resistance specified. Usually measured in kg/s      
      type: number      
      x-ngsi:      
        type: Property      
    pumpFlowRateMin:      
      description: Allowable range of volume of fluid being pumped against the resistance specified. Usually measured in kg/s      
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
      description: It must be equal to `Pump`      
      enum:      
        - Pump      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Pump"      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Pump/LICENSE.md      
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Pump/schema.json      
  x-model-tags: SAREF Pump      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 有效载荷示例    
#### Pump NGSI-v2 key-values 示例    
下面是一个以 JSON-LD 格式作为键值的 Pump 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Pump:5c6aa613-0829-405e-aeb6-ef000e26fea1",  
  "type": "Pump",  
  "connectionSize": 0.0736674796470771,  
  "flowResistanceMax": 0.5763414622833901,  
  "flowResistanceMin": 0.23194313125611832,  
  "netPositiveSuctionHead": 0.9430406136976697,  
  "nomminalRotationSpeed": 0.49997837892806263,  
  "operationTemperatureMax": 0.016630756942512148,  
  "operationTemperatureMin": 0.7235008225786019,  
  "pumpFlowRateMax": 0.2126600766557486,  
  "pumpFlowRateMin": 0.8849029838139153,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:13846972-f593-4662-96b5-92cefbbe8219",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:54ecdd7e-4ab8-4c41-b56b-47bb45c572f8",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:092c5cb0-1b8e-4bc9-88ee-ce226a23061f",  
    "urn:ngsi-ld:System:053dc8a9-bbb7-402c-8d99-522b8626091d",  
    "urn:ngsi-ld:System:60e0c6c5-ebd6-4460-aa78-442698c8204c"  
  ],  
  "hasManufacturer": "Pump Company Inc.",  
  "hasModel": "Pump 0.1.2",  
  "dateCreated": "2023-01-26T00:41:42Z",  
  "dateModified": "2023-01-26T10:20:35Z",  
  "source": "Import",  
  "name": "Pump",  
  "alternateName": "Pump type 2",  
  "description": "Pump of limited Pump types",  
  "dataProvider": "IFC file"  
}  
```  
</details>    
#### 泵 NGSI-v2 标准化示例    
下面是一个规范化 JSON-LD 格式的 Pump 示例。当不使用选项时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Pump:068a2569-0602-4845-8ed3-8ddb200bdcac",  
  "type": "Pump",  
  "connectionSize": {  
    "type": "Number",  
    "value": 0.8537944550916271  
  },  
  "flowResistanceMax": {  
    "type": "Number",  
    "value": 0.934151218696693  
  },  
  "flowResistanceMin": {  
    "type": "Number",  
    "value": 0.5798733223282941  
  },  
  "netPositiveSuctionHead": {  
    "type": "Number",  
    "value": 0.9236791362464654  
  },  
  "nomminalRotationSpeed": {  
    "type": "Number",  
    "value": 0.9434212309119704  
  },  
  "operationTemperatureMax": {  
    "type": "Number",  
    "value": 0.40126909555034673  
  },  
  "operationTemperatureMin": {  
    "type": "Number",  
    "value": 0.49855896547412504  
  },  
  "pumpFlowRateMax": {  
    "type": "Number",  
    "value": 0.8126244460338075  
  },  
  "pumpFlowRateMin": {  
    "type": "Number",  
    "value": 0.4387979987462379  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:BuildingSpace:30823ddd-b24b-4307-917c-72134cf789aa"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:PhysicalObject:f57afcb5-61fd-4e18-b9e0-4c246e0ed2c2"  
  },  
  "isSubSystemOf": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:System:93229da7-6aa4-42ad-8d91-7d529267dafd",  
      "urn:ngsi-ld:System:cd14cc46-1a6c-4058-ad6c-07b62d4944c0",  
      "urn:ngsi-ld:System:1dcc7d2b-1886-4006-970f-4c44a5213211"  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Pump Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Pump 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T09:00:15.8186104+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T18:30:43.9565309+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Pump"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Pump type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Pump of limited Pump types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>    
#### 泵 NGSI-LD 键值示例    
下面是一个以 JSON-LD 格式作为 key-values 的 Pump 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Pump:5c6aa613-0829-405e-aeb6-ef000e26fea1",  
  "type": "Pump",  
  "connectionSize": 0.0736674796470771,  
  "flowResistanceMax": 0.5763414622833901,  
  "flowResistanceMin": 0.23194313125611832,  
  "netPositiveSuctionHead": 0.9430406136976697,  
  "nomminalRotationSpeed": 0.49997837892806263,  
  "operationTemperatureMax": 0.016630756942512148,  
  "operationTemperatureMin": 0.7235008225786019,  
  "pumpFlowRateMax": 0.2126600766557486,  
  "pumpFlowRateMin": 0.8849029838139153,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:13846972-f593-4662-96b5-92cefbbe8219",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:54ecdd7e-4ab8-4c41-b56b-47bb45c572f8",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:092c5cb0-1b8e-4bc9-88ee-ce226a23061f",  
    "urn:ngsi-ld:System:053dc8a9-bbb7-402c-8d99-522b8626091d",  
    "urn:ngsi-ld:System:60e0c6c5-ebd6-4460-aa78-442698c8204c"  
  ],  
  "hasManufacturer": "Pump Company Inc.",  
  "hasModel": "Pump 0.1.2",  
  "dateCreated": "2023-01-26T00:41:42Z",  
  "dateModified": "2023-01-26T10:20:35Z",  
  "source": "Import",  
  "name": "Pump",  
  "alternateName": "Pump type 2",  
  "description": "Pump of limited Pump types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>    
#### 泵 NGSI-LD 归一化示例    
下面是一个规范化 JSON-LD 格式的 Pump 示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Pump:7ed480ca-f64d-42fd-9d2e-a792829d1467",  
  "type": "Pump",  
  "connectionSize": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T01:56:40Z",  
    "value": 0.439871049852415  
  },  
  "flowResistanceMax": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-26T10:30:54Z",  
    "value": 0.70272326323097  
  },  
  "flowResistanceMin": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-26T11:23:10Z",  
    "value": 0.748100252355086  
  },  
  "netPositiveSuctionHead": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-25T23:42:12Z",  
    "value": 0.4372375818125598  
  },  
  "nomminalRotationSpeed": {  
    "type": "Property",  
    "unitCode": "cycles/s",  
    "observedAt": "2023-01-25T16:47:26Z",  
    "value": 0.9055473204179818  
  },  
  "operationTemperatureMax": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T23:01:07Z",  
    "value": 0.19255105886794588  
  },  
  "operationTemperatureMin": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T02:59:51Z",  
    "value": 0.014765641352581182  
  },  
  "pumpFlowRateMax": {  
    "type": "Property",  
    "unitCode": "kg/s",  
    "observedAt": "2023-01-26T10:06:49Z",  
    "value": 0.2765428009146871  
  },  
  "pumpFlowRateMin": {  
    "type": "Property",  
    "unitCode": "kg/s",  
    "observedAt": "2023-01-26T00:29:22Z",  
    "value": 0.691611788348768  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:00bec903-1682-4d39-9164-6b6635d717c7"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:cf20b915-721e-4f55-b736-af772bdc68c2"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:08e18090-a9f4-4837-a6aa-3d218b14721c"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:646f75aa-9900-4722-98ce-b3811440d0ce"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:00fb7f96-ff82-4b41-8b6e-1e3d2d8b66c3"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Pump Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Pump 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T13:30:12Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-25T15:53:32Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Pump"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Pump type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Pump of limited Pump types"  
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
