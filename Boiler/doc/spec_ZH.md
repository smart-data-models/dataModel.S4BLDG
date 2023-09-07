<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：锅炉  
=====<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Boiler/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述：**锅炉是一种封闭的额定压力容器，使用天然气、取暖油或电力等能源加热水或其他流体。容器中的流体然后从锅炉中循环出来，用于各种工艺或加热应用。  
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
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `energySource[string]`: 能源。定义燃烧产生热量的能源或燃料的列表  - `hasManufacturer[string]`: 标识实体（如设备）制造商的关系。该值应为字符串或带有语言标记的字符串。  - `hasModel[string]`: 标识实体（如设备）模型的关系。该值应是字符串或带有语言标记的字符串  - `heatTransferSurfaceArea[number]`: 容器的总传热面积。通常以平方米（m2）为单位  - `id[*]`: 实体的唯一标识符  - `isContainedInBuildingSpace[*]`: 用于定义楼宇物理空间的实体。建筑空间包含设备或建筑对象。(建筑空间）  - `isContainedInPhysicalObject[*]`: 任何具有适当空间区域的物体。  (从 DUL 本体中提取的定义）（物理对象）  - `isSubSystemOf[array]`: 该物理对象所属系统的引用  - `isWaterStorageHeater[boolean]`: 用于识别锅炉是否具有存储容量（真）。如果为 FALSE，则表示锅炉没有内置存储容量，如即热式热水器。  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `nominalEnergyConsumption[number]`: 产生锅炉总热量输出所需的标称燃料消耗率。通常以瓦特（W，J/s）为计量单位  - `nominalPartLoadRatio[number]`: 允许部件负载率范围  - `operatingMode[string]`: 确定锅炉的运行模式  - `outletTemperatureMax[number]`: 水或蒸汽的允许出口温度。通常以开尔文（K）度为单位  - `outletTemperatureMin[number]`: 水或蒸汽的允许出口温度。通常以开尔文（K）度为单位  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `pressureRating[number]`: 由有管辖权的机构评定的锅炉额定压力。通常以帕斯卡（Pa，N/m2）为单位。  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `type[string]`: 必须等于 "Boiler  - `waterInletTemperatureMax[number]`: 允许的进水温度范围。通常以开尔文 (K) 度为单位  - `waterInletTemperatureMin[number]`: 允许的进水温度范围。通常以开尔文 (K) 度为单位  - `waterStorageCapacity[number]`: 储水能力。通常以立方米（m3）为计量单位  <!-- /30-PropertiesList -->  
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
Boiler:    
  description: 'A boiler is a closed, pressure-rated vessel in which water or other fluid is heated using an energy source such as natural gas, heating oil, or electricity. The fluid in the vessel is then circulated out of the boiler for use in various processes or heating applications.'    
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
    energySource:    
      description: The source of energy. Enumeration defining the energy source or fuel combusted to generate heat    
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
    heatTransferSurfaceArea:    
      description: Total heat transfer area of the vessel. Usually measured in square metre (m2)    
      type: number    
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
    isWaterStorageHeater:    
      description: 'This is used to identify if the boiler has storage capacity (TRUE). If FALSE, then there is no storage capacity built into the boiler, such as an instantaneous hot water heater'    
      type: boolean    
      x-ngsi:    
        type: Property    
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
    nominalEnergyConsumption:    
      description: 'Nominal fuel consumption rate required to produce the total boiler heat output. Usually measured in Watts (W, J/s)'    
      type: number    
      x-ngsi:    
        type: Property    
    nominalPartLoadRatio:    
      description: Allowable part load ratio range    
      type: number    
      x-ngsi:    
        type: Property    
    operatingMode:    
      description: Identifies the operating mode of the boiler    
      type: string    
      x-ngsi:    
        type: Property    
    outletTemperatureMax:    
      description: Allowable outlet temperature of either the water or the steam. Usually measured in degrees Kelvin (K)    
      type: number    
      x-ngsi:    
        type: Property    
    outletTemperatureMin:    
      description: Allowable outlet temperature of either the water or the steam. Usually measured in degrees Kelvin (K)    
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
    pressureRating:    
      description: 'Nominal pressure rating of the boiler as rated by the agency having jurisdiction. Usually measured in Pascals (Pa, N/m2)'    
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
      description: It must be equal to `Boiler`    
      enum:    
        - Boiler    
      type: string    
      x-ngsi:    
        type: Property    
    waterInletTemperatureMax:    
      description: Allowable water inlet temperature range. Usually measured in degrees Kelvin (K)    
      type: number    
      x-ngsi:    
        type: Property    
    waterInletTemperatureMin:    
      description: Allowable water inlet temperature range. Usually measured in degrees Kelvin (K)    
      type: number    
      x-ngsi:    
        type: Property    
    waterStorageCapacity:    
      description: Water storage capacity. Usually measured in cubic metre (m3)    
      type: number    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Boiler"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Boiler/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Boiler/schema.json    
  x-model-tags: 'SAREF, building'    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 有效载荷示例  
#### 锅炉 NGSI-v2 键值示例  
下面是一个以 JSON-LD 格式作为键值的锅炉示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Boiler:724c2f67-e55e-4971-8e74-55d6ecfa19c9",  
  "type": "Boiler",  
  "energySource": "United States of America",  
  "heatTransferSurfaceArea": 0.7853344933267346,  
  "isWaterStorageHeater": false,  
  "nominalEnergyConsumption": 0.6203749662936422,  
  "nominalPartLoadRatio": 0.8015670647257737,  
  "operatingMode": "systems",  
  "outletTemperatureMax": 0.16008580907721015,  
  "outletTemperatureMin": 0.04227267769006804,  
  "pressureRating": 0.5113599213422801,  
  "waterInletTemperatureMax": 0.9011788947791837,  
  "waterInletTemperatureMin": 0.24858493133262038,  
  "waterStorageCapacity": 0.5276371515431508,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:50afbc21-cf0f-4f69-b48a-47af5a287d38",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:f2bfaa08-a201-40bd-b1b3-fe5a4ba5d291",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:1cfd3123-93fa-408a-a750-dd5a6f0edcae",  
    "urn:ngsi-ld:System:fec748f9-6ee5-49af-93a4-5bffcc20e73c",  
    "urn:ngsi-ld:System:5ee8058b-c872-4237-9c94-82f22172c39e"  
  ],  
  "hasManufacturer": "Boiler Company Inc.",  
  "hasModel": "Boiler 0.1.2",  
  "dateCreated": "2023-01-26T09:03:19Z",  
  "dateModified": "2023-01-25T16:09:21Z",  
  "source": "Import",  
  "name": "Boiler",  
  "alternateName": "Boiler type 2",  
  "description": "Boiler of limited Boiler types",  
  "dataProvider": "IFC file"  
}  
```  
</details>  
#### 锅炉 NGSI-v2 标准化示例  
下面是一个规范化 JSON-LD 格式的 "锅炉 "示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Boiler:554e6cfc-a12b-466b-bdb5-251db87de147",  
  "type": "Boiler",  
  "energySource": {  
    "type": "Text",  
    "value": "Coordinator"  
  },  
  "heatTransferSurfaceArea": {  
    "type": "Measurement",  
    "value": 0.054241651152424186  
  },  
  "isWaterStorageHeater": {  
    "type": "Boolean",  
    "value": false  
  },  
  "nominalEnergyConsumption": {  
    "type": "Measurement",  
    "value": 0.015349430439582035  
  },  
  "nominalPartLoadRatio": {  
    "type": "Measurement",  
    "value": 0.15224995605259972  
  },  
  "operatingMode": {  
    "type": "Text",  
    "value": "bypass"  
  },  
  "outletTemperatureMax": {  
    "type": "Measurement",  
    "value": 0.6702304071347284  
  },  
  "outletTemperatureMin": {  
    "type": "Measurement",  
    "value":0.5096152218274909  
  },  
  "pressureRating": {  
    "type": "Measurement",  
    "value": 0.5974774605306619  
  },  
  "waterInletTemperatureMax": {  
    "type": "Measurement",  
    "value": 0.9398884749677864  
  },  
  "waterInletTemperatureMin": {  
    "type": "Measurement",  
    "value": 0.4089735417040705  
  },  
  "waterStorageCapacity": {  
    "type": "Measurement",  
    "value": 0.9413886423074906  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:BuildingSpace:ab8a7d6f-040b-4eb8-b6ea-f238a2ccc065"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:PhysicalObject:668e5ccf-c66c-43ea-ad8d-fca6862f3d04"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:2c2904e8-d4fa-4191-8b1b-4e06eaed77ff"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:820d0fb3-9cb6-4bc4-b706-515d91e3343f"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:a0370269-07a5-4bad-a6c0-15a382a279ce"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Boiler Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Boiler 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T10:00:09.4580486+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T18:35:13.9392676+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Boiler"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Boiler type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Boiler of limited Boiler types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### 锅炉 NGSI-LD 键值示例  
下面是一个以 JSON-LD 格式作为键值的锅炉示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Boiler:724c2f67-e55e-4971-8e74-55d6ecfa19c9",  
  "type": "Boiler",  
  "energySource": "United States of America",  
  "heatTransferSurfaceArea": 0.7853344933267346,  
  "isWaterStorageHeater": false,  
  "nominalEnergyConsumption": 0.6203749662936422,  
  "nominalPartLoadRatio": 0.8015670647257737,  
  "operatingMode": "systems",  
  "outletTemperatureMax": 0.16008580907721015,  
  "outletTemperatureMin": 0.04227267769006804,  
  "pressureRating": 0.5113599213422801,  
  "waterInletTemperatureMax": 0.9011788947791837,  
  "waterInletTemperatureMin": 0.24858493133262038,  
  "waterStorageCapacity": 0.5276371515431508,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:50afbc21-cf0f-4f69-b48a-47af5a287d38",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:f2bfaa08-a201-40bd-b1b3-fe5a4ba5d291",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:1cfd3123-93fa-408a-a750-dd5a6f0edcae",  
    "urn:ngsi-ld:System:fec748f9-6ee5-49af-93a4-5bffcc20e73c",  
    "urn:ngsi-ld:System:5ee8058b-c872-4237-9c94-82f22172c39e"  
  ],  
  "hasManufacturer": "Boiler Company Inc.",  
  "hasModel": "Boiler 0.1.2",  
  "dateCreated": "2023-01-26T09:03:19Z",  
  "dateModified": "2023-01-25T16:09:21Z",  
  "source": "Import",  
  "name": "Boiler",  
  "alternateName": "Boiler type 2",  
  "description": "Boiler of limited Boiler types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### 锅炉 NGSI-LD 标准化示例  
下面是一个规范化 JSON-LD 格式的 "锅炉 "示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Boiler:4f7a4533-13d0-4de0-b5e9-72dee067176a",  
  "type": "Boiler",  
  "energySource": {  
    "type": "Property",  
    "value": "Sri Lanka"  
  },  
  "heatTransferSurfaceArea": {  
    "type": "Property",  
    "unitCode": "m2",  
    "observedAt": "2023-01-25T19:16:12Z",  
    "value": 0.4182368568397056  
  },  
  "isWaterStorageHeater": {  
    "type": "Property",  
    "value": false  
  },  
  "nominalEnergyConsumption": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-25T23:06:57Z",  
    "value": 0.5252685918504294  
  },  
  "nominalPartLoadRatio": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-25T22:37:37Z",  
    "value": 0.481958764350527  
  },  
  "operatingMode": {  
    "type": "Property",  
    "value": "Auto Loan Account"  
  },  
  "outletTemperatureMax": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T17:03:10Z",  
    "value": 0.2786304815176084  
  },  
  "outletTemperatureMin": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T02:55:50Z",  
    "value": 0.4041488945350036  
  },  
  "pressureRating": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-25T18:00:19Z",  
    "value": 0.5561857737231611  
  },  
  "waterInletTemperatureMax": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T03:34:53Z",  
    "value": 0.242404197934733  
  },  
  "waterInletTemperatureMin": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T04:06:01Z",  
    "value": 0.46028861347866734  
  },  
  "waterStorageCapacity": {  
    "type": "Property",  
    "unitCode": "m3",  
    "observedAt": "2023-01-26T10:18:01Z",  
    "value": 0.22263600675421202  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:cfc926aa-ae2a-411e-b3d4-c315d7d19d9b"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:5e682b37-bcc1-441a-ad19-80615c70a84f"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:ba691c15-807f-48fb-b963-99961fd81a95"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:227bcf8f-170f-41ff-a88d-1e1cb67da411"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:7868b4ac-6685-4b3e-85ef-6494c909409c"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Boiler Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Boiler 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T17:50:43Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-25T23:43:57Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Boiler"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Boiler type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Boiler of limited Boiler types"  
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
