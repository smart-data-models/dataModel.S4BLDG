<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：变压器  
======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Transformer/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述：**变压器是一种将电能从一个电路转移到另一个电路的感应式固定装置。  变压器用于转换电力；用于其他目的的电信号的转换由其他实体处理：控制器转换任意信号，视听设备转换音频或视频流的信号，通信设备转换数据或其他通信用途的信号。  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `apparentPowerMax[number]`: 属性。最大表观功率/容量，单位为VA（伏安）。通常以瓦特（W，J/s）为单位测量。  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `hasManufacturer[string]`: 属性。识别实体（例如，设备）的制造商的关系。该值应是一个字符串或一个带有语言标签的字符串。  - `hasModel[string]`: 属性。识别实体（例如，设备）的模型的关系。该值应是一个字符串或一个带有语言标签的字符串。  - `id[*]`: 实体的唯一标识符  - `imaginaryImpedanceRatio[number]`: 属性。零序阻抗的虚数部分与变压器的正向阻抗的虚数部分（即短路电压的虚数部分）之间的比率。用于包括一个N型导体的三相变压器。  - `isContainedInBuildingSpace[*]`: 关系。一个用于定义建筑物理空间的实体。一个建筑空间包含设备或建筑对象。(建筑空间)  - `isContainedInPhysicalObject[*]`: 关系。任何具有适当空间区域的物体。  (从DUL本体论中提取的定义）（PhysicalObject）。  - `isNeutralPrimaryTerminalAvailable[boolean]`: 属性。指示初级绕组的中性点是否可以作为一个终端（=TRUE）或不（=FALSE）。  - `isNeutralSecondaryTerminalAvailable[boolean]`: 属性。次级绕组的中性点是否可以作为终端（=TRUE）或不（=FALSE）的指示。  - `isSubSystemOf[array]`: 关系。对该物理对象是其一部分的系统的引用。  - `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `name[string]`: 这个项目的名称。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `primaryApparentPower[number]`: 属性。已经转化的功率，以VA（伏安）为单位，在一次侧运行到变压器中。通常以瓦特（W，J/s）衡量。  - `primaryCurrent[number]`: 属性。将要被转换的电流，在初级侧运行到变压器中。通常以安培（A）为单位进行测量。  - `primaryFrequency[number]`: 属性。将被转换的频率，并在初级侧运行到变压器中。通常以周期/秒或赫兹（Hz）来衡量。  - `primaryVoltage[number]`: 属性。将要转化的电压，在初级侧流入变压器的电压。通常以伏特（V，W/A）为单位测量。  - `realImpedanceRatio[number]`: 属性。零序阻抗的实数部分与变压器的正向阻抗的实数部分（即短路电压的实数部分）之间的比率。用于包括一个N型导体的三相变压器。  - `secondaryApparentPower[number]`: 属性。以VA（伏特安培）为单位的功率，已被转化并从变压器的二次侧跑出来。通常以瓦特（W，J/s）为单位测量。  - `secondaryCurrent[number]`: 属性。已经转化并从变压器二次侧跑出来的电流。通常以安培（A）为单位测量。  - `secondaryCurrentType[string]`: 属性。可导致变压器输出的次级电流类型的列表。  - `secondaryFrequency[number]`: 属性。已经转换并从变压器二次侧跑出来的频率。通常以周期/秒或赫兹（Hz）测量。  - `secondaryVoltage[number]`: 属性。已经转化并从变压器二次侧跑出来的电压。通常以伏特（V，W/A）为单位测量。  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `transformerVectorGroup[string]`: 属性。变压器可能的矢量组的列表，该要求可从中设置。枚举列表中的值遵循标准的国际代码，其中第一个字母描述初级绕组的连接方式，第二个字母描述次级绕组的连接方式，数字描述电压和电流从初级到次级的旋转，其倍数为30度。D：表示绕组是三角连接的。Y：表示绕组是星形连接的。Z：表示绕组为人字形连接（一种特殊的启动连接，提供变压器的低电抗）。这种连接方式只适用于三相变压器。  - `type[string]`: 属性。它必须等于`变形器'。  <!-- /30-PropertiesList -->  
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
Transformer:    
  description: 'A transformer is an inductive stationary device that transfers electrical energy from one circuit to another.  Transformer is used to transform electric power; conversion of electric signals for other purposes is handled at other entities: Controller converts arbitrary signals, AudioVisualAppliance converts signals for audio or video streams, and CommunicationsAppliance converts signals for data or other communications usage.'    
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
    apparentPowerMax:    
      description: 'Property. Maximum apparent power/capacity in VA (volt ampere). Usually measured in Watts (W, J/s).'    
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
      anyOf: &transformer_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    imaginaryImpedanceRatio:    
      description: Property. The ratio between the imaginary part of the zero sequence impedance and the imaginary part of the positive impedance (i.e. imaginary part of the short-circuit voltage) of the transformer. Used for three-phase transformer which includes a N-conductor.    
      type: number    
      x-ngsi:    
        type: Property    
    isContainedInBuildingSpace:    
      anyOf: *transformer_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *transformer_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isNeutralPrimaryTerminalAvailable:    
      description: Property. An indication of whether the neutral point of the primary winding is available as a terminal (=TRUE) or not (= FALSE).    
      type: boolean    
      x-ngsi:    
        type: Property    
    isNeutralSecondaryTerminalAvailable:    
      description: Property. An indication of whether the neutral point of the secondary winding is available as a terminal (=TRUE) or not (= FALSE).    
      type: boolean    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *transformer_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    name:    
      description: The name of this item.    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *transformer_-_properties_-_iscontainedinbuildingspace_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    primaryApparentPower:    
      description: 'Property. The power in VA (volt ampere) that has been transformed and that runs into the transformer on the primary side. Usually measured in Watts (W, J/s).'    
      type: number    
      x-ngsi:    
        type: Property    
    primaryCurrent:    
      description: Property. The current that is going to be transformed and that runs into the transformer on the primary side. Usually measured in Ampere (A).    
      type: number    
      x-ngsi:    
        type: Property    
    primaryFrequency:    
      description: Property. The frequency that is going to be transformed and that runs into the transformer on the primary side. Usually measured in cycles/s or Hertz (Hz).    
      type: number    
      x-ngsi:    
        type: Property    
    primaryVoltage:    
      description: 'Property. The voltage that is going to be transformed and that runs into the transformer on the primary side. Usually measured in Volts (V, W/A).'    
      type: number    
      x-ngsi:    
        type: Property    
    realImpedanceRatio:    
      description: Property. The ratio between the real part of the zero sequence impedance and the real part of the positive impedance (i.e. real part of the short-circuit voltage) of the transformer. Used for three-phase transformer which includes a N-conductor.    
      type: number    
      x-ngsi:    
        type: Property    
    secondaryApparentPower:    
      description: 'Property. The power in VA (volt ampere) that has been transformed and is running out of the transformer on the secondary side. Usually measured in Watts (W, J/s).'    
      type: number    
      x-ngsi:    
        type: Property    
    secondaryCurrent:    
      description: Property. The current that has been transformed and is running out of the transformer on the secondary side. Usually measured in Ampere (A).    
      type: number    
      x-ngsi:    
        type: Property    
    secondaryCurrentType:    
      description: Property. A list of the secondary current types that can result from transformer output.    
      type: string    
      x-ngsi:    
        type: Property    
    secondaryFrequency:    
      description: Property. The frequency that has been transformed and is running out of the transformer on the secondary side. Usually measured in cycles/s or Hertz (Hz).    
      type: number    
      x-ngsi:    
        type: Property    
    secondaryVoltage:    
      description: 'Property. The voltage that has been transformed and is running out of the transformer on the secondary side. Usually measured in Volts (V, W/A).'    
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
    transformerVectorGroup:    
      description: 'Property. List of the possible vector groups for the transformer from which that required may be set. Values in the enumeration list follow a standard international code where the first letter describes how the primary windings are connected, the second letter describes how the secondary windings are connected, and the numbers describe the rotation of voltages and currents from the primary to the secondary side in multiples of 30 degrees. D: means that the windings are delta-connected. Y: means that the windings are star-connected. Z: means that the windings are zig-zag connected (a special start-connected providing low reactance of the transformer). The connectivity is only relevant for three-phase transformers.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: Property. It must be equal to `Transformer`.    
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
## ＃＃＃＃有效载荷的例子  
#### 变换器NGSI-v2关键值示例  
这里有一个以JSON-LD格式作为key-values的Transformer的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### 变压器NGSI-v2规范化示例  
这里有一个JSON-LD格式的Transformer的例子，是规范化的。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Transformer:7dc130e2-e429-4c26-b467-ec9d1f41e7b8",  
  "type": "Transformer",  
  "apparentPowerMax": {  
    "type": "Measurement",  
    "value":  0.6561932522421066  
  },  
  "imaginaryImpedanceRatio": {  
    "type": "Measurement",  
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
    "type": "Measurement",  
    "value":  0.23470397848013025  
  },  
  "primaryCurrent": {  
    "type": "Measurement",  
    "value":  0.7245530289719985  
  },  
  "primaryFrequency": {  
    "type": "Measurement",  
    "value":  0.18927842693402908  
  },  
  "primaryVoltage": {  
    "type": "Measurement",  
    "value":  0.359590276424793  
  },  
  "realImpedanceRatio": {  
    "type": "Measurement",  
    "value":  0.6917590580595899  
  },  
  "secondaryApparentPower": {  
    "type": "Measurement",  
    "value":  0.10075664755263747  
  },  
  "secondaryCurrent": {  
    "type": "Measurement",  
    "value": 0.1458215404162363  
  },  
  "secondaryCurrentType": {  
    "type": "Text",  
    "value": "Tasty Wooden Car"  
  },  
  "secondaryFrequency": {  
    "type": "Measurement",  
    "value":  0.09146741937660052  
  },  
  "secondaryVoltage": {  
    "type": "Measurement",  
    "value": 0.31779800995261864  
  },  
  "transformerVectorGroup": {  
    "type": "Text",  
    "value": "SMS"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:BuildingSpace:16bccee7-8244-4707-8d4b-c5a06b0fee75"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:PhysicalObject:b9a1bd5e-114e-41ba-b865-25b4b4c5c3c5"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:37554df5-ec0d-4e03-8697-7d562ff2134f"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:e967a169-474b-47a0-bd0c-a76ce8a5f7be"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:49a6b09b-2301-4b6e-a167-54ee44cc83d4"  
      }  
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
#### 变换器NGSI-LD关键值示例  
这里有一个以JSON-LD格式作为key-values的Transformer的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
#### 变压器NGSI-LD正常化的例子  
这里有一个JSON-LD格式的Transformer的例子，是规范化的。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
