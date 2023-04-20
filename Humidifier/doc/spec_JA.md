<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティ加湿器  
=========<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Humidifier/LICENSE.md)  
[文書が自動的に生成されます](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述です：**加湿器は、空気中に水分を加える装置です。  
バージョン：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性に型がない場合は、複数の型や異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: このアイテムの別称  - `application[string]`: プロパティです。加湿器のアプリケーションです。固定式：ダクト式流路分配システムに設置された加湿器。ポータブル：加湿器がダクト式配電盤に設置されていない。  - `areaServed[string]`: サービスまたは提供されるアイテムが提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: このアイテムの説明  - `hasManufacturer[string]`: プロパティ。エンティティ（例：デバイス）の製造者を特定する関係。値は、文字列または言語タグ付き文字列であることが期待される。  - `hasModel[string]`: プロパティです。エンティティ（例：デバイス）のモデルを識別する関係。値は、文字列または言語タグ付き文字列であることが期待される。  - `id[*]`: エンティティの一意な識別子  - `internalControl[string]`: 特性です。内部変調制御。  - `isContainedInBuildingSpace[*]`: 関係。建物の物理的空間を定義するために使用されるエンティティ。ビルディングスペースは、デバイスまたはビルディングオブジェクトを含む。(ビルディングスペース)  - `isContainedInPhysicalObject[*]`: 関係です。適切な空間領域を持つあらゆるオブジェクト。  (DULオントロジーから抽出した定義）（PhysicalObject)  - `isSubSystemOf[array]`: 関係。この物理オブジェクトが属するシステム（複数可）への参照。  - `location[*]`: アイテムへの Geojson 参照。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon のいずれかである。  - `name[string]`: この項目の名称です。  - `nominalAirFlowRate[object]`: 特性です。空気の流れの公称速度。通常、m3/sで測定される。  - `nominalMoistureGain[object]`: 特性。気流に加えられる水蒸気の公称速度。通常、kg/sで測定される。  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリストです。  - `seeAlso[*]`: アイテムに関する追加リソースを指す URI のリスト。  - `source[string]`: エンティティデータの元のソースをURLとして与える一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `type[string]`: プロパティを指定します。これは `Humidifier` と等しくなければならない。  - `waterRequirement[object]`: プロパティです。メイクアップウォーターの必要量。通常、m3/sで測定される。  - `weight[object]`: 特性です。デバイスの重量を表します。通常、キログラム（kg）またはグラム（g）で測定される。  <!-- /30-PropertiesList -->  
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
Humidifier:    
  description: A humidifier is a device that adds moisture into the air.    
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
    application:    
      description: 'Property. Humidifier application. Fixed: Humidifier installed in a ducted flow distribution system. Portable: Humidifier is not installed in a ducted flow distribution system.'    
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
      anyOf: &humidifier_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    internalControl:    
      description: Property. Internal modulation control.    
      type: string    
      x-ngsi:    
        type: Property    
    isContainedInBuildingSpace:    
      anyOf: *humidifier_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *humidifier_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *humidifier_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    nominalAirFlowRate:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: Property. Nominal rate of air flow. Usually measured in m3/s.    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: &humidifier_-_properties_-_nominalmoisturegain_-_properties    
        observedAt:    
          description: Property. A relationship stating the timestamp of an entity (e.g. a measurement).    
          format: date-time    
          type: string    
        unitCode:    
          description: Property. A relationship identifying the unit of measure used for a certain entity.    
          type: string    
        value:    
          description: 'Property. A relationship defining the value of a certain property, e.g., energy or power. Note that, even if numeric values are expected to enable reasoning, measurement values could use other datatypes.'    
          type: number    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    nominalMoistureGain:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: Property. Nominal rate of water vapor added into the airstream. Usually measured in kg/s.    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *humidifier_-_properties_-_nominalmoisturegain_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *humidifier_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      description: Property. It must be equal to `Humidifier`.    
      enum:    
        - Humidifier    
      type: string    
      x-ngsi:    
        type: Property    
    waterRequirement:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: Property. Make-up water requirement. Usually measured in m3/s.    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *humidifier_-_properties_-_nominalmoisturegain_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    weight:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: Property. The weight of the device. Usually measured in kilograms (kg) or grams (g).    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *humidifier_-_properties_-_nominalmoisturegain_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Humidifier"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Humidifier/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Humidifier/schema.json    
  x-model-tags: SAREF Humidifier    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### 加湿器NGSI-v2キーバリュー例  
ここでは、HumidifierをJSON-LD形式でkey-valuesとした例を示す。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Humidifier:ac37f3cb-91a4-420a-bf0c-0b9e7e172521",  
    "type": "Humidifier",  
    "application": "Trafficway",  
    "internalControl": "circuit",  
    "nominalAirFlowRate": 0.5067643159622129,  
    "nominalMoistureGain": 0.6949833248374234,  
    "waterRequirement": 0.006912028133186698,  
    "weight": 0.0357306217024943,  
    "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:09a4b404-f422-4f1c-b53e-23fabedd21c7",  
    "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:dea722e2-f244-4618-bd6d-40a74f6053c7",  
    "isSubSystemOf": [  
        "urn:ngsi-ld:System:7d1ab6f4-93d8-45f1-8075-e07d9f0a92ab",  
        "urn:ngsi-ld:System:97c9fe52-5019-4f15-9e09-b74248a9e008",  
        "urn:ngsi-ld:System:4adb71a2-0ae3-4ecc-9d29-9e913f5cb577"  
    ],  
    "hasManufacturer": "Humidifier Company Inc.",  
    "hasModel": "Humidifier 0.1.2",  
    "dateCreated": "2023-01-26T01:28:19Z",  
    "dateModified": "2023-01-26T00:58:24Z",  
    "source": "Import",  
    "name": "Humidifier",  
    "alternateName": "Humidifier type 2",  
    "description": "Humidifier of limited Humidifier types",  
    "dataProvider": "IFC file"  
}  
```  
</details>  
#### 加湿器 NGSI-v2 正規化例  
JSON-LD形式で正規化されたHumidifierの例を示します。これは、オプションを使用しない場合のNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Humidifier:fba02151-cd4b-4dfd-a7a7-37dafa66d943",  
  "type": "Humidifier",  
  "application": {  
    "type": "Text",  
    "value": "Small Soft Car"  
  },  
  "internalControl": {  
    "type": "Text",  
    "value": "mindshare"  
  },  
  "nominalAirFlowRate": {  
    "type": "Measurement",  
    "value":  0.9292903711390679  
  },  
  "nominalMoistureGain": {  
    "type": "Measurement",  
    "value":  0.8580622286778447  
  },  
  "waterRequirement": {  
    "type": "Measurement",  
    "value": 0.554538436027498  
  },  
  "weight": {  
    "type": "Measurement",  
    "value": 0.7752621626916505  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:BuildingSpace:e921e031-412b-425c-931b-c63634eb5c85"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:PhysicalObject:013cd1d5-1e31-4a2a-a666-8e18c85a0360"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:ea1d1a76-356e-491c-b5dc-17a8c456d7f7"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:f7b44810-8762-4e67-b4d0-6e4d9bb81b46"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:88bb7831-63c5-40bc-8349-7cef821db39c"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Humidifier Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Humidifier 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T08:47:34.1843489+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T06:27:14.5040882+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Humidifier"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Humidifier type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Humidifier of limited Humidifier types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### 加湿器 NGSI-LD キー値例  
ここでは、HumidifierをJSON-LD形式でkey-valuesとした例を示します。これは、`options=keyValues`を使用した場合にNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Humidifier:ac37f3cb-91a4-420a-bf0c-0b9e7e172521",  
  "type": "Humidifier",  
  "application": "Trafficway",  
  "internalControl": "circuit",  
  "nominalAirFlowRate": 0.5067643159622129,  
  "nominalMoistureGain": 0.6949833248374234,  
  "waterRequirement": 0.006912028133186698,  
  "weight": 0.0357306217024943,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:09a4b404-f422-4f1c-b53e-23fabedd21c7",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:dea722e2-f244-4618-bd6d-40a74f6053c7",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:7d1ab6f4-93d8-45f1-8075-e07d9f0a92ab",  
    "urn:ngsi-ld:System:97c9fe52-5019-4f15-9e09-b74248a9e008",  
    "urn:ngsi-ld:System:4adb71a2-0ae3-4ecc-9d29-9e913f5cb577"  
  ],  
  "hasManufacturer": "Humidifier Company Inc.",  
  "hasModel": "Humidifier 0.1.2",  
  "dateCreated": "2023-01-26T01:28:19Z",  
  "dateModified": "2023-01-26T00:58:24Z",  
  "source": "Import",  
  "name": "Humidifier",  
  "alternateName": "Humidifier type 2",  
  "description": "Humidifier of limited Humidifier types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### 加湿器 NGSI-LD 正規化例  
JSON-LD形式で正規化されたHumidifierの例を示します。これは、オプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Humidifier:7535836f-92b5-4489-b99c-424fab29c039",  
  "type": "Humidifier",  
  "application": {  
    "type": "Property",  
    "value": "payment"  
  },  
  "internalControl": {  
    "type": "Property",  
    "value": "national"  
  },  
  "nominalAirFlowRate": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-25T23:50:20Z",  
    "value": 0.6517710650891719  
  },  
  "nominalMoistureGain": {  
    "type": "Property",  
    "unitCode": "kg/s",  
    "observedAt": "2023-01-26T00:47:56Z",  
    "value": 0.7521424188536304  
  },  
  "waterRequirement": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-26T04:16:30Z",  
    "value": 0.37658219788129976  
  },  
  "weight": {  
    "type": "Property",  
    "unitCode": "g",  
    "observedAt": "2023-01-25T20:12:20Z",  
    "value": 0.348798884385924  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:89364634-51b8-4628-b785-be02d50d9653"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:748df8f3-6595-4591-bc38-4e393a942194"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:45f04a26-3ae7-4a68-a960-4e4c9667bbb8"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:b619039a-e060-41ce-8e61-cdbc63e86287"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:94b68acc-bf31-40d7-a089-1172ff14240a"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Humidifier Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Humidifier 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T19:33:58Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T04:06:21Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Humidifier"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Humidifier type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Humidifier of limited Humidifier types"  
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
