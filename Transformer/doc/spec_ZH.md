<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体：变压器    
======<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Transformer/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全球说明：**变压器是一种将电能从一个电路传输到另一个电路的感应式固定装置。  变压器用于转换电能；用于其他目的的电信号转换由其他实体处理：控制器转换任意信号，视听设备转换音频或视频流信号，通信设备转换数据或其他通信用途的信号。    
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
- `alternateName[string]`: 该项目的替代名称  - `apparentPowerMax[number]`: 最大视在功率/容量，单位 VA（伏安）。通常以瓦特（瓦，焦耳/秒）为计量单位  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `hasManufacturer[string]`: 标识实体（如设备）制造商的关系。该值应为字符串或带有语言标记的字符串。  - `hasModel[string]`: 标识实体（如设备）模型的关系。该值应是字符串或带有语言标记的字符串  - `id[*]`: 实体的唯一标识符  - `imaginaryImpedanceRatio[number]`: 变压器零序阻抗的虚部与正阻抗的虚部（即短路电压的虚部）之比。用于包括 N 型导体的三相变压器。  - `isContainedInBuildingSpace[*]`: 用于定义楼宇物理空间的实体。建筑空间包含设备或建筑对象。(建筑空间）  - `isContainedInPhysicalObject[*]`: 任何具有适当空间区域的物体。  (从 DUL 本体中提取的定义）（物理对象）  - `isNeutralPrimaryTerminalAvailable[boolean]`: 表示初级绕组的中性点是否可用作接线端子（=真）或不可用作接线端子（=假）  - `isNeutralSecondaryTerminalAvailable[boolean]`: 表示二次绕组的中性点是否可用作接线端子（=真）或不可用作接线端子（=假）  - `isSubSystemOf[array]`: 该物理对象所属系统的引用  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `primaryApparentPower[number]`: 变压器初级侧运行的功率，单位为 VA（伏安）。通常以瓦特（瓦，焦耳/秒）为计量单位  - `primaryCurrent[number]`: 变压器初级侧的电流。通常以安培（A）为计量单位  - `primaryFrequency[number]`: 变压器初级侧的频率。通常以周期/秒或赫兹（Hz）为单位测量  - `primaryVoltage[number]`: 变压器一次侧的电压。通常以伏特为单位（V，W/A）  - `realImpedanceRatio[number]`: 变压器零序阻抗的实部与正阻抗的实部（即短路电压的实部）之比。用于包括 N 型导体的三相变压器。  - `secondaryApparentPower[number]`: 变压器二次侧输出的功率，单位为 VA（伏安）。通常以瓦特（瓦，焦耳/秒）为计量单位  - `secondaryCurrent[number]`: 变压器二次侧已经变压并流出的电流。通常以安培（A）为单位测量  - `secondaryCurrentType[string]`: 变压器输出可能产生的次级电流类型列表  - `secondaryFrequency[number]`: 经过变换并从变压器二次侧输出的频率。通常以周期/秒或赫兹 (Hz) 为单位测量  - `secondaryVoltage[number]`: 经过变压后从变压器二次侧输出的电压。通常以伏特为单位（V，W/A）  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `transformerVectorGroup[string]`: 变压器可能的矢量组列表，可根据需要进行设置。枚举列表中的值采用标准国际代码，其中第一个字母表示一次绕组的连接方式，第二个字母表示二次绕组的连接方式，数字表示电压和电流从一次侧到二次侧的旋转角度，以 30 度的倍数表示。D：表示绕组为三角连接。Y：表示绕组为星形连接。Z：表示绕组为之字形连接（一种特殊的启动连接方式，可降低变压器的电抗）。连接方式只适用于三相变压器  - `type[string]`: 必须等于 "变压器  <!-- /30-PropertiesList -->    
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
Transformer:      
  description: 'A transformer is an inductive stationary device that transfers electrical energy from one circuit to another.  Transformer is used to transform electric power; conversion of electric signals for other purposes is handled at other entities: Controller converts arbitrary signals, AudioVisualAppliance converts signals for audio or video streams, and CommunicationsAppliance converts signals for data or other communications usage.'      
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
    apparentPowerMax:      
      description: 'Maximum apparent power/capacity in VA (volt ampere). Usually measured in Watts (W, J/s)'      
      type: number      
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
    imaginaryImpedanceRatio:      
      description: The ratio between the imaginary part of the zero sequence impedance and the imaginary part of the positive impedance (i.e. imaginary part of the short-circuit voltage) of the transformer. Used for three-phase transformer which includes a N-conductor      
      type: number      
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
    isNeutralPrimaryTerminalAvailable:      
      description: An indication of whether the neutral point of the primary winding is available as a terminal (=TRUE) or not (= FALSE)      
      type: boolean      
      x-ngsi:      
        type: Property      
    isNeutralSecondaryTerminalAvailable:      
      description: An indication of whether the neutral point of the secondary winding is available as a terminal (=TRUE) or not (= FALSE)      
      type: boolean      
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
    primaryApparentPower:      
      description: 'The power in VA (volt ampere) that has been transformed and that runs into the transformer on the primary side. Usually measured in Watts (W, J/s)'      
      type: number      
      x-ngsi:      
        type: Property      
    primaryCurrent:      
      description: The current that is going to be transformed and that runs into the transformer on the primary side. Usually measured in Ampere (A)      
      type: number      
      x-ngsi:      
        type: Property      
    primaryFrequency:      
      description: The frequency that is going to be transformed and that runs into the transformer on the primary side. Usually measured in cycles/s or Hertz (Hz)      
      type: number      
      x-ngsi:      
        type: Property      
    primaryVoltage:      
      description: 'The voltage that is going to be transformed and that runs into the transformer on the primary side. Usually measured in Volts (V, W/A)'      
      type: number      
      x-ngsi:      
        type: Property      
    realImpedanceRatio:      
      description: The ratio between the real part of the zero sequence impedance and the real part of the positive impedance (i.e. real part of the short-circuit voltage) of the transformer. Used for three-phase transformer which includes a N-conductor      
      type: number      
      x-ngsi:      
        type: Property      
    secondaryApparentPower:      
      description: 'The power in VA (volt ampere) that has been transformed and is running out of the transformer on the secondary side. Usually measured in Watts (W, J/s)'      
      type: number      
      x-ngsi:      
        type: Property      
    secondaryCurrent:      
      description: The current that has been transformed and is running out of the transformer on the secondary side. Usually measured in Ampere (A)      
      type: number      
      x-ngsi:      
        type: Property      
    secondaryCurrentType:      
      description: A list of the secondary current types that can result from transformer output      
      type: string      
      x-ngsi:      
        type: Property      
    secondaryFrequency:      
      description: The frequency that has been transformed and is running out of the transformer on the secondary side. Usually measured in cycles/s or Hertz (Hz)      
      type: number      
      x-ngsi:      
        type: Property      
    secondaryVoltage:      
      description: 'The voltage that has been transformed and is running out of the transformer on the secondary side. Usually measured in Volts (V, W/A)'      
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
    transformerVectorGroup:      
      description: 'List of the possible vector groups for the transformer from which that required may be set. Values in the enumeration list follow a standard international code where the first letter describes how the primary windings are connected, the second letter describes how the secondary windings are connected, and the numbers describe the rotation of voltages and currents from the primary to the secondary side in multiples of 30 degrees. D: means that the windings are delta-connected. Y: means that the windings are star-connected. Z: means that the windings are zig-zag connected (a special start-connected providing low reactance of the transformer). The connectivity is only relevant for three-phase transformers'      
      type: string      
      x-ngsi:      
        type: Property      
    type:      
      description: It must be equal to `Transformer`      
      enum:      
        - Transformer      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Transformer"      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Transformer/LICENSE.md      
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Transformer/schema.json      
  x-model-tags: SAREF Transformer      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 有效载荷示例    
#### 转换器 NGSI-v2 键值示例    
下面是一个以 JSON-LD 格式作为键值的变换器示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Transformer:4976b0ec-0c96-4ae1-91da-c906da8348da",  
  "type": "Transformer",  
  "apparentPowerMax": 0.17497838413457267,  
  "imaginaryImpedanceRatio": 0.5323895083879017,  
  "isNeutralPrimaryTerminalAvailable": false,  
  "isNeutralSecondaryTerminalAvailable": true,  
  "primaryApparentPower": 0.8765115449298688,  
  "primaryCurrent": 0.871670986786111,  
  "primaryFrequency": 0.141749759362659,  
  "primaryVoltage": 0.5038263292514936,  
  "realImpedanceRatio": 0.06325384828151492,  
  "secondaryApparentPower": 0.45704946090246745,  
  "secondaryCurrent": 0.4016609926228465,  
  "secondaryCurrentType": "Data",  
  "secondaryFrequency": 0.7436141485906284,  
  "secondaryVoltage": 0.4646450009162978,  
  "transformerVectorGroup": "Soft",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:51645089-5e36-4b9c-ad25-b97b58506919",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:6737e804-54ff-41c0-ba12-90dde24f3d59",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:38dfdf15-5a41-412d-9b05-435cb7809e6f",  
    "urn:ngsi-ld:System:b7274b46-33ec-4694-8dda-999197bb58c5",  
    "urn:ngsi-ld:System:b7d5c2ce-fc23-42d0-be8f-9e56a9f3c5db"  
  ],  
  "hasManufacturer": "Transformer Company Inc.",  
  "hasModel": "Transformer 0.1.2",  
  "dateCreated": "2023-01-25T16:42:43Z",  
  "dateModified": "2023-01-26T13:53:42Z",  
  "source": "Import",  
  "name": "Transformer",  
  "alternateName": "Transformer type 2",  
  "description": "Transformer of limited Transformer types",  
  "dataProvider": "IFC file"  
}  
```  
</details>    
#### 变压器 NGSI-v2 标准化示例    
下面是一个规范化 JSON-LD 格式的变换器示例。当不使用选项时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Transformer:7dc130e2-e429-4c26-b467-ec9d1f41e7b8",  
  "type": "Transformer",  
  "apparentPowerMax": {  
    "type": "Number",  
    "value": 0.6561932522421066  
  },  
  "imaginaryImpedanceRatio": {  
    "type": "Number",  
    "value": 0.7913482963385954  
  },  
  "isNeutralPrimaryTerminalAvailable": {  
    "type": "Boolean",  
    "value": true  
  },  
  "isNeutralSecondaryTerminalAvailable": {  
    "type": "Boolean",  
    "value": true  
  },  
  "primaryApparentPower": {  
    "type": "Number",  
    "value": 0.23470397848013025  
  },  
  "primaryCurrent": {  
    "type": "Number",  
    "value": 0.7245530289719985  
  },  
  "primaryFrequency": {  
    "type": "Number",  
    "value": 0.18927842693402908  
  },  
  "primaryVoltage": {  
    "type": "Number",  
    "value": 0.359590276424793  
  },  
  "realImpedanceRatio": {  
    "type": "Number",  
    "value": 0.6917590580595899  
  },  
  "secondaryApparentPower": {  
    "type": "Number",  
    "value": 0.10075664755263747  
  },  
  "secondaryCurrent": {  
    "type": "Number",  
    "value": 0.1458215404162363  
  },  
  "secondaryCurrentType": {  
    "type": "Text",  
    "value": "Tasty Wooden Car"  
  },  
  "secondaryFrequency": {  
    "type": "Number",  
    "value": 0.09146741937660052  
  },  
  "secondaryVoltage": {  
    "type": "Number",  
    "value": 0.31779800995261864  
  },  
  "transformerVectorGroup": {  
    "type": "Text",  
    "value": "SMS"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:BuildingSpace:16bccee7-8244-4707-8d4b-c5a06b0fee75"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:PhysicalObject:b9a1bd5e-114e-41ba-b865-25b4b4c5c3c5"  
  },  
  "isSubSystemOf": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:System:37554df5-ec0d-4e03-8697-7d562ff2134f",  
      "urn:ngsi-ld:System:e967a169-474b-47a0-bd0c-a76ce8a5f7be",  
      "urn:ngsi-ld:System:49a6b09b-2301-4b6e-a167-54ee44cc83d4"  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Transformer Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Transformer 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T20:08:21.2034652+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T22:13:38.7837862+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Transformer"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Transformer type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Transformer of limited Transformer types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>    
#### 转换器 NGSI-LD 键值示例    
下面是一个以 JSON-LD 格式作为键值的变换器示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Transformer:4976b0ec-0c96-4ae1-91da-c906da8348da",  
  "type": "Transformer",  
  "apparentPowerMax": 0.17497838413457267,  
  "imaginaryImpedanceRatio": 0.5323895083879017,  
  "isNeutralPrimaryTerminalAvailable": false,  
  "isNeutralSecondaryTerminalAvailable": true,  
  "primaryApparentPower": 0.8765115449298688,  
  "primaryCurrent": 0.871670986786111,  
  "primaryFrequency": 0.141749759362659,  
  "primaryVoltage": 0.5038263292514936,  
  "realImpedanceRatio": 0.06325384828151492,  
  "secondaryApparentPower": 0.45704946090246745,  
  "secondaryCurrent": 0.4016609926228465,  
  "secondaryCurrentType": "Data",  
  "secondaryFrequency": 0.7436141485906284,  
  "secondaryVoltage": 0.4646450009162978,  
  "transformerVectorGroup": "Soft",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:51645089-5e36-4b9c-ad25-b97b58506919",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:6737e804-54ff-41c0-ba12-90dde24f3d59",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:38dfdf15-5a41-412d-9b05-435cb7809e6f",  
    "urn:ngsi-ld:System:b7274b46-33ec-4694-8dda-999197bb58c5",  
    "urn:ngsi-ld:System:b7d5c2ce-fc23-42d0-be8f-9e56a9f3c5db"  
  ],  
  "hasManufacturer": "Transformer Company Inc.",  
  "hasModel": "Transformer 0.1.2",  
  "dateCreated": "2023-01-25T16:42:43Z",  
  "dateModified": "2023-01-26T13:53:42Z",  
  "source": "Import",  
  "name": "Transformer",  
  "alternateName": "Transformer type 2",  
  "description": "Transformer of limited Transformer types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>    
#### 变压器 NGSI-LD 归一化示例    
下面是一个规范化 JSON-LD 格式的变换器示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Transformer:24b95122-4055-44dc-82ad-09a2bcda9025",  
  "type": "Transformer",  
  "apparentPowerMax": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-25T20:30:38Z",  
    "value": 0.24466523496915848  
  },  
  "imaginaryImpedanceRatio": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T00:56:06Z",  
    "value": 0.0034198103714959682  
  },  
  "isNeutralPrimaryTerminalAvailable": {  
    "type": "Property",  
    "value": false  
  },  
  "isNeutralSecondaryTerminalAvailable": {  
    "type": "Property",  
    "value": true  
  },  
  "primaryApparentPower": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-26T12:47:55Z",  
    "value": 0.9141641275735504  
  },  
  "primaryCurrent": {  
    "type": "Property",  
    "unitCode": "A",  
    "observedAt": "2023-01-26T04:09:04Z",  
    "value": 0.21921580436899846  
  },  
  "primaryFrequency": {  
    "type": "Property",  
    "unitCode": "Hz",  
    "observedAt": "2023-01-26T11:27:17Z",  
    "value": 0.8873577584995188  
  },  
  "primaryVoltage": {  
    "type": "Property",  
    "unitCode": "W/A",  
    "observedAt": "2023-01-26T07:23:40Z",  
    "value": 0.33421317836814646  
  },  
  "realImpedanceRatio": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T03:38:23Z",  
    "value": 0.6061321069719529  
  },  
  "secondaryApparentPower": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-25T19:57:55Z",  
    "value": 0.3997980055591537  
  },  
  "secondaryCurrent": {  
    "type": "Property",  
    "unitCode": "A",  
    "observedAt": "2023-01-26T13:58:27Z",  
    "value": 0.2899846616898377  
  },  
  "secondaryCurrentType": {  
    "type": "Property",  
    "value": "human-resource"  
  },  
  "secondaryFrequency": {  
    "type": "Property",  
    "unitCode": "Hz",  
    "observedAt": "2023-01-26T03:39:16Z",  
    "value": 0.06983160765779406  
  },  
  "secondaryVoltage": {  
    "type": "Property",  
    "unitCode": "W/A",  
    "observedAt": "2023-01-26T07:19:14Z",  
    "value": 0.8594539881916403  
  },  
  "transformerVectorGroup": {  
    "type": "Property",  
    "value": "digital"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:ded8c891-dfe1-4973-966c-96ab6231373d"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:aab67381-2a15-4bdc-ab0f-953b17253b8f"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:d06b6674-162c-4593-a8fd-3874ef353008"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:d0aca3bd-bf1b-4e9e-a998-a76c9b1ac7a6"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:1ab049a0-7295-4eef-82a1-0bb422132435"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Transformer Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Transformer 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T06:32:52Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T05:11:11Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Transformer"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Transformer type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Transformer of limited Transformer types"  
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
