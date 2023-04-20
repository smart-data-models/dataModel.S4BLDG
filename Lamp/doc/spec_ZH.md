<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：灯具  
=====<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Lamp/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述：**灯是一种人工光源，如灯泡或灯管。  
版本：0.0。  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `colorAppearance[string]`: 属性。在DIN和CIE标准中，人工光源都是按其颜色外观来分类的。在人眼看来，它们都是白色的，只有通过直接比较才能发现差异。视觉性能并不直接受到颜色外观差异的影响。  - `colorRenderingIndex[number]`: 属性。CRI表示与相同色温的完美参考灯相比，一个光源对八种标准颜色的渲染程度。CRI的范围从1到100，100代表完美的渲染特性。  - `colorTemperature[object]`: 属性。任何辐射源的色温被定义为黑体或普朗克辐射器的温度（开尔文），其辐射与辐射源的色度相同。通常情况下，这些值只是近似的色温，因为黑体辐射器不可能发出每种色度值的辐射。最常见的人工光源的色温范围从低于3000K（暖白）到4000K（中间）和超过5000K（日光）。通常以开尔文度（K）来衡量。  - `contributedLuminousFlux[object]`: 属性。光通量是对辐射通量的光度测量，即从一个光源发出的光量。光通量的测量是针对内部的整体或内部的一部分（实心角的部分光通量）。所有其他测光参数都是光通量的导数。光通量的单位是流明（lm）。光通量是作为每个灯的标称值给出的。通常以流明（lm，Candela Steradian）来衡量。  - `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `hasManufacturer[string]`: 属性。识别实体（例如，设备）的制造商的关系。该值应是一个字符串或一个带有语言标签的字符串。  - `hasModel[string]`: 属性。识别实体（例如，设备）的模型的关系。该值应是一个字符串或一个带有语言标签的字符串。  - `id[*]`: 实体的唯一标识符  - `isContainedInBuildingSpace[*]`: 关系。一个用于定义建筑物理空间的实体。一个建筑空间包含设备或建筑对象。(建筑空间)  - `isContainedInPhysicalObject[*]`: 关系。任何具有适当空间区域的物体。  (从DUL本体论中提取的定义）（PhysicalObject）。  - `isSubSystemOf[array]`: 关系。对该物理对象是其一部分的系统的引用。  - `lampBallastType[string]`: 属性。镇流器的类型，用于在运行期间通过限制电流来稳定气体放电，并为启动提供必要的冲击电压。荧光灯、紧凑型荧光灯、高压水银灯、金属卤化物灯和高压钠灯等放电灯需要使用镇流器。电感镇流器是一种扼流圈，它根据自感应原理限制通过串联的灯管的电流。由此产生的电流和功率对灯的有效运行具有决定性作用。每种类型的灯都需要一个专门设计的镇流器，以符合灯在光通量、色彩外观和使用寿命方面的额定要求。荧光灯的电感镇流器有两种类型：KVG传统型（EC-A系列）和VVG低损耗镇流器（EC-B系列）。低损耗镇流器具有更高的效率，这意味着减少了镇流器的损耗，降低了热负荷。电子镇流器用于在高频率（约35 - 40 kHz）下运行荧光灯。  - `lampCompensationType[string]`: 属性。确定了用于功率因数校正和无线电抑制的补偿形式。  - `lampMaintenanceFactor[object]`: 财产。由于灯管折旧而造成的不可恢复的光通量损失，即由于老化和灰尘造成的灯具光输出的减少。  - `lightEmitterNominalPower[object]`: 属性。光发射器的额定功率。通常以瓦特（W，J/s）为单位测量。  - `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `name[string]`: 这个项目的名称。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `spectrumMax[object]`: 属性。辐射的光谱描述了它在波长方面的组成。例如，作为电磁辐射中人眼可见的部分，光是波长在大约380至780纳米（1纳米=10米）范围内的辐射。相应的颜色范围从紫罗兰到靛蓝、蓝色、绿色、黄色、橙色和红色不等。这些颜色形成了一个连续的光谱，其中不同的光谱部门相互融合。  - `spectrumMin[object]`: 属性。辐射的光谱描述了它在波长方面的组成。例如，作为电磁辐射中人眼可见的部分，光是波长在大约380至780纳米（1纳米=10米）范围内的辐射。相应的颜色范围从紫罗兰到靛蓝、蓝色、绿色、黄色、橙色和红色不等。这些颜色形成了一个连续的光谱，其中不同的光谱部门相互融合。  - `type[string]`: 属性。它必须等于 "Lamp"。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
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
    colorAppearance:    
      description: 'Property. In both the DIN and CIE standards, artificial light sources are classified in terms of their color appearance. To the human eye they all appear to be white the difference can only be detected by direct comparison. Visual performance is not directly affected by differences in color appearance.'    
      type: string    
      x-ngsi:    
        type: Property    
    colorRenderingIndex:    
      description: 'Property. The CRI indicates how well a light source renders eight standard colors compared to perfect reference lamp with the same color temperature. The CRI scale ranges from 1 to 100, with 100 representing perfect rendering properties.'    
      type: number    
      x-ngsi:    
        type: Property    
    colorTemperature:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: Property. The color temperature of any source of radiation is defined as the temperature (in Kelvin) of a black-body or Planckian radiator whose radiation has the same chromaticity as the source of radiation. Often the values are only approximate color temperatures as the black-body radiator cannot emit radiation of every chromaticity value. The color temperatures of the commonest artificial light sources range from less than 3000K (warm white) to 4000K (intermediate) and over 5000K (daylight). Usually measured in degrees Kelvin (K).    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: &lamp_-_properties_-_contributedluminousflux_-_properties    
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
    contributedLuminousFlux:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: 'Property. Luminous flux is a photometric measure of radiant flux, i.e. the volume of light emitted from a light source. Luminous flux is measured either for the interior as a whole or for a part of the interior (partial luminous flux for a solid angle). All other photometric parameters are derivatives of luminous flux. Luminous flux is measured in lumens (lm). The luminous flux is given as a nominal value for each lamp. Usually measured in Lumen (lm, Candela Steradian).'    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *lamp_-_properties_-_contributedluminousflux_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
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
      anyOf: &lamp_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      anyOf: *lamp_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *lamp_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *lamp_-_properties_-_iscontainedinbuildingspace_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Relationship    
    lampBallastType:    
      description: 'Property. The type of ballast used to stabilise gas discharge by limiting the current during operation and to deliver the necessary striking voltage for starting. Ballasts are needed to operate Discharge Lamps such as Fluorescent, Compact Fluorescent, High-pressure Mercury, Metal Halide and High-pressure Sodium Lamps. Magnetic ballasts are chokes which limit the current passing through a lamp connected in series on the principle of self-induction. The resultant current and power are decisive for the efficient operation of the lamp. A specially designed ballast is required for every type of lamp to comply with lamp rating in terms of Luminous Flux, Color Appearance and service life. The two types of magnetic ballasts for fluorescent lamps are KVG Conventional (EC-A series) and VVG Low-loss ballasts (EC-B series). Low-loss ballasts have a higher efficiency, which means reduced ballast losses and a lower thermal load. Electronic ballasts are used to run fluorescent lamps at high frequencies (approx. 35 - 40 kHz).'    
      type: string    
      x-ngsi:    
        type: Property    
    lampCompensationType:    
      description: Property. Identifies the form of compensation used for power factor correction and radio suppression.    
      type: string    
      x-ngsi:    
        type: Property    
    lampMaintenanceFactor:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: Property. Non recoverable losses of luminous flux of a lamp due to lamp depreciation i.e. the decreasing of light output of a luminaire due to aging and dirt.    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *lamp_-_properties_-_contributedluminousflux_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    lightEmitterNominalPower:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: 'Property. Light emitter nominal power. Usually measured in Watts (W, J/s).'    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *lamp_-_properties_-_contributedluminousflux_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
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
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *lamp_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    spectrumMax:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: 'Property. The spectrum of radiation describes its composition with regard to wavelength. Light, for example, as the portion of electromagnetic radiation that is visible to the human eye, is radiation with wavelengths in the range of approx. 380 to 780 nm (1 nm = 10 m). The corresponding range of colours varies from violet to indigo, blue, green, yellow, orange, and red. These colours form a continuous spectrum, in which the various spectral sectors merge into each other.'    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *lamp_-_properties_-_contributedluminousflux_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    spectrumMin:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: 'Property. The spectrum of radiation describes its composition with regard to wavelength. Light, for example, as the portion of electromagnetic radiation that is visible to the human eye, is radiation with wavelengths in the range of approx. 380 to 780 nm (1 nm = 10 m). The corresponding range of colours varies from violet to indigo, blue, green, yellow, orange, and red. These colours form a continuous spectrum, in which the various spectral sectors merge into each other.'    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *lamp_-_properties_-_contributedluminousflux_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    type:    
      description: Property. It must be equal to `Lamp`.    
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
## ＃＃＃＃有效载荷的例子  
#### Lamp NGSI-v2关键值示例  
这里有一个JSON-LD格式的Lamp作为key-values的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### 灯具NGSI-v2规范化示例  
下面是一个以JSON-LD格式规范化的Lamp的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### 灯具NGSI-LD关键值示例  
这里有一个JSON-LD格式的Lamp作为key-values的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
#### 灯具NGSI-LD正常化的例子  
下面是一个以JSON-LD格式规范化的Lamp的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
