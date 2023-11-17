<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
エンティティスペースヒーター    
==============<!-- /10-Header -->    
<!-- 15-License -->    
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/SpaceHeater/LICENSE.md)    
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
グローバルな説明**スペースヒーターは、電気、蒸気、温水などの熱源を利用し、輻射や自然対流を組み合わせて、限られた空間や面積を暖める。スペースヒーターの例としては、ラジエーター、コンベクター、ベースボード、フィン付チューブヒーターなどがある。  UnitaryEquipmentは、暖房、冷房、および／または除湿の組み合わ せをサポートするパッケージ型ユニットに使用されるべきである。Coilは、コ イルベースの床暖房に使用されるべきである。    
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
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `bodyMass[number]`: ヒーター全体の質量。通常、キログラム（kg）またはグラム（g）で測定される。  - `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `energySource[string]`: エネルギー源。熱を発生させるために燃焼されるエネルギー源または燃料を定義する列挙。  - `hasManufacturer[string]`: エンティティ（デバイスなど）の製造者を特定する関係。値は文字列または言語タグを持つ文字列であることが期待される。  - `hasModel[string]`: エンティティ（デバイスなど）のモデルを識別する関係。値は、文字列または言語タグを持つ文字列であることが期待される。  - `heatTransferDimension[string]`: スペースヒーターの形状による熱の伝わり方を示す。  - `heatTransferMedium[string]`: 熱媒体を定義する列挙（該当する場合  - `id[*]`: エンティティの一意識別子  - `isContainedInBuildingSpace[*]`: 建物の物理的空間を定義するために使用されるエンティティ。ビルディングスペースには、デバイスまたはビルディングオブジェクトが含まれる。(ビルディングスペース)  - `isContainedInPhysicalObject[*]`: 適切な空間領域を持つオブジェクト。  (DUL オントロジーより定義） （PhysicalObject）  - `isSubSystemOf[array]`: この物理オブジェクトが属するシステムへの参照。  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `name[string]`: このアイテムの名前  - `numberOfPanels[number]`: パネル数  - `numberOfSections[number]`: 使用セクション数  - `outputCapacity[number]`: メーカーが表示する公称熱出力の合計。通常、単位はワット（W、J/s）。  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `placementType[string]`: デバイスがどのように配置されるように設計されているかを示す  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `temperatureClassification[string]`: 低温 - 表面温度が比較的低く、通常は温水または電気で加熱される。 高温 - 表面温度が比較的高く、通常はガスまたは蒸気で加熱される。  - `thermalEfficiency[number]`: 総合熱効率は、熱伝達装置の総エネルギー出力をエネルギー入力で割ったものと定義される。  - `thermalMassHeatCapacity[number]`: 成分の質量と比熱の積  - `type[string]`: これは `SpaceHeater` と等しくなければならない。  <!-- /30-PropertiesList -->    
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
SpaceHeater:      
  description: 'Space heaters utilize a combination of radiation and/or natural convection using a heating source such as electricity, steam or hot water to heat a limited space or area. Examples of space heaters include radiators, convectors, baseboard and finned-tube heaters.  UnitaryEquipment should be used for packaged units supporting a combination of heating, cooling, and/or dehumidification; Coil should be used for coil-based floor heating.'      
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
    bodyMass:      
      description: Overall body mass of the heater. Usually measured in kilograms (kg) or grams (g)      
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
    energySource:      
      description: The source of energy. Enumeration defining the energy source or fuel cumbusted to generate heat      
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
    heatTransferDimension:      
      description: Indicates how heat is transmitted according to the shape of the space heater      
      type: string      
      x-ngsi:      
        type: Property      
    heatTransferMedium:      
      description: Enumeration defining the heat transfer medium if applicable      
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
    numberOfPanels:      
      description: Number of panels      
      type: number      
      x-ngsi:      
        type: Property      
    numberOfSections:      
      description: Number of sections used      
      type: number      
      x-ngsi:      
        type: Property      
    outputCapacity:      
      description: 'Total nominal heat output as listed by the manufacturer. Usually measured in Watts (W, J/s)'      
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
    placementType:      
      description: Indicates how the device is designed to be placed      
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
    temperatureClassification:      
      description: 'Enumeration defining the temperature classification of the space heater surface temperature. low temperature - surface temperature is relatively low, usually heated by hot water or electricity. high temperature - surface temperature is relatively high, usually heated by gas or steam'      
      type: string      
      x-ngsi:      
        type: Property      
    thermalEfficiency:      
      description: Overall Thermal Efficiency is defined as gross energy output of the heat transfer device divided by the energy input      
      type: number      
      x-ngsi:      
        type: Property      
    thermalMassHeatCapacity:      
      description: Product of component mass and specific heat      
      type: number      
      x-ngsi:      
        type: Property      
    type:      
      description: It must be equal to `SpaceHeater`      
      enum:      
        - SpaceHeater      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:SpaceHeater"      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/SpaceHeater/LICENSE.md      
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/SpaceHeater/schema.json      
  x-model-tags: SAREF SpaceHeater      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## ペイロードの例    
#### SpaceHeater NGSI-v2 キー値の例    
JSON-LD形式のSpaceHeaterのkey-valuesの例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:SpaceHeater:53d2376a-08be-43df-8614-5b506356b56b",  
  "type": "SpaceHeater",  
  "bodyMass": 0.2211394720882921,  
  "energySource": "Research",  
  "heatTransferDimension": "Sleek Rubber Chicken",  
  "heatTransferMedium": "calculating",  
  "numberOfPanels": 0.9912166099910465,  
  "numberOfSections": 0.10463526586778538,  
  "outputCapacity": 0.6425343578878625,  
  "placementType": "auxiliary",  
  "temperatureClassification": "haptic",  
  "thermalEfficiency": 0.996207265881601,  
  "thermalMassHeatCapacity": 0.42035461371680216,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:a23ba52c-ee89-44f3-8146-cc5642b8a5d4",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:da56307c-a927-4d61-bc78-329cf0c45486",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:8c588da8-ae9d-4339-b35e-3f621435ba77",  
    "urn:ngsi-ld:System:75045902-8a40-4a47-91ed-b55c98c26a56",  
    "urn:ngsi-ld:System:59e00885-77e1-4d66-9c7c-c3d0b2be5b30"  
  ],  
  "hasManufacturer": "SpaceHeater Company Inc.",  
  "hasModel": "SpaceHeater 0.1.2",  
  "dateCreated": "2023-01-26T11:00:53Z",  
  "dateModified": "2023-01-25T20:46:44Z",  
  "source": "Import",  
  "name": "SpaceHeater",  
  "alternateName": "SpaceHeater type 2",  
  "description": "SpaceHeater of limited SpaceHeater types",  
  "dataProvider": "IFC file"  
}  
```  
</details>    
#### スペースヒーター NGSI-v2 正規化例    
以下は、正規化されたJSON-LDフォーマットのSpaceHeaterの例である。これはNGSI-v2と互換性があり、オプションを使用しない場合、個々のエンティティのコンテキストデータを返します。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:SpaceHeater:b256e328-b21f-4f37-bcb4-d78364993e79",  
  "type": "SpaceHeater",  
  "bodyMass": {  
    "type": "Number",  
    "value": 0.7643146073425459  
  },  
  "energySource": {  
    "type": "Text",  
    "value": "Facilitator"  
  },  
  "heatTransferDimension": {  
    "type": "Text",  
    "value": "program"  
  },  
  "heatTransferMedium": {  
    "type": "Text",  
    "value": "Assurance"  
  },  
  "numberOfPanels": {  
    "type": "Number",  
    "value": 0.8127498709428745  
  },  
  "numberOfSections": {  
    "type": "Number",  
    "value": 0.8692658014070345  
  },  
  "outputCapacity": {  
    "type": "Number",  
    "value": 0.2717042496203792  
  },  
  "placementType": {  
    "type": "Text",  
    "value": "back up"  
  },  
  "temperatureClassification": {  
    "type": "Text",  
    "value": "SMTP"  
  },  
  "thermalEfficiency": {  
    "type": "Number",  
    "value": 0.16328303516805232  
  },  
  "thermalMassHeatCapacity": {  
    "type": "Number",  
    "value": 0.17753659327247795  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:BuildingSpace:c1f57310-b1ad-4a70-bdca-70f74bbcc002"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:PhysicalObject:e22ae82c-83a1-4ed9-b1f8-eeced3ba17d9"  
  },  
  "isSubSystemOf": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:System:6f519e2b-416a-4b2a-af7b-56974a5d00df",  
      "urn:ngsi-ld:System:16199b91-8c55-4645-8c14-536d1dff0fcc",  
      "urn:ngsi-ld:System:5526ed19-a6fa-4e22-a8bd-71a1027a9b02"  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "SpaceHeater Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "SpaceHeater 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T01:19:34.4200755+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T00:26:07.2902986+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "SpaceHeater"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "SpaceHeater type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "SpaceHeater of limited SpaceHeater types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>    
#### スペースヒーター NGSI-LD キー値の例    
JSON-LD形式のSpaceHeaterのkey-valuesの例です。options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返す。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:SpaceHeater:53d2376a-08be-43df-8614-5b506356b56b",  
  "type": "SpaceHeater",  
  "bodyMass": 0.2211394720882921,  
  "energySource": "Research",  
  "heatTransferDimension": "Sleek Rubber Chicken",  
  "heatTransferMedium": "calculating",  
  "numberOfPanels": 0.9912166099910465,  
  "numberOfSections": 0.10463526586778538,  
  "outputCapacity": 0.6425343578878625,  
  "placementType": "auxiliary",  
  "temperatureClassification": "haptic",  
  "thermalEfficiency": 0.996207265881601,  
  "thermalMassHeatCapacity": 0.42035461371680216,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:a23ba52c-ee89-44f3-8146-cc5642b8a5d4",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:da56307c-a927-4d61-bc78-329cf0c45486",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:8c588da8-ae9d-4339-b35e-3f621435ba77",  
    "urn:ngsi-ld:System:75045902-8a40-4a47-91ed-b55c98c26a56",  
    "urn:ngsi-ld:System:59e00885-77e1-4d66-9c7c-c3d0b2be5b30"  
  ],  
  "hasManufacturer": "SpaceHeater Company Inc.",  
  "hasModel": "SpaceHeater 0.1.2",  
  "dateCreated": "2023-01-26T11:00:53Z",  
  "dateModified": "2023-01-25T20:46:44Z",  
  "source": "Import",  
  "name": "SpaceHeater",  
  "alternateName": "SpaceHeater type 2",  
  "description": "SpaceHeater of limited SpaceHeater types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>    
#### スペースヒーター NGSI-LD 正規化例    
以下は、正規化されたJSON-LDフォーマットのSpaceHeaterの例である。これは、オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:SpaceHeater:61e1adc2-8b00-43d5-89ba-40afbd26cda5",  
  "type": "SpaceHeater",  
  "bodyMass": {  
    "type": "Property",  
    "unitCode": "g",  
    "observedAt": "2023-01-26T04:40:44Z",  
    "value": 0.40152893437379167  
  },  
  "energySource": {  
    "type": "Property",  
    "value": "groupware"  
  },  
  "heatTransferDimension": {  
    "type": "Property",  
    "value": "Licensed Frozen Bike"  
  },  
  "heatTransferMedium": {  
    "type": "Property",  
    "value": "Pakistan Rupee"  
  },  
  "numberOfPanels": {  
    "type": "Property",  
    "value": 0.13243335736611006  
  },  
  "numberOfSections": {  
    "type": "Property",  
    "value": 0.9440399239258307  
  },  
  "outputCapacity": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-26T05:12:20Z",  
    "value": 0.38330998929377036  
  },  
  "placementType": {  
    "type": "Property",  
    "value": "Way"  
  },  
  "temperatureClassification": {  
    "type": "Property",  
    "value": "Kip"  
  },  
  "thermalEfficiency": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-25T15:23:27Z",  
    "value": 0.8451012126787633  
  },  
  "thermalMassHeatCapacity": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-25T22:19:20Z",  
    "value": 0.7853573438622519  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:6018650a-68e3-465a-acb8-e51269656682"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:1bf687c2-f166-4d7b-82ea-e6bf6b5ccd78"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:a538c5b3-c04a-4d42-8cc7-045a50e3b61b"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:8d2af757-8dde-4c47-ade4-b6fe0a649d95"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:6b0fbbf7-519a-4971-b6be-70fbc4a5eadd"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "SpaceHeater Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "SpaceHeater 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T05:11:00Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T02:18:58Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "SpaceHeater"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "SpaceHeater type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "SpaceHeater of limited SpaceHeater types"  
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
