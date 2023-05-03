<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：电动汽车  
=======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/ElectricMotor/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述：**电动机是一种发动机，是将电能转换为机械能的机器。  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `electricMotorEfficiency[number]`: 属性。输出能力与接收能力的比率。  - `frameSize[string]`: 属性。根据在使用地点指定的框架尺寸的命名范围或根据特定的标准来指定框架尺寸。  - `hasManufacturer[string]`: 属性。识别实体（例如，设备）的制造商的关系。该值应是一个字符串或一个带有语言标签的字符串。  - `hasModel[string]`: 属性。识别实体（例如，设备）的模型的关系。该值应是一个字符串或一个带有语言标签的字符串。  - `hasPartWinding[boolean]`: 属性。指示电机是单速，即有一个单绕组（=FALSE）还是多速，即有部分绕组（=TRUE）。  - `id[*]`: 实体的唯一标识符  - `isContainedInBuildingSpace[*]`: 关系。一个用于定义建筑物理空间的实体。一个建筑空间包含设备或建筑对象。(建筑空间)  - `isContainedInPhysicalObject[*]`: 关系。任何具有适当空间区域的物体。  (从DUL本体论中提取的定义）（PhysicalObject）。  - `isGuarded[boolean]`: 属性。指示电机外壳是否有防护（= TRUE）或没有防护（= FALSE）。  - `isSubSystemOf[array]`: 关系。对该物理对象是其一部分的系统的引用。  - `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `lockedRotorCurrent[number]`: 属性。当电机电枢通电但不旋转时的输入电流。通常以安培（A）为单位测量。  - `motorEnclosureType[string]`: 属性。可用的电机外壳类型列表，可从中选择所需的电机外壳。  - `name[string]`: 这个项目的名称。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `powerOutputMax[number]`: 属性。发动机的最大额定输出功率。通常以瓦特（W，J/s）衡量。  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `startCurrentFactor[number]`: 财产。IEC。启动电流系数定义了发动机上的窥视启动电流会有多大。StartCurrentFactor乘以NominalCurrent，我们就得到了启动电流。  - `startingTime[number]`: 属性。电机在连接了被动设备的情况下，从静止开始，在其端子上施加额定电压的情况下，达到其额定速度所需的时间（秒）。  - `teTime[number]`: 属性。当电机在EX环境中使用时，电机可以在锁定转子的情况下运行的最大时间（单位：秒）。该时间表明，当电机的启动电流通过该装置时，保护装置应在该时间之前跳闸。  - `type[string]`: 属性。它必须等于 "电动马达"。  <!-- /30-PropertiesList -->  
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
ElectricMotor:    
  description: An electric motor is an engine that is a machine for converting electrical energy into mechanical energy.    
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
    electricMotorEfficiency:    
      description: Property. The ratio of output capacity to intake capacity.    
      type: number    
      x-ngsi:    
        type: Property    
    frameSize:    
      description: Property. Designation of the frame size according to the named range of frame sizes designated at the place of use or according to a given standard.    
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
    hasPartWinding:    
      description: 'Property. Indication of whether the motor is single speed, i.e. has a single winding (= FALSE) or multi-speed i.e.has part winding (= TRUE) .'    
      type: boolean    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &electricmotor_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      anyOf: *electricmotor_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *electricmotor_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isGuarded:    
      description: Property. Indication of whether the motor enclosure is guarded (= TRUE) or not (= FALSE).    
      type: boolean    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *electricmotor_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    lockedRotorCurrent:    
      description: Property. Input current when a motor armature is energized but not rotating. Usually measured in Ampere (A).    
      type: number    
      x-ngsi:    
        type: Property    
    motorEnclosureType:    
      description: Property. A list of the available types of motor enclosure from which that required may be selected.    
      type: string    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item.    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *electricmotor_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    startingTime:    
      description: 'Property. The time (in s) needed for the motor to reach its rated speed with its driven equipment attached, starting from standstill and at the nominal voltage applied at its terminals.'    
      type: number    
      x-ngsi:    
        type: Property    
    teTime:    
      description: Property. The maximum time (in s) at which the motor could run with locked rotor when the motor is used in an EX-environment. The time indicates that a protective device should trip before this time when the starting current of the motor is slowing through the device.    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: Property. It must be equal to `ElectricMotor`.    
      enum:    
        - ElectricMotor    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:ElectricMotor"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/ElectricMotor/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/ElectricMotor/schema.json    
  x-model-tags: SAREF ElectricMotor    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### ElectricMotor NGSI-v2 key-values 示例  
这里是一个以JSON-LD格式作为关键值的ElectricMotor的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:ElectricMotor:ea4bd048-a263-480d-be61-7de297bed540",  
    "type": "ElectricMotor",  
    "airFlowRateMax": 0.1608748792870458,  
    "airFlowRateMin": 0.5144201035637935,  
    "hasExteriorInsulation": true,  
    "hydraulicDiameter": 0.655988670157379,  
    "length": 0.6761801102701772,  
    "operationTemperatureMax": 0.9108707788637439,  
    "operationTemperatureMin": 0.38034850956825317,  
    "weight": 0.3440451194010431,  
    "workingPressureMax": 0.4689060124065172,  
    "workingPressureMin": 0.6786833167445696,  
    "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:b1cccba1-7a35-422c-aca4-800d8f462b00",  
    "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:a15795e2-b0d9-4ab0-863c-bc40e5e88fc6",  
    "isSubSystemOf": [  
        "urn:ngsi-ld:System:24f05820-a94f-4c53-bd66-bcb5bc451ee4",  
        "urn:ngsi-ld:System:eb6a2613-cf69-4cdc-a958-b8f24903fc46",  
        "urn:ngsi-ld:System:594815c7-5dd7-4910-93ca-ee2579c87739"  
    ],  
    "hasManufacturer": "ElectricMotor Company Inc.",  
    "hasModel": "ElectricMotor 0.1.2",  
    "dateCreated": "2023-01-25T16:58:38Z",  
    "dateModified": "2023-01-25T21:01:09Z",  
    "source": "Import",  
    "name": "ElectricMotor",  
    "alternateName": "ElectricMotor type 2",  
    "description": "ElectricMotor of limited ElectricMotor types",  
    "dataProvider": "IFC file",  
    "nominalFrequency": 0.6643858958243121,  
    "nominalSupplyVoltage": 0.9863230627218449,  
    "nominalSupplyVoltageMin": 0.5073272634060758,  
    "electricGeneratorEfficiency": 0.1422180140007665,  
    "powerOutputMax": 0.5320055721976125,  
    "startCurrentFactor": 0.7921279415808247,  
    "electricMotorEfficiency": 0.36137565435400376,  
    "frameSize": "Awesome",  
    "hasPartWinding": false,  
    "isGuarded": false,  
    "lockedRotorCurrent": 0.4948278478821372,  
    "motorEnclosureType": "target",  
    "startingTime": 0.7237739470818347,  
    "teTime": 0.32577211564738595  
}  
```  
</details>  
#### ElectricMotor NGSI-v2规范化示例  
下面是一个规范化的JSON-LD格式的ElectricMotor的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ElectricMotor:024aea5d-c781-4d5e-9b57-92672c75663d",  
  "type": "ElectricMotor",  
  "electricMotorEfficiency": {  
    "type": "Measurement",  
    "value": 0.14465653517328592  
  },  
  "frameSize": {  
    "type": "Text",  
    "value": "benchmark"  
  },  
  "hasPartWinding": {  
    "type": "Boolean",  
    "value": true  
  },  
  "isGuarded": {  
    "type": "Boolean",  
    "value": false  
  },  
  "lockedRotorCurrent": {  
    "type": "Measurement",  
    "value":  0.7069578753062778  
  },  
  "motorEnclosureType": {  
    "type": "Text",  
    "value": "Cambridgeshire"  
  },  
  "powerOutputMax": {  
    "type": "Measurement",  
    "value": 0.925424003891414  
  },  
  "startCurrentFactor": {  
    "type": "Measurement",  
    "value": 0.27335468276078645  
  },  
  "startingTime": {  
    "type": "Measurement",  
    "value":  0.8955138694697009  
  },  
  "teTime": {  
    "type": "Measurement",  
    "value": 0.024805742901409134  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:BuildingSpace:dec2fd4f-2093-4779-b571-841bac3ec419"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:PhysicalObject:42195e3f-cdb8-4603-952f-d9f52d9749ed"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:System:08a8c968-420c-464d-8458-784dd721cfbe"  
      },  
      {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:System:92362fba-3ddd-47af-a985-de2caf90f298"  
      },  
      {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:System:3033fd90-5610-490c-8b39-6f98c962af41"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "ElectricMotor Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "ElectricMotor 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T20:39:17.5806269+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T18:24:24.0858451+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "ElectricMotor"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "ElectricMotor type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "ElectricMotor of limited ElectricMotor types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### ElectricMotor NGSI-LD key-values 示例  
这里是一个以JSON-LD格式作为关键值的ElectricMotor的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ElectricMotor:ea4bd048-a263-480d-be61-7de297bed540",  
  "type": "ElectricMotor",  
  "airFlowRateMax": 0.1608748792870458,  
  "airFlowRateMin": 0.5144201035637935,  
  "hasExteriorInsulation": true,  
  "hydraulicDiameter": 0.655988670157379,  
  "length": 0.6761801102701772,  
  "operationTemperatureMax": 0.9108707788637439,  
  "operationTemperatureMin": 0.38034850956825317,  
  "weight": 0.3440451194010431,  
  "workingPressureMax": 0.4689060124065172,  
  "workingPressureMin": 0.6786833167445696,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:b1cccba1-7a35-422c-aca4-800d8f462b00",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:a15795e2-b0d9-4ab0-863c-bc40e5e88fc6",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:24f05820-a94f-4c53-bd66-bcb5bc451ee4",  
    "urn:ngsi-ld:System:eb6a2613-cf69-4cdc-a958-b8f24903fc46",  
    "urn:ngsi-ld:System:594815c7-5dd7-4910-93ca-ee2579c87739"  
  ],  
  "hasManufacturer": "ElectricMotor Company Inc.",  
  "hasModel": "ElectricMotor 0.1.2",  
  "dateCreated": "2023-01-25T16:58:38Z",  
  "dateModified": "2023-01-25T21:01:09Z",  
  "source": "Import",  
  "name": "ElectricMotor",  
  "alternateName": "ElectricMotor type 2",  
  "description": "ElectricMotor of limited ElectricMotor types",  
  "dataProvider": "IFC file",  
  "nominalFrequency": 0.6643858958243121,  
  "nominalSupplyVoltage": 0.9863230627218449,  
  "nominalSupplyVoltageMin": 0.5073272634060758,  
  "electricGeneratorEfficiency": 0.1422180140007665,  
  "powerOutputMax": 0.5320055721976125,  
  "startCurrentFactor": 0.7921279415808247,  
  "electricMotorEfficiency": 0.36137565435400376,  
  "frameSize": "Awesome",  
  "hasPartWinding": false,  
  "isGuarded": false,  
  "lockedRotorCurrent": 0.4948278478821372,  
  "motorEnclosureType": "target",  
  "startingTime": 0.7237739470818347,  
  "teTime": 0.32577211564738595,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### 电动汽车NGSI-LD规范化示例  
下面是一个规范化的JSON-LD格式的ElectricMotor的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ElectricMotor:c4e91c91-12f4-4dc5-aaae-4c7644c8d9df",  
  "type": "ElectricMotor",  
  "electricMotorEfficiency": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T08:26:24Z",  
    "value": 0.07012980187189011  
  },  
  "frameSize": {  
    "type": "Property",  
    "value": "Saint Martin"  
  },  
  "hasPartWinding": {  
    "type": "Property",  
    "value": false  
  },  
  "isGuarded": {  
    "type": "Property",  
    "value": false  
  },  
  "lockedRotorCurrent": {  
    "type": "Property",  
    "unitCode": "A",  
    "observedAt": "2023-01-26T10:56:17Z",  
    "value": 0.7593092722196552  
  },  
  "motorEnclosureType": {  
    "type": "Property",  
    "value": "Berkshire"  
  },  
  "powerOutputMax": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-26T08:12:29Z",  
    "value": 0.32215622178270653  
  },  
  "startCurrentFactor": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T06:44:33Z",  
    "value": 0.8565155734572442  
  },  
  "startingTime": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T08:12:12Z",  
    "value": 0.7168865515513289  
  },  
  "teTime": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T06:08:56Z",  
    "value": 0.2793471624901087  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:c89167bc-11d5-48cc-8cde-0ea875d76fe3"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:e8206186-a4b3-4030-80dc-a4e5ebe12ab4"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:20c42d2b-4216-458d-9ef0-a0fece28ca92"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:5418d44a-319c-46af-aa8a-83e59fb559e7"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:7baa4e2b-ac2d-4a9b-90a2-ef578b5091a7"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "ElectricMotor Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "ElectricMotor 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T09:43:59Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T14:02:00Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "ElectricMotor"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "ElectricMotor type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "ElectricMotor of limited ElectricMotor types"  
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
