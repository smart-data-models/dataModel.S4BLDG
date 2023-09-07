<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：冷却器  
======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Chiller/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述：**冷水机是一种通过蒸汽压缩或吸收式制冷循环从液体中带走热量的设备，用于冷却流体，通常是水或水与乙二醇的混合物。冷冻流体随后用于冷却建筑物内的空气和除湿。  
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
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `hasManufacturer[string]`: 标识实体（如设备）制造商的关系。该值应为字符串或带有语言标记的字符串。  - `hasModel[string]`: 标识实体（如设备）模型的关系。该值应是字符串或带有语言标记的字符串  - `id[*]`: 实体的唯一标识符  - `isContainedInBuildingSpace[*]`: 用于定义楼宇物理空间的实体。建筑空间包含设备或建筑对象。(建筑空间）  - `isContainedInPhysicalObject[*]`: 任何具有适当空间区域的物体。  (从 DUL 本体中提取的定义）（物理对象）  - `isSubSystemOf[array]`: 该物理对象所属系统的引用  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `nominalCapacity[number]`: 标称容量。通常以瓦特（W，J/s）为计量单位  - `nominalCondensingTemperature[number]`: 冷水机冷凝温度。通常以开氏度（K）为单位测量  - `nominalEfficiency[number]`: 名义条件下的名义冷水机效率。  - `nominalEvaporatingTemmperature[number]`: 冷却器蒸发温度，通常以开尔文 (K) 度为单位。  - `nominalHeatRejectionRate[number]`: 制冷效果与压缩机输入功率的热当量之和。通常以瓦特（W，J/s）为计量单位  - `nominalPowerConsumption[number]`: 标称总功耗。通常以瓦特（W，J/s）为计量单位  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `type[string]`: 必须等于 "Chiller  <!-- /30-PropertiesList -->  
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
Chiller:    
  description: 'A chiller is a device used to remove heat from a liquid via a vapor-compression or absorption refrigeration cycle to cool a fluid, typically water or a mixture of water and glycol. The chilled fluid is then used to cool and dehumidify air in a building.'    
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
    nominalCapacity:    
      description: 'Nominal capacity. Usually measured in Watts (W, J/s)'    
      type: number    
      x-ngsi:    
        type: Property    
    nominalCondensingTemperature:    
      description: Chiller condensing temperature. Usually measured in degrees Kelvin (K)    
      type: number    
      x-ngsi:    
        type: Property    
    nominalEfficiency:    
      description: 'Nominal chiller efficiency under nominal conditions. '    
      type: number    
      x-ngsi:    
        type: Property    
    nominalEvaporatingTemmperature:    
      description: Chiller evaporating temperature.Usually measured in degrees Kelvin (K)    
      type: number    
      x-ngsi:    
        type: Property    
    nominalHeatRejectionRate:    
      description: 'Sum of the refrigeration effect and the heat equivalent of the power input to the compressor. Usually measured in Watts (W, J/s)'    
      type: number    
      x-ngsi:    
        type: Property    
    nominalPowerConsumption:    
      description: 'Nominal total power consumption. Usually measured in Watts (W, J/s)'    
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
      description: It must be equal to `Chiller`    
      enum:    
        - Chiller    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Chiller"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Chiller/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Chiller/schema.json    
  x-model-tags: SAREF Chiller    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 有效载荷示例  
#### 冷风机 NGSI-v2 键值示例  
下面是一个以 JSON-LD 格式作为键值的 Chiller 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Chiller:ba7497f8-4fd6-4ec0-8dd8-00ed95bd51fc",  
  "type": "Chiller",  
  "nominalCapacity": 0.09475720530736764,  
  "nominalCondensingTemperature": 0.20516492572831713,  
  "nominalEfficiency": 0.9467840743079621,  
  "nominalEvaporatingTemmperature": 0.9391249200926837,  
  "nominalHeatRejectionRate": 0.6781215261931568,  
  "nominalPowerConsumption": 0.7316060776442138,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:53b1b818-f2bf-4bbf-9ba6-e3d431a11173",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:5d06c867-dc48-4267-b194-60642a22f0af",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:8c79471f-dea7-474b-985e-e5072ea36369",  
    "urn:ngsi-ld:System:e2e46075-3c25-46c4-80b4-da4b79faef4e",  
    "urn:ngsi-ld:System:9eea4295-8a6c-4efb-833e-1d6941c97754"  
  ],  
  "hasManufacturer": "Chiller Company Inc.",  
  "hasModel": "Chiller 0.1.2",  
  "dateCreated": "2023-01-25T19:42:28Z",  
  "dateModified": "2023-01-25T19:48:46Z",  
  "source": "Import",  
  "name": "Chiller",  
  "alternateName": "Chiller type 2",  
  "description": "Chiller of limited Chiller types",  
  "dataProvider": "IFC file"  
}  
```  
</details>  
#### 冷风机 NGSI-v2 标准化示例  
下面是一个规范化 JSON-LD 格式的 Chiller 示例。在不使用选项的情况下，该格式与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Chiller:fbbc813e-29ac-4462-9996-5a3d73d1ce98",  
  "type": "Chiller",  
  "nominalCapacity": {  
    "type": "Measurement",  
    "value": 0.0740819212946876  
  },  
  "nominalCondensingTemperature": {  
    "type": "Measurement",  
    "value": 0.5010709006481944  
  },  
  "nominalEfficiency": {  
    "type": "Measurement",  
    "value": 0.05897827362979524  
  },  
  "nominalEvaporatingTemmperature": {  
    "type": "Measurement",  
    "value": 0.0556993113916634  
  },  
  "nominalHeatRejectionRate": {  
    "type": "Measurement",  
    "value": 0.756236294011522  
  },  
  "nominalPowerConsumption": {  
    "type": "Measurement",  
    "value": 0.8474333854169832  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:BuildingSpace:0a2b8ec3-70d9-483f-8df0-dc7bbfa27d29"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:PhysicalObject:18da6c4b-5520-4b19-b3ee-2a91993c19de"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:b48e7b0c-7d5e-4087-89d4-c40a87ae78be"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:d9a20a72-def1-447e-ba8a-f601965fc681"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:474efe4e-7d74-4985-ac14-792dcb6b9d76"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Chiller Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Chiller 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T05:24:59.314133+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T04:27:01.3524196+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Chiller"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Chiller type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Chiller of limited Chiller types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### 冷风机 NGSI-LD 键值示例  
下面是一个以 JSON-LD 格式作为键值的 Chiller 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Chiller:ba7497f8-4fd6-4ec0-8dd8-00ed95bd51fc",  
  "type": "Chiller",  
  "nominalCapacity": 0.09475720530736764,  
  "nominalCondensingTemperature": 0.20516492572831713,  
  "nominalEfficiency": 0.9467840743079621,  
  "nominalEvaporatingTemmperature": 0.9391249200926837,  
  "nominalHeatRejectionRate": 0.6781215261931568,  
  "nominalPowerConsumption": 0.7316060776442138,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:53b1b818-f2bf-4bbf-9ba6-e3d431a11173",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:5d06c867-dc48-4267-b194-60642a22f0af",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:8c79471f-dea7-474b-985e-e5072ea36369",  
    "urn:ngsi-ld:System:e2e46075-3c25-46c4-80b4-da4b79faef4e",  
    "urn:ngsi-ld:System:9eea4295-8a6c-4efb-833e-1d6941c97754"  
  ],  
  "hasManufacturer": "Chiller Company Inc.",  
  "hasModel": "Chiller 0.1.2",  
  "dateCreated": "2023-01-25T19:42:28Z",  
  "dateModified": "2023-01-25T19:48:46Z",  
  "source": "Import",  
  "name": "Chiller",  
  "alternateName": "Chiller type 2",  
  "description": "Chiller of limited Chiller types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### 冷风机 NGSI-LD 归一化示例  
下面是一个规范化 JSON-LD 格式的冷冻机示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Chiller:1a99f350-0e1d-4466-8579-912c1f3c9b8f",  
  "type": "Chiller",  
  "nominalCapacity": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-26T09:47:03Z",  
    "value": 0.22554187711659102  
  },  
  "nominalCondensingTemperature": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T14:43:34Z",  
    "value": 0.1507511254687508  
  },  
  "nominalEfficiency": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T03:46:03Z",  
    "value": 0.3248755291390478  
  },  
  "nominalEvaporatingTemmperature": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T02:17:21Z",  
    "value": 0.13438649176620343  
  },  
  "nominalHeatRejectionRate": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-26T06:04:17Z",  
    "value": 0.0564283340666325  
  },  
  "nominalPowerConsumption": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-26T10:26:02Z",  
    "value": 0.8546772522263915  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:d78af157-a55d-46b9-8c56-d6c0eda32745"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:4748763d-3b35-487c-a6ad-3a9dfa510820"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:29fc2747-3753-44b5-8d88-3ae91cd4bc89"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:7a9aa253-a2eb-42ce-aeee-6130d158d18f"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:72503e97-5805-42a7-a24b-891925d2a999"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Chiller Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Chiller 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T10:57:45Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T04:43:33Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Chiller"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Chiller type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Chiller of limited Chiller types"  
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
