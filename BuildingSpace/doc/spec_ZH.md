<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：建筑空间  
=======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/BuildingSpace/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**用于定义建筑物理空间的实体。建筑空间包含设备或建筑对象。  
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
- `airVolume[number]`: 该建筑空间的空气体积。测量单位：立方米  - `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `bounds[object]`: 该建筑空间的边界在 3D 中表示为一个方框  	- `max[object]`: 代表三维空间中的一个点    
	- `min[object]`: 代表三维空间中的一个点    
- `buildingSpaceKind[string]`: 建筑空间的详细类型  - `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `id[*]`: 实体的唯一标识符  - `isSpaceOfBuilding[*]`: 建筑是指为居住者或其物品提供住所并矗立在一处的结构。建筑物也是建筑项目各组成部分空间结构层次中的一个基本要素（与场地、层数和空间一起）。建筑  - `isSpaceOfBuildingSpace[*]`: 用于定义楼宇物理空间的实体。建筑空间包含设备或建筑对象。(建筑空间）  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `type[string]`: 必须等于 `BuildingSpace  <!-- /30-PropertiesList -->  
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
BuildingSpace:    
  description: An entity used to define the physical spaces of the building. A building space contains devices or building objects.    
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
    airVolume:    
      description: Air Volume of this building space. Measured in m3    
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
    bounds:    
      description: Bounds of this building space represented as a box in 3D    
      properties:    
        max:    
          description: Represents a point in a 3D space    
          properties:    
            type:    
              description: NGSI-LD Entity Type    
              enum:    
                - Point    
              type: string    
              x-ngsi:    
                type: Property    
            x:    
              description: Coordinate X of the point    
              type: number    
              x-ngsi:    
                type: Property    
            y:    
              description: Coordinate Y of the point    
              type: number    
              x-ngsi:    
                type: Property    
            z:    
              description: Coordinate Z of the point    
              type: number    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        min:    
          description: Represents a point in a 3D space    
          properties:    
            type:    
              description: NGSI-LD Entity Type    
              enum:    
                - Point    
              type: string    
              x-ngsi:    
                type: Property    
            x:    
              description: Coordinate X of the point    
              type: number    
              x-ngsi:    
                type: Property    
            y:    
              description: Coordinate Y of the point    
              type: number    
              x-ngsi:    
                type: Property    
            z:    
              description: Coordinate Z of the point    
              type: number    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        type:    
          description: NGSI-LD Entity Type    
          enum:    
            - Bounds    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    buildingSpaceKind:    
      description: Detailed type of the Building Space    
      enum:    
        - BuildingElementProxy    
        - BuildingStorey    
        - Column    
        - Covering    
        - CurtainWall    
        - Door    
        - OpeningElement    
        - Plate    
        - Railing    
        - Roof    
        - Site    
        - Slab    
        - Space    
        - Stair    
        - StairFlight    
        - Storey    
        - Wall    
        - WallStandardCase    
        - Window    
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
    isSpaceOfBuilding:    
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
      description: 'A building represents a structure that provides shelter for its occupants or contents and stands in one place. The building is also used to provide a basic element within the spatial structure hierarchy for the components of a building project (together with site, storey, and space). (Building)'    
      x-ngsi:    
        type: Property    
    isSpaceOfBuildingSpace:    
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
      description: It must be equal to `BuildingSpace`    
      enum:    
        - BuildingSpace    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:BuildingSpace"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/BuildingSpace/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/BuildingSpace/schema.json    
  x-model-tags: SAREF BuildingSpace    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 有效载荷示例  
#### BuildingSpace NGSI-v2 键值示例  
下面是一个以 JSON-LD 格式作为键值的 BuildingSpace 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:BuildingSpace:cc956fa0-70f8-4110-a4d1-60eb1299bc8e",  
  "type": "BuildingSpace",  
  "airVolume": 0.9964475180399912,  
  "bounds": {  
    "max": {  
      "type": "Point",  
      "x": 0.6598941847785847,  
      "y": 0.29050046329217627,  
      "z": 0.5723987903652894  
    },  
    "min": {  
      "type": "Point",  
      "x": 0.2328925559580186,  
      "y": 0.7820178782873053,  
      "z": 0.703947078383337  
    }  
  },  
  "buildingSpaceKind": "Space",  
  "isSpaceOfBuilding": "urn:ngsi-ld:Building:5ba9925b-36c8-4243-bc1c-5095eefbc2c9",  
  "isSpaceOfBuildingSpace": "urn:ngsi-ld:BuildingSpace:bb5c5eb8-7224-4560-a8f3-0dd75742066d",  
  "dateCreated": "2023-01-26T10:56:49Z",  
  "dateModified": "2023-01-25T18:35:39Z",  
  "source": "Import",  
  "name": "BuildingSpace",  
  "alternateName": "BuildingSpace type 2",  
  "description": "BuildingSpace of limited BuildingSpace types",  
  "dataProvider": "IFC file"  
}  
```  
</details>  
#### BuildingSpace NGSI-v2 标准化示例  
下面是一个规范化 JSON-LD 格式的建筑空间示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:BuildingSpace:f341006e-3556-4699-8959-19edf7079bac",  
  "type": "BuildingSpace",  
  "airVolume": {  
    "type": "Measurement",  
    "value": 0.9064782098814886  
  },  
  "bounds": {  
    "type": "Bounds",  
    "value": {  
      "max": {  
        "type": "Point",  
        "value": {  
          "x": {  
            "type": "Float",  
            "value": 0.3435432568091691  
          },  
          "y": {  
            "type": "Float",  
            "value": 0.24905296319042758  
          },  
          "z": {  
            "type": "Float",  
            "value": 0.2845520466135202  
          }  
        }  
      },  
      "min": {  
        "type": "Point",  
        "value": {  
          "x": {  
            "type": "Float",  
            "value": 0.4907878164155083  
          },  
          "y": {  
            "type": "Float",  
            "value": 0.24758694946836612  
          },  
          "z": {  
            "type": "Float",  
            "value": 0.5473795276532545  
          }  
        }  
      }  
    }  
  },  
  "buildingSpaceKind": {  
    "type": "Text",  
    "value": "OpeningElement"  
  },  
  "isSpaceOfBuilding": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:Building:f61515c6-7ae8-497f-a5a0-a109d69c8ad9"  
  },  
  "isSpaceOfBuildingSpace": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:BuildingSpace:af38bc5d-cc8e-456b-933b-6f49a5a4347b"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T05:23:18.620809+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T01:47:26.1064065+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "BuildingSpace"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "BuildingSpace type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "BuildingSpace of limited BuildingSpace types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### 建筑空间 NGSI-LD 键值示例  
下面是一个以 JSON-LD 格式作为键值的 BuildingSpace 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:BuildingSpace:676ee568-16af-457c-898f-232c5900f75e",  
  "type": "BuildingSpace",  
  "airVolume": 0.6757573914426188,  
  "bounds": {  
    "max": {  
      "type": "Point",  
      "x": 0.11739641482930474,  
      "y": 0.6412223514966972,  
      "z": 0.8162459383914825  
    },  
    "min": {  
      "type": "Point",  
      "x": 0.656218944969374,  
      "y": 0.2590907017420844,  
      "z": 0.10417683913385478  
    }  
  },  
  "buildingSpaceKind": "Plate",  
  "isSpaceOfBuilding": "urn:ngsi-ld:Building:c09b1c10-d5bb-40cb-a76a-bbf551661d55",  
  "isSpaceOfBuildingSpace": "urn:ngsi-ld:BuildingSpace:0b32e85a-02bd-4ccb-a5ec-d4e4805121e9",  
  "dateCreated": "2023-01-25T17:03:22Z",  
  "dateModified": "2023-01-25T23:31:49Z",  
  "source": "Import",  
  "name": "BuildingSpace",  
  "alternateName": "BuildingSpace type 2",  
  "description": "BuildingSpace of limited BuildingSpace types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### 建筑空间 NGSI-LD 标准化示例  
下面是一个规范化 JSON-LD 格式的建筑空间示例。在不使用选项的情况下，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:BuildingSpace:d7cb7e92-0891-47f6-86a9-06a4aa5373bd",  
  "type": "BuildingSpace",  
  "airVolume": {  
    "type": "Property",  
    "unitCode": "m3",  
    "observedAt": "2023-01-26T13:10:25Z",  
    "value": 0.24704243447487917  
  },  
  "bounds": {  
    "type": "Property",  
    "value": {  
      "max": {  
        "type": "Property",  
        "value": {  
          "x": {  
            "type": "Property",  
            "value": 0.5826533723200945  
          },  
          "y": {  
            "type": "Property",  
            "value": 0.8080827869513028  
          },  
          "z": {  
            "type": "Property",  
            "value": 0.7573005865012242  
          }  
        }  
      },  
      "min": {  
        "type": "Property",  
        "value": {  
          "x": {  
            "type": "Property",  
            "value": 0.6273023443041038  
          },  
          "y": {  
            "type": "Property",  
            "value": 0.3279024163898896  
          },  
          "z": {  
            "type": "Property",  
            "value": 0.9097369934052144  
          }  
        }  
      }  
    }  
  },  
  "buildingSpaceKind": {  
    "type": "Property",  
    "value": "Covering"  
  },  
  "isSpaceOfBuilding": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Building:46ad9d28-a073-4895-a02e-eb5d12495b4a"  
  },  
  "isSpaceOfBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:fa3ff8f2-4340-4a60-8cfa-b08d35a62952"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T18:18:52Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T08:23:36Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "BuildingSpace"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "BuildingSpace type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "BuildingSpace of limited BuildingSpace types"  
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
