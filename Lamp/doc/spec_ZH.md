<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：灯  
====<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Lamp/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球说明：**灯是一种人造光源，如灯泡或灯管。  
版本： 0.0。  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理    
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `colorAppearance[string]`: 在 DIN 和 CIE 标准中，人工光源都是根据其颜色外观进行分类的。对人眼而言，它们看起来都是白色的，只有通过直接比较才能发现其中的差别。色彩外观的差异不会直接影响视觉效果  - `colorRenderingIndex[number]`: CRI 表示与色温相同的完美参考灯相比，光源呈现八种标准色的程度。CRI 的范围从 1 到 100，100 代表完美的呈现特性  - `colorTemperature[number]`: 任何辐射源的色温都被定义为黑体或普朗克辐射器的温度（开尔文），其辐射色度与辐射源相同。由于黑体辐射器不可能发出每种色度值的辐射，因此其值通常只是近似色温。最常见的人造光源的色温范围从小于 3000K（暖白）到 4000K（中等）和超过 5000K（日光）。通常以开氏度（K）为单位进行测量  - `contributedLuminousFlux[number]`: 光通量是对辐射通量的光度测量，即光源发出的光量。光通量的测量可以是室内整体光通量的测量，也可以是室内部分光通量的测量（实体角的部分光通量）。所有其他光度参数都是光通量的导数。光通量的单位是流明（lm）。每个灯泡的光通量都有一个标称值。通常以流明（lm）、坎德拉（Candela Steradian）为单位。  - `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `hasManufacturer[string]`: 标识实体（如设备）制造商的关系。该值应为字符串或带有语言标记的字符串。  - `hasModel[string]`: 标识实体（如设备）模型的关系。该值应是字符串或带有语言标记的字符串  - `id[*]`: 实体的唯一标识符  - `isContainedInBuildingSpace[*]`: 用于定义楼宇物理空间的实体。建筑空间包含设备或建筑对象。(建筑空间）  - `isContainedInPhysicalObject[*]`: 任何具有适当空间区域的物体。  (从 DUL 本体中提取的定义）（物理对象）  - `isSubSystemOf[array]`: 该物理对象所属系统的引用  - `lampBallastType[string]`: 镇流器用于在运行期间通过限制电流来稳定气体放电，并为启动提供必要的启动电压。荧光灯、紧凑型荧光灯、高压汞灯、金属卤化物灯和高压钠灯等放电灯都需要使用镇流器。电感镇流器是一种扼流圈，根据自感原理限制通过串联灯管的电流。由此产生的电流和功率对灯管的高效运行起着决定性作用。每种类型的灯管都需要专门设计的镇流器，以符合灯管在光通量、外观颜色和使用寿命方面的额定值。荧光灯镇流器分为 KVG 传统型（EC-A 系列）和 VVG 低损耗型（EC-B 系列）两种。低损耗镇流器的效率更高，这意味着镇流器损耗更小，热负荷更低。电子镇流器用于在高频率（约 35 - 40 kHz）下运行荧光灯。  - `lampCompensationType[string]`: 确定用于功率因数校正和无线电抑制的补偿形式  - `lampMaintenanceFactor[number]`: 因灯泡折旧（即灯具老化和污垢导致光输出下降）而造成的不可回收的灯泡光通量损失  - `lightEmitterNominalPower[number]`: 光发射器的额定功率。通常以瓦特（W，J/s）为计量单位  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `spectrumMax[number]`: 辐射光谱描述了辐射波长的组成。例如，人眼可见的那部分电磁辐射是波长在大约 380 到 780 nm（1 nm = 10 m）范围内的辐射。相应的颜色范围从紫色到靛蓝、蓝色、绿色、黄色、橙色和红色。这些颜色形成一个连续光谱，其中各个光谱段相互融合  - `spectrumMin[number]`: 辐射光谱描述了辐射波长的组成。例如，人眼可见的那部分电磁辐射是波长在大约 380 到 780 nm（1 nm = 10 m）范围内的辐射。相应的颜色范围从紫色到靛蓝、蓝色、绿色、黄色、橙色和红色。这些颜色形成一个连续光谱，其中各个光谱段相互融合  - `type[string]`: 必须等于 `Lamp`  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排列（点击查看详情）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Lamp:    
  description: A lamp is an artificial light source such as a light bulb or tube.    
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
    colorAppearance:    
      description: 'In both the DIN and CIE standards, artificial light sources are classified in terms of their color appearance. To the human eye they all appear to be white the difference can only be detected by direct comparison. Visual performance is not directly affected by differences in color appearance'    
      type: string    
      x-ngsi:    
        type: Property    
    colorRenderingIndex:    
      description: 'The CRI indicates how well a light source renders eight standard colors compared to perfect reference lamp with the same color temperature. The CRI scale ranges from 1 to 100, with 100 representing perfect rendering properties'    
      type: number    
      x-ngsi:    
        type: Property    
    colorTemperature:    
      description: The color temperature of any source of radiation is defined as the temperature (in Kelvin) of a black-body or Planckian radiator whose radiation has the same chromaticity as the source of radiation. Often the values are only approximate color temperatures as the black-body radiator cannot emit radiation of every chromaticity value. The color temperatures of the commonest artificial light sources range from less than 3000K (warm white) to 4000K (intermediate) and over 5000K (daylight). Usually measured in degrees Kelvin (K)    
      type: number    
      x-ngsi:    
        type: Property    
    contributedLuminousFlux:    
      description: 'Luminous flux is a photometric measure of radiant flux, i.e. the volume of light emitted from a light source. Luminous flux is measured either for the interior as a whole or for a part of the interior (partial luminous flux for a solid angle). All other photometric parameters are derivatives of luminous flux. Luminous flux is measured in lumens (lm). The luminous flux is given as a nominal value for each lamp. Usually measured in Lumen (lm, Candela Steradian)'    
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
    lampBallastType:    
      description: 'The type of ballast used to stabilise gas discharge by limiting the current during operation and to deliver the necessary striking voltage for starting. Ballasts are needed to operate Discharge Lamps such as Fluorescent, Compact Fluorescent, High-pressure Mercury, Metal Halide and High-pressure Sodium Lamps. Magnetic ballasts are chokes which limit the current passing through a lamp connected in series on the principle of self-induction. The resultant current and power are decisive for the efficient operation of the lamp. A specially designed ballast is required for every type of lamp to comply with lamp rating in terms of Luminous Flux, Color Appearance and service life. The two types of magnetic ballasts for fluorescent lamps are KVG Conventional (EC-A series) and VVG Low-loss ballasts (EC-B series). Low-loss ballasts have a higher efficiency, which means reduced ballast losses and a lower thermal load. Electronic ballasts are used to run fluorescent lamps at high frequencies (approx. 35 - 40 kHz)'    
      type: string    
      x-ngsi:    
        type: Property    
    lampCompensationType:    
      description: Identifies the form of compensation used for power factor correction and radio suppression    
      type: string    
      x-ngsi:    
        type: Property    
    lampMaintenanceFactor:    
      description: Non recoverable losses of luminous flux of a lamp due to lamp depreciation i.e. the decreasing of light output of a luminaire due to aging and dirt    
      type: number    
      x-ngsi:    
        type: Property    
    lightEmitterNominalPower:    
      description: 'Light emitter nominal power. Usually measured in Watts (W, J/s)'    
      type: number    
      x-ngsi:    
        type: Property    
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
    spectrumMax:    
      description: 'The spectrum of radiation describes its composition with regard to wavelength. Light, for example, as the portion of electromagnetic radiation that is visible to the human eye, is radiation with wavelengths in the range of approx. 380 to 780 nm (1 nm = 10 m). The corresponding range of colours varies from violet to indigo, blue, green, yellow, orange, and red. These colours form a continuous spectrum, in which the various spectral sectors merge into each other'    
      type: number    
      x-ngsi:    
        type: Property    
    spectrumMin:    
      description: 'The spectrum of radiation describes its composition with regard to wavelength. Light, for example, as the portion of electromagnetic radiation that is visible to the human eye, is radiation with wavelengths in the range of approx. 380 to 780 nm (1 nm = 10 m). The corresponding range of colours varies from violet to indigo, blue, green, yellow, orange, and red. These colours form a continuous spectrum, in which the various spectral sectors merge into each other'    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: It must be equal to `Lamp`    
      enum:    
        - Lamp    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Lamp"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Lamp/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Lamp/schema.json    
  x-model-tags: SAREF Lamp    
  x-version: 0.0.    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 有效载荷示例  
#### 灯 NGSI-v2 键值示例  
下面是一个以 JSON-LD 格式作为键值的灯的示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Lamp:732d4c91-579b-4ff8-b6f1-fcc429bcc3d7",  
    "type": "Lamp",  
    "colorAppearance": "Washington",  
    "colorRenderingIndex": 0.8153696255721333,  
    "colorTemperature": 0.09664075512365078,  
    "contributedLuminousFlux": 0.9207573270583412,  
    "lampBallastType": "Cape",  
    "lampCompensationType": "systematic",  
    "lampMaintenanceFactor": 0.4913004655459732,  
    "lightEmitterNominalPower": 0.2998024622331251,  
    "spectrumMax": 0.2518554879273158,  
    "spectrumMin": 0.7386218055211833,  
    "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:eb3dae30-05b0-44ba-8c58-172cd5f7b96e",  
    "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:5b981637-1f0e-41ac-b72d-4bc21f2bb629",  
    "isSubSystemOf": [  
        "urn:ngsi-ld:System:66da3c56-f167-4dd1-8691-9fea4013aa22",  
        "urn:ngsi-ld:System:1cab8165-219d-49db-823b-5eae961620c5",  
        "urn:ngsi-ld:System:76285f6c-9a86-48a1-94dd-e379a4fe4394"  
    ],  
    "hasManufacturer": "Lamp Company Inc.",  
    "hasModel": "Lamp 0.1.2",  
    "dateCreated": "2023-01-25T18:30:26Z",  
    "dateModified": "2023-01-25T16:57:18Z",  
    "source": "Import",  
    "name": "Lamp",  
    "alternateName": "Lamp type 2",  
    "description": "Lamp of limited Lamp types",  
    "dataProvider": "IFC file"  
}  
```  
</details>  
#### 灯具 NGSI-v2 标准化示例  
下面是一个规范化 JSON-LD 格式的 Lamp 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Lamp:e4e06bbb-5963-421b-b721-afbec54cf22e",  
  "type": "Lamp",  
  "colorAppearance": {  
    "type": "Text",  
    "value": "intranet"  
  },  
  "colorRenderingIndex": {  
    "type": "Float",  
    "value": 0.9381317485666679  
  },  
  "colorTemperature": {  
    "type": "Measurement",  
    "value":  0.162971670454518  
  },  
  "contributedLuminousFlux": {  
    "type": "Measurement",  
    "value":  0.9333222274075583  
  },  
  "lampBallastType": {  
    "type": "Text",  
    "value": "Intelligent"  
  },  
  "lampCompensationType": {  
    "type": "Text",  
    "value": "Web"  
  },  
  "lampMaintenanceFactor": {  
    "type": "Measurement",  
    "value":  0.7734465932124935  
  },  
  "lightEmitterNominalPower": {  
    "type": "Measurement",  
    "value":  0.34992609812300746  
  },  
  "spectrumMax": {  
    "type": "Measurement",  
    "value":  0.7513509645742688  
  },  
  "spectrumMin": {  
    "type": "Measurement",  
    "value":  0.6531361967308142  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:BuildingSpace:7f2b0435-7136-42aa-a3f5-14d718fe167b"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:PhysicalObject:870d927a-894d-443c-8202-a3f85d8010eb"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:21b3835c-564a-4b0c-9dc3-0f0e67489ad0"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:dfe58786-fa48-479c-97a9-09656f1751df"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:392b7d40-d54f-4e86-946f-7c89af254076"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Lamp Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Lamp 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T19:38:30.2179353+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T15:39:19.6056355+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Lamp"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Lamp type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Lamp of limited Lamp types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### 灯具 NGSI-LD 键值示例  
下面是一个以 JSON-LD 格式作为键值的灯的示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Lamp:732d4c91-579b-4ff8-b6f1-fcc429bcc3d7",  
  "type": "Lamp",  
  "colorAppearance": "Washington",  
  "colorRenderingIndex": 0.8153696255721333,  
  "colorTemperature": 0.09664075512365078,  
  "contributedLuminousFlux": 0.9207573270583412,  
  "lampBallastType": "Cape",  
  "lampCompensationType": "systematic",  
  "lampMaintenanceFactor": 0.4913004655459732,  
  "lightEmitterNominalPower": 0.2998024622331251,  
  "spectrumMax": 0.2518554879273158,  
  "spectrumMin": 0.7386218055211833,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:eb3dae30-05b0-44ba-8c58-172cd5f7b96e",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:5b981637-1f0e-41ac-b72d-4bc21f2bb629",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:66da3c56-f167-4dd1-8691-9fea4013aa22",  
    "urn:ngsi-ld:System:1cab8165-219d-49db-823b-5eae961620c5",  
    "urn:ngsi-ld:System:76285f6c-9a86-48a1-94dd-e379a4fe4394"  
  ],  
  "hasManufacturer": "Lamp Company Inc.",  
  "hasModel": "Lamp 0.1.2",  
  "dateCreated": "2023-01-25T18:30:26Z",  
  "dateModified": "2023-01-25T16:57:18Z",  
  "source": "Import",  
  "name": "Lamp",  
  "alternateName": "Lamp type 2",  
  "description": "Lamp of limited Lamp types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### 灯具 NGSI-LD 标准化示例  
下面是一个规范化 JSON-LD 格式灯的示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Lamp:a14c597e-ec02-4db5-aad5-6107d6435015",  
  "type": "Lamp",  
  "colorAppearance": {  
    "type": "Property",  
    "value": "card"  
  },  
  "colorRenderingIndex": {  
    "type": "Property",  
    "value": 0.6745960848595047  
  },  
  "colorTemperature": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T05:53:48Z",  
    "value": 0.03839635886669124  
  },  
  "contributedLuminousFlux": {  
    "type": "Property",  
    "unitCode": "Steradian",  
    "observedAt": "2023-01-26T12:44:07Z",  
    "value": 0.43828304543957874  
  },  
  "lampBallastType": {  
    "type": "Property",  
    "value": "mobile"  
  },  
  "lampCompensationType": {  
    "type": "Property",  
    "value": "seize"  
  },  
  "lampMaintenanceFactor": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T06:20:56Z",  
    "value": 0.035996560482205564  
  },  
  "lightEmitterNominalPower": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-25T17:44:26Z",  
    "value": 0.3144630350336074  
  },  
  "spectrumMax": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-25T17:43:19Z",  
    "value": 0.5533105661727246  
  },  
  "spectrumMin": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-25T16:58:44Z",  
    "value": 0.3399337921412814  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:550d9127-0996-4282-af73-1a7cbef3bee7"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:6fc10ce2-d07f-4837-9104-c17e7b33b812"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:a76465e2-2473-4048-849b-8f59eb40e19e"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:eaa2ffb0-4ea6-4904-a271-01c8cb171034"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:dc605242-4054-4fc8-89ba-8bce59724d02"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Lamp Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Lamp 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T21:41:50Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-25T17:39:08Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Lamp"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Lamp type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Lamp of limited Lamp types"  
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
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
