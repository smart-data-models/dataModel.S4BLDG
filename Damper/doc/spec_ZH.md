<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：风门  
=====<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Damper/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述：**风门通常参与暖通空调管道分配系统，用于控制或调节气流。  
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
- `airFlowRateMax[number]`: 最大允许空气流量。通常以 m3/s 为单位  - `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `bladeAction[string]`: 刀片动作  - `bladeEdge[string]`: 刀刃  - `bladeShape[string]`: 刀片形状平指三 V 形槽  - `bladeThickness[number]`: 阻尼器叶片的厚度。通常以毫米（mm）为单位  - `closeOffRating[number]`: 关闭额定值。通常以帕斯卡（Pa，N/m2）为单位测量  - `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `faceArea[number]`: 向气流开放的面面积。通常以平方米（m2）为单位  - `frameDepth[number]`: 阻尼器框架的长度（或深度）。通常以毫米（mm）为单位  - `frameThickness[number]`: 阻尼器框架材料的厚度。通常以毫米（mm）为单位  - `frameType[string]`: 风门使用的框架类型（如标准、单法兰、单反向法兰、双法兰等）  - `hasManufacturer[string]`: 标识实体（如设备）制造商的关系。该值应为字符串或带有语言标记的字符串。  - `hasModel[string]`: 标识实体（如设备）模型的关系。该值应是字符串或带有语言标记的字符串  - `id[*]`: 实体的唯一标识符  - `isContainedInBuildingSpace[*]`: 用于定义楼宇物理空间的实体。建筑空间包含设备或建筑对象。(建筑空间）  - `isContainedInPhysicalObject[*]`: 任何具有适当空间区域的物体。  (从 DUL 本体中提取的定义）（物理对象）  - `isSubSystemOf[array]`: 该物理对象所属系统的引用  - `leakageFullyClosed[number]`: 完全关闭时的泄漏量。通常以 m3/s 为单位  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `nominalAirFlowRate[number]`: 名义气流速度。通常以 m3/s 为单位  - `numberOfBlades[number]`: 刀片数量  - `openPressureDrop[number]`: 风门上的总压降。通常以帕斯卡（Pa，N/m2）为单位测量  - `operation[string]`: 风门运行的操作机制  - `operationMode[string]`: 该风门的运行模式  - `operationTemperatureMax[number]`: 允许的运行环境（空气、流体）温度范围。通常以开尔文 (K) 度为单位  - `operationTemperatureMin[number]`: 允许的运行环境（空气、流体）温度范围。通常以开尔文 (K) 度为单位  - `orientation[string]`: 制造商规定的阻尼器安装方向  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `temperatureRating[number]`: 温度等级。通常以开氏度（K）为单位测量  - `type[string]`: 必须等于 `Damper`  - `workingPressureMax[number]`: 最大工作压力。通常以帕斯卡（Pa，N/m2）为计量单位  <!-- /30-PropertiesList -->  
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
Damper:    
  description: A damper typically participates in an HVAC duct distribution system and is used to control or modulate the flow of air.    
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
    bladeAction:    
      description: Blade action    
      type: string    
      x-ngsi:    
        type: Property    
    bladeEdge:    
      description: Blade edge    
      type: string    
      x-ngsi:    
        type: Property    
    bladeShape:    
      description: Blade shape. Flat means triple V-groove    
      type: string    
      x-ngsi:    
        type: Property    
    bladeThickness:    
      description: The thickness of the damper blade. Usually measured in millimeters (mm)    
      type: number    
      x-ngsi:    
        type: Property    
    closeOffRating:    
      description: 'Close off rating. Usually measured in Pascals (Pa, N/m2)'    
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
    faceArea:    
      description: Face area open to the airstream. Usually measured in square metre (m2)    
      type: number    
      x-ngsi:    
        type: Property    
    frameDepth:    
      description: The length (or depth) of the damper frame. Usually measured in millimeters (mm)    
      type: number    
      x-ngsi:    
        type: Property    
    frameThickness:    
      description: The thickness of the damper frame material. Usually measured in millimeters (mm)    
      type: number    
      x-ngsi:    
        type: Property    
    frameType:    
      description: 'The type of frame used by the damper (e.g., Standard, Single Flange, Single Reversed Flange, Double Flange, etc.)'    
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
    leakageFullyClosed:    
      description: Leakage when fully closed. Usually measured in m3/s    
      type: number    
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
    nominalAirFlowRate:    
      description: Nominal rate of air flow. Usually measured in m3/s    
      type: number    
      x-ngsi:    
        type: Property    
    numberOfBlades:    
      description: Number of blades    
      type: number    
      x-ngsi:    
        type: Property    
    openPressureDrop:    
      description: 'Total pressure drop across damper. Usually measured in Pascals (Pa, N/m2)'    
      type: number    
      x-ngsi:    
        type: Property    
    operation:    
      description: The operational mechanism for the damper operation    
      type: string    
      x-ngsi:    
        type: Property    
    operationMode:    
      description: Operation mode of this damper    
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
    orientation:    
      description: The intended orientation for the damper as specified by the manufacturer    
      type: string    
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
    temperatureRating:    
      description: Temperature rating. Usually measured in degrees Kelvin (K)    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: It must be equal to `Damper`    
      enum:    
        - Damper    
      type: string    
      x-ngsi:    
        type: Property    
    workingPressureMax:    
      description: 'Maximum working pressure. Usually measured in Pascals (Pa, N/m2)'    
      type: number    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Damper"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Damper/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Damper/schema.json    
  x-model-tags: SAREF Damper    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 有效载荷示例  
#### 阻尼器 NGSI-v2 键值示例  
下面是一个以 JSON-LD 格式作为键值的 Damper 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Damper:65c94159-bfe6-416d-b02c-283479048fe3",  
  "type": "Damper",  
  "airFlowRateMax": 0.5927918101987754,  
  "bladeAction": "Belize Dollar",  
  "bladeEdge": "frictionless",  
  "bladeShape": "intermediate",  
  "bladeThickness": 0.5665758025960763,  
  "closeOffRating": 0.8924252696459434,  
  "faceArea": 0.45839947738381925,  
  "frameDepth": 0.6687870848219263,  
  "frameThickness": 0.6594470368135407,  
  "frameType": "Ergonomic",  
  "leakageFullyClosed": 0.052627216627954665,  
  "nominalAirFlowRate": 0.7333602290466408,  
  "numberOfBlades": 0.3476917428528077,  
  "openPressureDrop": 0.8991384789588308,  
  "operation": "Implemented",  
  "operationMode": "supply",  
  "operationTemperatureMax": 0.07772736087657628,  
  "operationTemperatureMin": 0.4857292385786113,  
  "orientation": "reboot",  
  "temperatureRating": 0.4909792118139581,  
  "workingPressureMax": 0.10839736205746486,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:c25bebe3-d546-4942-be72-9468ce218070",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:326da1c1-440d-4200-b598-a84e3bf5fdc1",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:007e61a9-027a-4662-a7a0-1e9e48f57886",  
    "urn:ngsi-ld:System:59945456-4e66-4c84-b637-7c771479a9f3",  
    "urn:ngsi-ld:System:023e0706-8d3d-411b-9e97-994a870341cd"  
  ],  
  "hasManufacturer": "Damper Company Inc.",  
  "hasModel": "Damper 0.1.2",  
  "dateCreated": "2023-01-25T18:10:59Z",  
  "dateModified": "2023-01-26T07:49:53Z",  
  "source": "Import",  
  "name": "Damper",  
  "alternateName": "Damper type 2",  
  "description": "Damper of limited Damper types",  
  "dataProvider": "IFC file"  
}  
```  
</details>  
#### 阻尼器 NGSI-v2 标准化示例  
下面是一个规范化 JSON-LD 格式的阻尼器示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Damper:30830dab-6aa5-4dd1-9e48-d6ac7e24e4bf",  
  "type": "Damper",  
  "airFlowRateMax": {  
    "type": "Measurement",  
    "value":  0.13813389168852752  
  },  
  "bladeAction": {  
    "type": "Text",  
    "value": "Spur"  
  },  
  "bladeEdge": {  
    "type": "Text",  
    "value": "Personal Loan Account"  
  },  
  "bladeShape": {  
    "type": "Text",  
    "value": "Human"  
  },  
  "bladeThickness": {  
    "type": "Measurement",  
    "value":  0.35230461364031296  
  },  
  "closeOffRating": {  
    "type": "Measurement",  
    "value":  0.171775838539866  
  },  
  "faceArea": {  
    "type": "Measurement",  
    "value": 0.4212393478883142  
  },  
  "frameDepth": {  
    "type": "Measurement",  
    "value": 0.8035081586701794  
  },  
  "frameThickness": {  
    "type": "Measurement",  
    "value":  0.28946308913206176  
  },  
  "frameType": {  
    "type": "Text",  
    "value": "Balanced"  
  },  
  "leakageFullyClosed": {  
    "type": "Measurement",  
    "value":  0.44075236436472953  
  },  
  "nominalAirFlowRate": {  
    "type": "Measurement",  
    "value":0.47305378645729657  
  },  
  "numberOfBlades": {  
    "type": "Float",  
    "value": 0.8083872561368712  
  },  
  "openPressureDrop": {  
    "type": "Measurement",  
    "value": 0.9106213284285767  
  },  
  "operation": {  
    "type": "Text",  
    "value": "Handcrafted Concrete Computer"  
  },  
  "operationMode": {  
    "type": "DamperOperationMode",  
    "value": "supply"  
  },  
  "operationTemperatureMax": {  
    "type": "Measurement",  
    "value":  0.87576324331876  
  },  
  "operationTemperatureMin": {  
    "type": "Measurement",  
    "value":  0.3952529455728351  
  },  
  "orientation": {  
    "type": "Text",  
    "value": "Mozambique"  
  },  
  "temperatureRating": {  
    "type": "Measurement",  
    "value":  0.43326401348250587  
  },  
  "workingPressureMax": {  
    "type": "Measurement",  
    "value":  0.2695729035947665  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:BuildingSpace:f19ff450-12f4-472a-985e-40b163530ccd"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:PhysicalObject:ee6c23f3-7261-4807-b3e3-703588646f02"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:a8f8f637-52c0-491d-890e-2806ffbdc6cd"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:7f5f939e-9a41-4ca6-95ff-4ece8ffec42c"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:ff7924ea-c532-40c9-a1ac-449c76216073"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Damper Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Damper 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T15:13:23.9679787+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T16:00:58.1902016+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Damper"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Damper type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Damper of limited Damper types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### 阻尼器 NGSI-LD 键值示例  
下面是一个以 JSON-LD 格式作为键值的 Damper 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Damper:65c94159-bfe6-416d-b02c-283479048fe3",  
  "type": "Damper",  
  "airFlowRateMax": 0.5927918101987754,  
  "bladeAction": "Belize Dollar",  
  "bladeEdge": "frictionless",  
  "bladeShape": "intermediate",  
  "bladeThickness": 0.5665758025960763,  
  "closeOffRating": 0.8924252696459434,  
  "faceArea": 0.45839947738381925,  
  "frameDepth": 0.6687870848219263,  
  "frameThickness": 0.6594470368135407,  
  "frameType": "Ergonomic",  
  "leakageFullyClosed": 0.052627216627954665,  
  "nominalAirFlowRate": 0.7333602290466408,  
  "numberOfBlades": 0.3476917428528077,  
  "openPressureDrop": 0.8991384789588308,  
  "operation": "Implemented",  
  "operationMode": "supply",  
  "operationTemperatureMax": 0.07772736087657628,  
  "operationTemperatureMin": 0.4857292385786113,  
  "orientation": "reboot",  
  "temperatureRating": 0.4909792118139581,  
  "workingPressureMax": 0.10839736205746486,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:c25bebe3-d546-4942-be72-9468ce218070",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:326da1c1-440d-4200-b598-a84e3bf5fdc1",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:007e61a9-027a-4662-a7a0-1e9e48f57886",  
    "urn:ngsi-ld:System:59945456-4e66-4c84-b637-7c771479a9f3",  
    "urn:ngsi-ld:System:023e0706-8d3d-411b-9e97-994a870341cd"  
  ],  
  "hasManufacturer": "Damper Company Inc.",  
  "hasModel": "Damper 0.1.2",  
  "dateCreated": "2023-01-25T18:10:59Z",  
  "dateModified": "2023-01-26T07:49:53Z",  
  "source": "Import",  
  "name": "Damper",  
  "alternateName": "Damper type 2",  
  "description": "Damper of limited Damper types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### 阻尼器 NGSI-LD 归一化示例  
下面是一个规范化 JSON-LD 格式的阻尼器示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Damper:99cb9b35-5f17-4e4d-89bb-e9d7bb88c2ba",  
  "type": "Damper",  
  "airFlowRateMax": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-26T10:15:08Z",  
    "value": 0.46010915943742847  
  },  
  "bladeAction": {  
    "type": "Property",  
    "value": "microchip"  
  },  
  "bladeEdge": {  
    "type": "Property",  
    "value": "Village"  
  },  
  "bladeShape": {  
    "type": "Property",  
    "value": "Netherlands Antillian Guilder"  
  },  
  "bladeThickness": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-25T21:36:37Z",  
    "value": 0.5214778377905084  
  },  
  "closeOffRating": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-25T18:21:40Z",  
    "value": 0.8241451329002358  
  },  
  "faceArea": {  
    "type": "Property",  
    "unitCode": "m2",  
    "observedAt": "2023-01-25T20:36:04Z",  
    "value": 0.6197704906516315  
  },  
  "frameDepth": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T14:05:58Z",  
    "value": 0.19371235604272175  
  },  
  "frameThickness": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-25T21:48:43Z",  
    "value": 0.630746648821536  
  },  
  "frameType": {  
    "type": "Property",  
    "value": "SAS"  
  },  
  "leakageFullyClosed": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-25T21:59:27Z",  
    "value": 0.8430168839934075  
  },  
  "nominalAirFlowRate": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-26T06:30:50Z",  
    "value": 0.8419372074040988  
  },  
  "numberOfBlades": {  
    "type": "Property",  
    "value": 0.2730424937241438  
  },  
  "openPressureDrop": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-26T04:03:50Z",  
    "value": 0.25493844227297535  
  },  
  "operation": {  
    "type": "Property",  
    "value": "partnerships"  
  },  
  "operationMode": {  
    "type": "Property",  
    "value": "exhaust"  
  },  
  "operationTemperatureMax": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T22:15:50Z",  
    "value": 0.4402985682699154  
  },  
  "operationTemperatureMin": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T11:49:40Z",  
    "value": 0.0015019955460002787  
  },  
  "orientation": {  
    "type": "Property",  
    "value": "Metrics"  
  },  
  "temperatureRating": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T16:28:22Z",  
    "value": 0.6012606116766228  
  },  
  "workingPressureMax": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-26T09:39:16Z",  
    "value": 0.320862748056973  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:573f5e7a-806c-4deb-878c-365ef09fe4d2"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:0cbecfb0-1008-4c54-99f6-510fba847457"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:972e3b8b-9613-4b3a-a798-f3e56587d999"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:0d09725f-1468-4352-92e9-39d0b647a683"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:0c5bf106-93a0-4eb9-a15d-a0d834088c94"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Damper Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Damper 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T10:37:53Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T10:42:54Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Damper"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Damper type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Damper of limited Damper types"  
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
