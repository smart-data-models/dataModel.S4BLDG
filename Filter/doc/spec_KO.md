<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: 필터    
=======<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Filter/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: **필터는 유체 및 가스에서 입자상 또는 기체상 물질을 제거하는 데 사용되는 장치입니다**.    
버전: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 속성 목록    
<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.    
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 해당 지역이 위치한 지역 및 국가 내 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.      
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호      
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `finalResistance[number]`: 교체가 필요한 경우의 필터 유체 저항(즉, ASHRAE 표준 52.1에 따라 필터를 교체해야 할 때 필터를 통과하는 최대 공기 유량에서의 압력 강하). 일반적으로 파스칼(Pa, N/m2) 단위로 측정됩니다.  - `fluidFlowRateMax[number]`: 전달할 수 있는 유체 유량의 가능한 범위입니다. 보통 m3/s 단위로 측정  - `fluidFlowRateMin[number]`: 전달할 수 있는 유체 유량의 가능한 범위입니다. 보통 m3/s 단위로 측정  - `hasManufacturer[string]`: 엔티티의 제조업체를 식별하는 관계(예: 장치)입니다. 값은 문자열 또는 언어 태그가 포함된 문자열로 예상됩니다.  - `hasModel[string]`: 엔티티의 모델(예: 장치)을 식별하는 관계입니다. 값은 문자열 또는 언어 태그가 포함된 문자열로 예상됩니다.  - `id[*]`: 엔티티의 고유 식별자  - `initialResistance[number]`: 초기 새 필터 유체 저항(즉, ASHRAE 표준 52.1에 따라 필터가 새 필터일 때 필터를 통과하는 최대 공기 유량에서의 압력 강하). 일반적으로 파스칼(Pa, N/m2) 단위로 측정됩니다.  - `isContainedInBuildingSpace[*]`: 건물의 물리적 공간을 정의하는 데 사용되는 엔티티입니다. 건물 공간에는 장치 또는 건물 개체가 포함됩니다. (빌딩 공간)  - `isContainedInPhysicalObject[*]`: 적절한 공간 영역을 가진 모든 객체.  (DUL 온톨로지에서 추출한 정의) (PhysicalObject)  - `isSubSystemOf[array]`: 이 피지컬 오브젝트가 속한 시스템에 대한 레퍼런스입니다.  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `nominalFilterFaceVelocity[number]`: 필터 페이스 속도. 보통 m/s 단위로 측정됩니다.  - `nominalFlowRate[number]`: 필터를 통과하는 공칭 유체 유량. 일반적으로 m3/s 단위로 측정됩니다.  - `nominalMediaSurfaceVelocity[number]`: 미디어 표면의 평균 유체 속도입니다. 보통 m/s 단위로 측정됩니다.  - `nominalParticleGeometricMeanDiameter[number]`: 공칭 효율과 관련된 입자의 기하학적 평균 직경입니다. 일반적으로 밀리미터(mm) 단위로 측정됩니다.  - `nominalParticleGeometricStandardDeviation[number]`: 공칭 효율과 관련된 입자 기하학적 표준 편차.  - `nominalPressureDrop[number]`: 필터 전체에 걸친 총 압력 강하량입니다. 일반적으로 파스칼(Pa, N/m2) 단위로 측정됩니다.  - `operationTemperatureMax[number]`: 허용되는 작동 주변(공기, 유체) 온도 범위. 일반적으로 켈빈(K) 단위로 측정됩니다.  - `operationTemperatureMin[number]`: 허용되는 작동 주변(공기, 유체) 온도 범위. 일반적으로 켈빈(K) 단위로 측정됩니다.  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `type[string]`: 필터`와 같아야 합니다.  - `weight[number]`: 장치의 무게입니다. 일반적으로 킬로그램(kg) 또는 그램(g) 단위로 측정됩니다.  <!-- /30-PropertiesList -->    
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
## 페이로드 예시    
#### NGSI-v2 키 값 필터링 예시    
다음은 키-값으로 JSON-LD 형식의 필터의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
#### 필터 NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 필터 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Filter:8e80455c-7f89-462c-b1f0-b84c6ac5e5cb",  
  "type": "Filter",  
  "finalResistance": {  
    "type": "Number",  
    "value": 0.25563353322549653  
  },  
  "fluidFlowRateMax": {  
    "type": "Number",  
    "value": 0.7441450852967011  
  },  
  "fluidFlowRateMin": {  
    "type": "Number",  
    "value": 0.32563792639259326  
  },  
  "initialResistance": {  
    "type": "Number",  
    "value": 0.41032135281652493  
  },  
  "nominalFilterFaceVelocity": {  
    "type": "Number",  
    "value": 0.829815297358211  
  },  
  "nominalFlowRate": {  
    "type": "Number",  
    "value": 0.569423507213339  
  },  
  "nominalMediaSurfaceVelocity": {  
    "type": "Number",  
    "value": 0.6085640129416107  
  },  
  "nominalParticleGeometricMeanDiameter": {  
    "type": "Number",  
    "value": 0.9736709365602062  
  },  
  "nominalParticleGeometricStandardDeviation": {  
    "type": "Number",  
    "value": 0.5284993250186989  
  },  
  "nominalPressureDrop": {  
    "type": "Number",  
    "value": 0.4856470985811685  
  },  
  "operationTemperatureMax": {  
    "type": "Number",  
    "value": 0.04450158146401939  
  },  
  "operationTemperatureMin": {  
    "type": "Number",  
    "value": 0.28211808830531604  
  },  
  "weight": {  
    "type": "Number",  
    "value": 0.5157014658259989  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:BuildingSpace:4468726f-7faa-4e8e-802e-337b7d4e2c38"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:PhysicalObject:a263b3b0-a5d7-4e38-a95f-75dd868ea6aa"  
  },  
  "isSubSystemOf": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:System:118a0d61-bba3-416e-a770-5ac45dfb66e7",  
      "urn:ngsi-ld:System:a7ba30cc-d8f3-423d-a1d6-284c130befee",  
      "urn:ngsi-ld:System:38485bc5-5ff4-49f1-b6fb-65b815b05795"  
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
#### 필터 NGSI-LD 키 값 예제    
다음은 키-값으로 JSON-LD 형식의 필터의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
#### 필터 NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 필터의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
