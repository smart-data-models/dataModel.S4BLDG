<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティアクチュエーター  
==============<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Actuator/LICENSE.md)  
[文書が自動的に生成されます](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述です：**アクチュエータとは、機構やシステムを動かしたり制御したりするための機械的な装置です。アクチュエータは、通常、空気、電気、または液体によって作られるエネルギーを受け取り、それを何らかの運動に変換します。  
バージョン：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性に型がない場合は、複数の型や異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: このアイテムの別称  - `areaServed[string]`: サービスまたは提供されるアイテムが提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: このアイテムの説明  - `failPosition[string]`: アクチュエータの必要なフェイルセーフ位置を指定します。  - `hasManufacturer[string]`: エンティティ（例：デバイス）の製造者を特定する関係。値は、文字列または言語タグ付き文字列であることが期待される。  - `hasModel[string]`: エンティティ（例：デバイス）のモデルを識別する関係。値は、文字列または言語タグ付き文字列であることが期待される。  - `id[*]`: エンティティの一意な識別子  - `isContainedInBuildingSpace[*]`: エンティティの一意な識別子  - `isContainedInPhysicalObject[*]`: エンティティの一意な識別子  - `isSubSystemOf[array]`: この物理オブジェクトが属するシステム（複数可）への参照。  - `location[*]`: アイテムへの Geojson 参照。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon のいずれかである。  - `manualOverride[boolean]`: ハンドオペレーションオペレーションがオーバーライドとして提供されるか（＝TRUE）、提供されないか（＝FALSE）を識別する。なお、手元操作の場合、この値はデフォルトでFALSEに設定する必要があります。  - `name[string]`: この項目の名称です。  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリストです。  - `seeAlso[*]`: アイテムに関する追加リソースを指す URI のリスト。  - `source[string]`: エンティティデータの元のソースをURLとして与える一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `type[string]`: Actuator`と等しくなければならない。  <!-- /30-PropertiesList -->  
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
Actuator:    
  description: 'An actuator is a mechanical device for moving or controlling a mechanism or system. An actuator takes energy, usually created by air, electricity, or liquid, and converts that into some kind of motion.'    
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
    failPosition:    
      description: Specifies the required fail-safe position of the actuator.    
      type: string    
      x-ngsi:    
        type: Property    
    hasManufacturer:    
      description: 'A relationship identifying the manufacturer of an entity (e.g., device). The value is expected to be a string or a string with language tag.'    
      type: string    
      x-ngsi:    
        type: Property    
    hasModel:    
      description: 'A relationship identifying the model of an entity (e.g., device). The value is expected to be a string or a string with language tag.'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &actuator_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      anyOf: *actuator_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *actuator_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *actuator_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    manualOverride:    
      description: Identifies whether hand-operated operation is provided as an override (= TRUE) or not (= FALSE). Note that this value should be set to FALSE by default in the case of a Hand Operated Actuator.    
      type: boolean    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item.    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *actuator_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      description: It must be equal to `Actuator`.    
      enum:    
        - Actuator    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Actuator"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Actuator/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Actuator/schema.json    
  x-model-tags: SAREF Actuator SMART DATA MODELS    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### アクチュエータ NGSI-v2 キー値例  
ActuatorをJSON-LD形式でkey-valuesとした例を示します。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Actuator:1f654c8f-195f-4f68-a9c4-25c365ae3bd6",  
  "type": "Actuator",  
  "failPosition": "Unbranded Wooden Sausages",  
  "manualOverride": true,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:a8d821fd-8f19-4cba-a43f-dcdd0f2bb364",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:6360ca8e-4c27-4e7e-898a-e47d0ec0645e",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:b9fec7d9-c68c-402e-bb66-a3eb1f3e96e9",  
    "urn:ngsi-ld:System:12c42d0d-1fc5-43ff-9379-dfd6db487931",  
    "urn:ngsi-ld:System:14affd1a-dfe6-4faf-babf-a85f5e1ed6c1"  
  ],  
  "hasManufacturer": "Actuator Company Inc.",  
  "hasModel": "Actuator 0.1.2",  
  "dateCreated": "2023-01-25T19:33:37Z",  
  "dateModified": "2023-01-25T22:06:00Z",  
  "source": "Import",  
  "name": "Actuator",  
  "alternateName": "Actuator type 2",  
  "description": "Actuator of limited Actuator types",  
  "dataProvider": "IFC file"  
}  
```  
</details>  
#### アクチュエータ NGSI-v2 正規化例  
JSON-LD形式で正規化されたActuatorの例を示します。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Actuator:aecfb0bd-43b4-473a-9322-fe8df558e535",  
  "type": "Actuator",  
  "failPosition": {  
    "type": "Text",  
    "value": "empowering"  
  },  
  "manualOverride": {  
    "type": "Boolean",  
    "value": false  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:BuildingSpace:2acb9221-64a7-4d25-b38e-cf2521fe6b17"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:PhysicalObject:0de814dd-30b0-45a4-891a-46642e50e718"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:System:e7bdaf31-1036-4bb0-b8d4-418e9637f3dc"  
      },  
      {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:System:20d4c669-0193-4696-a18b-43670e910dc1"  
      },  
      {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:System:44bd2cba-a5e7-49b6-8cd2-588ee52380bc"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Actuator Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Actuator 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T15:30:43.3546251+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T19:46:01.2883208+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Actuator"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Actuator type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Actuator of limited Actuator types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### アクチュエータ NGSI-LD キー値 例  
ActuatorをJSON-LD形式でkey-valuesとした例を示します。これは、`options=keyValues`を使用した場合にNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Actuator:306d626a-32fa-43a4-b9f0-ea70b87cf65a",  
  "type": "Actuator",  
  "failPosition": "back up",  
  "manualOverride": true,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:5f91e381-c6ae-435e-92fc-167556af51e9",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:d1e6f1f1-ffb2-48ff-9375-9392a14dfeda",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:723bf2c4-1838-4140-bb6d-fa1f11b61344",  
    "urn:ngsi-ld:System:87c9718f-06ec-4d7e-8813-539ed94152c5",  
    "urn:ngsi-ld:System:546ffdb7-1fbf-4f21-af57-ecc6a245b68a"  
  ],  
  "hasManufacturer": "Actuator Company Inc.",  
  "hasModel": "Actuator 0.1.2",  
  "dateCreated": "2023-01-26T05:42:38Z",  
  "dateModified": "2023-01-25T16:12:27Z",  
  "source": "Import",  
  "name": "Actuator",  
  "alternateName": "Actuator type 2",  
  "description": "Actuator of limited Actuator types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### アクチュエータ NGSI-LD 正規化例  
ActuatorをJSON-LD形式で正規化した例を示します。これはオプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Actuator:5b863181-8df8-445f-af71-9ac7b91390df",  
  "type": "Actuator",  
  "failPosition": {  
    "type": "Property",  
    "value": "leading-edge"  
  },  
  "manualOverride": {  
    "type": "Property",  
    "value": true  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:c03e390f-cde4-494f-bbe8-f09c4480151c"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:7101210f-7d8d-4f0a-98f2-b9ff70bff4f0"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:2d4ca6e0-52fc-4176-9cc7-43fd3ce0230d"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:80abce5e-3292-4432-aef1-d7982d090051"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:c6e1a0ce-73b7-48f9-9aa0-1c9d38720364"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Actuator Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Actuator 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T16:34:55Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-25T18:21:38Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Actuator"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Actuator type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Actuator of limited Actuator types"  
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
