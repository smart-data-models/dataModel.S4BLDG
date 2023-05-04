<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティTubeBundle（チューブバンドル  
=========================<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/TubeBundle/LICENSE.md)  
[文書が自動的に生成されます](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description：**チューブバンドルは、熱伝達に使用されるチューブやチューブの束からなる装置で、チラーやコイルなどの他のエネルギー変換装置内に通常含まれるものである**。  
バージョン：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性に型がない場合は、複数の型や異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: このアイテムの別称  - `areaServed[string]`: サービスまたは提供されるアイテムが提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: このアイテムの説明  - `foulingFactor[number]`: 特性。チューブバンドルに含まれるチューブのファウリング係数。通常、m2ケルビン/ワットで測定される。  - `hasManufacturer[string]`: プロパティ。エンティティ（例：デバイス）の製造者を特定する関係。値は、文字列または言語タグ付き文字列であることが期待される。  - `hasModel[string]`: プロパティです。エンティティ（例：デバイス）のモデルを識別する関係。値は、文字列または言語タグ付き文字列であることが期待される。  - `hasTurbulator[boolean]`: プロパティです。チューブにタービュレーターがある場合はTRUE、ない場合はFALSEです。  - `horizontalSpacing[number]`: 特性を示す。チューブバンドル内のチューブ間の水平方向の間隔。通常、ミリメートル（mm）単位で測定される。  - `id[*]`: エンティティの一意な識別子  - `inLineRowSpacing[number]`: 特性です。インラインチューブ列の間隔。通常、ミリメートル（mm）単位で測定される。  - `insideDiameter[number]`: 特性を示す。チューブバンドルに含まれるチューブの実際の内径。通常、ミリメートル（mm）単位で測定される。  - `isContainedInBuildingSpace[*]`: 関係。建物の物理的空間を定義するために使用されるエンティティ。ビルディングスペースは、デバイスまたはビルディングオブジェクトを含む。(ビルディングスペース)  - `isContainedInPhysicalObject[*]`: 関係です。適切な空間領域を持つあらゆるオブジェクト。  (DULオントロジーから抽出した定義）（PhysicalObject)  - `isSubSystemOf[array]`: 関係。この物理オブジェクトが属するシステム（複数可）への参照。  - `length[number]`: プロパティです。デバイスの仕上がり長さ。通常、ミリメートル（mm）単位で測定する。  - `location[*]`: アイテムへの Geojson 参照。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon のいずれかである。  - `name[string]`: この項目の名称です。  - `nominalDiameter[number]`: 特性。チューブバンドルに含まれるチューブの公称直径または幅。通常、ミリメートル（mm）単位で測定される。  - `numberOfCircuits[number]`: プロパティ流体管路の並列回路数  - `numberOfRows[number]`: プロパティ。チューブバンドルアセンブリのチューブ列の数。  - `outsideDiameter[number]`: 特性を示す。チューブバンドル内のチューブの実際の外径。通常、ミリメートル（mm）単位で測定される。  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリストです。  - `seeAlso[*]`: アイテムに関する追加リソースを指す URI のリスト。  - `source[string]`: エンティティデータの元のソースをURLとして与える一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `staggeredRowSpacing[number]`: 特性です。チューブ列の間隔を千鳥にしたもの。通常、ミリメートル（mm）単位で測定される。  - `thermalConductivity[number]`: 特性。チューブバンドルに含まれるチューブのファウリング係数。通常、m2ケルビン/ワットで測定される。  - `type[string]`: プロパティです。TubeBundle`と等しくなければならない。  - `verticalSpacing[number]`: 特性。チューブバンドル内のチューブ間の垂直方向の間隔。通常、ミリメートル（mm）単位で測定される。  - `volumen[number]`: 特性です。チューブおよびそのヘッダー内の流体の総量。通常、立方メートル（m3）単位で測定される。  <!-- /30-PropertiesList -->  
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
TubeBundle:    
  description: 'A tube bundle is a device consisting of tubes and bundles of tubes used for heat transfer and contained typically within other energy conversion devices, such as a chiller or coil.'    
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
    foulingFactor:    
      description: Property. Fouling factor of the tubes in the tube bundle. Usually measured in m2 Kelvin/Watt.    
      type: number    
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
    hasTurbulator:    
      description: 'Property. TRUE if the tube has a turbulator, FALSE if it does not.'    
      type: boolean    
      x-ngsi:    
        type: Property    
    horizontalSpacing:    
      description: Property. Horizontal spacing between tubes in the tube bundle. Usually measured in millimeters (mm).    
      type: number    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &tubebundle_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    inLineRowSpacing:    
      description: Property. In-line tube row spacing. Usually measured in millimeters (mm).    
      type: number    
      x-ngsi:    
        type: Property    
    insideDiameter:    
      description: Property. Actual inner diameter of the tube in the tube bundle. Usually measured in millimeters (mm).    
      type: number    
      x-ngsi:    
        type: Property    
    isContainedInBuildingSpace:    
      anyOf: *tubebundle_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *tubebundle_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *tubebundle_-_properties_-_iscontainedinbuildingspace_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Relationship    
    length:    
      description: Property. The finished length of the device. Usually measured in millimeters (mm).    
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
    nominalDiameter:    
      description: Property. Nominal diameter or width of the tubes in the tube bundle. Usually measured in millimeters (mm).    
      type: number    
      x-ngsi:    
        type: Property    
    numberOfCircuits:    
      description: Property. Number of parallel fluid tube circuits.    
      type: number    
      x-ngsi:    
        type: Property    
    numberOfRows:    
      description: Property. Number of tube rows in the tube bundle assembly.    
      type: number    
      x-ngsi:    
        type: Property    
    outsideDiameter:    
      description: Property. Actual outside diameter of the tube in the tube bundle. Usually measured in millimeters (mm).    
      type: number    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *tubebundle_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    staggeredRowSpacing:    
      description: Property. Staggered tube row spacing. Usually measured in millimeters (mm).    
      type: number    
      x-ngsi:    
        type: Property    
    thermalConductivity:    
      description: Property. Fouling factor of the tubes in the tube bundle. Usually measured in m2 Kelvin/Watt.    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: Property. It must be equal to `TubeBundle`.    
      enum:    
        - TubeBundle    
      type: string    
      x-ngsi:    
        type: Property    
    verticalSpacing:    
      description: Property. Vertical spacing between tubes in the tube bundle.Usually measured in millimeters (mm).    
      type: number    
      x-ngsi:    
        type: Property    
    volumen:    
      description: Property. Total volume of fluid in the tubes and their headers. Usually measured in cubic metre (m3).    
      type: number    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:TubeBundle"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/TubeBundle/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/TubeBundle/schema.json    
  x-model-tags: SAREF TubeBundle    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### TubeBundle NGSI-v2 キー値例  
TubeBundleをJSON-LD形式でkey-valuesとした例を示します。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:TubeBundle:ce27cf16-c4dc-4b93-a7e5-021f38a5a0b8",  
    "type": "TubeBundle",  
    "foulingFactor": 0.8435912145074106,  
    "hasTurbulator": true,  
    "horizontalSpacing": 0.45432121749623355,  
    "inLineRowSpacing": 0.9076815444305774,  
    "insideDiameter": 0.9701449888350496,  
    "length": 0.38222174657550045,  
    "nominalDiameter": 0.0408320640034282,  
    "numberOfCircuits": 0.7792295738277125,  
    "numberOfRows": 0.2682132970916634,  
    "outsideDiameter": 0.7194081859650397,  
    "staggeredRowSpacing": 0.31167087959205464,  
    "thermalConductivity": 0.9198905188483331,  
    "verticalSpacing": 0.8194554788890942,  
    "volumen": 0.7779813380010603,  
    "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:a13d415e-6116-43c4-a668-24f7dbf86bc1",  
    "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:6946c181-2515-406c-82f2-6bad063d7f8b",  
    "isSubSystemOf": [  
        "urn:ngsi-ld:System:8f497d54-7104-4546-8fa1-51c409c2b446",  
        "urn:ngsi-ld:System:adfb1f0e-a324-45c4-be4c-1127ac06e4ed",  
        "urn:ngsi-ld:System:614b0bb1-d2d9-425f-a7b1-4063e2ba74fa"  
    ],  
    "hasManufacturer": "TubeBundle Company Inc.",  
    "hasModel": "TubeBundle 0.1.2",  
    "dateCreated": "2023-01-26T00:58:36Z",  
    "dateModified": "2023-01-26T10:38:11Z",  
    "source": "Import",  
    "name": "TubeBundle",  
    "alternateName": "TubeBundle type 2",  
    "description": "TubeBundle of limited TubeBundle types",  
    "dataProvider": "IFC file"  
}  
```  
</details>  
#### TubeBundle NGSI-v2 正規化例  
TubeBundleをJSON-LD形式で正規化した例を示します。これは、オプションを使用しない場合のNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:TubeBundle:75ab66ce-2623-41a5-884f-ed9b90bde563",  
  "type": "TubeBundle",  
  "foulingFactor": {  
    "type": "Measurement",  
    "value": 0.10691025901902518  
  },  
  "hasTurbulator": {  
    "type": "Boolean",  
    "value": false  
  },  
  "horizontalSpacing": {  
    "type": "Measurement",  
    "value": 0.5021481278695225  
  },  
  "inLineRowSpacing": {  
    "type": "Measurement",  
    "value": 0.7015738944986649  
  },  
  "insideDiameter": {  
    "type": "Measurement",  
    "value": 0.47609748066140833  
  },  
  "length": {  
    "type": "Measurement",  
    "value": 0.6920310151935178  
  },  
  "nominalDiameter": {  
    "type": "Measurement",  
    "value": 0.7019643160884628  
  },  
  "numberOfCircuits": {  
    "type": "Float",  
    "value": 0.2146661280911759  
  },  
  "numberOfRows": {  
    "type": "Float",  
    "value": 0.7182471012018697  
  },  
  "outsideDiameter": {  
    "type": "Measurement",  
    "value": 0.41939698462727526  
  },  
  "staggeredRowSpacing": {  
    "type": "Measurement",  
    "value": 0.39127220946141616  
  },  
  "thermalConductivity": {  
    "type": "Measurement",  
    "value": 0.9507857927588059  
  },  
  "verticalSpacing": {  
    "type": "Measurement",  
    "value": 0.08491295072422345  
  },  
  "volumen": {  
    "type": "Measurement",  
    "value": 0.16253433369725145  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:BuildingSpace:e03ce9ef-23a6-4ad9-a533-a960cec73dbe"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:PhysicalObject:1c71e6d7-68ef-4a8d-9fde-985758f88344"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:c9a9c176-b562-42b7-ad80-cc8db2093faa"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:63e522a0-7de4-4bd9-9f94-094efdf565dc"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:0eebd7dc-010a-4f91-a4d1-da8b2a153b7b"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "TubeBundle Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "TubeBundle 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T11:52:01.9956382+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T07:18:26.9100211+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "TubeBundle"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "TubeBundle type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "TubeBundle of limited TubeBundle types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### TubeBundle NGSI-LD キー値例  
TubeBundleをJSON-LD形式でkey-valuesとした例を示します。これは、`options=keyValues`を使用した場合にNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:TubeBundle:ce27cf16-c4dc-4b93-a7e5-021f38a5a0b8",  
  "type": "TubeBundle",  
  "foulingFactor": 0.8435912145074106,  
  "hasTurbulator": true,  
  "horizontalSpacing": 0.45432121749623355,  
  "inLineRowSpacing": 0.9076815444305774,  
  "insideDiameter": 0.9701449888350496,  
  "length": 0.38222174657550045,  
  "nominalDiameter": 0.0408320640034282,  
  "numberOfCircuits": 0.7792295738277125,  
  "numberOfRows": 0.2682132970916634,  
  "outsideDiameter": 0.7194081859650397,  
  "staggeredRowSpacing": 0.31167087959205464,  
  "thermalConductivity": 0.9198905188483331,  
  "verticalSpacing": 0.8194554788890942,  
  "volumen": 0.7779813380010603,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:a13d415e-6116-43c4-a668-24f7dbf86bc1",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:6946c181-2515-406c-82f2-6bad063d7f8b",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:8f497d54-7104-4546-8fa1-51c409c2b446",  
    "urn:ngsi-ld:System:adfb1f0e-a324-45c4-be4c-1127ac06e4ed",  
    "urn:ngsi-ld:System:614b0bb1-d2d9-425f-a7b1-4063e2ba74fa"  
  ],  
  "hasManufacturer": "TubeBundle Company Inc.",  
  "hasModel": "TubeBundle 0.1.2",  
  "dateCreated": "2023-01-26T00:58:36Z",  
  "dateModified": "2023-01-26T10:38:11Z",  
  "source": "Import",  
  "name": "TubeBundle",  
  "alternateName": "TubeBundle type 2",  
  "description": "TubeBundle of limited TubeBundle types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### TubeBundle NGSI-LD 正規化例  
TubeBundleをJSON-LD形式で正規化した例を示します。これは、オプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:TubeBundle:e896fec0-f21f-4fa6-a73b-274bb42fb0fe",  
  "type": "TubeBundle",  
  "foulingFactor": {  
    "type": "Property",  
    "unitCode": "Kelvin/Watt",  
    "observedAt": "2023-01-25T15:34:45Z",  
    "value": 0.7896142805113859  
  },  
  "hasTurbulator": {  
    "type": "Property",  
    "value": false  
  },  
  "horizontalSpacing": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-25T18:38:27Z",  
    "value": 0.9299315212283089  
  },  
  "inLineRowSpacing": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T04:15:23Z",  
    "value": 0.12680136540868248  
  },  
  "insideDiameter": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T12:46:46Z",  
    "value": 0.9063711005346757  
  },  
  "length": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-25T15:58:18Z",  
    "value": 0.5121996408910179  
  },  
  "nominalDiameter": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T05:13:10Z",  
    "value": 0.8209837702761213  
  },  
  "numberOfCircuits": {  
    "type": "Property",  
    "value": 0.253153343197542  
  },  
  "numberOfRows": {  
    "type": "Property",  
    "value": 0.69547957104902  
  },  
  "outsideDiameter": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T07:32:26Z",  
    "value": 0.7479684351740756  
  },  
  "staggeredRowSpacing": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T08:06:42Z",  
    "value": 0.2757631103143954  
  },  
  "thermalConductivity": {  
    "type": "Property",  
    "unitCode": "Kelvin/Watt",  
    "observedAt": "2023-01-25T15:39:27Z",  
    "value": 0.28193770602031487  
  },  
  "verticalSpacing": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T06:27:04Z",  
    "value": 0.7886025280565963  
  },  
  "volumen": {  
    "type": "Property",  
    "unitCode": "m3",  
    "observedAt": "2023-01-26T05:29:35Z",  
    "value": 0.6238667384353597  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:4943f440-65d7-4fe4-834f-140d786124af"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:6b66c26d-c9a9-4e59-ba5f-5a17174fa9da"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:721e7dae-913a-4e6e-989b-30d545a7ec3d"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:c6a87a94-a7c7-4c31-9b33-6f3ad7861cd0"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:205f1bbb-6bff-422a-9121-4c30a002dfe3"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "TubeBundle Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "TubeBundle 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T21:28:33Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T00:41:51Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "TubeBundle"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "TubeBundle type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "TubeBundle of limited TubeBundle types"  
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
