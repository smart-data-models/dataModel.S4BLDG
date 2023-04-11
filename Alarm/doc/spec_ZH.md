<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：警报  
=====<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Alarm/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述：**报警器是一种装置，它向超出正常预期范围的条件或情况的存在发出信号，或激活这种装置。  警报器包括提供用于启动警报器的碎玻璃按钮和手动拉杆箱。**。  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `hasManufacturer[string]`: 属性。识别实体（例如，设备）的制造商的关系。该值应是一个字符串或一个带有语言标签的字符串。  - `hasModel[string]`: 属性。识别实体（例如，设备）的模型的关系。该值应是一个字符串或一个带有语言标签的字符串。  - `id[*]`: 实体的唯一标识符  - `isContainedInBuildingSpace[*]`: 关系。一个用于定义建筑物理空间的实体。一个建筑空间包含设备或建筑对象。(建筑空间)  - `isContainedInPhysicalObject[*]`: 关系。任何具有适当空间区域的物体。  (从DUL本体论中提取的定义）（PhysicalObject）。  - `isSubSystemOf[array]`: 关系。对该物理对象是其一部分的系统的引用。  - `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `name[string]`: 这个项目的名称。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `type[string]`: 属性。它必须等于报警。  <!-- /30-PropertiesList -->  
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
Alarm:    
  description: An alarm is a device that signals the existence of a condition or situation that is outside the boundaries of normal expectation or that activates such a device.  Alarms include the provision of break glass buttons and manual pull boxes that are used to activate alarms.    
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
      anyOf: &alarm_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      anyOf: *alarm_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *alarm_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *alarm_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
        anyOf: *alarm_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      description: Property. It must be equal to Alarm.    
      enum:    
        - Alarm    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Alarm"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Alarm/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Alarm/schema.json    
  x-model-tags: SAREF Alarm SMART DATA MODELS    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### 警报NGSI-v2关键值示例  
这里有一个以JSON-LD格式作为key-values的Alarm的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Alarm:403ddbdf-79c0-4923-9d07-4c962837c527",  
  "type": "Alarm",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:5920683a-3228-480c-82f6-17c1cf239df4",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:58a84941-5697-4bdd-a39b-0f509d89659f",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:d2fa7d6b-adfe-4b27-a231-c5c5edb297ad",  
    "urn:ngsi-ld:System:97320977-f3bd-47f8-8945-c15e1fc0c50f",  
    "urn:ngsi-ld:System:d05a0603-3ea4-4ed8-9a3d-edac79bae877"  
  ],  
  "hasManufacturer": "Alarm Company Inc.",  
  "hasModel": "Alarm 0.1.2",  
  "dateCreated": "2023-01-26T04:02:51Z",  
  "dateModified": "2023-01-26T07:49:05Z",  
  "source": "Import",  
  "name": "Alarm",  
  "alternateName": "Alarm type 2",  
  "description": "Alarm of limited Alarm types",  
  "dataProvider": "IFC file"  
}  
```  
</details>  
#### 警报NGSI-v2规范化示例  
下面是一个规范化的JSON-LD格式的报警器的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Alarm:8ae04687-4a9f-4cc8-acfa-2bc726781aaa",  
  "type": "Alarm",  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:BuildingSpace:db2e26a9-5f4a-4b2c-9510-e7f9e2239efa"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:PhysicalObject:1c447365-0f4e-4350-bfc7-a2974d8297dd"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:System:38982b54-aaed-4916-ad8f-fcfeccb8fe6d"  
      },  
      {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:System:d7ead903-19a3-4f08-90a8-52979e99bc2b"  
      },  
      {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:System:5baec201-65ae-41f9-b557-37bd69cd14bb"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Alarm Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Alarm 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T14:33:52.1440188+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T10:12:39.8292183+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Alarm"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Alarm type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Alarm of limited Alarm types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### 警报NGSI-LD关键值示例  
这里有一个以JSON-LD格式作为key-values的Alarm的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Alarm:5c49d555-274b-4ccd-b527-823329defc35",  
  "type": "Alarm",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:98c9f61a-d8f8-4326-b4f3-8845c97ad825",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:2651a0f9-1d1b-4204-bcfc-a55f2d51f3bd",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:8162840d-293b-4e69-a911-479d6040b540",  
    "urn:ngsi-ld:System:573efc0a-de49-43da-bed2-123de1138501",  
    "urn:ngsi-ld:System:565a39a6-eea4-4b32-8dcc-f10941da849a"  
  ],  
  "hasManufacturer": "Alarm Company Inc.",  
  "hasModel": "Alarm 0.1.2",  
  "dateCreated": "2023-01-25T17:55:12Z",  
  "dateModified": "2023-01-25T23:48:06Z",  
  "source": "Import",  
  "name": "Alarm",  
  "alternateName": "Alarm type 2",  
  "description": "Alarm of limited Alarm types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### 警报NGSI-LD正常化的例子  
下面是一个规范化的JSON-LD格式的报警器的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Alarm:3200afb8-5a97-4a51-b454-a7bb5e7dd272",  
  "type": "Alarm",  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:ef503257-cb0f-456e-88eb-90fee65efbd1"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:c6d91273-5403-4ffb-835d-5bc5f7778667"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:9cc30a80-baee-46bf-b844-9e5bfd93373f"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:c4d6a860-5659-4a7c-a2fe-6e910f200b84"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:4c12a0b6-c61d-40ec-9545-50e88d01592e"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Alarm Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Alarm 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T20:04:31Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T04:48:57Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Alarm"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Alarm type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Alarm of limited Alarm types"  
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
