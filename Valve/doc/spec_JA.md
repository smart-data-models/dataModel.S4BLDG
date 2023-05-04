<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティバルブ  
=========<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Valve/LICENSE.md)  
[文書が自動的に生成されます](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description：**バルブは、ビルサービス配管分配システムにおいて、流体の流れを制御または調節するために使用されます。  
バージョン：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性に型がない場合は、複数の型や異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: このアイテムの別称  - `areaServed[string]`: サービスまたは提供されるアイテムが提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `closeOffRating[number]`: プロパティです。クローズオフ定格。通常、パスカル（Pa、N/m2）で測定される。  - `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: このアイテムの説明  - `flowCoefficient[number]`: 特性。流量係数（単位圧力損失で全開のバルブを通過する流体の量）。通常、バルブのKvまたはCv値として表される。  - `hasManufacturer[string]`: プロパティ。エンティティ（例：デバイス）の製造者を特定する関係。値は、文字列または言語タグ付き文字列であることが期待される。  - `hasModel[string]`: プロパティです。エンティティ（例：デバイス）のモデルを識別する関係。値は、文字列または言語タグ付き文字列であることが期待される。  - `id[*]`: エンティティの一意な識別子  - `isContainedInBuildingSpace[*]`: 関係。建物の物理的空間を定義するために使用されるエンティティ。ビルディングスペースは、デバイスまたはビルディングオブジェクトを含む。(ビルディングスペース)  - `isContainedInPhysicalObject[*]`: 関係です。適切な空間領域を持つあらゆるオブジェクト。  (DULオントロジーから抽出した定義）（PhysicalObject)  - `isSubSystemOf[array]`: 関係。この物理オブジェクトが属するシステム（複数可）への参照。  - `location[*]`: アイテムへの Geojson 参照。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon のいずれかである。  - `name[string]`: この項目の名称です。  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリストです。  - `seeAlso[*]`: アイテムに関する追加リソースを指す URI のリスト。  - `size[number]`: 物件です。バルブへの接続部（蛇口、混合弁などの場合は各接続部）の大きさ。通常、ミリメートル（mm）単位で測定される。  - `source[string]`: エンティティデータの元のソースをURLとして与える一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `testPressure[number]`: 特性を示す。バルブが試験中に受けた最大圧力。通常、パスカル（Pa、N/m2）で測定される。  - `type[string]`: プロパティを指定します。これは `Valve` と等しくなければならない。  - `valveMechanism[string]`: 特性です。バルブの機能が達成されるメカニズムがどこにあるのか：BALL： ボディシートポートに対して相対的に回転可能なポート付きボールを持つバルブ。BUTTERFLY: 流線型のディスクが直径方向の軸を中心に回動するバルブ。コンフィギュレーションゲート：バルブ全体の圧力と流量の変化をより正確に制御するために、閉鎖ゲートが構成された方法で形成されているねじ込みバルブ。グランド：テーパー状の座面を持つバルブで、回転可能なプラグがグランドとグランドパッキンによって保持されている。GLOBE (グローブ)球状のボディを持つスクリューダウンバルブ。LUBRICATEDPLUG: プラグ面とボディの間に潤滑剤が圧力下で注入されるプラグバルブ。NEEDLE: パイプの中やパイプからの流れを調整するためのバルブで、細長い円錐が流れの軸に沿って動き、固定された円錐形のシートに対して閉じるようになっている。パラレルスライド（PARALLELSLIDE）：機械加工されたプレートが、形成された溝をスライドしてシールを形成するねじ込み式バルブ。PLUG: ボディシートポートに対して回転可能なポート付きプラグを持つバルブ。WEDGEGATE: テーパーガイドにフィットするウェッジ形状のプレートを持ち、シールを形成するスクリューダウンバルブ。  - `valveOperation[string]`: 特性を有する。という弁の作動方法：フロート： 水位によって上下するフロートの作用によって開閉するバルブ。フロートは，レバーやその他の機構に取り付けられたボールであることもある HYDRAULIC： 油圧作動によって開閉するバルブ LEVER： 油圧作動によって開閉するバルブレバーの作用でバルブ内のゲートを回転させることで開閉するバルブ。ロックシールド：開閉に特殊なロックシールドキーを使用する必要があるバルブで、通常運転時は操作機構がシュラウドで保護されています。モーターライズド（MOTORIZED）：モータライズド：アクチュエータの電動モータの動作により開閉するバルブ。 ニューマチック：空気圧の作動により開閉するバルブ。 ソレノイド：通常、アクチュエータにより開閉するバルブ：ゲートに作用するコイルの磁界によって通常開いた状態に保たれるが、磁界を発生させる電流が取り除かれると直ちに閉じるバルブ。スプリング（SPRING）：通常、プレート上のスプリングの圧力によって位置を保持されるが、流体の圧力がスプリングの圧力に打ち勝つのに十分であれば、開くようになる可能性があるバルブ。サーモスタット：必要な所定の温度を維持するために、ポートが開閉されるバルブ。ホイール：バルブ内のゲートを動かすホイールの作用により、開閉するバルブ。  - `valvePattern[string]`: 特性。バルブ内を流れる流体が通る直線的な経路、またはポートの数によって、バルブのポートが構成されていること：SINGLEPORT（シングルポート）：バルブが使用するシステムからの入口ポートが1つで、出口ポートが周囲の環境へ向かうバルブ。ANGLED_2_PORT： 流れの方向が 90 度変化するバルブ。STRAIGHT_2_PORT：流れが直進するバルブ。STRAIGHT_3_PORT：3つのポートに分かれているバルブ。CROSSOVER_4_PORT：4つのポートに分かれたバルブ。  - `workingPressure[number]`: 特性を示す。バルブの通常予想される最高使用圧力。通常、パスカル（Pa、N/m2）で測定される。  <!-- /30-PropertiesList -->  
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
Valve:    
  description: A valve is used in a building services piping distribution system to control or modulate the flow of the fluid.    
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
    flowCoefficient:    
      description: 'Property. Flow coefficient (the quantity of fluid that passes through a fully open valve at unit pressure drop), typically expressed as the Kv or Cv value for the valve.'    
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
    id:    
      anyOf: &valve_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      anyOf: *valve_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *valve_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *valve_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
        anyOf: *valve_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    size:    
      description: 'Property. The size of the connection to the valve (or to each connection for faucets, mixing valves, etc.). Usually measured in millimeters (mm).'    
      type: number    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    testPressure:    
      description: 'Property. The maximum pressure to which the valve has been subjected under test. Usually measured in Pascals (Pa, N/m2).'    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: Property. It must be equal to `Valve`.    
      enum:    
        - Valve    
      type: string    
      x-ngsi:    
        type: Property    
    valveMechanism:    
      description: 'Property. The mechanism by which the valve function is achieved where: BALL: Valve that has a ported ball that can be turned relative to the body seat ports. BUTTERFLY: Valve in which a streamlined disc pivots about a diametric axis. CONFIGUREDGATE: Screwdown valve in which the closing gate is shaped in a configured manner to have a more precise control of pressure and flow change across the valve. GLAND: Valve with a tapered seating, in which a rotatable plug is retained by means of a gland and gland packing. GLOBE: Screwdown valve that has a spherical body. LUBRICATEDPLUG: Plug valve in which a lubricant is injected under pressure between the plug face and the body. NEEDLE: Valve for regulating the flow in or from a pipe, in which a slender cone moves along the axis of flow to close against a fixed conical seat. PARALLELSLIDE: Screwdown valve that has a machined plate that slides in formed grooves to form a seal. PLUG: Valve that has a ported plug that can be turned relative to the body seat ports. WEDGEGATE: Screwdown valve that has a wedge shaped plate fitting into tapered guides to form a seal.'    
      type: string    
      x-ngsi:    
        type: Property    
    valveOperation:    
      description: 'Property. The method of valve operation where: DROPWEIGHT: A valve that is closed by the action of a weighted lever being released, the weight normally being prevented from dropping by being held by a wire, the closure normally being made by the action of heat on a fusible link in the wire FLOAT: A valve that is opened and closed by the action of a float that rises and falls with water level. The float may be a ball attached to a lever or other mechanism HYDRAULIC: A valve that is opened and closed by hydraulic actuation LEVER: A valve that is opened and closed by the action of a lever rotating the gate within the valve. LOCKSHIELD: A valve that requires the use of a special lockshield key for opening and closing, the operating mechanism being protected by a shroud during normal operation. MOTORIZED: A valve that is opened and closed by the action of an electric motor on an actuator PNEUMATIC: A valve that is opened and closed by pneumatic actuation SOLENOID: A valve that is normally held open by a magnetic field in a coil acting on the gate but that is closed immediately if the electrical current generating the magnetic field is removed. SPRING: A valve that is normally held in position by the pressure of a spring on a plate but that may be caused to open if the pressure of the fluid is sufficient to overcome the spring pressure. THERMOSTATIC: A valve in which the ports are opened or closed to maintain a required predetermined temperature. WHEEL: A valve that is opened and closed by the action of a wheel moving the gate within the valve.'    
      type: string    
      x-ngsi:    
        type: Property    
    valvePattern:    
      description: 'Property. The configuration of the ports of a valve according to either the linear route taken by a fluid flowing through the valve or by the number of ports where: SINGLEPORT: Valve that has a single entry port from the system that it serves, the exit port being to the surrounding environment. ANGLED_2_PORT: Valve in which the direction of flow is changed through 90 degrees. STRAIGHT_2_PORT: Valve in which the flow is straight through. STRAIGHT_3_PORT: Valve with three separate ports. CROSSOVER_4_PORT: Valve with 4 separate ports.'    
      type: string    
      x-ngsi:    
        type: Property    
    workingPressure:    
      description: 'Property. The normally expected maximum working pressure of the valve. Usually measured in Pascals (Pa, N/m2).'    
      type: number    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Valve"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Valve/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Valve/schema.json    
  x-model-tags: SAREF Valve    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### バルブNGSI-v2キーバリュー例  
ここでは、ValveをJSON-LD形式でkey-valuesとした例を示す。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Valve:5606802d-9bfc-41f4-b6cb-7a2dc52214ea",  
    "type": "Valve",  
    "closeOffRating": 0.9792941241344664,  
    "flowCoefficient": 0.825533650257277,  
    "size": 0.7178529493113952,  
    "testPressure": 0.9690729968605641,  
    "valveMechanism": "Greece",  
    "valveOperation": "auxiliary",  
    "valvePattern": "Consultant",  
    "workingPressure": 0.8773888966189294,  
    "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:c2e1097b-602a-49ef-b81e-73687c4868b3",  
    "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:663b3745-acf8-4b86-ab69-693afe57cf2c",  
    "isSubSystemOf": [  
        "urn:ngsi-ld:System:9ec35827-e00f-461e-8f22-5cd758f7f7f6",  
        "urn:ngsi-ld:System:aac7e87c-55fe-4c45-88aa-1cb36e3512f9",  
        "urn:ngsi-ld:System:a4adbc73-68e8-43c6-b366-adc5ffb0e4f8"  
    ],  
    "hasManufacturer": "Valve Company Inc.",  
    "hasModel": "Valve 0.1.2",  
    "dateCreated": "2023-01-25T17:39:28Z",  
    "dateModified": "2023-01-26T11:24:20Z",  
    "source": "Import",  
    "name": "Valve",  
    "alternateName": "Valve type 2",  
    "description": "Valve of limited Valve types",  
    "dataProvider": "IFC file"  
}  
```  
</details>  
#### Valve NGSI-v2 正規化例  
JSON-LD形式のValveを正規化した例を示します。これは、オプションを使用しない場合のNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Valve:5384a157-cc2a-4984-b4ed-4273d58990da",  
  "type": "Valve",  
  "closeOffRating": {  
    "type": "Measurement",  
    "value":  0.6442998208642058  
  },  
  "flowCoefficient": {  
    "type": "Measurement",  
    "value": 0.9502368316657622  
  },  
  "size": {  
    "type": "Measurement",  
    "value": 0.1757245625885473  
  },  
  "testPressure": {  
    "type": "Measurement",  
    "value":  0.3547642349477015  
  },  
  "valveMechanism": {  
    "type": "Text",  
    "value": "Comoro Franc"  
  },  
  "valveOperation": {  
    "type": "Text",  
    "value": "capacity"  
  },  
  "valvePattern": {  
    "type": "Text",  
    "value": "Regional"  
  },  
  "workingPressure": {  
    "type": "Measurement",  
    "value":  0.7616536973295315  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:BuildingSpace:4c2121a4-e126-4cee-bd63-517a31e19d0c"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:PhysicalObject:3b7bbebe-aa67-4d67-991d-8360e38cb075"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:a3691c28-c6b1-4dbd-8781-58c369f780f2"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:bd7d12e5-25ef-474b-93af-bba6ebef4782"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:0ee8b6da-5507-42c2-a80d-eaea8b13a894"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Valve Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Valve 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T15:00:30.8255456+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T14:02:17.0152497+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Valve"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Valve type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Valve of limited Valve types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### バルブ NGSI-LD キー値例  
ここでは、ValveをJSON-LD形式でkey-valuesとした例を示します。これは、`options=keyValues`を使用した場合にNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Valve:5606802d-9bfc-41f4-b6cb-7a2dc52214ea",  
  "type": "Valve",  
  "closeOffRating": 0.9792941241344664,  
  "flowCoefficient": 0.825533650257277,  
  "size": 0.7178529493113952,  
  "testPressure": 0.9690729968605641,  
  "valveMechanism": "Greece",  
  "valveOperation": "auxiliary",  
  "valvePattern": "Consultant",  
  "workingPressure": 0.8773888966189294,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:c2e1097b-602a-49ef-b81e-73687c4868b3",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:663b3745-acf8-4b86-ab69-693afe57cf2c",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:9ec35827-e00f-461e-8f22-5cd758f7f7f6",  
    "urn:ngsi-ld:System:aac7e87c-55fe-4c45-88aa-1cb36e3512f9",  
    "urn:ngsi-ld:System:a4adbc73-68e8-43c6-b366-adc5ffb0e4f8"  
  ],  
  "hasManufacturer": "Valve Company Inc.",  
  "hasModel": "Valve 0.1.2",  
  "dateCreated": "2023-01-25T17:39:28Z",  
  "dateModified": "2023-01-26T11:24:20Z",  
  "source": "Import",  
  "name": "Valve",  
  "alternateName": "Valve type 2",  
  "description": "Valve of limited Valve types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### バルブ NGSI-LD 正規化例  
JSON-LD形式のValveを正規化した例を示します。これは、オプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Valve:ca643e8d-ccbe-4bc2-a132-c5a51578501a",  
  "type": "Valve",  
  "closeOffRating": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-25T21:38:33Z",  
    "value": 0.4968075534065832  
  },  
  "flowCoefficient": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T07:44:38Z",  
    "value": 0.3336750880832986  
  },  
  "size": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T10:49:30Z",  
    "value": 0.686759934652535  
  },  
  "testPressure": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-26T10:54:40Z",  
    "value": 0.2729778598678245  
  },  
  "valveMechanism": {  
    "type": "Property",  
    "value": "SSL"  
  },  
  "valveOperation": {  
    "type": "Property",  
    "value": "navigate"  
  },  
  "valvePattern": {  
    "type": "Property",  
    "value": "Central"  
  },  
  "workingPressure": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-26T10:53:59Z",  
    "value": 0.9890036767805558  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:ef5535ea-a226-4e13-ad18-534fe0998b5e"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:269255de-ebf6-4014-b255-7769687247ae"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:3199df5c-0c82-41fa-8c1c-450850408792"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:756104c3-38c5-400b-9598-4a604d9415e1"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:e8b9c356-91e3-4ff9-a98c-5bcae397ed67"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Valve Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Valve 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T16:14:40Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T03:09:51Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Valve"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Valve type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Valve of limited Valve types"  
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
