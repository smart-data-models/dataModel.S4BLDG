<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：线圈  
=====<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Coil/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述：**线圈是一种用于在非混合介质之间提供热传递的装置。一个常见的例子是冷却线圈，它利用一个鳍状线圈，在其中循环冷冻水、防冻剂或制冷剂，用于从穿过线圈表面的空气中去除热量。盘管可用于加热或冷却目的，将一系列携带加热或冷却液体的管子（盘管）放入气流中。盘管可以由管子捆绑成蛇形或由翅片管构成，从而提供一个扩展的传热表面。  盘管也可用于非气流的情况，如嵌入楼板中。  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `airFlowRateMax[number]`: 属性。最大允许的空气流速。通常以m3/s测量。  - `airFlowRateMin[number]`: 财产。最小允许的空气流速。通常以m3/s测量。  - `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `hasManufacturer[string]`: 属性。识别实体（例如，设备）的制造商的关系。该值应是一个字符串或一个带有语言标签的字符串。  - `hasModel[string]`: 属性。识别实体（例如，设备）的模型的关系。该值应是一个字符串或一个带有语言标签的字符串。  - `id[*]`: 实体的唯一标识符  - `isContainedInBuildingSpace[*]`: 关系。一个用于定义建筑物理空间的实体。一个建筑空间包含设备或建筑对象。(建筑空间)  - `isContainedInPhysicalObject[*]`: 关系。任何具有适当空间区域的物体。  (从DUL本体论中提取的定义）（PhysicalObject）。  - `isSubSystemOf[array]`: 关系。对该物理对象是其一部分的系统的引用。  - `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `name[string]`: 这个项目的名称。  - `nominalLatentCapacity[number]`: 属性。标称潜伏能力。通常以瓦特（W，J/s）衡量。  - `nominalSensibleCapacity[number]`: 属性。名义上的感性能力。通常以瓦特（W，J/s）衡量。  - `nominalUa[number]`: 属性。名义UA值。  - `operationMode[string]`: 属性。该线圈的操作模式。  - `operationTemperatureMax[number]`: 属性。允许的操作环境（空气、液体）温度范围。通常以开尔文(K)度衡量。  - `operationTemperatureMin[number]`: 属性。允许的操作环境（空气、液体）温度范围。通常以开尔文(K)度衡量。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `placementType[string]`: 属性。表示设备是如何设计放置的。  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `type[string]`: 属性。它必须等于 "线圈"。  <!-- /30-PropertiesList -->  
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
Coil:    
  description: 'A coil is a device used to provide heat transfer between non-mixing media. A common example is a cooling coil, which utilizes a finned coil in which circulates chilled water, antifreeze, or refrigerant that is used to remove heat from air moving across the surface of the coil. A coil may be used either for heating or cooling purposes by placing a series of tubes (the coil) carrying a heating or cooling fluid into an airstream. The coil may be constructed from tubes bundled in a serpentine form or from finned tubes that give a extended heat transfer surface.  Coils may also be used for non-airflow cases such as embedded in a floor slab.'    
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
    airFlowRateMax:    
      description: Property. Maximum allowable air flow rate. Usually measured in m3/s.    
      type: number    
      x-ngsi:    
        type: Property    
    airFlowRateMin:    
      description: Property. Minimum allowable air flow rate. Usually measured in m3/s.    
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
      anyOf: &coil_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      anyOf: *coil_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *coil_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *coil_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    nominalLatentCapacity:    
      description: 'Property. Nominal latent capacity. Usually measured in Watts (W, J/s).'    
      type: number    
      x-ngsi:    
        type: Property    
    nominalSensibleCapacity:    
      description: 'Property. Nominal sensible capacity. Usually measured in Watts (W, J/s).'    
      type: number    
      x-ngsi:    
        type: Property    
    nominalUa:    
      description: Property. Nominal UA value.    
      type: number    
      x-ngsi:    
        type: Property    
    operationMode:    
      description: Property. Operation mode of this coil.    
      enum:    
        - cooling    
        - heating    
      type: string    
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
        anyOf: *coil_-_properties_-_iscontainedinbuildingspace_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    placementType:    
      description: Property. Indicates how the device is designed to be placed.    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: Property. It must be equal to `Coil`.    
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
## ＃＃＃＃有效载荷的例子  
#### 线圈NGSI-v2关键值示例  
这里有一个JSON-LD格式的Coil作为key-values的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### 线圈NGSI-v2规范化示例  
下面是一个规范化的JSON-LD格式的Coil的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
    "type": "Relationship",  
    "value": "urn:ngsi-ld:BuildingSpace:1070b255-7508-4019-ba0a-1ce8a03cf3b1"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:PhysicalObject:cef12274-adeb-41a5-aec1-8e254593bb26"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:System:65b917e6-ec39-4e2e-bce1-a52a52c176bc"  
      },  
      {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:System:61834f7f-655f-47f1-828c-755a25e7b026"  
      },  
      {  
        "type": "Relationship",  
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
#### 线圈NGSI-LD关键值示例  
这里有一个JSON-LD格式的Coil作为key-values的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
#### 线圈NGSI-LD规范化示例  
这里有一个JSON-LD格式的Coil的例子，是规范化的。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
