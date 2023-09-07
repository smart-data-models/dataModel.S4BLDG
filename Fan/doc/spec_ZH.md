<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：粉丝  
=====<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Fan/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述：**风扇是一种对气体施加机械功的装置。风扇的典型用途是在建筑服务空气分配系统中产生气流。  
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
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `capacityControlType[string]`: 入口叶片：通过调节进气叶片进行控制。变速驱动：通过变速驱动器进行控制。叶片间距角： 通过调整叶片间距角进行控制：通过调整叶片间距角进行控制。双速通过切换高速和低速进行控制。卸料阻尼器通过调节排气风门进行控制  - `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `hasManufacturer[string]`: 标识实体（如设备）制造商的关系。该值应为字符串或带有语言标记的字符串。  - `hasModel[string]`: 标识实体（如设备）模型的关系。该值应是字符串或带有语言标记的字符串  - `id[*]`: 实体的唯一标识符  - `isContainedInBuildingSpace[*]`: 用于定义楼宇物理空间的实体。建筑空间包含设备或建筑对象。(建筑空间）  - `isContainedInPhysicalObject[*]`: 任何具有适当空间区域的物体。  (从 DUL 本体中提取的定义）（物理对象）  - `isSubSystemOf[array]`: 该物理对象所属系统的引用  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `motorDriveType[string]`: 电机驱动类型：DIRECTDRIVE: 直接驱动。BELTDRIVE：皮带传动。COUPLING：联轴器。OTHER：其他电机驱动类型。UNKNOWN：未知电机驱动类型。  - `name[string]`: 该项目的名称  - `nominalAirFlowRate[number]`: 名义气流速度。通常以 m3/s 为单位  - `nominalPowerRate[number]`: 额定风扇功率率，通常以瓦特（W，J/s）为单位。  - `nominalRotationSpeed[number]`: 名义风扇转速。通常以周期/秒为单位  - `nominalStaticPressure[number]`: 风扇为确保空气流通而必须克服的气流内静压。通常以帕斯卡（Pa，N/m2）为单位。  - `nominalTotalPressure[number]`: 风扇上的额定总压升。通常以帕斯卡（Pa，N/m2）为单位。  - `operationMode[string]`: 该风扇的运行模式  - `operationTemperatureMax[number]`: 允许的运行环境（空气、流体）温度范围。通常以开尔文 (K) 度为单位  - `operationTemperatureMin[number]`: 允许的运行环境（空气、流体）温度范围。通常以开尔文 (K) 度为单位  - `operationalRiterial[number]`: 在最高运行环境空气温度下的运行时间。以秒 (s) 或天 (d) 或其他时间单位计量  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `type[string]`: 必须等于 `Fan`  <!-- /30-PropertiesList -->  
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
Fan:    
  description: A fan is a device which imparts mechanical work on a gas. A typical usage of a fan is to induce airflow in a building services air distribution system.    
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
    capacityControlType:    
      description: 'InletVane: Control by adjusting inlet vane. VariableSpeedDrive: Control by variable speed drive. BladePitchAngle: Control by adjusting blade pitch angle. TwoSpeed: Control by switch between high and low speed. DischargeDamper: Control by modulating discharge damper'    
      type: string    
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
    motorDriveType:    
      description: 'Motor drive type: DIRECTDRIVE: Direct drive. BELTDRIVE: Belt drive. COUPLING: Coupling. OTHER: Other type of motor drive. UNKNOWN: Unknown motor drive type. '    
      type: string    
      x-ngsi:    
        type: Property    
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
    nominalPowerRate:    
      description: 'Nominal fan power rate.Usually measured in Watts (W, J/s)'    
      type: number    
      x-ngsi:    
        type: Property    
    nominalRotationSpeed:    
      description: Nominal fan wheel speed. Usually measured in cycles/s    
      type: number    
      x-ngsi:    
        type: Property    
    nominalStaticPressure:    
      description: 'The static pressure within the air stream that the fan must overcome to insure designed circulation of air. Usually measured in Pascals (Pa, N/m2)'    
      type: number    
      x-ngsi:    
        type: Property    
    nominalTotalPressure:    
      description: 'Nominal total pressure rise across the fan. Usually measured in Pascals (Pa, N/m2)'    
      type: number    
      x-ngsi:    
        type: Property    
    operationMode:    
      description: Operation mode of this fan    
      enum:    
        - supply    
        - exhaust    
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
    operationalRiterial:    
      description: Time of operation at maximum operational ambient air temperature. Measured in seconds (s) or days (d) or other units of time    
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
      description: It must be equal to `Fan`    
      enum:    
        - Fan    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Fan"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Fan/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Fan/schema.json    
  x-model-tags: SAREF Fan    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 有效载荷示例  
#### 扇形 NGSI-v2 键值示例  
下面是一个以 JSON-LD 格式作为 key-values 的 Fan 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Fan:7cfafc6e-ab2a-4af0-94b0-d4ed9c92e2d9",  
    "type": "Fan",  
    "capacityControlType": "e-markets",  
    "motorDriveType": "gold",  
    "nominalAirFlowRate": 0.5484285000109488,  
    "nominalPowerRate": 0.4651302623864956,  
    "nominalRotationSpeed": 0.586889938002957,  
    "nominalStaticPressure": 0.3508757713471129,  
    "nominalTotalPressure": 0.7008373891464377,  
    "operationalRiterial": 0.3901575132094196,  
    "operationMode": "supply",  
    "operationTemperatureMax": 0.9178812499585061,  
    "operationTemperatureMin": 0.5225885446624712,  
    "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:38fc3969-81c7-4c67-a564-fdbe6353726a",  
    "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:722ffa89-4091-423f-832c-3af82a48d406",  
    "isSubSystemOf": [  
        "urn:ngsi-ld:System:624b2008-bd0a-4bf6-98bd-a8fc2979af6b",  
        "urn:ngsi-ld:System:4096cc3a-d7c0-4491-b5e1-a0b97a8db924",  
        "urn:ngsi-ld:System:0dd0f326-6f31-4676-8996-7c591e57a81f"  
    ],  
    "hasManufacturer": "Fan Company Inc.",  
    "hasModel": "Fan 0.1.2",  
    "dateCreated": "2023-01-26T11:05:33Z",  
    "dateModified": "2023-01-26T13:15:57Z",  
    "source": "Import",  
    "name": "Fan",  
    "alternateName": "Fan type 2",  
    "description": "Fan of limited Fan types",  
    "dataProvider": "IFC file"  
}  
```  
</details>  
#### 风扇 NGSI-v2 标准化示例  
下面是一个规范化 JSON-LD 格式的 Fan 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Fan:0da82317-969a-4395-8eb2-f98b9cd16de8",  
  "type": "Fan",  
  "capacityControlType": {  
    "type": "Text",  
    "value": "solutions"  
  },  
  "motorDriveType": {  
    "type": "Text",  
    "value": "hard drive"  
  },  
  "nominalAirFlowRate": {  
    "type": "Measurement",  
    "value": 0.3551507592337234  
  },  
  "nominalPowerRate": {  
    "type": "Measurement",  
    "value":  0.49309444253514245  
  },  
  "nominalRotationSpeed": {  
    "type": "Measurement",  
    "value":0.07199495596164263  
  },  
  "nominalStaticPressure": {  
    "type": "Measurement",  
    "value": 0.024615829657942068  
  },  
  "nominalTotalPressure": {  
    "type": "Measurement",  
    "value":  0.3030820859504  
  },  
  "operationalRiterial": {  
    "type": "Measurement",  
    "value":  0.21730931831819922  
  },  
  "operationMode": {  
    "type": "FanOperationMode",  
    "value": "supply"  
  },  
  "operationTemperatureMax": {  
    "type": "Measurement",  
    "value":0.6593703010837063  
  },  
  "operationTemperatureMin": {  
    "type": "Measurement",  
    "value":  0.23220611636698574  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:BuildingSpace:179a46d2-4adc-49bc-81ad-55bf8d570c04"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:PhysicalObject:1324382c-8a0d-4481-b501-20ced593647d"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:7bb675a4-c933-494f-9e7a-1ad7777c40c3"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:2122d54b-df0b-490a-8d2c-9611433a6950"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:bb112446-5445-482a-aacc-ca87dc610bd5"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Fan Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Fan 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T01:05:02.0601436+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T15:45:36.2919235+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Fan"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Fan type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Fan of limited Fan types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### 扇形 NGSI-LD 键值示例  
下面是一个以 JSON-LD 格式作为 key-values 的 Fan 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Fan:7cfafc6e-ab2a-4af0-94b0-d4ed9c92e2d9",  
  "type": "Fan",  
  "capacityControlType": "e-markets",  
  "motorDriveType": "gold",  
  "nominalAirFlowRate": 0.5484285000109488,  
  "nominalPowerRate": 0.4651302623864956,  
  "nominalRotationSpeed": 0.586889938002957,  
  "nominalStaticPressure": 0.3508757713471129,  
  "nominalTotalPressure": 0.7008373891464377,  
  "operationalRiterial": 0.3901575132094196,  
  "operationMode": "supply",  
  "operationTemperatureMax": 0.9178812499585061,  
  "operationTemperatureMin": 0.5225885446624712,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:38fc3969-81c7-4c67-a564-fdbe6353726a",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:722ffa89-4091-423f-832c-3af82a48d406",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:624b2008-bd0a-4bf6-98bd-a8fc2979af6b",  
    "urn:ngsi-ld:System:4096cc3a-d7c0-4491-b5e1-a0b97a8db924",  
    "urn:ngsi-ld:System:0dd0f326-6f31-4676-8996-7c591e57a81f"  
  ],  
  "hasManufacturer": "Fan Company Inc.",  
  "hasModel": "Fan 0.1.2",  
  "dateCreated": "2023-01-26T11:05:33Z",  
  "dateModified": "2023-01-26T13:15:57Z",  
  "source": "Import",  
  "name": "Fan",  
  "alternateName": "Fan type 2",  
  "description": "Fan of limited Fan types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### 扇形 NGSI-LD 标准化示例  
下面是一个规范化 JSON-LD 格式的范例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Fan:77858a3b-1931-4dba-a9af-2eb53daaa2ba",  
  "type": "Fan",  
  "capacityControlType": {  
    "type": "Property",  
    "value": "Jamaica"  
  },  
  "motorDriveType": {  
    "type": "Property",  
    "value": "Handmade Rubber Pants"  
  },  
  "nominalAirFlowRate": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-25T20:05:36Z",  
    "value": 0.24193379349820043  
  },  
  "nominalPowerRate": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-26T00:02:52Z",  
    "value": 0.9909189253853895  
  },  
  "nominalRotationSpeed": {  
    "type": "Property",  
    "unitCode": "cycles/s",  
    "observedAt": "2023-01-25T18:57:22Z",  
    "value": 0.31786177757080614  
  },  
  "nominalStaticPressure": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-25T20:44:04Z",  
    "value": 0.9226814968179932  
  },  
  "nominalTotalPressure": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-26T08:36:40Z",  
    "value": 0.7120424039244743  
  },  
  "operationalRiterial": {  
    "type": "Property",  
    "unitCode": "time",  
    "observedAt": "2023-01-25T22:23:39Z",  
    "value": 0.858472652447435  
  },  
  "operationMode": {  
    "type": "Property",  
    "value": "supply"  
  },  
  "operationTemperatureMax": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T17:43:31Z",  
    "value": 0.6990158373086164  
  },  
  "operationTemperatureMin": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T22:43:03Z",  
    "value": 0.070852494560947  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:4e9dc2df-6361-4376-979d-fb3f96ba8a2f"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:d80ed04b-6f2d-45eb-bcf9-f94ed0564d8f"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:e79640ab-b497-40a8-b020-23d2799cdb87"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:9c3ebe76-cc20-45d1-b436-759778c41424"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:b8bb079a-9cb2-4f4e-8f22-2e5ecbc4a37e"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Fan Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Fan 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T01:34:08Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T12:21:35Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Fan"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Fan type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Fan of limited Fan types"  
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
