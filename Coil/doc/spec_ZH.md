<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体：线圈    
=====<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Coil/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全局描述：**盘管是一种用于在非混合介质之间进行热传递的装置。一个常见的例子是冷却盘管，它利用翅片盘管中的冷冻水、防冻剂或制冷剂进行循环，用于去除在盘管表面移动的空气中的热量。盘管既可用于加热，也可用于冷却，方法是将一系列输送加热或冷却流体的管子（盘管）放入气流中。盘管可以由蛇形管或翅片管组成，翅片管可以提供更宽的传热表面。  盘管也可用于非气流情况，如嵌入楼板**。    
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
- `airFlowRateMax[number]`: 最大允许空气流量。通常以 m3/s 为单位  - `airFlowRateMin[number]`: 最小允许空气流速。通常以 m3/s 为单位  - `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `hasManufacturer[string]`: 标识实体（如设备）制造商的关系。该值应为字符串或带有语言标记的字符串。  - `hasModel[string]`: 标识实体（如设备）模型的关系。该值应是字符串或带有语言标记的字符串  - `id[*]`: 实体的唯一标识符  - `isContainedInBuildingSpace[*]`: 用于定义楼宇物理空间的实体。建筑空间包含设备或建筑对象。(建筑空间）  - `isContainedInPhysicalObject[*]`: 任何具有适当空间区域的物体。  (从 DUL 本体中提取的定义）（物理对象）  - `isSubSystemOf[array]`: 该物理对象所属系统的引用  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `nominalLatentCapacity[number]`: 名义潜容量。通常以瓦特（W，J/s）为计量单位  - `nominalSensibleCapacity[number]`: 标称显焓。通常以瓦特（W，J/s）为计量单位  - `nominalUa[number]`: 名义 UA 值  - `operationMode[string]`: 该线圈的运行模式  - `operationTemperatureMax[number]`: 允许的运行环境（空气、流体）温度范围。通常以开尔文 (K) 度为单位  - `operationTemperatureMin[number]`: 允许的运行环境（空气、流体）温度范围。通常以开尔文 (K) 度为单位  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `placementType[string]`: 表示设备的设计放置方式  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `type[string]`: 必须等于 "线圈  <!-- /30-PropertiesList -->    
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
Coil:      
  description: 'A coil is a device used to provide heat transfer between non-mixing media. A common example is a cooling coil, which utilizes a finned coil in which circulates chilled water, antifreeze, or refrigerant that is used to remove heat from air moving across the surface of the coil. A coil may be used either for heating or cooling purposes by placing a series of tubes (the coil) carrying a heating or cooling fluid into an airstream. The coil may be constructed from tubes bundled in a serpentine form or from finned tubes that give a extended heat transfer surface.  Coils may also be used for non-airflow cases such as embedded in a floor slab.'      
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
    airFlowRateMax:      
      description: Maximum allowable air flow rate. Usually measured in m3/s      
      type: number      
      x-ngsi:      
        type: Property      
    airFlowRateMin:      
      description: Minimum allowable air flow rate. Usually measured in m3/s      
      type: number      
      x-ngsi:      
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
    nominalLatentCapacity:      
      description: 'Nominal latent capacity. Usually measured in Watts (W, J/s)'      
      type: number      
      x-ngsi:      
        type: Property      
    nominalSensibleCapacity:      
      description: 'Nominal sensible capacity. Usually measured in Watts (W, J/s)'      
      type: number      
      x-ngsi:      
        type: Property      
    nominalUa:      
      description: Nominal UA value      
      type: number      
      x-ngsi:      
        type: Property      
    operationMode:      
      description: Operation mode of this coil      
      enum:      
        - cooling      
        - heating      
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
    placementType:      
      description: Indicates how the device is designed to be placed      
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
      description: It must be equal to `Coil`      
      enum:      
        - Coil      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Coil"      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Coil/LICENSE.md      
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Coil/schema.json      
  x-model-tags: SAREF Coil      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 有效载荷示例    
#### 线圈 NGSI-v2 键值示例    
下面是一个以 JSON-LD 格式作为键值的线圈示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Coil:180d0665-9242-42c6-b336-d7edcf8fc3b5",  
  "type": "Coil",  
  "airFlowRateMax": 0.22332143818011307,  
  "airFlowRateMin": 0.6369516028350278,  
  "nominalLatentCapacity": 0.9394595315602638,  
  "nominalSensibleCapacity": {  
    "type": 0.8014808985276609,  
    "nominalUa": 0.3738979404823001,  
    "operationMode": "cooling",  
    "operationTemperatureMax": 0.7510713399220631,  
    "operationTemperatureMin": 0.8674252304724047,  
    "placementType": "Money Market Account",  
    "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:c562a0a7-6355-46a0-a528-ebeea1b5af39",  
    "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:7d4df444-5662-45c4-81e8-28dd9e2ab52e",  
    "isSubSystemOf": [  
      "urn:ngsi-ld:System:98486c90-52da-48cf-af50-69449370e3b9",  
      "urn:ngsi-ld:System:afe412c8-8366-4eb1-b834-dc68c1e3d828",  
      "urn:ngsi-ld:System:b851de9e-48bd-4363-9d01-b17ab9469aea"  
    ],  
    "hasManufacturer": "Coil Company Inc.",  
    "hasModel": "Coil 0.1.2",  
    "dateCreated": "2023-01-25T23:02:47Z",  
    "dateModified": "2023-01-26T14:02:17Z",  
    "source": "Import",  
    "name": "Coil",  
    "alternateName": "Coil type 2",  
    "description": "Coil of limited Coil types",  
    "dataProvider": "IFC file"  
  }  
```  
</details>    
#### 卷材 NGSI-v2 标准化示例    
下面是一个以 JSON-LD 格式规范化的线圈示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Coil:13d40aef-8b95-4cb2-af1e-483e4c874941",  
  "type": "Coil",  
  "airFlowRateMax": {  
    "type": "Measurement",  
    "value": 0.6477373611080879  
  },  
  "airFlowRateMin": {  
    "type": "Measurement",  
    "value": 0.1367768463223733  
  },  
  "nominalLatentCapacity": {  
    "type": "Measurement",  
    "value": 0.6823953079495582  
  },  
  "nominalSensibleCapacity": {  
    "type": "Measurement",  
    "value": 0.9661532549311025  
  },  
  "nominalUa": {  
    "type": "Measurement",  
    "value": 0.5711236580496344  
  },  
  "operationMode": {  
    "type": "CoilOperationMode",  
    "value": "cooling"  
  },  
  "operationTemperatureMax": {  
    "type": "Measurement",  
    "value": 0.5575891151602635  
  },  
  "operationTemperatureMin": {  
    "type": "Measurement",  
    "value": 0.8396275897283132  
  },  
  "placementType": {  
    "type": "Text",  
    "value": "Buckinghamshire"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:BuildingSpace:1070b255-7508-4019-ba0a-1ce8a03cf3b1"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:PhysicalObject:cef12274-adeb-41a5-aec1-8e254593bb26"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:65b917e6-ec39-4e2e-bce1-a52a52c176bc"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:61834f7f-655f-47f1-828c-755a25e7b026"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:ab77fbe9-a323-477c-81bf-a9923abdf8ea"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Coil Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Coil 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T04:03:32.1629228+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T16:59:28.4436033+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Coil"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Coil type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Coil of limited Coil types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>    
#### 线圈 NGSI-LD 键值示例    
下面是一个以 JSON-LD 格式作为键值的线圈示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Coil:180d0665-9242-42c6-b336-d7edcf8fc3b5",  
  "type": "Coil",  
  "airFlowRateMax": 0.22332143818011307,  
  "airFlowRateMin": 0.6369516028350278,  
  "nominalLatentCapacity": 0.9394595315602638,  
  "nominalSensibleCapacity": {  
    "type": 0.8014808985276609,  
    "nominalUa": 0.3738979404823001,  
    "operationMode": "cooling",  
    "operationTemperatureMax": 0.7510713399220631,  
    "operationTemperatureMin": 0.8674252304724047,  
    "placementType": "Money Market Account",  
    "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:c562a0a7-6355-46a0-a528-ebeea1b5af39",  
    "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:7d4df444-5662-45c4-81e8-28dd9e2ab52e",  
    "isSubSystemOf": [  
      "urn:ngsi-ld:System:98486c90-52da-48cf-af50-69449370e3b9",  
      "urn:ngsi-ld:System:afe412c8-8366-4eb1-b834-dc68c1e3d828",  
      "urn:ngsi-ld:System:b851de9e-48bd-4363-9d01-b17ab9469aea"  
    ],  
    "hasManufacturer": "Coil Company Inc.",  
    "hasModel": "Coil 0.1.2",  
    "dateCreated": "2023-01-25T23:02:47Z",  
    "dateModified": "2023-01-26T14:02:17Z",  
    "source": "Import",  
    "name": "Coil",  
    "alternateName": "Coil type 2",  
    "description": "Coil of limited Coil types",  
    "dataProvider": "IFC file",  
    "@context": [  
      "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
      "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
  }  
```  
</details>    
#### 线圈 NGSI-LD 归一化示例    
下面是一个以 JSON-LD 格式规范化的线圈示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Coil:fcc6fa4b-fa43-42de-af7d-c8be6efda789",  
  "type": "Coil",  
  "airFlowRateMax": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-25T22:00:31Z",  
    "value": 0.461404719601072  
  },  
  "airFlowRateMin": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-26T12:18:55Z",  
    "value": 0.3100905584892091  
  },  
  "nominalLatentCapacity": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-25T15:57:00Z",  
    "value": 0.0859276056343462  
  },  
  "nominalSensibleCapacity": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-25T15:07:49Z",  
    "value": 0.9959034840230547  
  },  
  "nominalUa": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-25T16:07:27Z",  
    "value": 0.03766746157415857  
  },  
  "operationMode": {  
    "type": "Property",  
    "value": "cooling"  
  },  
  "operationTemperatureMax": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T15:22:24Z",  
    "value": 0.18992025947801072  
  },  
  "operationTemperatureMin": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T07:51:42Z",  
    "value": 0.6342100760763256  
  },  
  "placementType": {  
    "type": "Property",  
    "value": "SQL"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:61d397a1-954d-40ec-a4cc-cba2c10a07ca"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:ee042545-32fa-4adb-97e1-5007ccabcd63"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:cab59172-6cb8-443e-94b8-b6270aaa5e60"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:73b9f71e-63bb-49bf-96ef-f6f4922f4245"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:7607ea00-30f7-4271-a0f3-c0b1755be875"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Coil Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Coil 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T04:20:07Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-25T16:46:30Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Coil"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Coil type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Coil of limited Coil types"  
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
