<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：遮光设备  
=======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/ShadingDevice/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述：**遮阳设备是专门用于遮挡阳光、自然光或遮挡视线的设备。遮阳设备可以是外墙的一部分，也可以安装在建筑物内部，可以是固定的，也可以是可操作的。  
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
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `hasManufacturer[string]`: 标识实体（如设备）制造商的关系。该值应为字符串或带有语言标记的字符串。  - `hasModel[string]`: 标识实体（如设备）模型的关系。该值应是字符串或带有语言标记的字符串  - `id[*]`: 实体的唯一标识符  - `isContainedInBuildingSpace[*]`: 用于定义楼宇物理空间的实体。建筑空间包含设备或建筑对象。(建筑空间）  - `isContainedInPhysicalObject[*]`: 任何具有适当空间区域的物体。  (从 DUL 本体中提取的定义）（物理对象）  - `isExternal[boolean]`: 表示该构件是设计用于室外（"真"）还是不用于室外（"假"）。如果 (TRUE)，则为外部元件，面向建筑物外部  - `isSubSystemOf[array]`: 该物理对象所属系统的引用  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `mechanicalOperated[boolean]`: 表示该元件是否为机械操作（"真"），即手动操作（"假"）。  - `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `roughness[string]`: 表面垂直偏差的测量值  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `shadingDeviceType[string]`: 指定遮阳设备的类型  - `solarReflectance[number]`: (Rsol）：入射太阳辐射被遮阳系统反射的比率（也称为 _e）。请注意以下公式 Asol + Rsol + Tsol = 1  - `solarTransmittance[number]`: (Tsol) 直接穿过遮阳系统的入射太阳辐射的比率（也称为 _e）。请注意以下公式 Asol + Rsol + Tsol = 1  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `thermalTransmittance[number]`: 能量通过人体的传输速率。通常以瓦特/平方米开尔文为单位。  - `type[string]`: 必须等于 `ShadingDevice`.  - `visibleLightReflectance[number]`: 玻璃在正常入射时反射的可见光的比例。该值不带单位  - `visibleLightTransmittance[number]`: 正常入射时通过遮光系统的可见光的分数。该值不带单位  <!-- /30-PropertiesList -->  
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
ShadingDevice:    
  description: 'Shading devices are purpose built devices to protect from the sunlight, from natural light, or screening them from view. Shading devices can form part of the facade or can be mounted inside the building, they can be fixed or operable.'    
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
    isExternal:    
      description: Indication whether the element is designed for use in the exterior (TRUE) or not (FALSE). If (TRUE) it is an external element and faces the outside of the building    
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
    mechanicalOperated:    
      description: 'Indication whether the element is operated machanically (TRUE) or not, i.e. manually (FALSE)'    
      type: boolean    
      x-ngsi:    
        type: Property    
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
    roughness:    
      description: A measure of the vertical deviations of the surface    
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
    shadingDeviceType:    
      description: Specifies the type of shading device    
      type: string    
      x-ngsi:    
        type: Property    
    solarReflectance:    
      description: '(Rsol): The ratio of incident solar radiation that is reflected by a shading system (also named _e). Note the following equation Asol + Rsol + Tsol = 1'    
      type: number    
      x-ngsi:    
        type: Property    
    solarTransmittance:    
      description: (Tsol) The ratio of incident solar radiation that directly passes through a shading system (also named _e). Note the following equation Asol + Rsol + Tsol = 1    
      type: number    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    thermalTransmittance:    
      description: Rate at which energy is transmitted through a body. Usually measured in Watts/m2 Kelvin    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: It must be equal to `ShadingDevice`    
      enum:    
        - ShadingDevice    
      type: string    
      x-ngsi:    
        type: Property    
    visibleLightReflectance:    
      description: Fraction of the visible light that is reflected by the glazing at normal incidence. It is a value without unit    
      type: number    
      x-ngsi:    
        type: Property    
    visibleLightTransmittance:    
      description: Fraction of the visible light that passes the shading system at normal incidence. It is a value without unit    
      type: number    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:ShadingDevice"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/ShadingDevice/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/ShadingDevice/schema.json    
  x-model-tags: SAREF ShadingDevice    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 有效载荷示例  
#### ShadingDevice NGSI-v2 键值示例  
下面是一个以 JSON-LD 格式作为键值的 ShadingDevice 示例。当使用 "options=keyValues "时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:ShadingDevice:03281d48-cb47-4061-9208-b2a380b3d7cd",  
    "type": "ShadingDevice",  
    "isExternal": false,  
    "mechanicalOperated": true,  
    "roughness": "Executive",  
    "shadingDeviceType": "client-driven",  
    "solarReflectance": 0.7901767410172098,  
    "solarTransmittance": 0.5537106205704284,  
    "thermalTransmittance": 0.9786915841160174,  
    "visibleLightReflectance": 0.7194478774053882,  
    "visibleLightTransmittance": 0.8973320246848571,  
    "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:3f4442cb-0f79-4dad-81ba-69879612f561",  
    "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:de04c9b6-2d78-491f-987a-085ea71f747b",  
    "isSubSystemOf": [  
        "urn:ngsi-ld:System:fd063381-99e7-4b7d-8936-cd66932ba1e7",  
        "urn:ngsi-ld:System:5bfac8cc-a08e-4bc8-a9e8-474e8db84d73",  
        "urn:ngsi-ld:System:a4eef133-5e5d-4051-8b37-bf89e468f019"  
    ],  
    "hasManufacturer": "ShadingDevice Company Inc.",  
    "hasModel": "ShadingDevice 0.1.2",  
    "dateCreated": "2023-01-26T07:18:28Z",  
    "dateModified": "2023-01-26T08:58:08Z",  
    "source": "Import",  
    "name": "ShadingDevice",  
    "alternateName": "ShadingDevice type 2",  
    "description": "ShadingDevice of limited ShadingDevice types",  
    "dataProvider": "IFC file"  
}  
```  
</details>  
#### ShadingDevice NGSI-v2 标准化示例  
下面是一个规范化 JSON-LD 格式的 ShadingDevice 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ShadingDevice:b3c3bd8f-6f5a-400a-b43c-99c32bf7d036",  
  "type": "ShadingDevice",  
  "isExternal": {  
    "type": "Boolean",  
    "value": true  
  },  
  "mechanicalOperated": {  
    "type": "Boolean",  
    "value": false  
  },  
  "roughness": {  
    "type": "Text",  
    "value": "Home Loan Account"  
  },  
  "shadingDeviceType": {  
    "type": "Text",  
    "value": "program"  
  },  
  "solarReflectance": {  
    "type": "Measurement",  
    "value": 0.23462582512353236  
  },  
  "solarTransmittance": {  
    "type": "Measurement",  
    "value": 0.569468324137257  
  },  
  "thermalTransmittance": {  
    "type": "Measurement",  
    "value": 0.315308180363743  
  },  
  "visibleLightReflectance": {  
    "type": "Measurement",  
    "value": 0.6167477347282538  
  },  
  "visibleLightTransmittance": {  
    "type": "Measurement",  
    "value": 0.27849116636487137  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:BuildingSpace:6d6d4b35-2d0f-4590-bd7d-1e5cdc1d71fe"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:PhysicalObject:ff501e6f-1fbf-4dd4-9537-b3b6668f156b"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:6d7f1004-c306-4d6b-8b95-d661e62087df"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:9eedb406-9b0a-466e-99bf-d8b4721af694"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:c485e374-da84-4bff-8a79-7d35bdcd0dab"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "ShadingDevice Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "ShadingDevice 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T15:18:47.9518072+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T11:03:03.3618393+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "ShadingDevice"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "ShadingDevice type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "ShadingDevice of limited ShadingDevice types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### ShadingDevice NGSI-LD 键值示例  
下面是一个以 JSON-LD 格式作为键值的 ShadingDevice 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ShadingDevice:03281d48-cb47-4061-9208-b2a380b3d7cd",  
  "type": "ShadingDevice",  
  "isExternal": false,  
  "mechanicalOperated": true,  
  "roughness": "Executive",  
  "shadingDeviceType": "client-driven",  
  "solarReflectance": 0.7901767410172098,  
  "solarTransmittance": 0.5537106205704284,  
  "thermalTransmittance": 0.9786915841160174,  
  "visibleLightReflectance": 0.7194478774053882,  
  "visibleLightTransmittance": 0.8973320246848571,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:3f4442cb-0f79-4dad-81ba-69879612f561",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:de04c9b6-2d78-491f-987a-085ea71f747b",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:fd063381-99e7-4b7d-8936-cd66932ba1e7",  
    "urn:ngsi-ld:System:5bfac8cc-a08e-4bc8-a9e8-474e8db84d73",  
    "urn:ngsi-ld:System:a4eef133-5e5d-4051-8b37-bf89e468f019"  
  ],  
  "hasManufacturer": "ShadingDevice Company Inc.",  
  "hasModel": "ShadingDevice 0.1.2",  
  "dateCreated": "2023-01-26T07:18:28Z",  
  "dateModified": "2023-01-26T08:58:08Z",  
  "source": "Import",  
  "name": "ShadingDevice",  
  "alternateName": "ShadingDevice type 2",  
  "description": "ShadingDevice of limited ShadingDevice types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### ShadingDevice NGSI-LD 归一化示例  
下面是一个规范化 JSON-LD 格式的 ShadingDevice 示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ShadingDevice:98dd5d05-db70-4ebb-a39c-e286063cb137",  
  "type": "ShadingDevice",  
  "isExternal": {  
    "type": "Property",  
    "value": true  
  },  
  "mechanicalOperated": {  
    "type": "Property",  
    "value": true  
  },  
  "roughness": {  
    "type": "Property",  
    "value": "Practical Rubber Cheese"  
  },  
  "shadingDeviceType": {  
    "type": "Property",  
    "value": "parsing"  
  },  
  "solarReflectance": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T03:37:18Z",  
    "value": 0.378910710384914  
  },  
  "solarTransmittance": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T09:24:57Z",  
    "value": 0.9404860966072789  
  },  
  "thermalTransmittance": {  
    "type": "Property",  
    "unitCode": "Kelvin",  
    "observedAt": "2023-01-26T12:37:04Z",  
    "value": 0.471443015298326  
  },  
  "visibleLightReflectance": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T06:09:46Z",  
    "value": 0.7789148596577641  
  },  
  "visibleLightTransmittance": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T05:43:18Z",  
    "value": 0.9110422065316075  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:0bfda01f-c7bd-4db3-9a81-cfeb051cf629"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:53171831-ae73-45fa-8f15-b1c034e5b2af"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:b9d614e5-32c2-47cd-b5ba-23b2c8ed67ea"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:6048cde5-df44-4963-b770-29ace8711405"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:e2c351bf-c825-4bc9-a7ca-dc96552b8e38"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "ShadingDevice Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "ShadingDevice 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T15:37:39Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-25T17:44:25Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "ShadingDevice"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "ShadingDevice type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "ShadingDevice of limited ShadingDevice types"  
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
