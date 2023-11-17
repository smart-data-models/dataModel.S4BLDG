<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
エンティティコンプレッサー    
=============<!-- /10-Header -->    
<!-- 15-License -->    
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Compressor/LICENSE.md)    
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
グローバルな説明**コンプレッサーは、一般的に冷凍回路で使用される流体を圧縮する装置である。    
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
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `compressorSpeed[number]`: コンプレッサーの回転数。通常はサイクル/秒で測定される。  - `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `hasHotGasBypass[boolean]`: コンプレッサーにホットガスバイパスを提供するかどうか。TRUE = はい, FALSE = いいえ  - `hasManufacturer[string]`: エンティティ（デバイスなど）の製造者を特定する関係。値は文字列または言語タグを持つ文字列であることが期待される。  - `hasModel[string]`: エンティティ（デバイスなど）のモデルを識別する関係。値は、文字列または言語タグを持つ文字列であることが期待される。  - `id[*]`: エンティティの一意識別子  - `idealCapacity[number]`: 理想的な条件下でのコンプレッサー能力。通常、ワット（W、J/s）で測定される。  - `idealShaftPower[number]`: 理想状態でのコンプレッサーシャフト出力。通常、単位はワット（W、J/s）。  - `impellerDiameter[number]`: コンプレッサーのインペラーの直径 - 幾何学的に類似したコンプレッサーの性能を測定するために使用される。通常、ミリメートル（mm）で測定される。  - `isContainedInBuildingSpace[*]`: 建物の物理的空間を定義するために使用されるエンティティ。ビルディングスペースには、デバイスまたはビルディングオブジェクトが含まれる。(ビルディングスペース)  - `isContainedInPhysicalObject[*]`: 適切な空間領域を持つオブジェクト。  (DUL オントロジーより定義） （PhysicalObject）  - `isSubSystemOf[array]`: この物理オブジェクトが属するシステムへの参照。  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `name[string]`: このアイテムの名前  - `nominalCapacity[number]`: 公称容量。通常、単位はワット（W、J/s）。  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `partLoadRatioMax[number]`: 公称容量に対する最大部分負荷率  - `partLoadRatioMin[number]`: 公称容量に対する最低負荷率  - `powerSource[string]`: コンプレッサーを駆動する動力の種類  - `refrigerantClass[string]`: コンプレッサーで使用される冷媒クラス。CFC：クロロフルオロカーボン。HCFC：ハイドロクロロフルオロカーボン。HFC: ハイドロフルオロカーボン。  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `type[string]`: Compressor`と等しくなければならない。  <!-- /30-PropertiesList -->    
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
Compressor:      
  description: A compressor is a device that compresses a fluid typically used in a refrigeration circuit.      
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
    compressorSpeed:      
      description: Compressor speed. Usually measured in cycles/s      
      type: number      
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
    hasHotGasBypass:      
      description: 'Whether or not hot gas bypass is provided for the compressor. TRUE = Yes, FALSE = No'      
      type: boolean      
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
    idealCapacity:      
      description: 'Compressor capacity under ideal conditions. Usually measured in Watts (W, J/s)'      
      type: number      
      x-ngsi:      
        type: Property      
    idealShaftPower:      
      description: 'Compressor shaft power under ideal conditions. Usually measured in Watts (W, J/s)'      
      type: number      
      x-ngsi:      
        type: Property      
    impellerDiameter:      
      description: Diameter of compressor impeller - used to scale performance of geometrically similar compressors. Usually measured in millimeters (mm)      
      type: number      
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
    partLoadRatioMax:      
      description: Maximum part load ratio as a fraction of nominal capacity      
      type: number      
      x-ngsi:      
        type: Property      
    partLoadRatioMin:      
      description: Minimum part load ratio as a fraction of nominal capacity      
      type: number      
      x-ngsi:      
        type: Property      
    powerSource:      
      description: Type of power driving the compressor      
      type: string      
      x-ngsi:      
        type: Property      
    refrigerantClass:      
      description: 'Refrigerant class used by the compressor. CFC: Chlorofluorocarbons. HCFC: Hydrochlorofluorocarbons. HFC: Hydrofluorocarbons'      
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
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    type:      
      description: It must be equal to `Compressor`      
      enum:      
        - Compressor      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Compressor"      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Compressor/LICENSE.md      
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Compressor/schema.json      
  x-model-tags: SAREF Compressor      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## ペイロードの例    
#### コンプレッサー NGSI-v2 キー値の例    
JSON-LD形式のCompressorのkey-valuesの例である。options=keyValues`を使うとNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返す。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Compressor:99624683-cbb4-4bac-a458-e5bde1df9ff6",  
  "type": "Compressor",  
  "compressorSpeed": 0.679723675842234,  
  "hasHotGasBypass": true,  
  "idealCapacity": 0.7248048000316983,  
  "idealShaftPower": 0.47111429367476765,  
  "impellerDiameter": 0.8496808897888555,  
  "nominalCapacity": 0.8766392143544064,  
  "partLoadRatioMax": 0.5560596438051391,  
  "partLoadRatioMin": 0.22917332777815946,  
  "powerSource": "Practical Steel Chair",  
  "refrigerantClass": "protocol",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:9c3fb868-0647-4480-b105-2221a6cd3354",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:868ed081-1e1b-497f-a18f-11c416e2a90e",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:157c6a62-21ad-4aa4-b3d2-5a0ec1f2c667",  
    "urn:ngsi-ld:System:6fd790f8-68de-4047-a771-4b245c4aff90",  
    "urn:ngsi-ld:System:18a2426a-2c96-4064-959d-98e7aba7904d"  
  ],  
  "hasManufacturer": "Compressor Company Inc.",  
  "hasModel": "Compressor 0.1.2",  
  "dateCreated": "2023-01-26T10:11:46Z",  
  "dateModified": "2023-01-26T05:03:38Z",  
  "source": "Import",  
  "name": "Compressor",  
  "alternateName": "Compressor type 2",  
  "description": "Compressor of limited Compressor types",  
  "dataProvider": "IFC file"  
}  
```  
</details>    
#### コンプレッサー NGSI-v2 正規化例    
以下は、正規化されたJSON-LD形式のCompressorの例である。これは、オプションを使用しない場合はNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Compressor:5286e31e-5c79-4133-93c4-07c1f3574128",  
  "type": "Compressor",  
  "compressorSpeed": {  
    "type": "Number",  
    "value": 0.6951462722377054  
  },  
  "hasHotGasBypass": {  
    "type": "Boolean",  
    "value": true  
  },  
  "idealCapacity": {  
    "type": "Number",  
    "value": 0.3445800754974827  
  },  
  "idealShaftPower": {  
    "type": "Number",  
    "value": 0.8311250404203112  
  },  
  "impellerDiameter": {  
    "type": "Number",  
    "value": 0.868808285450986  
  },  
  "nominalCapacity": {  
    "type": "Number",  
    "value": 0.9287385861700207  
  },  
  "partLoadRatioMax": {  
    "type": "Number",  
    "value": 0.38901369640969274  
  },  
  "partLoadRatioMin": {  
    "type": "Number",  
    "value": 0.9657934764992187  
  },  
  "powerSource": {  
    "type": "Text",  
    "value": "bluetooth"  
  },  
  "refrigerantClass": {  
    "type": "Text",  
    "value": "Fresh"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:BuildingSpace:91df3ba9-787a-4ebb-9be6-ae4c05263de1"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:PhysicalObject:e9909895-084e-4023-9a5a-001322f825f9"  
  },  
  "isSubSystemOf": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:System:7ebaae6c-b549-4610-8df4-9c28cebe42a9",  
      "urn:ngsi-ld:System:cedc316a-3057-4f0b-9800-db9757c47286",  
      "urn:ngsi-ld:System:b64d7a83-9d09-405a-82dc-e2dc92ba7ae5"  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Compressor Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Compressor 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T08:32:27.8745501+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T12:23:46.0320445+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Compressor"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Compressor type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Compressor of limited Compressor types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>    
#### 圧縮機 NGSI-LD キー値の例    
CompressorのJSON-LD形式のkey-valuesの例です。options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返す。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Compressor:99624683-cbb4-4bac-a458-e5bde1df9ff6",  
  "type": "Compressor",  
  "compressorSpeed": 0.679723675842234,  
  "hasHotGasBypass": true,  
  "idealCapacity": 0.7248048000316983,  
  "idealShaftPower": 0.47111429367476765,  
  "impellerDiameter": 0.8496808897888555,  
  "nominalCapacity": 0.8766392143544064,  
  "partLoadRatioMax": 0.5560596438051391,  
  "partLoadRatioMin": 0.22917332777815946,  
  "powerSource": "Practical Steel Chair",  
  "refrigerantClass": "protocol",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:9c3fb868-0647-4480-b105-2221a6cd3354",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:868ed081-1e1b-497f-a18f-11c416e2a90e",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:157c6a62-21ad-4aa4-b3d2-5a0ec1f2c667",  
    "urn:ngsi-ld:System:6fd790f8-68de-4047-a771-4b245c4aff90",  
    "urn:ngsi-ld:System:18a2426a-2c96-4064-959d-98e7aba7904d"  
  ],  
  "hasManufacturer": "Compressor Company Inc.",  
  "hasModel": "Compressor 0.1.2",  
  "dateCreated": "2023-01-26T10:11:46Z",  
  "dateModified": "2023-01-26T05:03:38Z",  
  "source": "Import",  
  "name": "Compressor",  
  "alternateName": "Compressor type 2",  
  "description": "Compressor of limited Compressor types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>    
#### コンプレッサー NGSI-LD 正規化例    
以下は、正規化されたJSON-LD形式のCompressorの例である。これは、オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Compressor:ff065369-a64b-4950-8bcd-ea73c6f6bf34",  
  "type": "Compressor",  
  "compressorSpeed": {  
    "type": "Property",  
    "unitCode": "cycles/s",  
    "observedAt": "2023-01-26T02:36:18Z",  
    "value": 0.23988109283737147  
  },  
  "hasHotGasBypass": {  
    "type": "Property",  
    "value": true  
  },  
  "idealCapacity": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-25T18:17:55Z",  
    "value": 0.37381644415955617  
  },  
  "idealShaftPower": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-25T19:36:02Z",  
    "value": 0.7352666167757617  
  },  
  "impellerDiameter": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-25T16:56:06Z",  
    "value": 0.4819044880876878  
  },  
  "nominalCapacity": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-26T02:02:53Z",  
    "value": 0.42903531710900167  
  },  
  "partLoadRatioMax": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-25T20:48:37Z",  
    "value": 0.44114941929726603  
  },  
  "partLoadRatioMin": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-25T21:57:43Z",  
    "value": 0.8407270037851944  
  },  
  "powerSource": {  
    "type": "Property",  
    "value": "Mississippi"  
  },  
  "refrigerantClass": {  
    "type": "Property",  
    "value": "initiatives"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:200fbc88-04e4-4634-9ab8-31a7ffd7801a"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:6516f3b0-d423-45b0-bcfe-f5a361c118a1"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:0d189ba5-fbb5-42f9-b221-e481ed2215b3"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:682f3690-3403-45d3-8c59-d62b82b2dbb3"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:f346ab7e-bb7c-4da8-853f-f37193cfe98e"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Compressor Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Compressor 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T12:36:15Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-25T17:29:33Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Compressor"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Compressor type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Compressor of limited Compressor types"  
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
