<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
エンティティ加湿器    
=========<!-- /10-Header -->    
<!-- 15-License -->    
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Humidifier/LICENSE.md)    
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
グローバルな説明**加湿器は空気中に水分を加える装置です。    
バージョン: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## プロパティのリスト    
<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。    
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。      
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: この項目の別名  - `application[string]`: 加湿器の用途。固定式：ダクト式加湿器。ポータブル：加湿器がダクト式配水システムに設置されていない場合。  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `hasManufacturer[string]`: エンティティ（デバイスなど）の製造者を特定する関係。値は文字列または言語タグを持つ文字列であることが期待される。  - `hasModel[string]`: エンティティ（デバイスなど）のモデルを識別する関係。値は、文字列または言語タグを持つ文字列であることが期待される。  - `id[*]`: エンティティの一意識別子  - `internalControl[string]`: 内部変調コントロール  - `isContainedInBuildingSpace[*]`: 建物の物理的空間を定義するために使用されるエンティティ。ビルディングスペースには、デバイスまたはビルディングオブジェクトが含まれる。(ビルディングスペース)  - `isContainedInPhysicalObject[*]`: 適切な空間領域を持つオブジェクト。  (DUL オントロジーより定義） （PhysicalObject）  - `isSubSystemOf[array]`: この物理オブジェクトが属するシステムへの参照。  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `name[string]`: このアイテムの名前  - `nominalAirFlowRate[number]`: 空気の公称流量。通常m3/s単位。  - `nominalMoistureGain[number]`: 気流中に添加される水蒸気の公称速度。通常、kg/s単位で測定される。  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `type[string]`: これは `Humidifier` と等しくなければならない。  - `waterRequirement[number]`: メークアップ水の必要量。通常m3/sで測定される。  - `weight[number]`: 装置の重量。通常、キログラム（kg）またはグラム（g）で測定される。  <!-- /30-PropertiesList -->    
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
    application:      
      description: 'Humidifier application. Fixed: Humidifier installed in a ducted flow distribution system. Portable: Humidifier is not installed in a ducted flow distribution system'      
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
    internalControl:      
      description: Internal modulation control      
      type: string      
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
    nominalAirFlowRate:      
      description: Nominal rate of air flow. Usually measured in m3/s      
      type: number      
      x-ngsi:      
        type: Property      
    nominalMoistureGain:      
      description: Nominal rate of water vapor added into the airstream. Usually measured in kg/s      
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
      description: It must be equal to `Humidifier`      
      enum:      
        - Humidifier      
      type: string      
      x-ngsi:      
        type: Property      
    waterRequirement:      
      description: Make-up water requirement. Usually measured in m3/s      
      type: number      
      x-ngsi:      
        type: Property      
    weight:      
      description: The weight of the device. Usually measured in kilograms (kg) or grams (g)      
      type: number      
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
#### 加湿器 NGSI-v2 キー値の例    
JSON-LD形式の加湿器のkey-valuesの例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると個々のエンティティのコンテキストデータを返す。    
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
以下は、正規化されたJSON-LD形式の加湿器の例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。    
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
    "type": "Number",  
    "value": 0.9292903711390679  
  },  
  "nominalMoistureGain": {  
    "type": "Number",  
    "value": 0.8580622286778447  
  },  
  "waterRequirement": {  
    "type": "Number",  
    "value": 0.554538436027498  
  },  
  "weight": {  
    "type": "Number",  
    "value": 0.7752621626916505  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:BuildingSpace:e921e031-412b-425c-931b-c63634eb5c85"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:PhysicalObject:013cd1d5-1e31-4a2a-a666-8e18c85a0360"  
  },  
  "isSubSystemOf": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:System:ea1d1a76-356e-491c-b5dc-17a8c456d7f7",  
      "urn:ngsi-ld:System:f7b44810-8762-4e67-b4d0-6e4d9bb81b46",  
      "urn:ngsi-ld:System:88bb7831-63c5-40bc-8349-7cef821db39c"  
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
#### 加湿器 NGSI-LD キー値の例    
JSON-LD形式の加湿器の例をkey-valuesとして示す。options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返す。    
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
以下は、正規化されたJSON-LD形式の加湿器の例である。これは、オプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。    
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
