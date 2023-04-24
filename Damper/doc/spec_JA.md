<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティダンパー  
==========<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Damper/LICENSE.md)  
[文書が自動的に生成されます](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述です：**ダンパーは、通常、HVACダクト分配システムに参加し、空気の流れを制御または調節するために使用されます。  
バージョン：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性に型がない場合は、複数の型や異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `airFlowRateMax[number]`: 特性です。最大許容空気流量のこと。通常、m3/sで測定される。  - `alternateName[string]`: このアイテムの別称  - `areaServed[string]`: サービスまたは提供されるアイテムが提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `bladeAction[string]`: 特性です。ブレードアクション。  - `bladeEdge[string]`: 特性です。ブレードエッジです。  - `bladeShape[string]`: 特性です。ブレードの形状です。フラットとは3重のV溝を意味します。  - `bladeThickness[number]`: 特性です。ダンパーブレードの厚さです。通常、ミリメートル（mm）単位で測定される。  - `closeOffRating[number]`: プロパティです。クローズオフ定格。通常、パスカル（Pa、N/m2）で測定される。  - `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: このアイテムの説明  - `faceArea[number]`: 特性です。気流に開放されたフェイス面積。通常、平方メートル（m2）単位で測定される。  - `frameDepth[number]`: 特性。ダンパーフレームの長さ（または奥行き）です。通常、ミリメートル（mm）単位で測定される。  - `frameThickness[number]`: 特性を示す。ダンパーフレームの素材の厚さ。通常、ミリメートル（mm）単位で測定される。  - `frameType[string]`: 特性を示す。ダンパーが使用するフレームの種類（例：標準、シングルフランジ、シングル逆フランジ、ダブルフランジなど）。  - `hasManufacturer[string]`: プロパティ。エンティティ（例：デバイス）の製造者を特定する関係。値は、文字列または言語タグ付き文字列であることが期待される。  - `hasModel[string]`: プロパティです。エンティティ（例：デバイス）のモデルを識別する関係。値は、文字列または言語タグ付き文字列であることが期待される。  - `id[*]`: エンティティの一意な識別子  - `isContainedInBuildingSpace[*]`: 関係。建物の物理的空間を定義するために使用されるエンティティ。ビルディングスペースは、デバイスまたはビルディングオブジェクトを含む。(ビルディングスペース)  - `isContainedInPhysicalObject[*]`: 関係です。適切な空間領域を持つあらゆるオブジェクト。  (DULオントロジーから抽出した定義）（PhysicalObject)  - `isSubSystemOf[array]`: 関係。この物理オブジェクトが属するシステム（複数可）への参照。  - `leakageFullyClosed[number]`: 特性です。全閉時のリーク量。通常、m3/sで測定される。  - `location[*]`: アイテムへの Geojson 参照。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon のいずれかである。  - `name[string]`: この項目の名称です。  - `nominalAirFlowRate[number]`: 特性です。空気の流れの公称速度。通常、m3/sで測定される。  - `numberOfBlades[number]`: 特性です。ブレードの数。  - `openPressureDrop[number]`: 特性です。ダンパーを横切る総圧力損失。通常パスカル（Pa、N/m2）で測定される。  - `operation[string]`: 特性です。ダンパー操作の操作機構。  - `operationMode[string]`: 特性です。本ダンパーの動作モード。  - `operationTemperatureMax[number]`: 特性を示す。許容される動作周囲（空気、液体）温度範囲。通常、ケルビン（K）単位で測定される。  - `operationTemperatureMin[number]`: 特性を示す。許容される動作周囲（空気、液体）温度範囲。通常、ケルビン（K）単位で測定される。  - `orientation[string]`: 特性を有する。メーカーが指定するダンパーの意図する方向。  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリストです。  - `seeAlso[*]`: アイテムに関する追加リソースを指す URI のリスト。  - `source[string]`: エンティティデータの元のソースをURLとして与える一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `temperatureRating[number]`: 特性です。温度定格。通常、ケルビン（K）単位で測定される。  - `type[string]`: プロパティです。Damper`と等しくなければならない。  - `workingPressureMax[number]`: 特性です。最高使用圧力。通常パスカル（Pa、N/m2）で測定される。  <!-- /30-PropertiesList -->  
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
Damper:    
  description: A damper typically participates in an HVAC duct distribution system and is used to control or modulate the flow of air.    
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
    airFlowRateMax:    
      description: Property. Maximum allowable air flow rate. Usually measured in m3/s.    
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
    bladeAction:    
      description: Property. Blade action.    
      type: string    
      x-ngsi:    
        type: Property    
    bladeEdge:    
      description: Property. Blade edge.    
      type: string    
      x-ngsi:    
        type: Property    
    bladeShape:    
      description: Property. Blade shape. Flat means triple V-groove.    
      type: string    
      x-ngsi:    
        type: Property    
    bladeThickness:    
      description: Property. The thickness of the damper blade. Usually measured in millimeters (mm).    
      type: number    
      x-ngsi:    
        type: Property    
    closeOffRating:    
      description: 'Property. Close off rating. Usually measured in Pascals (Pa, N/m2).'    
      type: number    
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
    faceArea:    
      description: Property. Face area open to the airstream. Usually measured in square metre (m2).    
      type: number    
      x-ngsi:    
        type: Property    
    frameDepth:    
      description: Property. The length (or depth) of the damper frame. Usually measured in millimeters (mm).    
      type: number    
      x-ngsi:    
        type: Property    
    frameThickness:    
      description: Property. The thickness of the damper frame material. Usually measured in millimeters (mm).    
      type: number    
      x-ngsi:    
        type: Property    
    frameType:    
      description: 'Property. The type of frame used by the damper (e.g., Standard, Single Flange, Single Reversed Flange, Double Flange, etc.).'    
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
      anyOf: &damper_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      anyOf: *damper_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *damper_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *damper_-_properties_-_iscontainedinbuildingspace_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Relationship    
    leakageFullyClosed:    
      description: Property. Leakage when fully closed. Usually measured in m3/s.    
      type: number    
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
    nominalAirFlowRate:    
      description: Property. Nominal rate of air flow. Usually measured in m3/s.    
      type: number    
      x-ngsi:    
        type: Property    
    numberOfBlades:    
      description: Property. Number of blades.    
      type: number    
      x-ngsi:    
        type: Property    
    openPressureDrop:    
      description: 'Property. Total pressure drop across damper. Usually measured in Pascals (Pa, N/m2).'    
      type: number    
      x-ngsi:    
        type: Property    
    operation:    
      description: Property. The operational mechanism for the damper operation.    
      type: string    
      x-ngsi:    
        type: Property    
    operationMode:    
      description: Property. Operation mode of this damper.    
      enum:    
        - supply    
        - exhaust    
      type: string    
      x-ngsi:    
        type: Property    
    operationTemperatureMax:    
      description: 'Property. Allowable operation ambient (air, fluid) temperature range. Usually measured in degrees Kelvin (K).'    
      type: number    
      x-ngsi:    
        type: Property    
    operationTemperatureMin:    
      description: 'Property. Allowable operation ambient (air, fluid) temperature range. Usually measured in degrees Kelvin (K).'    
      type: number    
      x-ngsi:    
        type: Property    
    orientation:    
      description: Property. The intended orientation for the damper as specified by the manufacturer.    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *damper_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    temperatureRating:    
      description: Property. Temperature rating. Usually measured in degrees Kelvin (K).    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: Property. It must be equal to `Damper`.    
      enum:    
        - Damper    
      type: string    
      x-ngsi:    
        type: Property    
    workingPressureMax:    
      description: 'Property. Maximum working pressure. Usually measured in Pascals (Pa, N/m2).'    
      type: number    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Damper"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Damper/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Damper/schema.json    
  x-model-tags: SAREF Damper    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### ダンパーNGSI-v2キーバリュー例  
ここでは、DamperをJSON-LD形式でkey-valuesとした例を示す。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Damper:65c94159-bfe6-416d-b02c-283479048fe3",  
  "type": "Damper",  
  "airFlowRateMax": 0.5927918101987754,  
  "bladeAction": "Belize Dollar",  
  "bladeEdge": "frictionless",  
  "bladeShape": "intermediate",  
  "bladeThickness": 0.5665758025960763,  
  "closeOffRating": 0.8924252696459434,  
  "faceArea": 0.45839947738381925,  
  "frameDepth": 0.6687870848219263,  
  "frameThickness": 0.6594470368135407,  
  "frameType": "Ergonomic",  
  "leakageFullyClosed": 0.052627216627954665,  
  "nominalAirFlowRate": 0.7333602290466408,  
  "numberOfBlades": 0.3476917428528077,  
  "openPressureDrop": 0.8991384789588308,  
  "operation": "Implemented",  
  "operationMode": "supply",  
  "operationTemperatureMax": 0.07772736087657628,  
  "operationTemperatureMin": 0.4857292385786113,  
  "orientation": "reboot",  
  "temperatureRating": 0.4909792118139581,  
  "workingPressureMax": 0.10839736205746486,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:c25bebe3-d546-4942-be72-9468ce218070",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:326da1c1-440d-4200-b598-a84e3bf5fdc1",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:007e61a9-027a-4662-a7a0-1e9e48f57886",  
    "urn:ngsi-ld:System:59945456-4e66-4c84-b637-7c771479a9f3",  
    "urn:ngsi-ld:System:023e0706-8d3d-411b-9e97-994a870341cd"  
  ],  
  "hasManufacturer": "Damper Company Inc.",  
  "hasModel": "Damper 0.1.2",  
  "dateCreated": "2023-01-25T18:10:59Z",  
  "dateModified": "2023-01-26T07:49:53Z",  
  "source": "Import",  
  "name": "Damper",  
  "alternateName": "Damper type 2",  
  "description": "Damper of limited Damper types",  
  "dataProvider": "IFC file"  
}  
```  
</details>  
#### ダンパー NGSI-v2 正規化例  
以下は、正規化されたJSON-LD形式のDamperの例である。これは、オプションを使用しない場合のNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Damper:30830dab-6aa5-4dd1-9e48-d6ac7e24e4bf",  
  "type": "Damper",  
  "airFlowRateMax": {  
    "type": "Measurement",  
    "value":  0.13813389168852752  
  },  
  "bladeAction": {  
    "type": "Text",  
    "value": "Spur"  
  },  
  "bladeEdge": {  
    "type": "Text",  
    "value": "Personal Loan Account"  
  },  
  "bladeShape": {  
    "type": "Text",  
    "value": "Human"  
  },  
  "bladeThickness": {  
    "type": "Measurement",  
    "value":  0.35230461364031296  
  },  
  "closeOffRating": {  
    "type": "Measurement",  
    "value":  0.171775838539866  
  },  
  "faceArea": {  
    "type": "Measurement",  
    "value": 0.4212393478883142  
  },  
  "frameDepth": {  
    "type": "Measurement",  
    "value": 0.8035081586701794  
  },  
  "frameThickness": {  
    "type": "Measurement",  
    "value":  0.28946308913206176  
  },  
  "frameType": {  
    "type": "Text",  
    "value": "Balanced"  
  },  
  "leakageFullyClosed": {  
    "type": "Measurement",  
    "value":  0.44075236436472953  
  },  
  "nominalAirFlowRate": {  
    "type": "Measurement",  
    "value":0.47305378645729657  
  },  
  "numberOfBlades": {  
    "type": "Float",  
    "value": 0.8083872561368712  
  },  
  "openPressureDrop": {  
    "type": "Measurement",  
    "value": 0.9106213284285767  
  },  
  "operation": {  
    "type": "Text",  
    "value": "Handcrafted Concrete Computer"  
  },  
  "operationMode": {  
    "type": "DamperOperationMode",  
    "value": "supply"  
  },  
  "operationTemperatureMax": {  
    "type": "Measurement",  
    "value":  0.87576324331876  
  },  
  "operationTemperatureMin": {  
    "type": "Measurement",  
    "value":  0.3952529455728351  
  },  
  "orientation": {  
    "type": "Text",  
    "value": "Mozambique"  
  },  
  "temperatureRating": {  
    "type": "Measurement",  
    "value":  0.43326401348250587  
  },  
  "workingPressureMax": {  
    "type": "Measurement",  
    "value":  0.2695729035947665  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:BuildingSpace:f19ff450-12f4-472a-985e-40b163530ccd"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:PhysicalObject:ee6c23f3-7261-4807-b3e3-703588646f02"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:a8f8f637-52c0-491d-890e-2806ffbdc6cd"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:7f5f939e-9a41-4ca6-95ff-4ece8ffec42c"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:ff7924ea-c532-40c9-a1ac-449c76216073"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Damper Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Damper 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T15:13:23.9679787+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T16:00:58.1902016+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Damper"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Damper type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Damper of limited Damper types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### ダンパーNGSI-LDキーバリュ-例  
ここでは、DamperをJSON-LD形式でkey-valuesとした例を示します。これは `options=keyValues` を使用した場合に NGSI-LD と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Damper:65c94159-bfe6-416d-b02c-283479048fe3",  
  "type": "Damper",  
  "airFlowRateMax": 0.5927918101987754,  
  "bladeAction": "Belize Dollar",  
  "bladeEdge": "frictionless",  
  "bladeShape": "intermediate",  
  "bladeThickness": 0.5665758025960763,  
  "closeOffRating": 0.8924252696459434,  
  "faceArea": 0.45839947738381925,  
  "frameDepth": 0.6687870848219263,  
  "frameThickness": 0.6594470368135407,  
  "frameType": "Ergonomic",  
  "leakageFullyClosed": 0.052627216627954665,  
  "nominalAirFlowRate": 0.7333602290466408,  
  "numberOfBlades": 0.3476917428528077,  
  "openPressureDrop": 0.8991384789588308,  
  "operation": "Implemented",  
  "operationMode": "supply",  
  "operationTemperatureMax": 0.07772736087657628,  
  "operationTemperatureMin": 0.4857292385786113,  
  "orientation": "reboot",  
  "temperatureRating": 0.4909792118139581,  
  "workingPressureMax": 0.10839736205746486,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:c25bebe3-d546-4942-be72-9468ce218070",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:326da1c1-440d-4200-b598-a84e3bf5fdc1",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:007e61a9-027a-4662-a7a0-1e9e48f57886",  
    "urn:ngsi-ld:System:59945456-4e66-4c84-b637-7c771479a9f3",  
    "urn:ngsi-ld:System:023e0706-8d3d-411b-9e97-994a870341cd"  
  ],  
  "hasManufacturer": "Damper Company Inc.",  
  "hasModel": "Damper 0.1.2",  
  "dateCreated": "2023-01-25T18:10:59Z",  
  "dateModified": "2023-01-26T07:49:53Z",  
  "source": "Import",  
  "name": "Damper",  
  "alternateName": "Damper type 2",  
  "description": "Damper of limited Damper types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### ダンパー NGSI-LD 正規化例  
以下は、正規化されたJSON-LD形式のDamperの例である。これはオプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Damper:99cb9b35-5f17-4e4d-89bb-e9d7bb88c2ba",  
  "type": "Damper",  
  "airFlowRateMax": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-26T10:15:08Z",  
    "value": 0.46010915943742847  
  },  
  "bladeAction": {  
    "type": "Property",  
    "value": "microchip"  
  },  
  "bladeEdge": {  
    "type": "Property",  
    "value": "Village"  
  },  
  "bladeShape": {  
    "type": "Property",  
    "value": "Netherlands Antillian Guilder"  
  },  
  "bladeThickness": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-25T21:36:37Z",  
    "value": 0.5214778377905084  
  },  
  "closeOffRating": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-25T18:21:40Z",  
    "value": 0.8241451329002358  
  },  
  "faceArea": {  
    "type": "Property",  
    "unitCode": "m2",  
    "observedAt": "2023-01-25T20:36:04Z",  
    "value": 0.6197704906516315  
  },  
  "frameDepth": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T14:05:58Z",  
    "value": 0.19371235604272175  
  },  
  "frameThickness": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-25T21:48:43Z",  
    "value": 0.630746648821536  
  },  
  "frameType": {  
    "type": "Property",  
    "value": "SAS"  
  },  
  "leakageFullyClosed": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-25T21:59:27Z",  
    "value": 0.8430168839934075  
  },  
  "nominalAirFlowRate": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-26T06:30:50Z",  
    "value": 0.8419372074040988  
  },  
  "numberOfBlades": {  
    "type": "Property",  
    "value": 0.2730424937241438  
  },  
  "openPressureDrop": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-26T04:03:50Z",  
    "value": 0.25493844227297535  
  },  
  "operation": {  
    "type": "Property",  
    "value": "partnerships"  
  },  
  "operationMode": {  
    "type": "Property",  
    "value": "exhaust"  
  },  
  "operationTemperatureMax": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T22:15:50Z",  
    "value": 0.4402985682699154  
  },  
  "operationTemperatureMin": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T11:49:40Z",  
    "value": 0.0015019955460002787  
  },  
  "orientation": {  
    "type": "Property",  
    "value": "Metrics"  
  },  
  "temperatureRating": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T16:28:22Z",  
    "value": 0.6012606116766228  
  },  
  "workingPressureMax": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-26T09:39:16Z",  
    "value": 0.320862748056973  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:573f5e7a-806c-4deb-878c-365ef09fe4d2"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:0cbecfb0-1008-4c54-99f6-510fba847457"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:972e3b8b-9613-4b3a-a798-f3e56587d999"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:0d09725f-1468-4352-92e9-39d0b647a683"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:0c5bf106-93a0-4eb9-a15d-a0d834088c94"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Damper Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Damper 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T10:37:53Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T10:42:54Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Damper"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Damper type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Damper of limited Damper types"  
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
