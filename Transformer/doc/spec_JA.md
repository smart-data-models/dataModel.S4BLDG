<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティトランスフォーマー  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Transformer/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな説明**変圧器は、ある回路から別の回路へ電気エネルギーを伝達する誘導性の静止装置である。  変圧器は電力を変換するために使用され、他の目的のための電気信号の変換は他のエンティティで処理される：Controllerは任意の信号を変換し、AudioVisualApplianceはオーディオまたはビデオストリームの信号を変換し、CommunicationsApplianceはデータまたはその他の通信用途の信号を変換する。  
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
- `alternateName[string]`: この項目の別名  - `apparentPowerMax[number]`: 最大皮相電力／容量をVA（ボルトアンペア）で表す。通常はワット（W、J/s）で測定される。  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `hasManufacturer[string]`: エンティティ（デバイスなど）の製造者を特定する関係。値は文字列または言語タグを持つ文字列であることが期待される。  - `hasModel[string]`: エンティティ（デバイスなど）のモデルを識別する関係。値は、文字列または言語タグを持つ文字列であることが期待される。  - `id[*]`: エンティティの一意識別子  - `imaginaryImpedanceRatio[number]`: 変圧器の零相インピーダンスの虚部と正相インピーダンスの虚部（すなわち短絡電圧の虚部）の比。N導体を含む三相変圧器に使用される。  - `isContainedInBuildingSpace[*]`: 建物の物理的空間を定義するために使用されるエンティティ。ビルディングスペースには、デバイスまたはビルディングオブジェクトが含まれる。(ビルディングスペース)  - `isContainedInPhysicalObject[*]`: 適切な空間領域を持つオブジェクト。  (DUL オントロジーより定義） （PhysicalObject）  - `isNeutralPrimaryTerminalAvailable[boolean]`: 一次巻線の中性点が端子として利用可能かどうかの表示 (=TRUE) または利用可能でないかどうかの表示 (= FALSE)  - `isNeutralSecondaryTerminalAvailable[boolean]`: 二次巻線の中性点が端子として利用可能であるか（＝TRUE）、そうでないか（＝FALSE）を示す。  - `isSubSystemOf[array]`: この物理オブジェクトが属するシステムへの参照。  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `name[string]`: このアイテムの名前  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `primaryApparentPower[number]`: 変圧され、一次側トランスに流れ込むVA（ボルトアンペア）単位の電力。通常はワット（W、J/s）で測定される。  - `primaryCurrent[number]`: 変圧されようとする電流で、一次側で変圧器に流れ込むもの。通常、アンペア（A）で測定される。  - `primaryFrequency[number]`: 変圧される周波数で、一次側のトランスに流れる。通常、サイクル/秒またはヘルツ（Hz）で測定される。  - `primaryVoltage[number]`: 変圧されようとしている電圧で、一次側で変圧器に流れる。通常、単位はボルト（V、W/A）。  - `realImpedanceRatio[number]`: 変圧器の零相インピーダンスの実部と正相インピーダンスの実部（すなわち短絡電圧の実部）の比。N導体を含む三相変圧器に使用される。  - `secondaryApparentPower[number]`: 変圧器から二次側に流出する、変圧されたVA（ボルトアンペア）単位の電力。通常はワット（W、J/s）で測定される。  - `secondaryCurrent[number]`: 変圧器から二次側に流出する電流。通常はアンペア（A）で測定される。  - `secondaryCurrentType[string]`: トランス出力から発生する可能性のある二次電流タイプのリスト  - `secondaryFrequency[number]`: 変圧器から二次側に流出する周波数。通常、サイクル/秒またはヘルツ（Hz）で測定される。  - `secondaryVoltage[number]`: 変圧器から二次側に流出する電圧。通常、単位はボルト（V、W/A）。  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `transformerVectorGroup[string]`: 変圧器に設定可能なベクトルグループのリスト。列挙リストの値は、最初の文字が一次巻線の接続方法を、2 番目の文字が二次巻線の接続方法を表し、数字が一次側から二次側への電圧と電流の回転を 30 度の倍数で表す標準国際コードに従う。D: 巻線がデルタ結線されていることを意味する。Y: 巻線がスター結線であることを示します。Z: 巻線がジグザグ結線(変圧器の低リアクタンスを実現する特殊なスタート結線)であることを意味する。接続性は三相変圧器のみに関係する。  - `type[string]`: これは `Transformer` と等しくなければならない。  <!-- /30-PropertiesList -->  
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
Transformer:    
  description: 'A transformer is an inductive stationary device that transfers electrical energy from one circuit to another.  Transformer is used to transform electric power; conversion of electric signals for other purposes is handled at other entities: Controller converts arbitrary signals, AudioVisualAppliance converts signals for audio or video streams, and CommunicationsAppliance converts signals for data or other communications usage.'    
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
    apparentPowerMax:    
      description: 'Maximum apparent power/capacity in VA (volt ampere). Usually measured in Watts (W, J/s)'    
      type: number    
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
    imaginaryImpedanceRatio:    
      description: The ratio between the imaginary part of the zero sequence impedance and the imaginary part of the positive impedance (i.e. imaginary part of the short-circuit voltage) of the transformer. Used for three-phase transformer which includes a N-conductor    
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
    isNeutralPrimaryTerminalAvailable:    
      description: An indication of whether the neutral point of the primary winding is available as a terminal (=TRUE) or not (= FALSE)    
      type: boolean    
      x-ngsi:    
        type: Property    
    isNeutralSecondaryTerminalAvailable:    
      description: An indication of whether the neutral point of the secondary winding is available as a terminal (=TRUE) or not (= FALSE)    
      type: boolean    
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
    primaryApparentPower:    
      description: 'The power in VA (volt ampere) that has been transformed and that runs into the transformer on the primary side. Usually measured in Watts (W, J/s)'    
      type: number    
      x-ngsi:    
        type: Property    
    primaryCurrent:    
      description: The current that is going to be transformed and that runs into the transformer on the primary side. Usually measured in Ampere (A)    
      type: number    
      x-ngsi:    
        type: Property    
    primaryFrequency:    
      description: The frequency that is going to be transformed and that runs into the transformer on the primary side. Usually measured in cycles/s or Hertz (Hz)    
      type: number    
      x-ngsi:    
        type: Property    
    primaryVoltage:    
      description: 'The voltage that is going to be transformed and that runs into the transformer on the primary side. Usually measured in Volts (V, W/A)'    
      type: number    
      x-ngsi:    
        type: Property    
    realImpedanceRatio:    
      description: The ratio between the real part of the zero sequence impedance and the real part of the positive impedance (i.e. real part of the short-circuit voltage) of the transformer. Used for three-phase transformer which includes a N-conductor    
      type: number    
      x-ngsi:    
        type: Property    
    secondaryApparentPower:    
      description: 'The power in VA (volt ampere) that has been transformed and is running out of the transformer on the secondary side. Usually measured in Watts (W, J/s)'    
      type: number    
      x-ngsi:    
        type: Property    
    secondaryCurrent:    
      description: The current that has been transformed and is running out of the transformer on the secondary side. Usually measured in Ampere (A)    
      type: number    
      x-ngsi:    
        type: Property    
    secondaryCurrentType:    
      description: A list of the secondary current types that can result from transformer output    
      type: string    
      x-ngsi:    
        type: Property    
    secondaryFrequency:    
      description: The frequency that has been transformed and is running out of the transformer on the secondary side. Usually measured in cycles/s or Hertz (Hz)    
      type: number    
      x-ngsi:    
        type: Property    
    secondaryVoltage:    
      description: 'The voltage that has been transformed and is running out of the transformer on the secondary side. Usually measured in Volts (V, W/A)'    
      type: number    
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
    transformerVectorGroup:    
      description: 'List of the possible vector groups for the transformer from which that required may be set. Values in the enumeration list follow a standard international code where the first letter describes how the primary windings are connected, the second letter describes how the secondary windings are connected, and the numbers describe the rotation of voltages and currents from the primary to the secondary side in multiples of 30 degrees. D: means that the windings are delta-connected. Y: means that the windings are star-connected. Z: means that the windings are zig-zag connected (a special start-connected providing low reactance of the transformer). The connectivity is only relevant for three-phase transformers'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: It must be equal to `Transformer`    
      enum:    
        - Transformer    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Transformer"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Transformer/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Transformer/schema.json    
  x-model-tags: SAREF Transformer    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### トランスフォーマ NGSI-v2 キー値の例  
JSON-LD形式のTransformerのkey-valuesの例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Transformer:4976b0ec-0c96-4ae1-91da-c906da8348da",  
    "type": "Transformer",  
    "apparentPowerMax": 0.17497838413457267,  
    "imaginaryImpedanceRatio": 0.5323895083879017,  
    "isNeutralPrimaryTerminalAvailable": false,  
    "isNeutralSecondaryTerminalAvailable": true,  
    "primaryApparentPower": 0.8765115449298688,  
    "primaryCurrent": 0.871670986786111,  
    "primaryFrequency": 0.141749759362659,  
    "primaryVoltage": 0.5038263292514936,  
    "realImpedanceRatio": 0.06325384828151492,  
    "secondaryApparentPower": 0.45704946090246745,  
    "secondaryCurrent": 0.4016609926228465,  
    "secondaryCurrentType": "Data",  
    "secondaryFrequency": 0.7436141485906284,  
    "secondaryVoltage": 0.4646450009162978,  
    "transformerVectorGroup": "Soft",  
    "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:51645089-5e36-4b9c-ad25-b97b58506919",  
    "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:6737e804-54ff-41c0-ba12-90dde24f3d59",  
    "isSubSystemOf": [  
        "urn:ngsi-ld:System:38dfdf15-5a41-412d-9b05-435cb7809e6f",  
        "urn:ngsi-ld:System:b7274b46-33ec-4694-8dda-999197bb58c5",  
        "urn:ngsi-ld:System:b7d5c2ce-fc23-42d0-be8f-9e56a9f3c5db"  
    ],  
    "hasManufacturer": "Transformer Company Inc.",  
    "hasModel": "Transformer 0.1.2",  
    "dateCreated": "2023-01-25T16:42:43Z",  
    "dateModified": "2023-01-26T13:53:42Z",  
    "source": "Import",  
    "name": "Transformer",  
    "alternateName": "Transformer type 2",  
    "description": "Transformer of limited Transformer types",  
    "dataProvider": "IFC file"  
}  
```  
</details>  
#### 変換器 NGSI-v2 正規化例  
以下は、正規化されたJSON-LDフォーマットのTransformerの例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Transformer:7dc130e2-e429-4c26-b467-ec9d1f41e7b8",  
  "type": "Transformer",  
  "apparentPowerMax": {  
    "type": "Measurement",  
    "value":  0.6561932522421066  
  },  
  "imaginaryImpedanceRatio": {  
    "type": "Measurement",  
    "value": 0.7913482963385954  
  },  
  "isNeutralPrimaryTerminalAvailable": {  
    "type": "Boolean",  
    "value": true  
  },  
  "isNeutralSecondaryTerminalAvailable": {  
    "type": "Boolean",  
    "value": true  
  },  
  "primaryApparentPower": {  
    "type": "Measurement",  
    "value":  0.23470397848013025  
  },  
  "primaryCurrent": {  
    "type": "Measurement",  
    "value":  0.7245530289719985  
  },  
  "primaryFrequency": {  
    "type": "Measurement",  
    "value":  0.18927842693402908  
  },  
  "primaryVoltage": {  
    "type": "Measurement",  
    "value":  0.359590276424793  
  },  
  "realImpedanceRatio": {  
    "type": "Measurement",  
    "value":  0.6917590580595899  
  },  
  "secondaryApparentPower": {  
    "type": "Measurement",  
    "value":  0.10075664755263747  
  },  
  "secondaryCurrent": {  
    "type": "Measurement",  
    "value": 0.1458215404162363  
  },  
  "secondaryCurrentType": {  
    "type": "Text",  
    "value": "Tasty Wooden Car"  
  },  
  "secondaryFrequency": {  
    "type": "Measurement",  
    "value":  0.09146741937660052  
  },  
  "secondaryVoltage": {  
    "type": "Measurement",  
    "value": 0.31779800995261864  
  },  
  "transformerVectorGroup": {  
    "type": "Text",  
    "value": "SMS"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:BuildingSpace:16bccee7-8244-4707-8d4b-c5a06b0fee75"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:PhysicalObject:b9a1bd5e-114e-41ba-b865-25b4b4c5c3c5"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:37554df5-ec0d-4e03-8697-7d562ff2134f"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:e967a169-474b-47a0-bd0c-a76ce8a5f7be"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:49a6b09b-2301-4b6e-a167-54ee44cc83d4"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Transformer Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Transformer 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T20:08:21.2034652+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T22:13:38.7837862+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Transformer"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Transformer type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Transformer of limited Transformer types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### トランスフォーマ NGSI-LD キー値の例  
JSON-LD形式のTransformerのkey-valuesの例である。options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Transformer:4976b0ec-0c96-4ae1-91da-c906da8348da",  
  "type": "Transformer",  
  "apparentPowerMax": 0.17497838413457267,  
  "imaginaryImpedanceRatio": 0.5323895083879017,  
  "isNeutralPrimaryTerminalAvailable": false,  
  "isNeutralSecondaryTerminalAvailable": true,  
  "primaryApparentPower": 0.8765115449298688,  
  "primaryCurrent": 0.871670986786111,  
  "primaryFrequency": 0.141749759362659,  
  "primaryVoltage": 0.5038263292514936,  
  "realImpedanceRatio": 0.06325384828151492,  
  "secondaryApparentPower": 0.45704946090246745,  
  "secondaryCurrent": 0.4016609926228465,  
  "secondaryCurrentType": "Data",  
  "secondaryFrequency": 0.7436141485906284,  
  "secondaryVoltage": 0.4646450009162978,  
  "transformerVectorGroup": "Soft",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:51645089-5e36-4b9c-ad25-b97b58506919",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:6737e804-54ff-41c0-ba12-90dde24f3d59",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:38dfdf15-5a41-412d-9b05-435cb7809e6f",  
    "urn:ngsi-ld:System:b7274b46-33ec-4694-8dda-999197bb58c5",  
    "urn:ngsi-ld:System:b7d5c2ce-fc23-42d0-be8f-9e56a9f3c5db"  
  ],  
  "hasManufacturer": "Transformer Company Inc.",  
  "hasModel": "Transformer 0.1.2",  
  "dateCreated": "2023-01-25T16:42:43Z",  
  "dateModified": "2023-01-26T13:53:42Z",  
  "source": "Import",  
  "name": "Transformer",  
  "alternateName": "Transformer type 2",  
  "description": "Transformer of limited Transformer types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### 変換器 NGSI-LD 正規化例  
以下は、正規化されたJSON-LDフォーマットのTransformerの例である。これは、オプションを使用しない場合、NGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Transformer:24b95122-4055-44dc-82ad-09a2bcda9025",  
  "type": "Transformer",  
  "apparentPowerMax": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-25T20:30:38Z",  
    "value": 0.24466523496915848  
  },  
  "imaginaryImpedanceRatio": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T00:56:06Z",  
    "value": 0.0034198103714959682  
  },  
  "isNeutralPrimaryTerminalAvailable": {  
    "type": "Property",  
    "value": false  
  },  
  "isNeutralSecondaryTerminalAvailable": {  
    "type": "Property",  
    "value": true  
  },  
  "primaryApparentPower": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-26T12:47:55Z",  
    "value": 0.9141641275735504  
  },  
  "primaryCurrent": {  
    "type": "Property",  
    "unitCode": "A",  
    "observedAt": "2023-01-26T04:09:04Z",  
    "value": 0.21921580436899846  
  },  
  "primaryFrequency": {  
    "type": "Property",  
    "unitCode": "Hz",  
    "observedAt": "2023-01-26T11:27:17Z",  
    "value": 0.8873577584995188  
  },  
  "primaryVoltage": {  
    "type": "Property",  
    "unitCode": "W/A",  
    "observedAt": "2023-01-26T07:23:40Z",  
    "value": 0.33421317836814646  
  },  
  "realImpedanceRatio": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T03:38:23Z",  
    "value": 0.6061321069719529  
  },  
  "secondaryApparentPower": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-25T19:57:55Z",  
    "value": 0.3997980055591537  
  },  
  "secondaryCurrent": {  
    "type": "Property",  
    "unitCode": "A",  
    "observedAt": "2023-01-26T13:58:27Z",  
    "value": 0.2899846616898377  
  },  
  "secondaryCurrentType": {  
    "type": "Property",  
    "value": "human-resource"  
  },  
  "secondaryFrequency": {  
    "type": "Property",  
    "unitCode": "Hz",  
    "observedAt": "2023-01-26T03:39:16Z",  
    "value": 0.06983160765779406  
  },  
  "secondaryVoltage": {  
    "type": "Property",  
    "unitCode": "W/A",  
    "observedAt": "2023-01-26T07:19:14Z",  
    "value": 0.8594539881916403  
  },  
  "transformerVectorGroup": {  
    "type": "Property",  
    "value": "digital"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:ded8c891-dfe1-4973-966c-96ab6231373d"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:aab67381-2a15-4bdc-ab0f-953b17253b8f"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:d06b6674-162c-4593-a8fd-3874ef353008"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:d0aca3bd-bf1b-4e9e-a998-a76c9b1ac7a6"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:1ab049a0-7295-4eef-82a1-0bb422132435"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Transformer Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Transformer 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T06:32:52Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T05:11:11Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Transformer"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Transformer type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Transformer of limited Transformer types"  
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
