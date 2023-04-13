<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：冷却塔  
======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/CoolingTower/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述：**冷却塔是一种通过水等流体的循环，通过部分蒸发降低温度，将热量排到环境空气中的装置。  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `ambientDesignDryBulbTemperature[number]`: 属性。用于选择冷却塔的环境设计干球温度。通常以开尔文(K)度测量。  - `ambientDesignWetBulbTemperature[number]`: 属性。用于选择冷却塔的环境设计湿球温度。通常以开尔文(K)度测量。  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `basinReserveVolume[number]`: 属性。冷却塔盆地中工作和溢流水平之间的体积。通常以立方米（m3）衡量。  - `capacityControl[string]`: 财产。FanCycling：风扇循环开启和关闭以控制负载。双速风扇：风扇在低速和高速之间切换以控制负载。变速风扇：风扇速度变化以控制负载。阻尼器控制：阻尼器调节气流以控制负载。旁通阀控制：旁通阀调节水流以控制负载。多串联泵：打开/关闭多系列泵以控制工作。双速泵：在高/低泵速之间切换以控制工作。变速泵：改变泵速以控制工作。  - `circuitType[string]`: 属性。OpenCircuit：将水直接暴露在冷却气氛中。关闭电路：流体通过一个热交换器与大气分离。湿式：气流或热交换表面被蒸发冷却。干的：没有蒸发到空气流中。干-湿：干式塔和湿式塔的组合。  - `controlStrategy[string]`: 属性。FixedExitingWaterTemp: 控制容量以维持一个固定的出口水温。WetBulbTempReset：设定点根据湿球温度进行重置。  - `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `flowArrangement[string]`: 属性。逆流：空气和水流从不同方向进入。交叉流动：空气和水的流动是垂直的。平行流：空气和水流在同一方向进入。  - `hasManufacturer[string]`: 属性。识别实体（例如，设备）的制造商的关系。该值应是一个字符串或一个带有语言标签的字符串。  - `hasModel[string]`: 属性。识别实体（例如，设备）的模型的关系。该值应是一个字符串或一个带有语言标签的字符串。  - `id[*]`: 实体的唯一标识符  - `isContainedInBuildingSpace[*]`: 关系。一个用于定义建筑物理空间的实体。一个建筑空间包含设备或建筑对象。(建筑空间)  - `isContainedInPhysicalObject[*]`: 关系。任何具有适当空间区域的物体。  (从DUL本体论中提取的定义）（PhysicalObject）。  - `isSubSystemOf[array]`: 关系。对该物理对象是其一部分的系统的引用。  - `liftElevationDifference[number]`: 属性。冷却塔底盘和塔顶之间的高差。通常以毫米（mm）为单位测量。  - `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `name[string]`: 这个项目的名称。  - `nominalCapacity[number]`: 属性。标称容量。通常以瓦特（W，J/s）衡量。  - `numberOfCells[number]`: 属性。一个冷却塔单元中的单元数。  - `operationTemperatureMax[number]`: 属性。允许的操作环境（空气、液体）温度范围。通常以开尔文(K)度衡量。  - `operationTemperatureMin[number]`: 属性。允许的操作环境（空气、液体）温度范围。通常以开尔文(K)度衡量。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `sprayType[string]`: 属性。喷雾填充：水被喷到气流中。SplashTypeFill：水在连续的一排防溅条上层叠。FilmTypeFill：水在密密麻麻的片状物上流动，形成一个薄层。  - `type[string]`: 属性。它必须等于`冷却塔'。  - `waterRequirement[number]`: 财产。补水需求。通常以m3/s测量。  <!-- /30-PropertiesList -->  
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
CoolingTower:    
  description: A cooling tower is a device which rejects heat to ambient air by circulating a fluid such as water through it to reduce its temperature by partial evaporation.    
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
    ambientDesignDryBulbTemperature:    
      description: Property. Ambient design dry bulb temperature used for selecting the cooling tower. Usually measured in degrees Kelvin (K).    
      type: number    
      x-ngsi:    
        type: Property    
    ambientDesignWetBulbTemperature:    
      description: Property. Ambient design wet bulb temperature used for selecting the cooling tower. Usually measured in degrees Kelvin (K).    
      type: number    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    basinReserveVolume:    
      description: Property. Volume between operating and overflow levels in cooling tower basin. Usually measured in cubic metre (m3).    
      type: number    
      x-ngsi:    
        type: Property    
    capacityControl:    
      description: 'Property. FanCycling: Fan is cycled on and off to control duty. TwoSpeedFan: Fan is switched between low and high speed to control duty. VariableSpeedFan: Fan speed is varied to control duty. DampersControl: Dampers modulate the air flow to control duty. BypassValveControl: Bypass valve modulates the water flow to control duty. MultipleSeriesPumps: Turn on/off multiple series pump to control duty. TwoSpeedPump: Switch between high/low pump speed to control duty. VariableSpeedPump: vary pump speed to control duty.'    
      type: string    
      x-ngsi:    
        type: Property    
    circuitType:    
      description: 'Property. OpenCircuit: Exposes water directly to the cooling atmosphere. CloseCircuit: The fluid is separated from the atmosphere by a heat exchanger. Wet: The air stream or the heat exchange surface is evaporatively cooled. Dry: No evaporation into the air stream. DryWet: A combination of a dry tower and a wet tower.'    
      type: string    
      x-ngsi:    
        type: Property    
    controlStrategy:    
      description: 'Property. FixedExitingWaterTemp: The capacity is controlled to maintain a fixed exiting water temperature. WetBulbTempReset: The set-point is reset based on the wet-bulb temperature.'    
      type: string    
      x-ngsi:    
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
    flowArrangement:    
      description: 'Property. CounterFlow: Air and water flow enter in different directions. CrossFlow: Air and water flow are perpendicular. ParallelFlow: air and water flow enter in same directions.'    
      type: string    
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
      anyOf: &coolingtower_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      anyOf: *coolingtower_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *coolingtower_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *coolingtower_-_properties_-_iscontainedinbuildingspace_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Relationship    
    liftElevationDifference:    
      description: Property. Elevation difference between cooling tower sump and the top of the tower. Usually measured in millimeters (mm).    
      type: number    
      x-ngsi:    
        type: Property    
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
    nominalCapacity:    
      description: 'Property. Nominal capacity. Usually measured in Watts (W, J/s).'    
      type: number    
      x-ngsi:    
        type: Property    
    numberOfCells:    
      description: Property. Number of cells in one cooling tower unit.    
      type: number    
      x-ngsi:    
        type: Property    
    operationTemperatureMax:    
      description: 'Property. Allowable operation ambient (air, fluid) temperature range. Usually measured in degrees Kelvin (K).'    
      type: number    
      x-ngsi:    
        type: Property    
    operationTemperatureMin:    
      description: 'Property. Allowable operation ambient (air, fluid) temperature range. Usually measured in degrees Kelvin (K).'    
      type: number    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *coolingtower_-_properties_-_iscontainedinbuildingspace_-_anyof    
        description: Property. Unique identifier of the entity    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    sprayType:    
      description: 'Property. SprayFilled: Water is sprayed into airflow. SplashTypeFill: water cascades over successive rows of splash bars. FilmTypeFill: water flows in a thin layer over closely spaced sheets.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: Property. It must be equal to `CoolingTower`.    
      enum:    
        - CoolingTower    
      type: string    
      x-ngsi:    
        type: Property    
    waterRequirement:    
      description: Property. Make-up water requirement. Usually measured in m3/s.    
      type: number    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:CoolingTower"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/CoolingTower/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/CoolingTower/schema.json    
  x-model-tags: SAREF CoolingTower    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### CoolingTower NGSI-v2关键值示例  
这里是一个以JSON-LD格式作为key-values的CoolingTower的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:CoolingTower:c628d24d-5b25-4b99-838e-35676956d307",  
  "type": "CoolingTower",  
  "ambientDesignDryBulbTemperature": 0.7275209381168831,  
  "ambientDesignWetBulbTemperature": 0.8419497776651206,  
  "basinReserveVolume": 0.9886525691530367,  
  "capacityControl": "Lead",  
  "circuitType": "virtual",  
  "controlStrategy": "Harbors",  
  "flowArrangement": "Extensions",  
  "liftElevationDifference": 0.9337996577856725,  
  "nominalCapacity": 0.8043496896372141,  
  "numberOfCells": 0.03361385186991317,  
  "operationTemperatureMax": 0.7125610456321683,  
  "operationTemperatureMin": 0.3015974804386986,  
  "sprayType": "programming",  
  "waterRequirement": 0.1817597423361893,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:6871b1ec-cfce-4a60-83c2-9f07b13d1703",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:e2a48930-276e-4972-9283-82fbc22faf85",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:aea47887-bc5b-47c3-aeb0-870506d76580",  
    "urn:ngsi-ld:System:2791b628-8fc1-4ec1-91a7-26efbbc892a3",  
    "urn:ngsi-ld:System:c0623c49-ae1f-4772-9323-a94078dbdb86"  
  ],  
  "hasManufacturer": "CoolingTower Company Inc.",  
  "hasModel": "CoolingTower 0.1.2",  
  "dateCreated": "2023-01-26T12:17:43Z",  
  "dateModified": "2023-01-25T16:13:00Z",  
  "source": "Import",  
  "name": "CoolingTower",  
  "alternateName": "CoolingTower type 2",  
  "description": "CoolingTower of limited CoolingTower types",  
  "dataProvider": "IFC file"  
}  
```  
</details>  
#### CoolingTower NGSI-v2规范化示例  
下面是一个以JSON-LD格式规范化的CoolingTower的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:CoolingTower:7995c5cf-c8c3-4e42-92db-6dd840796eae",  
  "type": "CoolingTower",  
  "ambientDesignDryBulbTemperature": {  
    "type": "Measurement",  
    "value": 0.36789185492213194  
  },  
  "ambientDesignWetBulbTemperature": {  
    "type": "Measurement",  
    "value": 0.1490037569659941  
  },  
  "basinReserveVolume": {  
    "type": "Measurement",  
    "value": 0.9142388286093716  
  },  
  "capacityControl": {  
    "type": "Text",  
    "value": "next-generation"  
  },  
  "circuitType": {  
    "type": "Text",  
    "value": "morph"  
  },  
  "controlStrategy": {  
    "type": "Text",  
    "value": "Concrete"  
  },  
  "flowArrangement": {  
    "type": "Text",  
    "value": "access"  
  },  
  "liftElevationDifference": {  
    "type": "Measurement",  
    "value": 0.6134421322995507  
  },  
  "nominalCapacity": {  
    "type": "Measurement",  
    "value": 0.14285208313177855  
  },  
  "numberOfCells": {  
    "type": "Float",  
    "value": 0.9307947920697038  
  },  
  "operationTemperatureMax": {  
    "type": "Measurement",  
    "value": 0.33271163839338236  
  },  
  "operationTemperatureMin": {  
    "type": "Measurement",  
    "value": 0.8346930607066967  
  },  
  "sprayType": {  
    "type": "Text",  
    "value": "synthesizing"  
  },  
  "waterRequirement": {  
    "type": "Measurement",  
    "value": 0.6749365729986966  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:BuildingSpace:e1c9dc03-9887-49df-9577-a24218339c39"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:PhysicalObject:d6e1c0cc-a656-4343-8572-21de93d365ba"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:972d1b4b-ab6d-474c-a742-c75822d6c7b8"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:8c7d509c-66b4-4504-ad2e-d7ec82146ba2"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:42d552ca-9fdd-4838-804e-41f34d6f61f7"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "CoolingTower Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "CoolingTower 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T21:28:15.4871264+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T13:03:39.0857574+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "CoolingTower"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "CoolingTower type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "CoolingTower of limited CoolingTower types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### CoolingTower NGSI-LD关键值示例  
这里是一个以JSON-LD格式作为key-values的CoolingTower的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:CoolingTower:c628d24d-5b25-4b99-838e-35676956d307",  
  "type": "CoolingTower",  
  "ambientDesignDryBulbTemperature": 0.7275209381168831,  
  "ambientDesignWetBulbTemperature": 0.8419497776651206,  
  "basinReserveVolume": 0.9886525691530367,  
  "capacityControl": "Lead",  
  "circuitType": "virtual",  
  "controlStrategy": "Harbors",  
  "flowArrangement": "Extensions",  
  "liftElevationDifference": 0.9337996577856725,  
  "nominalCapacity": 0.8043496896372141,  
  "numberOfCells": 0.03361385186991317,  
  "operationTemperatureMax": 0.7125610456321683,  
  "operationTemperatureMin": 0.3015974804386986,  
  "sprayType": "programming",  
  "waterRequirement": 0.1817597423361893,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:6871b1ec-cfce-4a60-83c2-9f07b13d1703",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:e2a48930-276e-4972-9283-82fbc22faf85",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:aea47887-bc5b-47c3-aeb0-870506d76580",  
    "urn:ngsi-ld:System:2791b628-8fc1-4ec1-91a7-26efbbc892a3",  
    "urn:ngsi-ld:System:c0623c49-ae1f-4772-9323-a94078dbdb86"  
  ],  
  "hasManufacturer": "CoolingTower Company Inc.",  
  "hasModel": "CoolingTower 0.1.2",  
  "dateCreated": "2023-01-26T12:17:43Z",  
  "dateModified": "2023-01-25T16:13:00Z",  
  "source": "Import",  
  "name": "CoolingTower",  
  "alternateName": "CoolingTower type 2",  
  "description": "CoolingTower of limited CoolingTower types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### CoolingTower NGSI-LD归一化实例  
下面是一个以JSON-LD格式规范化的CoolingTower的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:CoolingTower:eb831bd2-82be-42c3-a0c9-a6c0a231e316",  
  "type": "CoolingTower",  
  "ambientDesignDryBulbTemperature": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T08:09:09Z",  
    "value": 0.9762464796853121  
  },  
  "ambientDesignWetBulbTemperature": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T14:29:40Z",  
    "value": 0.3062794162138128  
  },  
  "basinReserveVolume": {  
    "type": "Property",  
    "unitCode": "m3",  
    "observedAt": "2023-01-26T01:28:50Z",  
    "value": 0.9472477891325785  
  },  
  "capacityControl": {  
    "type": "Property",  
    "value": "input"  
  },  
  "circuitType": {  
    "type": "Property",  
    "value": "Mauritania"  
  },  
  "controlStrategy": {  
    "type": "Property",  
    "value": "Investor"  
  },  
  "flowArrangement": {  
    "type": "Property",  
    "value": "Direct"  
  },  
  "liftElevationDifference": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T02:02:47Z",  
    "value": 0.36539365901818843  
  },  
  "nominalCapacity": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-25T22:40:21Z",  
    "value": 0.3624642546775261  
  },  
  "numberOfCells": {  
    "type": "Property",  
    "value": 0.5588013730579288  
  },  
  "operationTemperatureMax": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T23:30:50Z",  
    "value": 0.660338038211496  
  },  
  "operationTemperatureMin": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T23:56:27Z",  
    "value": 0.0877235060077185  
  },  
  "sprayType": {  
    "type": "Property",  
    "value": "Money Market Account"  
  },  
  "waterRequirement": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-25T16:48:25Z",  
    "value": 0.40722633971933253  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:61ad4f84-a577-49d5-a088-aa301efa4ec6"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:f02a5bc4-2f87-4ff7-8dd7-fb61243128a1"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:b9323186-933c-46fd-815f-7f025b04ca80"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:1cea31ba-2978-4af2-b717-5c2a98a431b4"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:13dbe647-863b-4b1f-b10c-1737310d7c51"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "CoolingTower Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "CoolingTower 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T23:05:59Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-25T18:47:19Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "CoolingTower"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "CoolingTower type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "CoolingTower of limited CoolingTower types"  
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
