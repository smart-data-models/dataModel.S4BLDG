<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティ蒸発冷却器  
===========<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/EvaporativeCooler/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな説明**蒸発式クーラーは、水蒸気を飽和させることによって空気を冷却する装置である。  
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
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `flowArrangement[string]`: 逆流：空気と水の流れが異なる方向に入る。CrossFlow：空気と水の流れが垂直。ParallelFlow：空気と水の流れが同じ方向に入る。  - `hasManufacturer[string]`: エンティティ（デバイスなど）の製造者を特定する関係。値は文字列または言語タグを持つ文字列であることが期待される。  - `hasModel[string]`: エンティティ（デバイスなど）のモデルを識別する関係。値は、文字列または言語タグを持つ文字列であることが期待される。  - `heatExchangeArea[number]`: 熱交換面積。通常は平方メートル（m2）で測定される。  - `id[*]`: エンティティの一意識別子  - `isContainedInBuildingSpace[*]`: 建物の物理的空間を定義するために使用されるエンティティ。ビルディングスペースには、デバイスまたはビルディングオブジェクトが含まれる。(ビルディングスペース)  - `isContainedInPhysicalObject[*]`: 適切な空間領域を持つオブジェクト。  (DUL オントロジーより定義） （PhysicalObject）  - `isSubSystemOf[array]`: この物理オブジェクトが属するシステムへの参照。  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `name[string]`: このアイテムの名前  - `operationTemperatureMax[number]`: 許容動作周囲（空気、液体）温度範囲。通常、単位はケルビン（K）。  - `operationTemperatureMin[number]`: 許容動作周囲（空気、液体）温度範囲。通常、単位はケルビン（K）。  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `type[string]`: これは `EvaporativeCooler` と等しくなければならない。  - `waterRequirement[number]`: メークアップ水の必要量。通常m3/sで測定される。  <!-- /30-PropertiesList -->  
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
EvaporativeCooler:    
  description: An evaporative cooler is a device that cools air by saturating it with water vapor.    
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
    flowArrangement:    
      description: 'CounterFlow: Air and water flow enter in different directions. CrossFlow: Air and water flow are perpendicular. ParallelFlow: air and water flow enter in same directions'    
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
    heatExchangeArea:    
      description: Heat exchange area. Usually measured in square metre (m2)    
      type: number    
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
    operationTemperatureMax:    
      description: 'Allowable operation ambient (air, fluid) temperature range. Usually measured in degrees Kelvin (K)'    
      type: number    
      x-ngsi:    
        type: Property    
    operationTemperatureMin:    
      description: 'Allowable operation ambient (air, fluid) temperature range. Usually measured in degrees Kelvin (K)'    
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
      description: It must be equal to `EvaporativeCooler`    
      enum:    
        - EvaporativeCooler    
      type: string    
      x-ngsi:    
        type: Property    
    waterRequirement:    
      description: Make-up water requirement. Usually measured in m3/s    
      type: number    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:EvaporativeCooler"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/EvaporativeCooler/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/EvaporativeCooler/schema.json    
  x-model-tags: SAREF EvaporativeCooler    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### EvaporativeCooler NGSI-v2 キー値の例  
以下はEvaporativeCoolerのJSON-LD形式のkey-valuesの例である。これは NGSI-v2 と互換性があり、`options=keyValues` を使用すると個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:EvaporativeCooler:54b020f5-a24c-4e78-af69-ab730287a7fb",  
    "type": "EvaporativeCooler",  
    "flowArrangement": "Walk",  
    "heatExchangeArea": 0.0154798489699417,  
    "operationTemperatureMax": 0.8076614358257233,  
    "operationTemperatureMin": 0.05752519637609499,  
    "waterRequirement": 0.48344490145201957,  
    "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:b2cc75eb-3d85-44ce-b594-0c9c036f5f20",  
    "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:76419a51-5245-4bbe-b246-b2d4278d8c91",  
    "isSubSystemOf": [  
        "urn:ngsi-ld:System:ad240648-fa46-4518-82b1-4f4baa6d5de7",  
        "urn:ngsi-ld:System:3f9f73d3-72a5-4538-8869-c17a4b9df476",  
        "urn:ngsi-ld:System:ec373deb-a7d7-4b21-9e0e-9adffd16c74c"  
    ],  
    "hasManufacturer": "EvaporativeCooler Company Inc.",  
    "hasModel": "EvaporativeCooler 0.1.2",  
    "dateCreated": "2023-01-26T11:22:41Z",  
    "dateModified": "2023-01-26T09:06:31Z",  
    "source": "Import",  
    "name": "EvaporativeCooler",  
    "alternateName": "EvaporativeCooler type 2",  
    "description": "EvaporativeCooler of limited EvaporativeCooler types",  
    "dataProvider": "IFC file"  
}  
```  
</details>  
#### EvaporativeCooler NGSI-v2 正規化例  
以下は正規化されたJSON-LD形式のEvaporativeCoolerの例である。これは、NGSI-v2と互換性があり、オプションを使用しない場合、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:EvaporativeCooler:0a346c54-49ed-4047-a778-8db06579e512",  
  "type": "EvaporativeCooler",  
  "flowArrangement": {  
    "type": "Text",  
    "value": "Music"  
  },  
  "heatExchangeArea": {  
    "type": "Measurement",  
    "value": 0.7281726107323353  
  },  
  "operationTemperatureMax": {  
    "type": "Measurement",  
    "value": 0.6966196068493681  
  },  
  "operationTemperatureMin": {  
    "type": "Measurement",  
    "value": 0.2633641809598216  
  },  
  "waterRequirement": {  
    "type": "Measurement",  
    "value": 0.34619924829877713  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:BuildingSpace:09f6bb8b-789e-4410-a7d4-8927eea55d49"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:PhysicalObject:d4b8632d-7fad-4de8-901e-4efd140dbd98"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:0dd5150e-9430-493e-aba8-3843ca28c5e9"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:c101e62e-699a-4ac8-82c9-271f229e05ba"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:8dea165b-31d9-40ac-900e-eced972e318d"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "EvaporativeCooler Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "EvaporativeCooler 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T19:12:10.9508051+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T07:18:26.9847952+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "EvaporativeCooler"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "EvaporativeCooler type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "EvaporativeCooler of limited EvaporativeCooler types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### EvaporativeCooler NGSI-LD キー値の例  
以下はEvaporativeCoolerをJSON-LD形式でkey-valuesとして表した例である。これは NGSI-LD と互換性があり、`options=keyValues` を使うと個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:EvaporativeCooler:54b020f5-a24c-4e78-af69-ab730287a7fb",  
  "type": "EvaporativeCooler",  
  "flowArrangement": "Walk",  
  "heatExchangeArea": 0.0154798489699417,  
  "operationTemperatureMax": 0.8076614358257233,  
  "operationTemperatureMin": 0.05752519637609499,  
  "waterRequirement": 0.48344490145201957,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:b2cc75eb-3d85-44ce-b594-0c9c036f5f20",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:76419a51-5245-4bbe-b246-b2d4278d8c91",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:ad240648-fa46-4518-82b1-4f4baa6d5de7",  
    "urn:ngsi-ld:System:3f9f73d3-72a5-4538-8869-c17a4b9df476",  
    "urn:ngsi-ld:System:ec373deb-a7d7-4b21-9e0e-9adffd16c74c"  
  ],  
  "hasManufacturer": "EvaporativeCooler Company Inc.",  
  "hasModel": "EvaporativeCooler 0.1.2",  
  "dateCreated": "2023-01-26T11:22:41Z",  
  "dateModified": "2023-01-26T09:06:31Z",  
  "source": "Import",  
  "name": "EvaporativeCooler",  
  "alternateName": "EvaporativeCooler type 2",  
  "description": "EvaporativeCooler of limited EvaporativeCooler types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### 蒸発冷却器 NGSI-LD 正規化例  
以下は、正規化されたJSON-LD形式のEvaporativeCoolerの例である。これは、オプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:EvaporativeCooler:1eca9015-b483-4e0b-9f5c-eda9902c092d",  
  "type": "EvaporativeCooler",  
  "flowArrangement": {  
    "type": "Property",  
    "value": "COM"  
  },  
  "heatExchangeArea": {  
    "type": "Property",  
    "unitCode": "m2",  
    "observedAt": "2023-01-25T17:08:28Z",  
    "value": 0.7584250696633893  
  },  
  "operationTemperatureMax": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T18:14:01Z",  
    "value": 0.692516512025741  
  },  
  "operationTemperatureMin": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T20:42:27Z",  
    "value": 0.7188097385031748  
  },  
  "waterRequirement": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-26T08:51:16Z",  
    "value": 0.11534754798971114  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:73720b9e-732d-4566-91b8-7155f46be5ce"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:b0b36411-8e0e-460e-9e23-b05ab337d6b5"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:b0207455-4fc3-4b08-bdcf-9b605a3c4ca5"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:7ed66c88-e9d3-4b03-8cb8-a3a5cac78535"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:6c3a2470-0188-4b7f-b870-9cd359fd4111"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "EvaporativeCooler Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "EvaporativeCooler 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T00:32:51Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T12:51:38Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "EvaporativeCooler"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "EvaporativeCooler type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "EvaporativeCooler of limited EvaporativeCooler types"  
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
