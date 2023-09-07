<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティコンデンサー  
============<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Condenser/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな説明**コンデンサーは、通常、冷媒のような物質を気体状態から液体状態に凝縮させることによって、熱を放散させるために使用される装置である。  
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
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `externalSurfaceArea[number]`: 外部表面積（一次面積と二次面積の両方）。通常は平方メートル（m2）で測定される。  - `hasManufacturer[string]`: エンティティ（デバイスなど）の製造者を特定する関係。値は文字列または言語タグを持つ文字列であることが期待される。  - `hasModel[string]`: エンティティ（デバイスなど）のモデルを識別する関係。値は、文字列または言語タグを持つ文字列であることが期待される。  - `id[*]`: エンティティの一意識別子  - `internalRefrigerantVolume[number]`: 蒸発器（冷媒側）の内部容積。通常、立方メートル（m3）で測定される。  - `internalSurfaceArea[number]`: 内部表面積。通常は平方メートル（m2）で測定される。  - `internalWaterVolume[number]`: 蒸発器（水側）の内部容積。通常、立方メートル（m3）で測定される。  - `isContainedInBuildingSpace[*]`: 建物の物理的空間を定義するために使用されるエンティティ。ビルディングスペースには、デバイスまたはビルディングオブジェクトが含まれる。(ビルディングスペース)  - `isContainedInPhysicalObject[*]`: 適切な空間領域を持つオブジェクト。  (DUL オントロジーより定義） （PhysicalObject）  - `isSubSystemOf[array]`: この物理オブジェクトが属するシステムへの参照。  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `name[string]`: このアイテムの名前  - `nominalHeatTransferArea[number]`: 公称総合熱伝達率に関連する公称伝熱表面積。通常、平方メートル（m2）で測定される。  - `nominalHeatTransferCoefficient[number]`: 公称伝熱面積に関連する公称総合熱伝達率。通常、単位はワット/m2ケルビン。  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `refrigerantClass[string]`: コンプレッサーで使用される冷媒クラス。CFC：クロロフルオロカーボン。HCFC：ハイドロクロロフルオロカーボン。HFC: ハイドロフルオロカーボン。  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `type[string]`: それは `Condenser` と等しくなければならない。  <!-- /30-PropertiesList -->  
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
Condenser:    
  description: 'A condenser is a device that is used to dissipate heat, typically by condensing a substance such as a refrigerant from its gaseous to its liquid state.'    
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
    externalSurfaceArea:    
      description: External surface area (both primary and secondary area). Usually measured in square metre (m2)    
      type: number    
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
    internalRefrigerantVolume:    
      description: Internal volume of evaporator (refrigerant side). Usually measured in cubic metre (m3)    
      type: number    
      x-ngsi:    
        type: Property    
    internalSurfaceArea:    
      description: Internal surface area. Usually measured in square metre (m2)    
      type: number    
      x-ngsi:    
        type: Property    
    internalWaterVolume:    
      description: Internal volume of evaporator (water side). Usually measured in cubic metre (m3)    
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
    nominalHeatTransferArea:    
      description: Nominal heat transfer surface area associated with nominal overall heat transfer coefficient. Usually measured in square metre (m2)    
      type: number    
      x-ngsi:    
        type: Property    
    nominalHeatTransferCoefficient:    
      description: Nominal overall heat transfer coefficient associated with nominal heat transfer area. Usually measured in Watts/m2 Kelvin    
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
      description: It must be equal to `Condenser`    
      enum:    
        - Condenser    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Condenser"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Condenser/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Condenser/schema.json    
  x-model-tags: SAREF Condenser    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### コンデンサー NGSI-v2 キー値の例  
以下は、JSON-LD フォーマットの Condenser のキー値の例である。これは NGSI-v2 と互換性があり、`options=keyValues` を使用すると個々のエンティティのコンテキスト・データを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Condenser:2adcb166-23ce-4061-8062-952d5f2402b9",  
  "type": "Condenser",  
  "externalSurfaceArea": 0.18804655027013273,  
  "internalRefrigerantVolume": 0.1588694072031649,  
  "internalSurfaceArea": 0.884829655411807,  
  "internalWaterVolume": 0.7576300292464242,  
  "nominalHeatTransferArea": 0.04220384603580274,  
  "nominalHeatTransferCoefficient": 0.4901767947128819,  
  "refrigerantClass": "Barbados",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:7ba37c8a-b348-4fc5-8191-22dbe255c23e",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:f9999243-09ea-40b2-892a-63bfd9062a09",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:374a6c1e-348f-46a2-824d-616554f66351",  
    "urn:ngsi-ld:System:0bd6a865-18bc-40a2-b1cf-64af77762cee",  
    "urn:ngsi-ld:System:e8c3da85-a230-40e1-832c-e03b342a1160"  
  ],  
  "hasManufacturer": "Condenser Company Inc.",  
  "hasModel": "Condenser 0.1.2",  
  "dateCreated": "2023-01-25T15:55:59Z",  
  "dateModified": "2023-01-26T06:49:28Z",  
  "source": "Import",  
  "name": "Condenser",  
  "alternateName": "Condenser type 2",  
  "description": "Condenser of limited Condenser types",  
  "dataProvider": "IFC file"  
}  
```  
</details>  
#### コンデンサー NGSI-v2 正規化例  
以下は、正規化された JSON-LD フォーマットの Condenser の例である。これは、オプションを使用しない場合は NGSI-v2 と互換性があり、個々のエンティティのコンテキスト・データを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Condenser:e22782fc-5392-4dd2-b891-29b5fbf683cd",  
  "type": "Condenser",  
  "externalSurfaceArea": {  
    "type": "Measurement",  
    "value": 0.1255332761606085  
  },  
  "internalRefrigerantVolume": {  
    "type": "Measurement",  
    "value": 0.5305579766612258  
  },  
  "internalSurfaceArea": {  
    "type": "Measurement",  
    "value": 0.7094627719374283  
  },  
  "internalWaterVolume": {  
    "type": "Measurement",  
    "value": 0.3123303218703414  
  },  
  "nominalHeatTransferArea": {  
    "type": "Measurement",  
    "value": 0.4444793909507544  
  },  
  "nominalHeatTransferCoefficient": {  
    "type": "Measurement",  
    "value": 0.6428769642448905  
  },  
  "refrigerantClass": {  
    "type": "Text",  
    "value": "Ergonomic Fresh Pants"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:BuildingSpace:ae10b0d7-9929-45cc-bf0c-3e3ab5380c1a"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:PhysicalObject:a3e1362f-7a17-46e9-a997-fd763290b5a2"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:47267553-d21a-42f8-b1b9-b24ec529e8ad"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:878dd196-c9af-43d7-8d36-344fa19ca56f"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:366cc386-314f-4591-9f3f-4099890c74e7"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Condenser Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Condenser 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T23:40:11.0211053+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T22:43:21.3342982+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Condenser"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Condenser type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Condenser of limited Condenser types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### コンデンサー NGSI-LD キー値 例  
以下はコンデンサーを JSON-LD フォーマットの key-values で表した例である。これは NGSI-LD と互換性があり、`options=keyValues` を使うと個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Condenser:2adcb166-23ce-4061-8062-952d5f2402b9",  
  "type": "Condenser",  
  "externalSurfaceArea": 0.18804655027013273,  
  "internalRefrigerantVolume": 0.1588694072031649,  
  "internalSurfaceArea": 0.884829655411807,  
  "internalWaterVolume": 0.7576300292464242,  
  "nominalHeatTransferArea": 0.04220384603580274,  
  "nominalHeatTransferCoefficient": 0.4901767947128819,  
  "refrigerantClass": "Barbados",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:7ba37c8a-b348-4fc5-8191-22dbe255c23e",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:f9999243-09ea-40b2-892a-63bfd9062a09",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:374a6c1e-348f-46a2-824d-616554f66351",  
    "urn:ngsi-ld:System:0bd6a865-18bc-40a2-b1cf-64af77762cee",  
    "urn:ngsi-ld:System:e8c3da85-a230-40e1-832c-e03b342a1160"  
  ],  
  "hasManufacturer": "Condenser Company Inc.",  
  "hasModel": "Condenser 0.1.2",  
  "dateCreated": "2023-01-25T15:55:59Z",  
  "dateModified": "2023-01-26T06:49:28Z",  
  "source": "Import",  
  "name": "Condenser",  
  "alternateName": "Condenser type 2",  
  "description": "Condenser of limited Condenser types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### コンデンサー NGSI-LD 正規化例  
以下は、正規化された JSON-LD フォーマットの Condenser の例である。これは、オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキスト・データを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Condenser:290f1265-1ded-4706-b549-43d7ddcaa239",  
  "type": "Condenser",  
  "externalSurfaceArea": {  
    "type": "Property",  
    "unitCode": "m2",  
    "observedAt": "2023-01-26T11:04:44Z",  
    "value": 0.3471102075551651  
  },  
  "internalRefrigerantVolume": {  
    "type": "Property",  
    "unitCode": "m3",  
    "observedAt": "2023-01-26T10:30:09Z",  
    "value": 0.696994206179287  
  },  
  "internalSurfaceArea": {  
    "type": "Property",  
    "unitCode": "m2",  
    "observedAt": "2023-01-25T14:42:31Z",  
    "value": 0.7522617883905902  
  },  
  "internalWaterVolume": {  
    "type": "Property",  
    "unitCode": "m3",  
    "observedAt": "2023-01-26T09:25:42Z",  
    "value": 0.5807649609435256  
  },  
  "nominalHeatTransferArea": {  
    "type": "Property",  
    "unitCode": "m2",  
    "observedAt": "2023-01-26T05:15:12Z",  
    "value": 0.6105994546410142  
  },  
  "nominalHeatTransferCoefficient": {  
    "type": "Property",  
    "unitCode": "Kelvin",  
    "observedAt": "2023-01-25T14:28:56Z",  
    "value": 0.17023310849677553  
  },  
  "refrigerantClass": {  
    "type": "Property",  
    "value": "Generic Metal Pants"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:b7d758c3-cd93-4ce4-a414-28e5a714b67c"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:9d98233b-6df5-418e-b43c-5f98c921296f"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:6ba8c28a-2ebf-4a11-ba34-b7d778896bf9"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:3f480247-b6e3-4cc3-89e1-5c1f88507e48"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:645beb56-0f95-4b35-a0ed-56d848e575f1"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Condenser Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Condenser 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T22:14:26Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T02:56:43Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Condenser"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Condenser type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Condenser of limited Condenser types"  
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
