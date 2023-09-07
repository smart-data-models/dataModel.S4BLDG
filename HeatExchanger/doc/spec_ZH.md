<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：热交换器  
=======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/HeatExchanger/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球说明：**热交换器是一种用于在非混合介质（如板式和管壳式热交换器）之间进行热传递的设备。热交换器（HeatExchanger）通常用于水侧分配系统，以从液体向另一种液体（通常为水基）回收能量，而空气热回收（AirToAirHeatRecovery）通常用于气侧分配系统，以从气体向气体（通常为空气）回收能量。  
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
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `arrangement[string]`: 定义热交换器的基本流量安排：逆流：逆流换热器布置。CROSSFLOW（横流）：横流换热器布置。PARALLELFLOW（平行流）：平行流换热器布置。MULTIPASS：多路流换热器布置。OTHER：上述未定义的其他类型的热交换器流动布置。  - `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `hasManufacturer[string]`: 标识实体（如设备）制造商的关系。该值应为字符串或带有语言标记的字符串。  - `hasModel[string]`: 标识实体（如设备）模型的关系。该值应是字符串或带有语言标记的字符串  - `id[*]`: 实体的唯一标识符  - `isContainedInBuildingSpace[*]`: 用于定义楼宇物理空间的实体。建筑空间包含设备或建筑对象。(建筑空间）  - `isContainedInPhysicalObject[*]`: 任何具有适当空间区域的物体。  (从 DUL 本体中提取的定义）（物理对象）  - `isSubSystemOf[array]`: 该物理对象所属系统的引用  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `type[string]`: 必须等于 "HeatExchanger  <!-- /30-PropertiesList -->  
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
HeatExchanger:    
  description: 'A heat exchanger is a device used to provide heat transfer between non-mixing media such as plate and shell and tube heat exchangers. HeatExchanger is commonly used on water-side distribution systems to recover energy from a liquid to another liquid (typically water-based), whereas AirToAirHeatRecovery is commonly used on air-side distribution systems to recover energy from a gas to a gas (usually air).'    
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
    arrangement:    
      description: 'Defines the basic flow arrangements for the heat exchanger: COUNTERFLOW: Counterflow heat exchanger arrangement. CROSSFLOW: Crossflow heat exchanger arrangement. PARALLELFLOW: Parallel flow heat exchanger arrangement. MULTIPASS: Multipass flow heat exchanger arrangement. OTHER: Other type of heat exchanger flow arrangement not defined above'    
      type: string    
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
      description: It must be equal to `HeatExchanger`    
      enum:    
        - HeatExchanger    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:HeatExchanger"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/HeatExchanger/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/HeatExchanger/schema.json    
  x-model-tags: SAREF HeatExchanger    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 有效载荷示例  
#### 热交换器 NGSI-v2 关键值示例  
下面是一个以 JSON-LD 格式作为键值的 HeatExchanger 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:HeatExchanger:b0f22640-66d7-4a7f-ab63-62b499e7e849",  
  "type": "HeatExchanger",  
  "arrangement": "calculating",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:04ee5ba4-9f7e-43fa-8c45-b756d6bd1b45",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:ca0a85a8-93e8-4cf1-a28b-03eb796f53a3",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:f746caae-43c4-48eb-b7d9-ab95bd858565",  
    "urn:ngsi-ld:System:bf897dfe-ac97-4e1d-8023-bae2465118b9",  
    "urn:ngsi-ld:System:9f9aec4e-7365-49ce-835b-5422973ae19a"  
  ],  
  "hasManufacturer": "HeatExchanger Company Inc.",  
  "hasModel": "HeatExchanger 0.1.2",  
  "dateCreated": "2023-01-26T11:52:54Z",  
  "dateModified": "2023-01-26T05:48:15Z",  
  "source": "Import",  
  "name": "HeatExchanger",  
  "alternateName": "HeatExchanger type 2",  
  "description": "HeatExchanger of limited HeatExchanger types",  
  "dataProvider": "IFC file"  
}  
```  
</details>  
#### 热交换器 NGSI-v2 标准化示例  
下面是一个规范化 JSON-LD 格式的热交换器示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:HeatExchanger:2fcd41c1-136e-4cff-b439-7c44260bcf66",  
  "type": "HeatExchanger",  
  "arrangement": {  
    "type": "Text",  
    "value": "Assistant"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:BuildingSpace:9ef5478c-5f5f-4d2c-81b3-5cb9317ee70f"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:PhysicalObject:d8a9c2c6-a3e9-414d-a8ac-a69f959d7b70"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:cce1367c-262f-41d6-88ca-6d3032cfb193"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:90db3c34-a2b8-4511-89cb-353fd855fce4"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:3bbddac3-223b-449d-884e-1cc4d04eeb79"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "HeatExchanger Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "HeatExchanger 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T07:35:03.9392521+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T21:26:27.4267913+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "HeatExchanger"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "HeatExchanger type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "HeatExchanger of limited HeatExchanger types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### 热交换器 NGSI-LD 关键值 示例  
下面是一个以 JSON-LD 格式作为键值的 HeatExchanger 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:HeatExchanger:8eb41206-4a42-4c26-a9ec-6c124d99d9e8",  
  "type": "HeatExchanger",  
  "arrangement": "bus",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:3d853493-b844-4211-b74c-e68b3eb511d3",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:e8054111-5920-4e1d-8832-c33a629673b2",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:46ac40f7-045b-4524-8592-aead52715c98",  
    "urn:ngsi-ld:System:7ec365c9-eef7-43ed-9511-d3aefe39afc4",  
    "urn:ngsi-ld:System:2f3a1c27-a079-4a8d-90f2-ee75c56a1c3e"  
  ],  
  "hasManufacturer": "HeatExchanger Company Inc.",  
  "hasModel": "HeatExchanger 0.1.2",  
  "dateCreated": "2023-01-26T12:05:41Z",  
  "dateModified": "2023-01-25T22:11:27Z",  
  "source": "Import",  
  "name": "HeatExchanger",  
  "alternateName": "HeatExchanger type 2",  
  "description": "HeatExchanger of limited HeatExchanger types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### 热交换器 NGSI-LD 归一化示例  
下面是一个以 JSON-LD 格式规范化的热交换器示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:HeatExchanger:c46c932b-140d-4d0e-8e6c-23a71b24e0f1",  
  "type": "HeatExchanger",  
  "arrangement": {  
    "type": "Property",  
    "value": "Integration"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:c1be2cb8-f889-4ecb-a784-f69890a58887"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:0bd7f4d1-bfea-46a1-96ff-ef8ca5c3a860"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:de5626c3-0724-4126-9891-1a66ac44b329"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:024690f4-219f-4098-a217-bc1c554a7eb7"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:2a908d89-b5f0-4a0f-8b55-eb8433107ca0"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "HeatExchanger Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "HeatExchanger 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T19:13:00Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-25T22:12:50Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "HeatExchanger"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "HeatExchanger type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "HeatExchanger of limited HeatExchanger types"  
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
