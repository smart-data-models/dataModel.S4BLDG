<!-- 10-Header -->
  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

エンティティチラー  
=========
<!-- /10-Header -->
  
<!-- 15-License -->
  

[オープンライセンス](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Chiller/LICENSE.md)  

[文書が自動的に生成されます](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->
  
<!-- 20-Description -->
  

Global description：チラーは、蒸気圧縮または吸収冷凍サイクルによって液体から熱を除去し、流体（通常は水または水とグリコールの混合物）を冷却するために使用される装置である**。冷やされた流体は、次に建物の空気を冷却し、除湿するために使用されます**。  

バージョン：0.0.2  
<!-- /20-Description -->
  
<!-- 30-PropertiesList -->
  


## プロパティ一覧  


<sup><sub>[*] 属性に型がない場合は、複数の型や異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)
- `alternateName[string]`: このアイテムの別称  
- `areaServed[string]`: サービスまたは提供されるアイテムが提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)
- `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  
- `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  
- `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  
- `description[string]`: このアイテムの説明  
- `hasManufacturer[string]`: プロパティ。エンティティ（例：デバイス）の製造者を特定する関係。値は、文字列または言語タグ付き文字列であることが期待される。  
- `hasModel[string]`: プロパティです。エンティティ（例：デバイス）のモデルを識別する関係。値は、文字列または言語タグ付き文字列であることが期待される。  
- `id[*]`: エンティティの一意な識別子  
- `isContainedInBuildingSpace[*]`: 関係。建物の物理的空間を定義するために使用されるエンティティ。ビルディングスペースは、デバイスまたはビルディングオブジェクトを含む。(ビルディングスペース)  
- `isContainedInPhysicalObject[*]`: 関係です。適切な空間領域を持つあらゆるオブジェクト。  (DULオントロジーから抽出した定義）（PhysicalObject)  
- `isSubSystemOf[array]`: 関係。この物理オブジェクトが属するシステム（複数可）への参照。  
- `location[*]`: アイテムへの Geojson 参照。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon のいずれかである。  
- `name[string]`: この項目の名称です。  
- `nominalCapacity[object]`: 特性です。公称容量。通常、ワット（W、J/s）で測定される。  
- `nominalCondensingTemperature[object]`: 特性です。Chiller condensing temperature（チラー凝縮温度）。通常、ケルビン(K)単位で測定する。  
- `nominalEfficiency[object]`: 特性です。公称条件下でのチラー効率。  
- `nominalEvaporatingTemmperature[object]`: 特性。チラー蒸発温度。通常、ケルビン(K)単位で測定される。  
- `nominalHeatRejectionRate[object]`: 特性。冷凍効果と圧縮機に入力される電力の熱等価値の合計。通常、ワット（W、J/s）単位で測定される。  
- `nominalPowerConsumption[object]`: 特性です。公称総消費電力。通常、ワット（W、J/s）単位で測定される。  
- `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリストです。  
- `seeAlso[*]`: アイテムに関する追加リソースを指す URI のリスト。  
- `source[string]`: エンティティデータの元のソースをURLとして与える一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  
- `type[string]`: プロパティです。これは `Chiller` と等しくなければならない。  
<!-- /30-PropertiesList -->
  
<!-- 35-RequiredProperties -->
  

必須プロパティ  
- `id`  
- `type`  
<!-- /35-RequiredProperties -->
  
<!-- 40-RequiredProperties -->
  
<!-- /40-RequiredProperties -->
  
<!-- 50-DataModelHeader -->
  

## プロパティのデータモデル記述  

アルファベット順（クリックで詳細表示）  
<!-- /50-DataModelHeader -->
  
<!-- 60-ModelYaml -->
  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
Chiller:    
  description: 'A chiller is a device used to remove heat from a liquid via a vapor-compression or absorption refrigeration cycle to cool a fluid, typically water or a mixture of water and glycol. The chilled fluid is then used to cool and dehumidify air in a building.'    
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
      anyOf: &chiller_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      anyOf: *chiller_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *chiller_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *chiller_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    nominalCapacity:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: 'Property. Nominal capacity. Usually measured in Watts (W, J/s).'    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: &chiller_-_properties_-_nominalcondensingtemperature_-_properties    
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
    nominalCondensingTemperature:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: Property. Chiller condensing temperature. Usually measured in degrees Kelvin (K).    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *chiller_-_properties_-_nominalcondensingtemperature_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    nominalEfficiency:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: 'Property. Nominal chiller efficiency under nominal conditions. '    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *chiller_-_properties_-_nominalcondensingtemperature_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    nominalEvaporatingTemmperature:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: Property. Chiller evaporating temperature.Usually measured in degrees Kelvin (K).    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *chiller_-_properties_-_nominalcondensingtemperature_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    nominalHeatRejectionRate:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: 'Property. Sum of the refrigeration effect and the heat equivalent of the power input to the compressor. Usually measured in Watts (W, J/s).'    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *chiller_-_properties_-_nominalcondensingtemperature_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    nominalPowerConsumption:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: 'Property. Nominal total power consumption. Usually measured in Watts (W, J/s).'    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *chiller_-_properties_-_nominalcondensingtemperature_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *chiller_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      description: Property. It must be equal to `Chiller`.    
      enum:    
        - Chiller    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Chiller"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Chiller/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Chiller/schema.json    
  x-model-tags: SAREF Chiller    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->
  
<!-- 70-MiddleNotes -->
  
<!-- /70-MiddleNotes -->
  
<!-- 80-Examples -->
  

## ペイロードの例  

#### Chiller NGSI-v2 キー値例  

ここでは、ChillerをJSON-LD形式でkey-valuesとした例を示します。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:Chiller:ba7497f8-4fd6-4ec0-8dd8-00ed95bd51fc",  
  "type": "Chiller",  
  "nominalCapacity": 0.09475720530736764,  
  "nominalCondensingTemperature": 0.20516492572831713,  
  "nominalEfficiency": 0.9467840743079621,  
  "nominalEvaporatingTemmperature": 0.9391249200926837,  
  "nominalHeatRejectionRate": 0.6781215261931568,  
  "nominalPowerConsumption": 0.7316060776442138,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:53b1b818-f2bf-4bbf-9ba6-e3d431a11173",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:5d06c867-dc48-4267-b194-60642a22f0af",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:8c79471f-dea7-474b-985e-e5072ea36369",  
    "urn:ngsi-ld:System:e2e46075-3c25-46c4-80b4-da4b79faef4e",  
    "urn:ngsi-ld:System:9eea4295-8a6c-4efb-833e-1d6941c97754"  
  ],  
  "hasManufacturer": "Chiller Company Inc.",  
  "hasModel": "Chiller 0.1.2",  
  "dateCreated": "2023-01-25T19:42:28Z",  
  "dateModified": "2023-01-25T19:48:46Z",  
  "source": "Import",  
  "name": "Chiller",  
  "alternateName": "Chiller type 2",  
  "description": "Chiller of limited Chiller types",  
  "dataProvider": "IFC file"  
}  
```  
</details>  

#### Chiller NGSI-v2 正規化例  

ここでは、正規化されたJSON-LD形式のChillerの例を示す。これは、オプションを使用しない場合のNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:Chiller:fbbc813e-29ac-4462-9996-5a3d73d1ce98",  
  "type": "Chiller",  
  "nominalCapacity": {  
    "type": "Measurement",  
    "value": 0.0740819212946876  
  },  
  "nominalCondensingTemperature": {  
    "type": "Measurement",  
    "value": 0.5010709006481944  
  },  
  "nominalEfficiency": {  
    "type": "Measurement",  
    "value": 0.05897827362979524  
  },  
  "nominalEvaporatingTemmperature": {  
    "type": "Measurement",  
    "value": 0.0556993113916634  
  },  
  "nominalHeatRejectionRate": {  
    "type": "Measurement",  
    "value": 0.756236294011522  
  },  
  "nominalPowerConsumption": {  
    "type": "Measurement",  
    "value": 0.8474333854169832  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:BuildingSpace:0a2b8ec3-70d9-483f-8df0-dc7bbfa27d29"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:PhysicalObject:18da6c4b-5520-4b19-b3ee-2a91993c19de"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:System:b48e7b0c-7d5e-4087-89d4-c40a87ae78be"  
      },  
      {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:System:d9a20a72-def1-447e-ba8a-f601965fc681"  
      },  
      {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:System:474efe4e-7d74-4985-ac14-792dcb6b9d76"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Chiller Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Chiller 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T05:24:59.314133+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T04:27:01.3524196+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Chiller"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Chiller type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Chiller of limited Chiller types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  

#### チラーNGSI-LDキー値例  

ここでは、ChillerをJSON-LD形式でkey-valuesとした例を示します。これは、`options=keyValues`を使用した場合にNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:Chiller:ba7497f8-4fd6-4ec0-8dd8-00ed95bd51fc",  
  "type": "Chiller",  
  "nominalCapacity": 0.09475720530736764,  
  "nominalCondensingTemperature": 0.20516492572831713,  
  "nominalEfficiency": 0.9467840743079621,  
  "nominalEvaporatingTemmperature": 0.9391249200926837,  
  "nominalHeatRejectionRate": 0.6781215261931568,  
  "nominalPowerConsumption": 0.7316060776442138,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:53b1b818-f2bf-4bbf-9ba6-e3d431a11173",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:5d06c867-dc48-4267-b194-60642a22f0af",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:8c79471f-dea7-474b-985e-e5072ea36369",  
    "urn:ngsi-ld:System:e2e46075-3c25-46c4-80b4-da4b79faef4e",  
    "urn:ngsi-ld:System:9eea4295-8a6c-4efb-833e-1d6941c97754"  
  ],  
  "hasManufacturer": "Chiller Company Inc.",  
  "hasModel": "Chiller 0.1.2",  
  "dateCreated": "2023-01-25T19:42:28Z",  
  "dateModified": "2023-01-25T19:48:46Z",  
  "source": "Import",  
  "name": "Chiller",  
  "alternateName": "Chiller type 2",  
  "description": "Chiller of limited Chiller types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  

#### 冷熱機器 NGSI-LD 正規化例  

ここでは、JSON-LD形式で正規化されたChillerの例を示します。これはオプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:Chiller:1a99f350-0e1d-4466-8579-912c1f3c9b8f",  
  "type": "Chiller",  
  "nominalCapacity": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-26T09:47:03Z",  
    "value": 0.22554187711659102  
  },  
  "nominalCondensingTemperature": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T14:43:34Z",  
    "value": 0.1507511254687508  
  },  
  "nominalEfficiency": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T03:46:03Z",  
    "value": 0.3248755291390478  
  },  
  "nominalEvaporatingTemmperature": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T02:17:21Z",  
    "value": 0.13438649176620343  
  },  
  "nominalHeatRejectionRate": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-26T06:04:17Z",  
    "value": 0.0564283340666325  
  },  
  "nominalPowerConsumption": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-26T10:26:02Z",  
    "value": 0.8546772522263915  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:d78af157-a55d-46b9-8c56-d6c0eda32745"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:4748763d-3b35-487c-a6ad-3a9dfa510820"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:29fc2747-3753-44b5-8d88-3ae91cd4bc89"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:7a9aa253-a2eb-42ce-aeee-6130d158d18f"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:72503e97-5805-42a7-a24b-891925d2a999"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Chiller Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Chiller 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T10:57:45Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T04:43:33Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Chiller"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Chiller type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Chiller of limited Chiller types"  
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
  
