<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: 응축기    
========<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Condenser/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: **콘덴서는 일반적으로 냉매와 같은 물질을 기체 상태에서 액체 상태로 응축하여 열을 발산하는 데 사용되는 장치입니다.**    
버전: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 속성 목록    
<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.    
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.      
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호      
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `externalSurfaceArea[number]`: 외부 표면적(기본 및 보조 면적 모두). 일반적으로 평방미터(m2) 단위로 측정됩니다.  - `hasManufacturer[string]`: 엔티티의 제조업체를 식별하는 관계(예: 장치)입니다. 값은 문자열 또는 언어 태그가 포함된 문자열로 예상됩니다.  - `hasModel[string]`: 엔티티의 모델(예: 장치)을 식별하는 관계입니다. 값은 문자열 또는 언어 태그가 포함된 문자열로 예상됩니다.  - `id[*]`: 엔티티의 고유 식별자  - `internalRefrigerantVolume[number]`: 증발기의 내부 부피(냉매 측). 일반적으로 입방미터(m3) 단위로 측정됩니다.  - `internalSurfaceArea[number]`: 내부 표면적. 보통 평방미터(m2) 단위로 측정됩니다.  - `internalWaterVolume[number]`: 증발기 내부 부피(물 쪽). 일반적으로 입방미터(m3) 단위로 측정됩니다.  - `isContainedInBuildingSpace[*]`: 건물의 물리적 공간을 정의하는 데 사용되는 엔티티입니다. 건물 공간에는 장치 또는 건물 개체가 포함됩니다. (빌딩 공간)  - `isContainedInPhysicalObject[*]`: 적절한 공간 영역을 가진 모든 객체.  (DUL 온톨로지에서 추출한 정의) (PhysicalObject)  - `isSubSystemOf[array]`: 이 피지컬 오브젝트가 속한 시스템에 대한 레퍼런스입니다.  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `nominalHeatTransferArea[number]`: 공칭 전체 열전달 계수와 관련된 공칭 열전달 표면적. 일반적으로 평방미터(m2) 단위로 측정됩니다.  - `nominalHeatTransferCoefficient[number]`: 공칭 열전달 면적과 관련된 공칭 전체 열전달 계수입니다. 일반적으로 와트/m2 켈빈 단위로 측정됩니다.  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `refrigerantClass[string]`: 컴프레서에 사용되는 냉매 등급입니다. CFC: 염화불화탄소. HCFC: 수소염화불화탄소. HFC: 수소불화탄소  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `type[string]`: 응축기`와 같아야 합니다.  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
필수 속성    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 속성에 대한 데이터 모델 설명    
알파벳순으로 정렬(자세한 내용을 보려면 클릭)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
Condenser:      
  description: 'A condenser is a device that is used to dissipate heat, typically by condensing a substance such as a refrigerant from its gaseous to its liquid state.'      
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
    externalSurfaceArea:      
      description: External surface area (both primary and secondary area). Usually measured in square metre (m2)      
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
    internalRefrigerantVolume:      
      description: Internal volume of evaporator (refrigerant side). Usually measured in cubic metre (m3)      
      type: number      
      x-ngsi:      
        type: Property      
    internalSurfaceArea:      
      description: Internal surface area. Usually measured in square metre (m2)      
      type: number      
      x-ngsi:      
        type: Property      
    internalWaterVolume:      
      description: Internal volume of evaporator (water side). Usually measured in cubic metre (m3)      
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
    nominalHeatTransferArea:      
      description: Nominal heat transfer surface area associated with nominal overall heat transfer coefficient. Usually measured in square metre (m2)      
      type: number      
      x-ngsi:      
        type: Property      
    nominalHeatTransferCoefficient:      
      description: Nominal overall heat transfer coefficient associated with nominal heat transfer area. Usually measured in Watts/m2 Kelvin      
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
    refrigerantClass:      
      description: 'Refrigerant class used by the compressor. CFC: Chlorofluorocarbons. HCFC: Hydrochlorofluorocarbons. HFC: Hydrofluorocarbons'      
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
    type:      
      description: It must be equal to `Condenser`      
      enum:      
        - Condenser      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Condenser"      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Condenser/LICENSE.md      
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Condenser/schema.json      
  x-model-tags: SAREF Condenser      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 페이로드 예시    
#### 콘덴서 NGSI-v2 키 값 예제    
다음은 키-값으로 JSON-LD 형식의 콘덴서 예제입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Condenser:2adcb166-23ce-4061-8062-952d5f2402b9",  
  "type": "Condenser",  
  "externalSurfaceArea": 0.18804655027013273,  
  "internalRefrigerantVolume": 0.1588694072031649,  
  "internalSurfaceArea": 0.884829655411807,  
  "internalWaterVolume": 0.7576300292464242,  
  "nominalHeatTransferArea": 0.04220384603580274,  
  "nominalHeatTransferCoefficient": 0.4901767947128819,  
  "refrigerantClass": "Barbados",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:7ba37c8a-b348-4fc5-8191-22dbe255c23e",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:f9999243-09ea-40b2-892a-63bfd9062a09",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:374a6c1e-348f-46a2-824d-616554f66351",  
    "urn:ngsi-ld:System:0bd6a865-18bc-40a2-b1cf-64af77762cee",  
    "urn:ngsi-ld:System:e8c3da85-a230-40e1-832c-e03b342a1160"  
  ],  
  "hasManufacturer": "Condenser Company Inc.",  
  "hasModel": "Condenser 0.1.2",  
  "dateCreated": "2023-01-25T15:55:59Z",  
  "dateModified": "2023-01-26T06:49:28Z",  
  "source": "Import",  
  "name": "Condenser",  
  "alternateName": "Condenser type 2",  
  "description": "Condenser of limited Condenser types",  
  "dataProvider": "IFC file"  
}  
```  
</details>    
#### 콘덴서 NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 콘덴서 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Condenser:e22782fc-5392-4dd2-b891-29b5fbf683cd",  
  "type": "Condenser",  
  "externalSurfaceArea": {  
    "type": "Number",  
    "value": 0.1255332761606085  
  },  
  "internalRefrigerantVolume": {  
    "type": "Number",  
    "value": 0.5305579766612258  
  },  
  "internalSurfaceArea": {  
    "type": "Number",  
    "value": 0.7094627719374283  
  },  
  "internalWaterVolume": {  
    "type": "Number",  
    "value": 0.3123303218703414  
  },  
  "nominalHeatTransferArea": {  
    "type": "Number",  
    "value": 0.4444793909507544  
  },  
  "nominalHeatTransferCoefficient": {  
    "type": "Number",  
    "value": 0.6428769642448905  
  },  
  "refrigerantClass": {  
    "type": "Text",  
    "value": "Ergonomic Fresh Pants"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:BuildingSpace:ae10b0d7-9929-45cc-bf0c-3e3ab5380c1a"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:PhysicalObject:a3e1362f-7a17-46e9-a997-fd763290b5a2"  
  },  
  "isSubSystemOf": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:System:47267553-d21a-42f8-b1b9-b24ec529e8ad",  
      "urn:ngsi-ld:System:878dd196-c9af-43d7-8d36-344fa19ca56f",  
      "urn:ngsi-ld:System:366cc386-314f-4591-9f3f-4099890c74e7"  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Condenser Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Condenser 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T23:40:11.0211053+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T22:43:21.3342982+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Condenser"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Condenser type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Condenser of limited Condenser types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>    
#### 콘덴서 NGSI-LD 키 값 예시    
다음은 키 값으로 JSON-LD 형식의 콘덴서 예제입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Condenser:2adcb166-23ce-4061-8062-952d5f2402b9",  
  "type": "Condenser",  
  "externalSurfaceArea": 0.18804655027013273,  
  "internalRefrigerantVolume": 0.1588694072031649,  
  "internalSurfaceArea": 0.884829655411807,  
  "internalWaterVolume": 0.7576300292464242,  
  "nominalHeatTransferArea": 0.04220384603580274,  
  "nominalHeatTransferCoefficient": 0.4901767947128819,  
  "refrigerantClass": "Barbados",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:7ba37c8a-b348-4fc5-8191-22dbe255c23e",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:f9999243-09ea-40b2-892a-63bfd9062a09",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:374a6c1e-348f-46a2-824d-616554f66351",  
    "urn:ngsi-ld:System:0bd6a865-18bc-40a2-b1cf-64af77762cee",  
    "urn:ngsi-ld:System:e8c3da85-a230-40e1-832c-e03b342a1160"  
  ],  
  "hasManufacturer": "Condenser Company Inc.",  
  "hasModel": "Condenser 0.1.2",  
  "dateCreated": "2023-01-25T15:55:59Z",  
  "dateModified": "2023-01-26T06:49:28Z",  
  "source": "Import",  
  "name": "Condenser",  
  "alternateName": "Condenser type 2",  
  "description": "Condenser of limited Condenser types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>    
#### 콘덴서 NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 콘덴서 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Condenser:290f1265-1ded-4706-b549-43d7ddcaa239",  
  "type": "Condenser",  
  "externalSurfaceArea": {  
    "type": "Property",  
    "unitCode": "m2",  
    "observedAt": "2023-01-26T11:04:44Z",  
    "value": 0.3471102075551651  
  },  
  "internalRefrigerantVolume": {  
    "type": "Property",  
    "unitCode": "m3",  
    "observedAt": "2023-01-26T10:30:09Z",  
    "value": 0.696994206179287  
  },  
  "internalSurfaceArea": {  
    "type": "Property",  
    "unitCode": "m2",  
    "observedAt": "2023-01-25T14:42:31Z",  
    "value": 0.7522617883905902  
  },  
  "internalWaterVolume": {  
    "type": "Property",  
    "unitCode": "m3",  
    "observedAt": "2023-01-26T09:25:42Z",  
    "value": 0.5807649609435256  
  },  
  "nominalHeatTransferArea": {  
    "type": "Property",  
    "unitCode": "m2",  
    "observedAt": "2023-01-26T05:15:12Z",  
    "value": 0.6105994546410142  
  },  
  "nominalHeatTransferCoefficient": {  
    "type": "Property",  
    "unitCode": "Kelvin",  
    "observedAt": "2023-01-25T14:28:56Z",  
    "value": 0.17023310849677553  
  },  
  "refrigerantClass": {  
    "type": "Property",  
    "value": "Generic Metal Pants"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:b7d758c3-cd93-4ce4-a414-28e5a714b67c"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:9d98233b-6df5-418e-b43c-5f98c921296f"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:6ba8c28a-2ebf-4a11-ba34-b7d778896bf9"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:3f480247-b6e3-4cc3-89e1-5c1f88507e48"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:645beb56-0f95-4b35-a0ed-56d848e575f1"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Condenser Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Condenser 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T22:14:26Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T02:56:43Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Condenser"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Condenser type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Condenser of limited Condenser types"  
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
