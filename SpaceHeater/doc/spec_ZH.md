<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体：太空加热器    
========<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/SpaceHeater/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全球描述：**空间加热器利用辐射和/或自然对流的组合，使用电、蒸汽或热水等加热源加热有限的空间或区域。空间加热器的例子包括散热器、对流器、底板和翅片管加热器。  UnitaryEquipment（单元设备）应用于支持加热、冷却和/或除湿组合的成套设备；Coil（盘管）应用于基于盘管的地板采暖**。    
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
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `bodyMass[number]`: 加热器的总体质量。通常以千克（kg）或克（g）为计量单位  - `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `energySource[string]`: 能源。定义产生热量的能源或燃料的列举  - `hasManufacturer[string]`: 标识实体（如设备）制造商的关系。该值应为字符串或带有语言标记的字符串。  - `hasModel[string]`: 标识实体（如设备）模型的关系。该值应是字符串或带有语言标记的字符串  - `heatTransferDimension[string]`: 根据空间加热器的形状显示热量传播方式  - `heatTransferMedium[string]`: 定义传热介质的枚举（如适用  - `id[*]`: 实体的唯一标识符  - `isContainedInBuildingSpace[*]`: 用于定义楼宇物理空间的实体。建筑空间包含设备或建筑对象。(建筑空间）  - `isContainedInPhysicalObject[*]`: 任何具有适当空间区域的物体。  (从 DUL 本体中提取的定义）（物理对象）  - `isSubSystemOf[array]`: 该物理对象所属系统的引用  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `numberOfPanels[number]`: 面板数量  - `numberOfSections[number]`: 使用科室数量  - `outputCapacity[number]`: 制造商列出的总标称热输出。通常以瓦特（W，J/s）为计量单位  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `placementType[string]`: 表示设备的设计放置方式  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `temperatureClassification[string]`: 低温 - 表面温度相对较低，通常用热水或电加热。 高温 - 表面温度相对较高，通常用燃气或蒸汽加热。  - `thermalEfficiency[number]`: 整体热效率的定义是：传热设备输出的总能量除以输入的能量  - `thermalMassHeatCapacity[number]`: 成分质量与比热的乘积  - `type[string]`: 必须等于 `SpaceHeater`  <!-- /30-PropertiesList -->    
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
SpaceHeater:      
  description: 'Space heaters utilize a combination of radiation and/or natural convection using a heating source such as electricity, steam or hot water to heat a limited space or area. Examples of space heaters include radiators, convectors, baseboard and finned-tube heaters.  UnitaryEquipment should be used for packaged units supporting a combination of heating, cooling, and/or dehumidification; Coil should be used for coil-based floor heating.'      
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
    bodyMass:      
      description: Overall body mass of the heater. Usually measured in kilograms (kg) or grams (g)      
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
    energySource:      
      description: The source of energy. Enumeration defining the energy source or fuel cumbusted to generate heat      
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
    heatTransferDimension:      
      description: Indicates how heat is transmitted according to the shape of the space heater      
      type: string      
      x-ngsi:      
        type: Property      
    heatTransferMedium:      
      description: Enumeration defining the heat transfer medium if applicable      
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
    numberOfPanels:      
      description: Number of panels      
      type: number      
      x-ngsi:      
        type: Property      
    numberOfSections:      
      description: Number of sections used      
      type: number      
      x-ngsi:      
        type: Property      
    outputCapacity:      
      description: 'Total nominal heat output as listed by the manufacturer. Usually measured in Watts (W, J/s)'      
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
    temperatureClassification:      
      description: 'Enumeration defining the temperature classification of the space heater surface temperature. low temperature - surface temperature is relatively low, usually heated by hot water or electricity. high temperature - surface temperature is relatively high, usually heated by gas or steam'      
      type: string      
      x-ngsi:      
        type: Property      
    thermalEfficiency:      
      description: Overall Thermal Efficiency is defined as gross energy output of the heat transfer device divided by the energy input      
      type: number      
      x-ngsi:      
        type: Property      
    thermalMassHeatCapacity:      
      description: Product of component mass and specific heat      
      type: number      
      x-ngsi:      
        type: Property      
    type:      
      description: It must be equal to `SpaceHeater`      
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
## 有效载荷示例    
#### SpaceHeater NGSI-v2 键值示例    
下面是一个以 JSON-LD 格式作为键值的 SpaceHeater 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
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
#### SpaceHeater NGSI-v2 标准化示例    
下面是一个规范化 JSON-LD 格式的 SpaceHeater 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:SpaceHeater:b256e328-b21f-4f37-bcb4-d78364993e79",  
  "type": "SpaceHeater",  
  "bodyMass": {  
    "type": "Number",  
    "value": 0.7643146073425459  
  },  
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
    "type": "Number",  
    "value": 0.8127498709428745  
  },  
  "numberOfSections": {  
    "type": "Number",  
    "value": 0.8692658014070345  
  },  
  "outputCapacity": {  
    "type": "Number",  
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
    "type": "Number",  
    "value": 0.16328303516805232  
  },  
  "thermalMassHeatCapacity": {  
    "type": "Number",  
    "value": 0.17753659327247795  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:BuildingSpace:c1f57310-b1ad-4a70-bdca-70f74bbcc002"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:PhysicalObject:e22ae82c-83a1-4ed9-b1f8-eeced3ba17d9"  
  },  
  "isSubSystemOf": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:System:6f519e2b-416a-4b2a-af7b-56974a5d00df",  
      "urn:ngsi-ld:System:16199b91-8c55-4645-8c14-536d1dff0fcc",  
      "urn:ngsi-ld:System:5526ed19-a6fa-4e22-a8bd-71a1027a9b02"  
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
#### SpaceHeater NGSI-LD 键值示例    
下面是一个以 JSON-LD 格式作为键值的 SpaceHeater 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
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
#### SpaceHeater NGSI-LD 归一化示例    
下面是一个规范化 JSON-LD 格式的 SpaceHeater 示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
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
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
