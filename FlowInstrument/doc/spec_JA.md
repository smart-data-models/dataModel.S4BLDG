<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティフローインストゥルメント  
==================<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/FlowInstrument/LICENSE.md)  
[文書が自動的に生成されます](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description：**流量計は、ある点におけるシステムの特定の特性の値を読み取り、表示する、または2点間の特性の値の差を表示するものである。  計器は通常、ある時点における特性の値を決定することを目的とするものである。経時的に値を記録または積分することは、計器の目的ではない（ただし、そのような機能を果たす記録装置に接続されることはある）。このエンティティは、あらゆる形態の機械式流量計（温度計、圧力計など）および電気式流量計（電流計、電圧計など）を対象とする**。  
バージョン：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性に型がない場合は、複数の型や異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: このアイテムの別称  - `areaServed[string]`: サービスまたは提供されるアイテムが提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: このアイテムの説明  - `hasManufacturer[string]`: プロパティ。エンティティ（例：デバイス）の製造者を特定する関係。値は、文字列または言語タグ付き文字列であることが期待される。  - `hasModel[string]`: プロパティです。エンティティ（例：デバイス）のモデルを識別する関係。値は、文字列または言語タグ付き文字列であることが期待される。  - `id[*]`: エンティティの一意な識別子  - `isContainedInBuildingSpace[*]`: 関係。建物の物理的空間を定義するために使用されるエンティティ。ビルディングスペースは、デバイスまたはビルディングオブジェクトを含む。(ビルディングスペース)  - `isContainedInPhysicalObject[*]`: 関係です。適切な空間領域を持つあらゆるオブジェクト。  (DULオントロジーから抽出した定義）（PhysicalObject)  - `isSubSystemOf[array]`: 関係。この物理オブジェクトが属するシステム（複数可）への参照。  - `location[*]`: アイテムへの Geojson 参照。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon のいずれかである。  - `name[string]`: この項目の名称です。  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリストです。  - `seeAlso[*]`: アイテムに関する追加リソースを指す URI のリスト。  - `source[string]`: エンティティデータの元のソースをURLとして与える一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `type[string]`: プロパティです。これは `FlowInstrument` と等しくなければならない。  <!-- /30-PropertiesList -->  
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
FlowInstrument:    
  description: 'A flow instrument reads and displays the value of a particular property of a system at a point, or displays the difference in the value of a property between two points.  Instrumentation is typically for the purpose of determining the value of the property at a point in time. It is not the purpose of an instrument to record or integrate the values over time (although they may be connected to recording devices that do perform such a function). This entity provides for all forms of mechanical flow instrument (thermometers, pressure gauges etc.) and electrical flow instruments (ammeters, voltmeters etc.)'    
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
      anyOf: &flowinstrument_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      anyOf: *flowinstrument_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *flowinstrument_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *flowinstrument_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *flowinstrument_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      description: Property. It must be equal to `FlowInstrument`.    
      enum:    
        - FlowInstrument    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:FlowInstrument"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/FlowInstrument/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/FlowInstrument/schema.json    
  x-model-tags: SAREF FlowInstrument    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### FlowInstrument NGSI-v2 キー値例  
FlowInstrumentをJSON-LD形式でkey-valuesとした例である。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:FlowInstrument:dae4680c-2e88-47e6-b993-f1e29b3f50c8",  
  "type": "FlowInstrument",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:fa1fe74d-f153-43f7-be65-1e4e6498dddd",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:415ee32f-19dc-487b-bb68-8d3819ac2bb5",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:7c9c5054-0de4-4113-808f-7fe6f98c3c4c",  
    "urn:ngsi-ld:System:befc8c25-4c95-4564-9e8f-2691b142c2aa",  
    "urn:ngsi-ld:System:30e906e9-8f14-4a95-8769-5a741e3ab247"  
  ],  
  "hasManufacturer": "FlowInstrument Company Inc.",  
  "hasModel": "FlowInstrument 0.1.2",  
  "dateCreated": "2023-01-25T22:14:07Z",  
  "dateModified": "2023-01-26T07:11:48Z",  
  "source": "Import",  
  "name": "FlowInstrument",  
  "alternateName": "FlowInstrument type 2",  
  "description": "FlowInstrument of limited FlowInstrument types",  
  "dataProvider": "IFC file"  
}  
```  
</details>  
#### FlowInstrument NGSI-v2 正規化例  
以下は、正規化されたJSON-LD形式のFlowInstrumentの例である。これは、オプションを使用しない場合のNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:FlowInstrument:0c00b2fc-6e77-40f7-893f-62b6bf889a28",  
  "type": "FlowInstrument",  
  "isContainedInBuildingSpace": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:BuildingSpace:9536fac3-8558-4d91-b41d-0ebc36181d1f"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:PhysicalObject:7d996944-8111-452d-af1a-e9ad243db4e9"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:9c5662ef-5dcd-4b51-9058-5a833f3afe72"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:06ad7437-bd68-4c38-b3ba-3dcb2ad626c7"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:52b6e1ce-e462-4ab0-b156-22a051b05d40"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "FlowInstrument Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "FlowInstrument 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T23:14:36.4680373+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T18:10:08.8180513+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "FlowInstrument"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "FlowInstrument type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "FlowInstrument of limited FlowInstrument types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### FlowInstrument NGSI-LD キー値例  
FlowInstrumentをJSON-LD形式でkey-valuesとした例である。これは、`options=keyValues`を使用した場合にNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:FlowInstrument:d447c3e2-3835-4bb9-80a3-8d4701a1396b",  
  "type": "FlowInstrument",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:0f95033a-db7c-4b6d-879a-60c29086ed63",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:cc0d4687-1f82-4e06-af21-c305c5002e8c",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:52a46d2f-3cb0-4dd0-ba5a-3c250d549475",  
    "urn:ngsi-ld:System:cd0c8606-a259-4a7b-ba37-5c7f482c48ac",  
    "urn:ngsi-ld:System:313373da-fa79-43b3-8fbb-84cb2cd36777"  
  ],  
  "hasManufacturer": "FlowInstrument Company Inc.",  
  "hasModel": "FlowInstrument 0.1.2",  
  "dateCreated": "2023-01-25T21:58:25Z",  
  "dateModified": "2023-01-25T20:06:56Z",  
  "source": "Import",  
  "name": "FlowInstrument",  
  "alternateName": "FlowInstrument type 2",  
  "description": "FlowInstrument of limited FlowInstrument types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### フローインスツルメント NGSI-LD 正規化例  
FlowInstrumentをJSON-LD形式で正規化した例を示す。これはオプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:FlowInstrument:410ba33d-1e01-45cd-aff7-00e43a13b5a3",  
  "type": "FlowInstrument",  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:3a053b81-b006-4f1c-8ece-a0b6ac287370"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:9e9a65e8-d47d-4a86-ab3b-f27e71079999"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:079c7aa5-a497-4294-97ce-d74d1f342d5f"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:300fb87b-d35b-409b-8201-96368defed80"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:7a99376b-7a65-45e5-8b81-515c9d9676ac"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "FlowInstrument Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "FlowInstrument 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T16:30:30Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T10:36:54Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "FlowInstrument"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "FlowInstrument type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "FlowInstrument of limited FlowInstrument types"  
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
