<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティSwitchingDevice（スイッチングデバイス  
================================<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/SwitchingDevice/LICENSE.md)  
[文書が自動的に生成されます](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述です：**スイッチは、ケーブル配電システム（電気回路）において、電気の流れを制御または変調するために使用されます。  スイッチには、電力、通信、オーディオビジュアル、または利用可能なポートによって決定されるその他の配電システムタイプに使用されるものが含まれる**。  
バージョン：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性に型がない場合は、複数の型や異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: このアイテムの別称  - `areaServed[string]`: サービスまたは提供されるアイテムが提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: このアイテムの説明  - `hasLock[boolean]`: 特性を示す。スイッチングデバイスにキー操作によるロックがあるか（＝TRUE）、ない（＝FALSE）かを示す表示。  - `hasManufacturer[string]`: プロパティ。エンティティ（例：デバイス）の製造者を特定する関係。値は、文字列または言語タグ付き文字列であることが期待される。  - `hasModel[string]`: プロパティです。エンティティ（例：デバイス）のモデルを識別する関係。値は、文字列または言語タグ付き文字列であることが期待される。  - `id[*]`: エンティティの一意な識別子  - `isContainedInBuildingSpace[*]`: 関係。建物の物理的空間を定義するために使用されるエンティティ。ビルディングスペースは、デバイスまたはビルディングオブジェクトを含む。(ビルディングスペース)  - `isContainedInPhysicalObject[*]`: 関係です。適切な空間領域を持つあらゆるオブジェクト。  (DULオントロジーから抽出した定義）（PhysicalObject)  - `isIlluminated[boolean]`: 特性を示す。スイッチがオンであることを示す点灯表示（＝TRUE）か、そうでないことを示す点灯表示（＝FALSE）かを示す。  - `isSubSystemOf[array]`: 関係。この物理オブジェクトが属するシステム（複数可）への参照。  - `legend[string]`: 特性を示す。目的または機能を示すために、凡例としてスイッチに刻まれ、または適用されるテキスト。  - `location[*]`: アイテムへの Geojson 参照。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon のいずれかである。  - `name[string]`: この項目の名称です。  - `numberOfGangs[number]`: プロパティです。このスイッチのギャング/ボタンの数。  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリストです。  - `seeAlso[*]`: アイテムに関する追加リソースを指す URI のリスト。  - `source[string]`: エンティティデータの元のソースをURLとして与える一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `switchFunction[string]`: 特性です。機能的に異なるスイッチの種類を示す。  - `type[string]`: プロパティを指定します。SwitchingDevice`と等しくなければならない。  <!-- /30-PropertiesList -->  
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
SwitchingDevice:    
  description: 'A switch is used in a cable distribution system (electrical circuit) to control or modulate the flow of electricity.  Switches include those used for electrical power, communications, audio-visual, or other distribution system types as determined by the available ports.'    
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
    hasLock:    
      description: Property. Indication of whether a switching device has a key operated lock (=TRUE) or not (= FALSE).    
      type: boolean    
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
      anyOf: &switchingdevice_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      anyOf: *switchingdevice_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *switchingdevice_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isIlluminated:    
      description: Property. An indication of whether there is an illuminated indicator to show that the switch is on (=TRUE) or not (= FALSE).    
      type: boolean    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *switchingdevice_-_properties_-_iscontainedinbuildingspace_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Relationship    
    legend:    
      description: Property. A text inscribed or applied to the switch as a legend to indicate purpose or function.    
      type: string    
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
    numberOfGangs:    
      description: Property. Number of gangs/buttons on this switch.    
      type: number    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *switchingdevice_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    switchFunction:    
      description: Property. Indicates types of switches which differs in functionality.    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: Property. It must be equal to `SwitchingDevice`.    
      enum:    
        - SwitchingDevice    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:SwitchingDevice"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/SwitchingDevice/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/SwitchingDevice/schema.json    
  x-model-tags: SAREF SwitchingDevice    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### SwitchingDevice NGSI-v2 キー値例  
SwitchingDeviceをJSON-LD形式でkey-valuesとした例を示します。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SwitchingDevice:d8e17d30-bfcb-4ad1-9818-243476f0ff19",  
  "type": "SwitchingDevice",  
  "hasLock": false,  
  "isIlluminated": false,  
  "legend": "scalable",  
  "numberOfGangs": 0.544077071366429,  
  "switchFunction": "Buckinghamshire",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:c7530605-2247-4bde-ae54-4a47f12ef77e",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:b3524873-2c7c-4957-b565-c6960afb249f",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:d464a297-36d2-48a5-b3de-b2ed2acbe8a5",  
    "urn:ngsi-ld:System:a503eea6-3293-4436-bda0-547c41cbfa32",  
    "urn:ngsi-ld:System:74c732c2-46a0-491d-8f69-d716f2fb2290"  
  ],  
  "hasManufacturer": "SwitchingDevice Company Inc.",  
  "hasModel": "SwitchingDevice 0.1.2",  
  "dateCreated": "2023-01-26T11:11:18Z",  
  "dateModified": "2023-01-26T13:36:28Z",  
  "source": "Import",  
  "name": "SwitchingDevice",  
  "alternateName": "SwitchingDevice type 2",  
  "description": "SwitchingDevice of limited SwitchingDevice types",  
  "dataProvider": "IFC file"  
}  
```  
</details>  
#### SwitchingDevice NGSI-v2 正規化例  
SwitchingDeviceをJSON-LD形式で正規化した例を示します。これは、オプションを使用しない場合のNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SwitchingDevice:70a299ac-a0dc-41dd-8435-1bf5894318b7",  
  "type": "SwitchingDevice",  
  "hasLock": {  
    "type": "Boolean",  
    "value": false  
  },  
  "isIlluminated": {  
    "type": "Boolean",  
    "value": false  
  },  
  "legend": {  
    "type": "Text",  
    "value": "azure"  
  },  
  "numberOfGangs": {  
    "type": "Float",  
    "value": 0.7570991778458094  
  },  
  "switchFunction": {  
    "type": "Text",  
    "value": "Pennsylvania"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:BuildingSpace:fd192f21-f024-44c0-a65e-f4c6496b90db"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:PhysicalObject:12cc4e62-5aae-40e4-8ec3-cf7d03428278"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:39fdf781-f35a-4371-a82b-12e07350d2f9"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:637cc212-2eeb-4b81-abb9-5a9004e2c306"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:f2b36833-fcb4-42c0-9f65-dbecee562bfc"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "SwitchingDevice Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "SwitchingDevice 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T14:36:12.8047906+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T14:13:46.8572673+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "SwitchingDevice"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "SwitchingDevice type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "SwitchingDevice of limited SwitchingDevice types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### SwitchingDevice NGSI-LD キー値例  
ここでは、SwitchingDeviceをJSON-LD形式でkey-valuesとした例を示します。これは、`options=keyValues`を使用した場合にNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SwitchingDevice:00b594ac-3494-4b6f-8a5b-c4882d204cae",  
  "type": "SwitchingDevice",  
  "hasLock": true,  
  "isIlluminated": false,  
  "legend": "collaborative",  
  "numberOfGangs": 0.541629847213168,  
  "switchFunction": "Bermudian Dollar customarily known as Bermuda Dollar",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:1bd1de21-886b-4ddb-9330-64c8e5a08f50",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:1caf12ed-a715-4d64-bec7-a325e6d6b0dd",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:9d61eceb-dc6f-4bfd-8068-218f5999f951",  
    "urn:ngsi-ld:System:0e6df523-0bcf-4433-b7ea-edc645e46410",  
    "urn:ngsi-ld:System:749d7847-f7f9-42a7-b3aa-8be01f7f2892"  
  ],  
  "hasManufacturer": "SwitchingDevice Company Inc.",  
  "hasModel": "SwitchingDevice 0.1.2",  
  "dateCreated": "2023-01-25T22:22:20Z",  
  "dateModified": "2023-01-26T04:25:27Z",  
  "source": "Import",  
  "name": "SwitchingDevice",  
  "alternateName": "SwitchingDevice type 2",  
  "description": "SwitchingDevice of limited SwitchingDevice types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### SwitchingDevice NGSI-LD 正規化例  
SwitchingDeviceをJSON-LD形式で正規化した例を示します。これはオプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SwitchingDevice:89173dc8-f726-4b8f-81dc-37dcc5d475f0",  
  "type": "SwitchingDevice",  
  "hasLock": {  
    "type": "Property",  
    "value": false  
  },  
  "isIlluminated": {  
    "type": "Property",  
    "value": false  
  },  
  "legend": {  
    "type": "Property",  
    "value": "back up"  
  },  
  "numberOfGangs": {  
    "type": "Property",  
    "value": 0.5828729445432342  
  },  
  "switchFunction": {  
    "type": "Property",  
    "value": "West Virginia"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:beccbf7b-2aa0-4dc1-adf3-42054cc2e91e"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:61dd8c81-0312-45b3-9124-b583cb813cdf"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:11496c39-7ff1-49ea-8a5c-5bc46ecd6d51"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:93fc5f6f-03b4-4f6c-a339-8cb30d5a504d"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:3ca1ea38-b73c-4731-aaa1-0c050dac66a9"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "SwitchingDevice Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "SwitchingDevice 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T01:16:50Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T03:54:22Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "SwitchingDevice"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "SwitchingDevice type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "SwitchingDevice of limited SwitchingDevice types"  
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
