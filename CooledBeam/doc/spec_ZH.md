<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：凉爽的光束  
========<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/CooledBeam/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述：**冷梁（或称冷梁）是一种通常用于冷却空气的装置，它通过空间上方的裸露翅片管使流体（如冷冻水）循环。通常安装在天花板附近的头顶上，冷却梁利用对流来冷却它下面的空间，作为空间中自然上升的暖空气的散热器。一旦被冷却，空气就会自然回落到地板上，循环再次开始。  
版本：0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `coilLength[number]`: 属性。线圈的长度。通常以毫米（mm）为单位测量。  - `coilWidth[number]`: 属性。线圈的宽度。通常以毫米为单位 (mm)  - `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `finishColor[string]`: 属性。冷却梁的饰面颜色。  - `hasManufacturer[string]`: 属性。识别实体（例如，设备）的制造商的关系。该值应是一个字符串或一个带有语言标签的字符串。  - `hasModel[string]`: 属性。识别实体（例如，设备）的模型的关系。该值应是一个字符串或一个带有语言标签的字符串。  - `id[*]`: 实体的唯一标识符  - `integratedLightingType[string]`: 属性。冷却梁上的综合照明。  - `isContainedInBuildingSpace[*]`: 关系。一个用于定义建筑物理空间的实体。一个建筑空间包含设备或建筑对象。(建筑空间)  - `isContainedInPhysicalObject[*]`: 关系。任何具有适当空间区域的物体。  (从DUL本体论中提取的定义）（PhysicalObject）。  - `isFreeHanging[boolean]`: 财产。它是自由悬挂式的吗（不是安装在假天花板上）？  - `isSubSystemOf[array]`: 关系。对该物理对象是其一部分的系统的引用。  - `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `name[string]`: 这个项目的名称。  - `nominalCoolingCapacity[number]`: 属性。标称冷却能力。通常以瓦特（W，J/s）衡量。  - `nominalHeatingCapacity[number]`: 属性。标称加热能力。通常以瓦特（W，J/s）衡量。  - `nominalReturnWaterTemperatureCooling[number]`: 属性。公称回水温度（指公称冷却能力）。通常以开尔文(K)度测量。  - `nominalReturnWaterTemperatureHeating[number]`: 属性。公称回水温度（指公称加热能力）。通常以开尔文(K)度衡量。  - `nominalSorroundingHumidityCooling[number]`: 属性。公称周围湿度（指公称冷却能力）。通常以开尔文(K)度衡量。  - `nominalSorroundingTemperatureCooling[number]`: 属性。标称周围温度（指标称冷却能力）。通常以开尔文(K)度衡量。  - `nominalSorroundingTemperatureHeating[number]`: 属性。标称周围温度（指标称加热能力）。通常以开尔文(K)度衡量。  - `nominalSupplyWaterTemperatureCooling[number]`: 属性。标称供水温度（指标称冷却能力）。通常以开尔文(K)度测量。  - `nominalSupplyWaterTemperatureHeating[number]`: 属性。标称供水温度（指标称加热能力）。通常以开尔文(K)度衡量。  - `nominalWaterFlowCooling[number]`: 属性。名义水流量（指名义冷却能力）。通常以m3/s测量。  - `nominalWaterFlowHeating[number]`: 属性。名义水流量（指名义加热能力）。通常以m3/s测量。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `pipeConnectionEnum[string]`: 属性。管道连接到冷却梁的方式。  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `type[string]`: 属性。它必须等于`CooledBeam`。  - `waterFlowControlSystemType[string]`: 属性。工厂安装的水流控制系统。  - `waterPressureMax[number]`: 属性。允许的水路工作压力范围。通常以帕斯卡（Pa，N/m2）为单位。  - `waterPressureMin[number]`: 属性。允许的水路工作压力范围。通常以帕斯卡（Pa，N/m2）为单位。  <!-- /30-PropertiesList -->  
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
CooledBeam:    
  description: 'A cooled beam (or chilled beam) is a device typically used to cool air by circulating a fluid such as chilled water through exposed finned tubes above a space. Typically mounted overhead near or within a ceiling, the cooled beam uses convection to cool the space below it by acting as a heat sink for the naturally rising warm air of the space. Once cooled, the air naturally drops back to the floor where the cycle begins again.'    
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
    coilLength:    
      description: Property. Length of coil. Usually measured in millimeters (mm).    
      type: number    
      x-ngsi:    
        type: Property    
    coilWidth:    
      description: Property. Width of coil. Usually measured in millimeters (mm    
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
    finishColor:    
      description: Property. Finish color for cooled beam.    
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
      anyOf: &cooledbeam_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    integratedLightingType:    
      description: Property. Integrated lighting in cooled beam.    
      type: string    
      x-ngsi:    
        type: Property    
    isContainedInBuildingSpace:    
      anyOf: *cooledbeam_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *cooledbeam_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isFreeHanging:    
      description: 'Property. Is it free hanging type (not mounted in a false ceiling)?'    
      type: boolean    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *cooledbeam_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    nominalCoolingCapacity:    
      description: 'Property. Nominal cooling capacity. Usually measured in Watts (W, J/s).'    
      type: number    
      x-ngsi:    
        type: Property    
    nominalHeatingCapacity:    
      description: 'Property. Nominal heating capacity. Usually measured in Watts (W, J/s).'    
      type: number    
      x-ngsi:    
        type: Property    
    nominalReturnWaterTemperatureCooling:    
      description: Property. Nominal return water temperature (refers to nominal cooling capacity). Usually measured in degrees Kelvin (K).    
      type: number    
      x-ngsi:    
        type: Property    
    nominalReturnWaterTemperatureHeating:    
      description: Property. Nominal return water temperature (refers to nominal heating capacity). Usually measured in degrees Kelvin (K).    
      type: number    
      x-ngsi:    
        type: Property    
    nominalSorroundingHumidityCooling:    
      description: Property. Nominal surrounding humidity (refers to nominal cooling capacity). Usually measured in degrees Kelvin (K).    
      type: number    
      x-ngsi:    
        type: Property    
    nominalSorroundingTemperatureCooling:    
      description: Property. Nominal surrounding temperature (refers to nominal cooling capacity). Usually measured in degrees Kelvin (K).    
      type: number    
      x-ngsi:    
        type: Property    
    nominalSorroundingTemperatureHeating:    
      description: Property. Nominal surrounding temperature (refers to nominal heating capacity). Usually measured in degrees Kelvin (K).    
      type: number    
      x-ngsi:    
        type: Property    
    nominalSupplyWaterTemperatureCooling:    
      description: Property. Nominal supply water temperature (refers to nominal cooling capacity). Usually measured in degrees Kelvin (K).    
      type: number    
      x-ngsi:    
        type: Property    
    nominalSupplyWaterTemperatureHeating:    
      description: Property. Nominal supply water temperature (refers to nominal heating capacity). Usually measured in degrees Kelvin (K).    
      type: number    
      x-ngsi:    
        type: Property    
    nominalWaterFlowCooling:    
      description: Property. Nominal water flow (refers to nominal cooling capacity). Usually measured in m3/s.    
      type: number    
      x-ngsi:    
        type: Property    
    nominalWaterFlowHeating:    
      description: Property. Nominal water flow (refers to nominal heating capacity). Usually measured in m3/s.    
      type: number    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *cooledbeam_-_properties_-_iscontainedinbuildingspace_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    pipeConnectionEnum:    
      description: Property. The manner in which the pipe connection is made to the cooled beam.    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: Property. It must be equal to `CooledBeam`.    
      enum:    
        - CooledBeam    
      type: string    
      x-ngsi:    
        type: Property    
    waterFlowControlSystemType:    
      description: Property. Factory fitted waterflow control system.    
      type: string    
      x-ngsi:    
        type: Property    
    waterPressureMax:    
      description: 'Property. Allowable water circuit working pressure range. Usually measured in Pascals (Pa, N/m2).'    
      type: number    
      x-ngsi:    
        type: Property    
    waterPressureMin:    
      description: 'Property. Allowable water circuit working pressure range. Usually measured in Pascals (Pa, N/m2).'    
      type: number    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:CooledBeam"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/CooledBeam/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/CooledBeam/schema.json    
  x-model-tags: SAREF CooledBeam SMART DATA MODELS    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### CooledBeam NGSI-v2关键值示例  
这里是一个以JSON-LD格式作为关键值的CooledBeam的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:CooledBeam:82040ca8-778f-478d-a8fd-28485704919f",  
  "type": "CooledBeam",  
  "coilLength": 0.12136965337189098,  
  "coilWidth": 0.9739362570796377,  
  "finishColor": "deposit",  
  "integratedLightingType": "Metrics",  
  "isFreeHanging": false,  
  "nominalCoolingCapacity": 0.25517130161811685,  
  "nominalHeatingCapacity": 0.979299961039553,  
  "nominalReturnWaterTemperatureCooling": 0.8331575990645163,  
  "nominalReturnWaterTemperatureHeating": 0.8257910510708837,  
  "nominalSorroundingHumidityCooling": 0.08831404123432451,  
  "nominalSorroundingTemperatureCooling": 0.8951747110468832,  
  "nominalSorroundingTemperatureHeating": 0.7722529144575002,  
  "nominalSupplyWaterTemperatureCooling": 0.510069259798832,  
  "nominalSupplyWaterTemperatureHeating": 0.9682117435710755,  
  "nominalWaterFlowCooling": 0.640621498291464,  
  "nominalWaterFlowHeating": 0.3754874763938201,  
  "pipeConnectionEnum": "Falls",  
  "waterFlowControlSystemType": "Forks",  
  "waterPressureMax": 0.6809509740238233,  
  "waterPressureMin": 0.3372474470208946,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:29882bc5-9d20-4d25-b276-5bdf4f6981e1",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:13d83cbf-6e67-4d40-85da-46a7032fbde9",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:dfeed4f8-88d6-4475-89b3-71faa705f8a4",  
    "urn:ngsi-ld:System:23813ba9-d7b1-475b-b245-c32d08798cc3",  
    "urn:ngsi-ld:System:daa546ea-d20c-4761-98b2-e17e050b4625"  
  ],  
  "hasManufacturer": "CooledBeam Company Inc.",  
  "hasModel": "CooledBeam 0.1.2",  
  "dateCreated": "2023-01-26T05:29:03Z",  
  "dateModified": "2023-01-26T10:03:56Z",  
  "source": "Import",  
  "name": "CooledBeam",  
  "alternateName": "CooledBeam type 2",  
  "description": "CooledBeam of limited CooledBeam types",  
  "dataProvider": "IFC file"  
}  
```  
</details>  
#### CooledBeam NGSI-v2规范化示例  
下面是一个以JSON-LD格式规范化的CooledBeam的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:CooledBeam:38dcdd25-ae94-441c-8409-218ec91e3006",  
  "type": "CooledBeam",  
  "coilLength": {  
    "type": "Measurement",  
    "value": 0.4277226249853211  
  },  
  "coilWidth": {  
    "type": "Measurement",  
    "value":0.6183775851562611  
  },  
  "finishColor": {  
    "type": "Text",  
    "value": "Associate"  
  },  
  "integratedLightingType": {  
    "type": "Text",  
    "value": "Washington"  
  },  
  "isFreeHanging": {  
    "type": "Boolean",  
    "value": false  
  },  
  "nominalCoolingCapacity": {  
    "type": "Measurement",  
    "value":0.45857043485420457  
  },  
  "nominalHeatingCapacity": {  
    "type": "Measurement",  
    "value":  0.37812382267356337  
  },  
  "nominalReturnWaterTemperatureCooling": {  
    "type": "Measurement",  
    "value":  0.973742767691913  
  },  
  "nominalReturnWaterTemperatureHeating": {  
    "type": "Measurement",  
    "value":  0.6848085584395665  
  },  
  "nominalSorroundingHumidityCooling": {  
    "type": "Measurement",  
    "value":  0.4100986776385609  
  },  
  "nominalSorroundingTemperatureCooling": {  
    "type": "Measurement",  
    "value":  0.039909771141081074  
  },  
  "nominalSorroundingTemperatureHeating": {  
    "type": "Measurement",  
    "value":  0.3023923557796515  
  },  
  "nominalSupplyWaterTemperatureCooling": {  
    "type": "Measurement",  
    "value":  0.7562940127899793  
  },  
  "nominalSupplyWaterTemperatureHeating": {  
    "type": "Measurement",  
    "value":  0.31198678394809454  
  },  
  "nominalWaterFlowCooling": {  
    "type": "Measurement",  
    "value":  0.40924277893308847  
  },  
  "nominalWaterFlowHeating": {  
    "type": "Measurement",  
    "value":  0.9345939456733873  
  },  
  "pipeConnectionEnum": {  
    "type": "Text",  
    "value": "extensible"  
  },  
  "waterFlowControlSystemType": {  
    "type": "Text",  
    "value": "Interactions"  
  },  
  "waterPressureMax": {  
    "type": "Measurement",  
    "value":  0.07837257218461391  
  },  
  "waterPressureMin": {  
    "type": "Measurement",  
    "value": 0.03742669539477306  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:BuildingSpace:3e03fe30-3728-4867-ab51-b147c2d3e63b"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:PhysicalObject:cfd9df05-18b1-44f4-b1ee-da55226255e9"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:a4b0cda0-b373-4ae9-b2c7-e2cff5429e1e"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:216f6f83-8bd1-456f-9bed-36dbec41a3aa"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:d19ccffa-f134-46fc-8f9f-77656bb91649"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "CooledBeam Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "CooledBeam 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T21:51:06.7954024+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T00:15:46.9435362+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "CooledBeam"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "CooledBeam type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "CooledBeam of limited CooledBeam types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### CooledBeam NGSI-LD关键值示例  
这里是一个以JSON-LD格式作为key-values的CooledBeam的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:CooledBeam:82040ca8-778f-478d-a8fd-28485704919f",  
  "type": "CooledBeam",  
  "coilLength": 0.12136965337189098,  
  "coilWidth": 0.9739362570796377,  
  "finishColor": "deposit",  
  "integratedLightingType": "Metrics",  
  "isFreeHanging": false,  
  "nominalCoolingCapacity": 0.25517130161811685,  
  "nominalHeatingCapacity": 0.979299961039553,  
  "nominalReturnWaterTemperatureCooling": 0.8331575990645163,  
  "nominalReturnWaterTemperatureHeating": 0.8257910510708837,  
  "nominalSorroundingHumidityCooling": 0.08831404123432451,  
  "nominalSorroundingTemperatureCooling": 0.8951747110468832,  
  "nominalSorroundingTemperatureHeating": 0.7722529144575002,  
  "nominalSupplyWaterTemperatureCooling": 0.510069259798832,  
  "nominalSupplyWaterTemperatureHeating": 0.9682117435710755,  
  "nominalWaterFlowCooling": 0.640621498291464,  
  "nominalWaterFlowHeating": 0.3754874763938201,  
  "pipeConnectionEnum": "Falls",  
  "waterFlowControlSystemType": "Forks",  
  "waterPressureMax": 0.6809509740238233,  
  "waterPressureMin": 0.3372474470208946,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:29882bc5-9d20-4d25-b276-5bdf4f6981e1",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:13d83cbf-6e67-4d40-85da-46a7032fbde9",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:dfeed4f8-88d6-4475-89b3-71faa705f8a4",  
    "urn:ngsi-ld:System:23813ba9-d7b1-475b-b245-c32d08798cc3",  
    "urn:ngsi-ld:System:daa546ea-d20c-4761-98b2-e17e050b4625"  
  ],  
  "hasManufacturer": "CooledBeam Company Inc.",  
  "hasModel": "CooledBeam 0.1.2",  
  "dateCreated": "2023-01-26T05:29:03Z",  
  "dateModified": "2023-01-26T10:03:56Z",  
  "source": "Import",  
  "name": "CooledBeam",  
  "alternateName": "CooledBeam type 2",  
  "description": "CooledBeam of limited CooledBeam types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### CooledBeam NGSI-LD 归一化实例  
下面是一个以JSON-LD格式规范化的CooledBeam的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:CooledBeam:baa66543-6434-4e28-8e85-20b2b260d404",  
  "type": "CooledBeam",  
  "coilLength": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-25T18:59:14Z",  
    "value": 0.45413352830053977  
  },  
  "coilWidth": {  
    "type": "Property",  
    "unitCode": "m",  
    "observedAt": "2023-01-26T07:44:01Z",  
    "value": 0.2692385089640058  
  },  
  "finishColor": {  
    "type": "Property",  
    "value": "indigo"  
  },  
  "integratedLightingType": {  
    "type": "Property",  
    "value": "Graphical User Interface"  
  },  
  "isFreeHanging": {  
    "type": "Property",  
    "value": false  
  },  
  "nominalCoolingCapacity": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-26T09:40:29Z",  
    "value": 0.3030442126473498  
  },  
  "nominalHeatingCapacity": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-26T02:43:04Z",  
    "value": 0.7091959285173477  
  },  
  "nominalReturnWaterTemperatureCooling": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T10:09:02Z",  
    "value": 0.4048762377790246  
  },  
  "nominalReturnWaterTemperatureHeating": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T08:24:33Z",  
    "value": 0.33261295327987683  
  },  
  "nominalSorroundingHumidityCooling": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T12:36:33Z",  
    "value": 0.5632800434491262  
  },  
  "nominalSorroundingTemperatureCooling": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T11:31:42Z",  
    "value": 0.47265451181389695  
  },  
  "nominalSorroundingTemperatureHeating": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T18:37:57Z",  
    "value": 0.18090042184548072  
  },  
  "nominalSupplyWaterTemperatureCooling": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T21:17:20Z",  
    "value": 0.9122743224756777  
  },  
  "nominalSupplyWaterTemperatureHeating": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T17:52:00Z",  
    "value": 0.9207552089629301  
  },  
  "nominalWaterFlowCooling": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-25T15:05:33Z",  
    "value": 0.06592489938443258  
  },  
  "nominalWaterFlowHeating": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-26T13:42:04Z",  
    "value": 0.3446198206084118  
  },  
  "pipeConnectionEnum": {  
    "type": "Property",  
    "value": "SSL"  
  },  
  "waterFlowControlSystemType": {  
    "type": "Property",  
    "value": "supply-chains"  
  },  
  "waterPressureMax": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-25T17:35:39Z",  
    "value": 0.8610847602415933  
  },  
  "waterPressureMin": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-26T03:28:09Z",  
    "value": 0.9088584704707019  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:6689ca11-b361-48b4-950d-07edf1182e97"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:2e350952-8c19-46a2-a2c2-8d30c54d03cb"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:cf124c7e-8f71-424a-93b5-64643c889f30"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:a72f7b54-3f5c-4b66-9463-f20f7127cff6"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:ce488063-f9a9-44c4-ac0f-f79e2977a2d4"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "CooledBeam Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "CooledBeam 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T23:43:55Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-25T20:21:43Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "CooledBeam"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "CooledBeam type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "CooledBeam of limited CooledBeam types"  
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
