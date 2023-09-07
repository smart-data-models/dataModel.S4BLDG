<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティフィルター  
===========<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Filter/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな説明**フィルターとは、流体や気体から粒子状物質や気体状物質を除去するための装置である。  
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
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `finalResistance[number]`: 交換が必要な場合のフィルター流体抵抗（すなわち、ASHRAE規格52.1によるフィルター交換が必要な場合のフィルターを横切る最大空気流量における圧力損失）。通常はパスカル（Pa、N/m2）で測定される。  - `fluidFlowRateMax[number]`: 送出可能な流体流量の範囲。通常m3/s単位  - `fluidFlowRateMin[number]`: 送出可能な流体流量の範囲。通常m3/s単位  - `hasManufacturer[string]`: エンティティ（デバイスなど）の製造者を特定する関係。値は文字列または言語タグを持つ文字列であることが期待される。  - `hasModel[string]`: エンティティ（デバイスなど）のモデルを識別する関係。値は、文字列または言語タグを持つ文字列であることが期待される。  - `id[*]`: エンティティの一意識別子  - `initialResistance[number]`: 初期新品フィルター流体抵抗（すなわち、ASHRAE規格52.1によるフィルター新品時のフィルターを横切る最大空気流量における圧力損失）。通常パスカル（Pa、N/m2）で測定される。  - `isContainedInBuildingSpace[*]`: 建物の物理的空間を定義するために使用されるエンティティ。ビルディングスペースには、デバイスまたはビルディングオブジェクトが含まれる。(ビルディングスペース)  - `isContainedInPhysicalObject[*]`: 適切な空間領域を持つオブジェクト。  (DUL オントロジーより定義） （PhysicalObject）  - `isSubSystemOf[array]`: この物理オブジェクトが属するシステムへの参照。  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `name[string]`: このアイテムの名前  - `nominalFilterFaceVelocity[number]`: フィルター面速度。通常m/sで測定される。  - `nominalFlowRate[number]`: フィルターを通過する流体の公称流量。通常m3/s単位。  - `nominalMediaSurfaceVelocity[number]`: 媒体表面での平均流速。通常m/s単位で測定される。  - `nominalParticleGeometricMeanDiameter[number]`: 公称効率に関連する粒子の幾何平均直径。通常はミリメートル（mm）単位で測定される。  - `nominalParticleGeometricStandardDeviation[number]`: 公称効率に関連する粒子の幾何学的標準偏差。  - `nominalPressureDrop[number]`: フィルターを横切る総圧力損失。通常パスカル（Pa、N/m2）で測定される。  - `operationTemperatureMax[number]`: 許容動作周囲（空気、液体）温度範囲。通常、単位はケルビン（K）。  - `operationTemperatureMin[number]`: 許容動作周囲（空気、液体）温度範囲。通常、単位はケルビン（K）。  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `type[string]`: これは `Filter` と等しくなければならない。  - `weight[number]`: 装置の重量。通常、キログラム（kg）またはグラム（g）で測定される。  <!-- /30-PropertiesList -->  
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
Filter:    
  description: A filter is an apparatus used to remove particulate or gaseous matter from fluids and gases.    
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
    finalResistance:    
      description: 'Filter fluid resistance when replacement is required (i.e., Pressure drop at the maximum air flowrate across the filter when the filter needs replacement per ASHRAE Standard 52.1). Usually measured in Pascals (Pa, N/m2)'    
      type: number    
      x-ngsi:    
        type: Property    
    fluidFlowRateMax:    
      description: Possible range of fluid flowrate that can be delivered. Usually measured in m3/s    
      type: number    
      x-ngsi:    
        type: Property    
    fluidFlowRateMin:    
      description: Possible range of fluid flowrate that can be delivered. Usually measured in m3/s    
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
    initialResistance:    
      description: 'Initial new filter fluid resistance (i.e., pressure drop at the maximum air flowrate across the filter when the filter is new per ASHRAE Standard 52.1). Usually measured in Pascals (Pa, N/m2)'    
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
    nominalFilterFaceVelocity:    
      description: Filter face velocity. Usually measured in m/s    
      type: number    
      x-ngsi:    
        type: Property    
    nominalFlowRate:    
      description: Nominal fluid flow rate through the filter. Usually measured in m3/s    
      type: number    
      x-ngsi:    
        type: Property    
    nominalMediaSurfaceVelocity:    
      description: Average fluid velocity at the media surface. Usually measured in m/s    
      type: number    
      x-ngsi:    
        type: Property    
    nominalParticleGeometricMeanDiameter:    
      description: Particle geometric mean diameter associated with nominal efficiency. Usually measured in millimeters (mm)    
      type: number    
      x-ngsi:    
        type: Property    
    nominalParticleGeometricStandardDeviation:    
      description: 'Particle geometric standard deviation associated with nominal efficiency. '    
      type: number    
      x-ngsi:    
        type: Property    
    nominalPressureDrop:    
      description: 'Total pressure drop across the filter. Usually measured in Pascals (Pa, N/m2)'    
      type: number    
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
      description: It must be equal to `Filter`    
      enum:    
        - Filter    
      type: string    
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
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Filter"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Filter/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Filter/schema.json    
  x-model-tags: SAREF Filter    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### NGSI-v2 キー値のフィルタリング 例  
以下は、JSON-LD形式のFilterをkey-valuesとした例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Filter:cab351de-0353-4d67-ba3e-f8e496fff6ee",  
    "type": "Filter",  
    "finalResistance": 0.046716566596463616,  
    "fluidFlowRateMax": 0.5234640867427633,  
    "fluidFlowRateMin": 0.88979941896976,  
    "initialResistance": 0.9155546427779283,  
    "nominalFilterFaceVelocity": 0.6586465369680704,  
    "nominalFlowRate": 0.08419722940470808,  
    "nominalMediaSurfaceVelocity": 0.2909288017995001,  
    "nominalParticleGeometricMeanDiameter": 0.25048971083477223,  
    "nominalParticleGeometricStandardDeviation": 0.6860967233212114,  
    "nominalPressureDrop": 0.4382746309750293,  
    "operationTemperatureMax": 0.41660145070952037,  
    "operationTemperatureMin": 0.7951736951400654,  
    "weight": 0.9846229044529057,  
    "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:0f3368a3-5989-4693-b29e-37aaa17be464",  
    "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:78c5cc6c-d740-45dd-968c-43361a780e2c",  
    "isSubSystemOf": [  
        "urn:ngsi-ld:System:c57a69ec-9b26-4933-b4ce-580e5edb9b72",  
        "urn:ngsi-ld:System:0132ad74-ea74-4d20-b0d0-bb4fa1a19af9",  
        "urn:ngsi-ld:System:be24c623-c5c4-4da0-b4ea-552cb1d31a71"  
    ],  
    "hasManufacturer": "Filter Company Inc.",  
    "hasModel": "Filter 0.1.2",  
    "dateCreated": "2023-01-26T06:33:09Z",  
    "dateModified": "2023-01-26T13:51:08Z",  
    "source": "Import",  
    "name": "Filter",  
    "alternateName": "Filter type 2",  
    "description": "Filter of limited Filter types",  
    "dataProvider": "IFC file"  
}  
```  
</details>  
#### フィルタ NGSI-v2 正規化例  
以下は、正規化されたJSON-LD形式のFilterの例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Filter:8e80455c-7f89-462c-b1f0-b84c6ac5e5cb",  
  "type": "Filter",  
  "finalResistance": {  
    "type": "Measurement",  
    "value": 0.25563353322549653  
  },  
  "fluidFlowRateMax": {  
    "type": "Measurement",  
    "value":0.7441450852967011  
  },  
  "fluidFlowRateMin": {  
    "type": "Measurement",  
    "value":  0.32563792639259326  
  },  
  "initialResistance": {  
    "type": "Measurement",  
    "value": 0.41032135281652493  
  },  
  "nominalFilterFaceVelocity": {  
    "type": "Measurement",  
    "value": 0.829815297358211  
  },  
  "nominalFlowRate": {  
    "type": "Measurement",  
    "value":  0.569423507213339  
  },  
  "nominalMediaSurfaceVelocity": {  
    "type": "Measurement",  
    "value":  0.6085640129416107  
  },  
  "nominalParticleGeometricMeanDiameter": {  
    "type": "Measurement",  
    "value":  0.9736709365602062  
  },  
  "nominalParticleGeometricStandardDeviation": {  
    "type": "Measurement",  
    "value": 0.5284993250186989  
  },  
  "nominalPressureDrop": {  
    "type": "Measurement",  
    "value": 0.4856470985811685  
  },  
  "operationTemperatureMax": {  
    "type": "Measurement",  
    "value":  0.04450158146401939  
  },  
  "operationTemperatureMin": {  
    "type": "Measurement",  
    "value":  0.28211808830531604  
  },  
  "weight": {  
    "type": "Measurement",  
    "value": 0.5157014658259989  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:BuildingSpace:4468726f-7faa-4e8e-802e-337b7d4e2c38"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:PhysicalObject:a263b3b0-a5d7-4e38-a95f-75dd868ea6aa"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:118a0d61-bba3-416e-a770-5ac45dfb66e7"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:a7ba30cc-d8f3-423d-a1d6-284c130befee"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:38485bc5-5ff4-49f1-b6fb-65b815b05795"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Filter Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Filter 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T04:44:52.9377605+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T18:30:35.796352+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Filter"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Filter type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Filter of limited Filter types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### NGSI-LD キー値のフィルタリング 例  
以下は、JSON-LD形式のFilterをkey-valuesとした例である。options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Filter:cab351de-0353-4d67-ba3e-f8e496fff6ee",  
  "type": "Filter",  
  "finalResistance": 0.046716566596463616,  
  "fluidFlowRateMax": 0.5234640867427633,  
  "fluidFlowRateMin": 0.88979941896976,  
  "initialResistance": 0.9155546427779283,  
  "nominalFilterFaceVelocity": 0.6586465369680704,  
  "nominalFlowRate": 0.08419722940470808,  
  "nominalMediaSurfaceVelocity": 0.2909288017995001,  
  "nominalParticleGeometricMeanDiameter": 0.25048971083477223,  
  "nominalParticleGeometricStandardDeviation": 0.6860967233212114,  
  "nominalPressureDrop": 0.4382746309750293,  
  "operationTemperatureMax": 0.41660145070952037,  
  "operationTemperatureMin": 0.7951736951400654,  
  "weight": 0.9846229044529057,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:0f3368a3-5989-4693-b29e-37aaa17be464",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:78c5cc6c-d740-45dd-968c-43361a780e2c",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:c57a69ec-9b26-4933-b4ce-580e5edb9b72",  
    "urn:ngsi-ld:System:0132ad74-ea74-4d20-b0d0-bb4fa1a19af9",  
    "urn:ngsi-ld:System:be24c623-c5c4-4da0-b4ea-552cb1d31a71"  
  ],  
  "hasManufacturer": "Filter Company Inc.",  
  "hasModel": "Filter 0.1.2",  
  "dateCreated": "2023-01-26T06:33:09Z",  
  "dateModified": "2023-01-26T13:51:08Z",  
  "source": "Import",  
  "name": "Filter",  
  "alternateName": "Filter type 2",  
  "description": "Filter of limited Filter types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### フィルタ NGSI-LD 正規化例  
以下は、正規化されたJSON-LD形式のFilterの例である。これは、オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Filter:fbeb6c10-5a65-4f37-b472-05630b596d96",  
  "type": "Filter",  
  "finalResistance": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-26T01:00:57Z",  
    "value": 0.5605621121413891  
  },  
  "fluidFlowRateMax": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-26T09:29:26Z",  
    "value": 0.8457030696896928  
  },  
  "fluidFlowRateMin": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-26T01:24:07Z",  
    "value": 0.4281237576056126  
  },  
  "initialResistance": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-26T13:16:00Z",  
    "value": 0.9855925634968424  
  },  
  "nominalFilterFaceVelocity": {  
    "type": "Property",  
    "unitCode": "m/s",  
    "observedAt": "2023-01-26T03:08:23Z",  
    "value": 0.6912281080254741  
  },  
  "nominalFlowRate": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-25T15:48:08Z",  
    "value": 0.022821238860702198  
  },  
  "nominalMediaSurfaceVelocity": {  
    "type": "Property",  
    "unitCode": "m/s",  
    "observedAt": "2023-01-25T22:13:37Z",  
    "value": 0.5684154129668265  
  },  
  "nominalParticleGeometricMeanDiameter": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T07:32:19Z",  
    "value": 0.229698552370729  
  },  
  "nominalParticleGeometricStandardDeviation": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T02:48:53Z",  
    "value": 0.8264025547190669  
  },  
  "nominalPressureDrop": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-25T19:24:30Z",  
    "value": 0.6662603303962529  
  },  
  "operationTemperatureMax": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T00:52:23Z",  
    "value": 0.8600599815414807  
  },  
  "operationTemperatureMin": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T18:39:35Z",  
    "value": 0.11197463391152895  
  },  
  "weight": {  
    "type": "Property",  
    "unitCode": "g",  
    "observedAt": "2023-01-26T06:38:32Z",  
    "value": 0.39067890635291025  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:3ad9289e-2153-42f6-821a-e050b0cece56"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:14828a20-966b-491d-8c5d-06e0e9323fe3"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:4f4ca1e9-532c-4518-b84b-92e00d43255a"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:4be15aec-065d-404f-aedd-e477a5a61f23"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:7e718726-9abe-49e6-ae69-96d1277a5af0"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Filter Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Filter 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T21:32:07Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-25T21:47:48Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Filter"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Filter type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Filter of limited Filter types"  
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
