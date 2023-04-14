<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：电流存储设备(ElectricFlowStorageDevice)  
====================================<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/ElectricFlowStorageDevice/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述：**电流量储存装置是一种储存电能的装置，并可从其中逐步释放能量。  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `hasManufacturer[string]`: 属性。识别实体（例如，设备）的制造商的关系。该值应是一个字符串或一个带有语言标签的字符串。  - `hasModel[string]`: 属性。识别实体（例如，设备）的模型的关系。该值应是一个字符串或一个带有语言标签的字符串。  - `id[*]`: 实体的唯一标识符  - `isContainedInBuildingSpace[*]`: 关系。一个用于定义建筑物理空间的实体。一个建筑空间包含设备或建筑对象。(建筑空间)  - `isContainedInPhysicalObject[*]`: 关系。任何具有适当空间区域的物体。  (从DUL本体论中提取的定义）（PhysicalObject）。  - `isSubSystemOf[array]`: 关系。对该物理对象是其一部分的系统的引用。  - `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `name[string]`: 这个项目的名称。  - `nominalFrequency[number]`: 属性。电源的额定频率。通常以周期/秒或赫兹（Hz）来衡量。  - `nominalSupplyVoltage[number]`: 属性。电源的额定电压。通常以伏特（V，W/A）为单位。  - `nominalSupplyVoltageMin[number]`: 属性。电源的最大和最小允许电压，例如，380V/440V的界限可适用于400V的额定电压。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 提供实体数据原始来源的一连串字符，作为一个URL。建议为源提供者的完全合格域名，或源对象的URL。  - `type[string]`: 属性。它必须等于`ElectricFlowStorageDevice`。  <!-- /30-PropertiesList -->  
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
ElectricFlowStorageDevice:    
  description: An electric flow storage device is a device in which electrical energy is stored and from which energy may be progressively released.    
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
      anyOf: &electricflowstoragedevice_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      anyOf: *electricflowstoragedevice_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *electricflowstoragedevice_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *electricflowstoragedevice_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    nominalFrequency:    
      description: Property. The nominal frequency of the supply. Usually measured in cycles/s or Hertz (Hz).    
      type: number    
      x-ngsi:    
        type: Property    
    nominalSupplyVoltage:    
      description: 'Property. The nominal voltage of the supply. Usually measured in Volts (V, W/A).'    
      type: number    
      x-ngsi:    
        type: Property    
    nominalSupplyVoltageMin:    
      description: Property. The maximum and minimum allowed voltage of the supply e.g. boundaries of 380V/440V may be applied for a nominal voltage of 400V.    
      type: number    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *electricflowstoragedevice_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    type:    
      description: Property. It must be equal to `ElectricFlowStorageDevice`.    
      enum:    
        - ElectricFlowStorageDevice    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:ElectricFlowStorageDevice"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/ElectricFlowStorageDevice/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/ElectricFlowStorageDevice/schema.json    
  x-model-tags: SAREF ElectricFlowStorageDevice    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### ElectricFlowStorageDevice NGSI-v2关键值示例  
这里是一个ElectricFlowStorageDevice的例子，以JSON-LD格式作为关键值。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ElectricFlowStorageDevice:60491652-ea6b-4e3c-8c4d-b0ae10defbda",  
  "type": "ElectricFlowStorageDevice",  
  "nominalFrequency": 0.6643858958243121,  
  "nominalSupplyVoltage": 0.9863230627218449,  
  "nominalSupplyVoltageMin": 0.5073272634060758,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:783aa5ff-fb6a-4fd8-863d-82a133f5d062",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:2602e1ee-c225-4703-9046-53bad81695f9",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:7aa13a80-05f1-4b1e-b973-4a4c88b729e8",  
    "urn:ngsi-ld:System:c34c6ce4-1336-4a37-a951-7710dd32550f",  
    "urn:ngsi-ld:System:dfeb61ff-fb62-4890-b453-918fe7a49b98"  
  ],  
  "hasManufacturer": "ElectricFlowStorageDevice Company Inc.",  
  "hasModel": "ElectricFlowStorageDevice 0.1.2",  
  "dateCreated": "2023-01-25T18:29:30Z",  
  "dateModified": "2023-01-25T14:18:54Z",  
  "source": "Import",  
  "name": "ElectricFlowStorageDevice",  
  "alternateName": "ElectricFlowStorageDevice type 2",  
  "description": "ElectricFlowStorageDevice of limited ElectricFlowStorageDevice types",  
  "dataProvider": "IFC file"  
}  
```  
</details>  
#### ElectricFlowStorageDevice NGSI-v2规范化实例  
这里有一个ElectricFlowStorageDevice的例子，是以JSON-LD格式规范化的。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ElectricFlowStorageDevice:4596f0a6-514a-4513-a666-3b9ade359305",  
  "type": "ElectricFlowStorageDevice",  
  "nominalFrequency": {  
    "type": "Measurement",  
    "value":  0.42581504045433194  
  },  
  "nominalSupplyVoltage": {  
    "type": "Measurement",  
    "value":  0.025200397292739596  
  },  
  "nominalSupplyVoltageMin": {  
    "type": "Measurement",  
    "value": 0.05204546916613961  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:BuildingSpace:235bfb6d-5039-45ea-95f9-094db1283634"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:PhysicalObject:9b54ca95-3f90-4be8-b32a-b585f8a9f867"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:0292e70d-da07-4d14-b8d8-c81c27c44683"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:6dce885f-2c53-414b-b0b2-9f2b88f0376d"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:a52f7099-5638-4b97-98c6-d24acc53edc6"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "ElectricFlowStorageDevice Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "ElectricFlowStorageDevice 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T09:43:01.2422472+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T15:38:19.0396796+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "ElectricFlowStorageDevice"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "ElectricFlowStorageDevice type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "ElectricFlowStorageDevice of limited ElectricFlowStorageDevice types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### ElectricFlowStorageDevice NGSI-LD关键值示例  
这里是一个ElectricFlowStorageDevice的例子，以JSON-LD格式作为key-values。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ElectricFlowStorageDevice:60491652-ea6b-4e3c-8c4d-b0ae10defbda",  
  "type": "ElectricFlowStorageDevice",  
  "nominalFrequency": 0.6643858958243121,  
  "nominalSupplyVoltage": 0.9863230627218449,  
  "nominalSupplyVoltageMin": 0.5073272634060758,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:783aa5ff-fb6a-4fd8-863d-82a133f5d062",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:2602e1ee-c225-4703-9046-53bad81695f9",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:7aa13a80-05f1-4b1e-b973-4a4c88b729e8",  
    "urn:ngsi-ld:System:c34c6ce4-1336-4a37-a951-7710dd32550f",  
    "urn:ngsi-ld:System:dfeb61ff-fb62-4890-b453-918fe7a49b98"  
  ],  
  "hasManufacturer": "ElectricFlowStorageDevice Company Inc.",  
  "hasModel": "ElectricFlowStorageDevice 0.1.2",  
  "dateCreated": "2023-01-25T18:29:30Z",  
  "dateModified": "2023-01-25T14:18:54Z",  
  "source": "Import",  
  "name": "ElectricFlowStorageDevice",  
  "alternateName": "ElectricFlowStorageDevice type 2",  
  "description": "ElectricFlowStorageDevice of limited ElectricFlowStorageDevice types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### ElectricFlowStorageDevice NGSI-LD规范化实例  
这里有一个ElectricFlowStorageDevice的例子，是以JSON-LD格式规范化的。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ElectricFlowStorageDevice:88efe032-f0b1-4d6b-9ff0-d3955cdcd6e7",  
  "type": "ElectricFlowStorageDevice",  
  "nominalFrequency": {  
    "type": "Property",  
    "unitCode": "Hz",  
    "observedAt": "2023-01-25T19:08:38Z",  
    "value": 0.6604645004424095  
  },  
  "nominalSupplyVoltage": {  
    "type": "Property",  
    "unitCode": "W/A",  
    "observedAt": "2023-01-26T06:40:20Z",  
    "value": 0.7889839353290103  
  },  
  "nominalSupplyVoltageMin": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T13:04:38Z",  
    "value": 0.5759276076424262  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:8d1a4801-d77d-48ce-8fdb-6b0e6bf737f2"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:42136020-035a-4946-8a49-99cbfde581e2"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:d553b00a-f3fe-4293-922d-8b665ed69e0d"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:7d32b669-8e92-4b94-9807-effabcb49391"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:242276cc-61da-4555-8b5f-769fd606ae0f"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "ElectricFlowStorageDevice Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "ElectricFlowStorageDevice 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T04:39:29Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-25T22:59:03Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "ElectricFlowStorageDevice"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "ElectricFlowStorageDevice type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "ElectricFlowStorageDevice of limited ElectricFlowStorageDevice types"  
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
