<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティBuildingSpace（ビルスペース  
==========================<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/BuildingSpace/LICENSE.md)  
[文書が自動的に生成されます](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述：**建物の物理的な空間を定義するために使用されるエンティティです。建物空間には、デバイスや建物オブジェクトが含まれる。  
バージョン：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性に型がない場合は、複数の型や異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `airVolume[number]`: プロパティです。この建物空間の空気量。m3単位で測定される。  - `alternateName[string]`: このアイテムの別称  - `areaServed[string]`: サービスまたは提供されるアイテムが提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `bounds[*]`: プロパティ。この建物空間の境界を3Dのボックスで表現しています。  - `buildingSpaceKind[string]`: Property（プロパティ）。建物スペースの詳細タイプ。  - `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: このアイテムの説明  - `id[*]`: エンティティの一意な識別子  - `isSpaceOfBuilding[*]`: 関係です。建物とは、居住者または内容物に避難場所を提供し、一カ所に建っている構造物を表す。また、建築物は、建築プロジェクトの構成要素の空間構造階層における基本要素（敷地、階数、空間とともに。）(建物)  - `isSpaceOfBuildingSpace[*]`: 関係。建物の物理的空間を定義するために使用されるエンティティ。ビルディングスペースは、デバイスまたはビルディングオブジェクトを含む。(ビルディングスペース)  - `location[*]`: アイテムへの Geojson 参照。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon のいずれかとする。  - `name[string]`: この項目の名称です。  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリストです。  - `seeAlso[*]`: アイテムに関する追加リソースを指す URI のリスト。  - `source[string]`: エンティティデータの元のソースをURLとして与える一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `type[string]`: プロパティを指定します。BuildingSpace`と等しくなければならない。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
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
    airVolume:    
      description: Property. Air Volume of this building space. Measured in m3.    
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
      description: Property. Bounds of this building space represented as a box in 3D.    
      properties:    
        max:    
          description: Property. Represents a point in a 3D space.    
          properties: &buildingspace_-_properties_-_bounds_-_properties_-_min_-_properties    
            type:    
              description: Property. Property. NGSI-LD Entity Type.    
              enum:    
                - Point    
              type: string    
            x:    
              description: Property. Coordinate X of the point.    
              type: number    
            y:    
              description: Property. Coordinate Y of the point.    
              type: number    
            z:    
              description: Property. Coordinate Z of the point.    
              type: number    
          type: object    
        min:    
          description: Property. Represents a point in a 3D space.    
          properties: *buildingspace_-_properties_-_bounds_-_properties_-_min_-_properties    
          type: object    
        type:    
          description: Property. Property. NGSI-LD Entity Type.    
          enum:    
            - Bounds    
          type: string    
      type: object    
      x-ngsi:    
        type: Property    
    buildingSpaceKind:    
      description: Property. Detailed type of the Building Space.    
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
    id:    
      anyOf: &buildingspace_-_properties_-_isspaceofbuilding_-_anyof    
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
    isSpaceOfBuilding:    
      anyOf: *buildingspace_-_properties_-_isspaceofbuilding_-_anyof    
      description: 'Relationship. A building represents a structure that provides shelter for its occupants or contents and stands in one place. The building is also used to provide a basic element within the spatial structure hierarchy for the components of a building project (together with site, storey, and space). (Building)'    
      x-ngsi:    
        type: Property    
    isSpaceOfBuildingSpace:    
      anyOf: *buildingspace_-_properties_-_isspaceofbuilding_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
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
        anyOf: *buildingspace_-_properties_-_isspaceofbuilding_-_anyof    
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
      description: Property. It must be equal to `BuildingSpace`.    
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
## ペイロードの例  
#### BuildingSpace NGSI-v2 キーバリュー例  
BuildingSpaceをJSON-LD形式でkey-valuesとした例を示します。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### BuildingSpace NGSI-v2 正規化例  
JSON-LD形式で正規化されたBuildingSpaceの例を示します。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:BuildingSpace:f341006e-3556-4699-8959-19edf7079bac",  
  "type": "BuildingSpace",  
  "airVolume": {  
    "type": "Measurement",  
    "value": {  
      0.9064782098814886  
    }  
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
#### BuildingSpace NGSI-LD キーバリューの例  
BuildingSpaceをJSON-LD形式でkey-valuesとした例を示します。これは、`options=keyValues`を使用した場合にNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### 建物空間 NGSI-LD 正規化例  
JSON-LD形式のBuildingSpaceを正規化した例を示します。これは、オプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
