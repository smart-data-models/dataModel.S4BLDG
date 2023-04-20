<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティファン  
=========<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Fan/LICENSE.md)  
[文書が自動的に生成されます](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述です：**ファンは、気体に機械的な働きを与える装置である。ファンの典型的な使用方法は、ビルサービスの空気分配システムで空気の流れを誘導することです。  
バージョン：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性に型がない場合は、複数の型や異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: このアイテムの別称  - `areaServed[string]`: サービスまたは提供されるアイテムが提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `capacityControlType[string]`: プロパティInletVane（インレットベーン）：インレットベーンを調整することで制御します。VariableSpeedDrive（可変速ドライブ）：可変速駆動で制御する。BladePitchAngle：ブレードピッチアングル：ブレードピッチアングルを調整することで制御します。TwoSpeed（ツースピード高速と低速の切り替えで制御します。DischargeDamper（ディスチャージダンパー）：吐出ダンパーの調整で制御します。  - `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: このアイテムの説明  - `hasManufacturer[string]`: プロパティ。エンティティ（例：デバイス）の製造者を特定する関係。値は、文字列または言語タグ付き文字列であることが期待される。  - `hasModel[string]`: プロパティです。エンティティ（例：デバイス）のモデルを識別する関係。値は、文字列または言語タグ付き文字列であることが期待される。  - `id[*]`: エンティティの一意な識別子  - `isContainedInBuildingSpace[*]`: 関係。建物の物理的空間を定義するために使用されるエンティティ。ビルディングスペースは、デバイスまたはビルディングオブジェクトを含む。(ビルディングスペース)  - `isContainedInPhysicalObject[*]`: 関係です。適切な空間領域を持つあらゆるオブジェクト。  (DULオントロジーから抽出した定義）（PhysicalObject)  - `isSubSystemOf[array]`: 関係。この物理オブジェクトが属するシステム（複数可）への参照。  - `location[*]`: アイテムへの Geojson 参照。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon のいずれかとする。  - `motorDriveType[string]`: 特性です。モータードライブタイプ：DIRECTDRIVE：ダイレクトドライブ。BELTDRIVE：ベルトドライブ。COUPLING：カップリング。OTHER：その他のモータードライブタイプ。UNKNOWN：不明なモータードライブタイプ。  - `name[string]`: この項目の名称です。  - `nominalAirFlowRate[object]`: 特性です。空気の流れの公称速度。通常、m3/sで測定される。  - `nominalPowerRate[object]`: 特性。公称ファン出力率。通常、ワット（W、J/s）で測定されます。  - `nominalRotationSpeed[object]`: 特性です。ファンホイールの公称回転数。通常、サイクル/sで測定される。  - `nominalStaticPressure[object]`: 特性。設計された空気の循環を保証するために、ファンが克服しなければならない空気流内の静圧。通常、パスカル（Pa、N/m2）で測定される。  - `nominalTotalPressure[object]`: 特性。ファンを横切る公称総圧力上昇。通常パスカル（Pa、N/m2）で測定される。  - `operationMode[string]`: プロパティこのファンの動作モード。  - `operationTemperatureMax[object]`: 特性を示す。許容される動作周囲（空気、液体）温度範囲。通常、ケルビン（K）単位で測定される。  - `operationTemperatureMin[object]`: 特性を示す。許容される動作周囲（空気、液体）温度範囲。通常、ケルビン（K）単位で測定される。  - `operationalRiterial[object]`: 特性です。最大動作周囲空気温度での動作時間。秒（s）または日（d）または他の時間の単位で測定される。  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリストです。  - `seeAlso[*]`: アイテムに関する追加リソースを指す URI のリスト。  - `source[string]`: エンティティデータの元のソースをURLとして与える一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `type[string]`: プロパティです。これは `Fan` と等しくなければならない。  <!-- /30-PropertiesList -->  
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
Fan:    
  description: A fan is a device which imparts mechanical work on a gas. A typical usage of a fan is to induce airflow in a building services air distribution system.    
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
    capacityControlType:    
      description: 'Property. InletVane: Control by adjusting inlet vane. VariableSpeedDrive: Control by variable speed drive. BladePitchAngle: Control by adjusting blade pitch angle. TwoSpeed: Control by switch between high and low speed. DischargeDamper: Control by modulating discharge damper.'    
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
      anyOf: &fan_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      anyOf: *fan_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *fan_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *fan_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    motorDriveType:    
      description: 'Property. Motor drive type: DIRECTDRIVE: Direct drive. BELTDRIVE: Belt drive. COUPLING: Coupling. OTHER: Other type of motor drive. UNKNOWN: Unknown motor drive type. '    
      type: string    
      x-ngsi:    
        type: Property    
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
      properties: &fan_-_properties_-_nominalpowerrate_-_properties    
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
    nominalPowerRate:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: 'Property. Nominal fan power rate.Usually measured in Watts (W, J/s).'    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *fan_-_properties_-_nominalpowerrate_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    nominalRotationSpeed:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: Property. Nominal fan wheel speed. Usually measured in cycles/s.    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *fan_-_properties_-_nominalpowerrate_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    nominalStaticPressure:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: 'Property. The static pressure within the air stream that the fan must overcome to insure designed circulation of air. Usually measured in Pascals (Pa, N/m2).'    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *fan_-_properties_-_nominalpowerrate_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    nominalTotalPressure:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: 'Property. Nominal total pressure rise across the fan. Usually measured in Pascals (Pa, N/m2).'    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *fan_-_properties_-_nominalpowerrate_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    operationMode:    
      description: Property. Operation mode of this fan.    
      enum:    
        - supply    
        - exhaust    
      type: string    
      x-ngsi:    
        type: Property    
    operationTemperatureMax:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: 'Property. Allowable operation ambient (air, fluid) temperature range. Usually measured in degrees Kelvin (K).'    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *fan_-_properties_-_nominalpowerrate_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    operationTemperatureMin:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: 'Property. Allowable operation ambient (air, fluid) temperature range. Usually measured in degrees Kelvin (K).'    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *fan_-_properties_-_nominalpowerrate_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    operationalRiterial:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: Property. Time of operation at maximum operational ambient air temperature. Measured in seconds (s) or days (d) or other units of time.    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *fan_-_properties_-_nominalpowerrate_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *fan_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      description: Property. It must be equal to `Fan`.    
      enum:    
        - Fan    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Fan"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Fan/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Fan/schema.json    
  x-model-tags: SAREF Fan    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### ファンNGSI-v2キーバリュー例  
ここでは、JSON-LD形式でFanをkey-valuesとした例を示す。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Fan:7cfafc6e-ab2a-4af0-94b0-d4ed9c92e2d9",  
    "type": "Fan",  
    "capacityControlType": "e-markets",  
    "motorDriveType": "gold",  
    "nominalAirFlowRate": 0.5484285000109488,  
    "nominalPowerRate": 0.4651302623864956,  
    "nominalRotationSpeed": 0.586889938002957,  
    "nominalStaticPressure": 0.3508757713471129,  
    "nominalTotalPressure": 0.7008373891464377,  
    "operationalRiterial": 0.3901575132094196,  
    "operationMode": "supply",  
    "operationTemperatureMax": 0.9178812499585061,  
    "operationTemperatureMin": 0.5225885446624712,  
    "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:38fc3969-81c7-4c67-a564-fdbe6353726a",  
    "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:722ffa89-4091-423f-832c-3af82a48d406",  
    "isSubSystemOf": [  
        "urn:ngsi-ld:System:624b2008-bd0a-4bf6-98bd-a8fc2979af6b",  
        "urn:ngsi-ld:System:4096cc3a-d7c0-4491-b5e1-a0b97a8db924",  
        "urn:ngsi-ld:System:0dd0f326-6f31-4676-8996-7c591e57a81f"  
    ],  
    "hasManufacturer": "Fan Company Inc.",  
    "hasModel": "Fan 0.1.2",  
    "dateCreated": "2023-01-26T11:05:33Z",  
    "dateModified": "2023-01-26T13:15:57Z",  
    "source": "Import",  
    "name": "Fan",  
    "alternateName": "Fan type 2",  
    "description": "Fan of limited Fan types",  
    "dataProvider": "IFC file"  
}  
```  
</details>  
#### ファンNGSI-v2正規化例  
ここでは、JSON-LD形式のFanを正規化した例を示す。これは、オプションを使用しない場合のNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Fan:0da82317-969a-4395-8eb2-f98b9cd16de8",  
  "type": "Fan",  
  "capacityControlType": {  
    "type": "Text",  
    "value": "solutions"  
  },  
  "motorDriveType": {  
    "type": "Text",  
    "value": "hard drive"  
  },  
  "nominalAirFlowRate": {  
    "type": "Measurement",  
    "value": 0.3551507592337234  
  },  
  "nominalPowerRate": {  
    "type": "Measurement",  
    "value":  0.49309444253514245  
  },  
  "nominalRotationSpeed": {  
    "type": "Measurement",  
    "value":0.07199495596164263  
  },  
  "nominalStaticPressure": {  
    "type": "Measurement",  
    "value": 0.024615829657942068  
  },  
  "nominalTotalPressure": {  
    "type": "Measurement",  
    "value":  0.3030820859504  
  },  
  "operationalRiterial": {  
    "type": "Measurement",  
    "value":  0.21730931831819922  
  },  
  "operationMode": {  
    "type": "FanOperationMode",  
    "value": "supply"  
  },  
  "operationTemperatureMax": {  
    "type": "Measurement",  
    "value":0.6593703010837063  
  },  
  "operationTemperatureMin": {  
    "type": "Measurement",  
    "value":  0.23220611636698574  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:BuildingSpace:179a46d2-4adc-49bc-81ad-55bf8d570c04"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:PhysicalObject:1324382c-8a0d-4481-b501-20ced593647d"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:7bb675a4-c933-494f-9e7a-1ad7777c40c3"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:2122d54b-df0b-490a-8d2c-9611433a6950"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:bb112446-5445-482a-aacc-ca87dc610bd5"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Fan Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Fan 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T01:05:02.0601436+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T15:45:36.2919235+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Fan"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Fan type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Fan of limited Fan types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### ファンNGSI-LDのキーバリュー例  
ここでは、JSON-LD形式でFanをkey-valuesとする例を示す。これは、`options=keyValues`を使用した場合にNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Fan:7cfafc6e-ab2a-4af0-94b0-d4ed9c92e2d9",  
  "type": "Fan",  
  "capacityControlType": "e-markets",  
  "motorDriveType": "gold",  
  "nominalAirFlowRate": 0.5484285000109488,  
  "nominalPowerRate": 0.4651302623864956,  
  "nominalRotationSpeed": 0.586889938002957,  
  "nominalStaticPressure": 0.3508757713471129,  
  "nominalTotalPressure": 0.7008373891464377,  
  "operationalRiterial": 0.3901575132094196,  
  "operationMode": "supply",  
  "operationTemperatureMax": 0.9178812499585061,  
  "operationTemperatureMin": 0.5225885446624712,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:38fc3969-81c7-4c67-a564-fdbe6353726a",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:722ffa89-4091-423f-832c-3af82a48d406",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:624b2008-bd0a-4bf6-98bd-a8fc2979af6b",  
    "urn:ngsi-ld:System:4096cc3a-d7c0-4491-b5e1-a0b97a8db924",  
    "urn:ngsi-ld:System:0dd0f326-6f31-4676-8996-7c591e57a81f"  
  ],  
  "hasManufacturer": "Fan Company Inc.",  
  "hasModel": "Fan 0.1.2",  
  "dateCreated": "2023-01-26T11:05:33Z",  
  "dateModified": "2023-01-26T13:15:57Z",  
  "source": "Import",  
  "name": "Fan",  
  "alternateName": "Fan type 2",  
  "description": "Fan of limited Fan types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### ファン NGSI-LD 正規化例  
ここでは、JSON-LD形式のFanを正規化した例を示す。これはオプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Fan:77858a3b-1931-4dba-a9af-2eb53daaa2ba",  
  "type": "Fan",  
  "capacityControlType": {  
    "type": "Property",  
    "value": "Jamaica"  
  },  
  "motorDriveType": {  
    "type": "Property",  
    "value": "Handmade Rubber Pants"  
  },  
  "nominalAirFlowRate": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-25T20:05:36Z",  
    "value": 0.24193379349820043  
  },  
  "nominalPowerRate": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-26T00:02:52Z",  
    "value": 0.9909189253853895  
  },  
  "nominalRotationSpeed": {  
    "type": "Property",  
    "unitCode": "cycles/s",  
    "observedAt": "2023-01-25T18:57:22Z",  
    "value": 0.31786177757080614  
  },  
  "nominalStaticPressure": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-25T20:44:04Z",  
    "value": 0.9226814968179932  
  },  
  "nominalTotalPressure": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-26T08:36:40Z",  
    "value": 0.7120424039244743  
  },  
  "operationalRiterial": {  
    "type": "Property",  
    "unitCode": "time",  
    "observedAt": "2023-01-25T22:23:39Z",  
    "value": 0.858472652447435  
  },  
  "operationMode": {  
    "type": "Property",  
    "value": "supply"  
  },  
  "operationTemperatureMax": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T17:43:31Z",  
    "value": 0.6990158373086164  
  },  
  "operationTemperatureMin": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T22:43:03Z",  
    "value": 0.070852494560947  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:4e9dc2df-6361-4376-979d-fb3f96ba8a2f"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:d80ed04b-6f2d-45eb-bcf9-f94ed0564d8f"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:e79640ab-b497-40a8-b020-23d2799cdb87"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:9c3ebe76-cc20-45d1-b436-759778c41424"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:b8bb079a-9cb2-4f4e-8f22-2e5ecbc4a37e"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Fan Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Fan 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T01:34:08Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T12:21:35Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Fan"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Fan type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Fan of limited Fan types"  
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
