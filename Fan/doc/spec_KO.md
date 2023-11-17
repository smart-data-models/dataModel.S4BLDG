<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: 팬    
======<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Fan/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: **팬은 가스에 기계적 작업을 부여하는 장치입니다. 팬의 일반적인 용도는 건물 서비스 공기 분배 시스템에서 공기 흐름을 유도하는 것입니다.    
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
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `capacityControlType[string]`: 흡입구 베인: 흡입구 베인을 조정하여 제어합니다. 가변 속도 드라이브: 가변 속도 드라이브로 제어합니다. BladePitchAngle: 블레이드 피치 각도를 조정하여 제어합니다. TwoSpeed: 고속과 저속 사이를 전환하여 제어합니다. 방전 댐퍼: 방전 댐퍼를 조절하여 제어  - `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `hasManufacturer[string]`: 엔티티의 제조업체를 식별하는 관계(예: 장치)입니다. 값은 문자열 또는 언어 태그가 포함된 문자열로 예상됩니다.  - `hasModel[string]`: 엔티티의 모델(예: 장치)을 식별하는 관계입니다. 값은 문자열 또는 언어 태그가 포함된 문자열로 예상됩니다.  - `id[*]`: 엔티티의 고유 식별자  - `isContainedInBuildingSpace[*]`: 건물의 물리적 공간을 정의하는 데 사용되는 엔티티입니다. 건물 공간에는 장치 또는 건물 개체가 포함됩니다. (빌딩 공간)  - `isContainedInPhysicalObject[*]`: 적절한 공간 영역을 가진 모든 객체.  (DUL 온톨로지에서 추출한 정의) (PhysicalObject)  - `isSubSystemOf[array]`: 이 피지컬 오브젝트가 속한 시스템에 대한 레퍼런스입니다.  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `motorDriveType[string]`: 모터 구동 유형: 다이렉트 드라이브: 다이렉트 드라이브. 벨트 드라이브: 벨트 드라이브. 커플링: 커플링. 기타: 다른 유형의 모터 드라이브. 알 수 없음: 알 수 없는 모터 드라이브 유형.  - `name[string]`: 이 항목의 이름  - `nominalAirFlowRate[number]`: 공칭 공기 흐름 속도. 보통 m3/s 단위로 측정됩니다.  - `nominalPowerRate[number]`: 공칭 팬 전력 속도(보통 와트(W, J/s) 단위로 측정)  - `nominalRotationSpeed[number]`: 공칭 팬 휠 속도. 일반적으로 사이클/초 단위로 측정됩니다.  - `nominalStaticPressure[number]`: 설계된 공기 순환을 보장하기 위해 팬이 극복해야 하는 공기 흐름 내의 정압입니다. 일반적으로 파스칼(Pa, N/m2) 단위로 측정됩니다.  - `nominalTotalPressure[number]`: 팬 전체에 걸친 공칭 총 압력 상승. 일반적으로 파스칼(Pa, N/m2) 단위로 측정됩니다.  - `operationMode[string]`: 이 팬의 작동 모드  - `operationTemperatureMax[number]`: 허용되는 작동 주변(공기, 유체) 온도 범위. 일반적으로 켈빈(K) 단위로 측정됩니다.  - `operationTemperatureMin[number]`: 허용되는 작동 주변(공기, 유체) 온도 범위. 일반적으로 켈빈(K) 단위로 측정됩니다.  - `operationalRiterial[number]`: 최대 작동 주변 온도에서 작동한 시간입니다. 초(s) 또는 일(d) 또는 기타 시간 단위로 측정됨  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `type[string]`: 팬`과 같아야 합니다.  <!-- /30-PropertiesList -->    
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
Fan:      
  description: A fan is a device which imparts mechanical work on a gas. A typical usage of a fan is to induce airflow in a building services air distribution system.      
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
    capacityControlType:      
      description: 'InletVane: Control by adjusting inlet vane. VariableSpeedDrive: Control by variable speed drive. BladePitchAngle: Control by adjusting blade pitch angle. TwoSpeed: Control by switch between high and low speed. DischargeDamper: Control by modulating discharge damper'      
      type: string      
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
    motorDriveType:      
      description: 'Motor drive type: DIRECTDRIVE: Direct drive. BELTDRIVE: Belt drive. COUPLING: Coupling. OTHER: Other type of motor drive. UNKNOWN: Unknown motor drive type. '      
      type: string      
      x-ngsi:      
        type: Property      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    nominalAirFlowRate:      
      description: Nominal rate of air flow. Usually measured in m3/s      
      type: number      
      x-ngsi:      
        type: Property      
    nominalPowerRate:      
      description: 'Nominal fan power rate.Usually measured in Watts (W, J/s)'      
      type: number      
      x-ngsi:      
        type: Property      
    nominalRotationSpeed:      
      description: Nominal fan wheel speed. Usually measured in cycles/s      
      type: number      
      x-ngsi:      
        type: Property      
    nominalStaticPressure:      
      description: 'The static pressure within the air stream that the fan must overcome to insure designed circulation of air. Usually measured in Pascals (Pa, N/m2)'      
      type: number      
      x-ngsi:      
        type: Property      
    nominalTotalPressure:      
      description: 'Nominal total pressure rise across the fan. Usually measured in Pascals (Pa, N/m2)'      
      type: number      
      x-ngsi:      
        type: Property      
    operationMode:      
      description: Operation mode of this fan      
      enum:      
        - supply      
        - exhaust      
      type: string      
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
    operationalRiterial:      
      description: Time of operation at maximum operational ambient air temperature. Measured in seconds (s) or days (d) or other units of time      
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
      description: It must be equal to `Fan`      
      enum:      
        - Fan      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Fan"      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Fan/LICENSE.md      
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Fan/schema.json      
  x-model-tags: SAREF Fan      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 페이로드 예시    
#### 팬 NGSI-v2 키 값 예시    
다음은 JSON-LD 형식의 팬을 키값으로 사용하는 예제입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Fan:7cfafc6e-ab2a-4af0-94b0-d4ed9c92e2d9",  
  "type": "Fan",  
  "capacityControlType": "e-markets",  
  "motorDriveType": "gold",  
  "nominalAirFlowRate": 0.5484285000109488,  
  "nominalPowerRate": 0.4651302623864956,  
  "nominalRotationSpeed": 0.586889938002957,  
  "nominalStaticPressure": 0.3508757713471129,  
  "nominalTotalPressure": 0.7008373891464377,  
  "operationalRiterial": 0.3901575132094196,  
  "operationMode": "supply",  
  "operationTemperatureMax": 0.9178812499585061,  
  "operationTemperatureMin": 0.5225885446624712,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:38fc3969-81c7-4c67-a564-fdbe6353726a",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:722ffa89-4091-423f-832c-3af82a48d406",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:624b2008-bd0a-4bf6-98bd-a8fc2979af6b",  
    "urn:ngsi-ld:System:4096cc3a-d7c0-4491-b5e1-a0b97a8db924",  
    "urn:ngsi-ld:System:0dd0f326-6f31-4676-8996-7c591e57a81f"  
  ],  
  "hasManufacturer": "Fan Company Inc.",  
  "hasModel": "Fan 0.1.2",  
  "dateCreated": "2023-01-26T11:05:33Z",  
  "dateModified": "2023-01-26T13:15:57Z",  
  "source": "Import",  
  "name": "Fan",  
  "alternateName": "Fan type 2",  
  "description": "Fan of limited Fan types",  
  "dataProvider": "IFC file"  
}  
```  
</details>    
#### 팬 NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 팬 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Fan:0da82317-969a-4395-8eb2-f98b9cd16de8",  
  "type": "Fan",  
  "capacityControlType": {  
    "type": "Text",  
    "value": "solutions"  
  },  
  "motorDriveType": {  
    "type": "Text",  
    "value": "hard drive"  
  },  
  "nominalAirFlowRate": {  
    "type": "Number",  
    "value": 0.3551507592337234  
  },  
  "nominalPowerRate": {  
    "type": "Number",  
    "value": 0.49309444253514245  
  },  
  "nominalRotationSpeed": {  
    "type": "Number",  
    "value": 0.07199495596164263  
  },  
  "nominalStaticPressure": {  
    "type": "Number",  
    "value": 0.024615829657942068  
  },  
  "nominalTotalPressure": {  
    "type": "Number",  
    "value": 0.3030820859504  
  },  
  "operationalRiterial": {  
    "type": "Number",  
    "value": 0.21730931831819922  
  },  
  "operationMode": {  
    "type": "Text",  
    "value": "supply"  
  },  
  "operationTemperatureMax": {  
    "type": "Number",  
    "value": 0.6593703010837063  
  },  
  "operationTemperatureMin": {  
    "type": "Number",  
    "value": 0.23220611636698574  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:BuildingSpace:179a46d2-4adc-49bc-81ad-55bf8d570c04"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:PhysicalObject:1324382c-8a0d-4481-b501-20ced593647d"  
  },  
  "isSubSystemOf": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:System:7bb675a4-c933-494f-9e7a-1ad7777c40c3",  
      "urn:ngsi-ld:System:2122d54b-df0b-490a-8d2c-9611433a6950",  
      "urn:ngsi-ld:System:bb112446-5445-482a-aacc-ca87dc610bd5"  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Fan Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Fan 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T01:05:02.0601436+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T15:45:36.2919235+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Fan"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Fan type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Fan of limited Fan types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>    
#### 팬 NGSI-LD 키 값 예시    
다음은 키-값으로 JSON-LD 형식의 팬 예시입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Fan:7cfafc6e-ab2a-4af0-94b0-d4ed9c92e2d9",  
  "type": "Fan",  
  "capacityControlType": "e-markets",  
  "motorDriveType": "gold",  
  "nominalAirFlowRate": 0.5484285000109488,  
  "nominalPowerRate": 0.4651302623864956,  
  "nominalRotationSpeed": 0.586889938002957,  
  "nominalStaticPressure": 0.3508757713471129,  
  "nominalTotalPressure": 0.7008373891464377,  
  "operationalRiterial": 0.3901575132094196,  
  "operationMode": "supply",  
  "operationTemperatureMax": 0.9178812499585061,  
  "operationTemperatureMin": 0.5225885446624712,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:38fc3969-81c7-4c67-a564-fdbe6353726a",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:722ffa89-4091-423f-832c-3af82a48d406",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:624b2008-bd0a-4bf6-98bd-a8fc2979af6b",  
    "urn:ngsi-ld:System:4096cc3a-d7c0-4491-b5e1-a0b97a8db924",  
    "urn:ngsi-ld:System:0dd0f326-6f31-4676-8996-7c591e57a81f"  
  ],  
  "hasManufacturer": "Fan Company Inc.",  
  "hasModel": "Fan 0.1.2",  
  "dateCreated": "2023-01-26T11:05:33Z",  
  "dateModified": "2023-01-26T13:15:57Z",  
  "source": "Import",  
  "name": "Fan",  
  "alternateName": "Fan type 2",  
  "description": "Fan of limited Fan types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>    
#### 팬 NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 팬 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Fan:77858a3b-1931-4dba-a9af-2eb53daaa2ba",  
  "type": "Fan",  
  "capacityControlType": {  
    "type": "Property",  
    "value": "Jamaica"  
  },  
  "motorDriveType": {  
    "type": "Property",  
    "value": "Handmade Rubber Pants"  
  },  
  "nominalAirFlowRate": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-25T20:05:36Z",  
    "value": 0.24193379349820043  
  },  
  "nominalPowerRate": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-26T00:02:52Z",  
    "value": 0.9909189253853895  
  },  
  "nominalRotationSpeed": {  
    "type": "Property",  
    "unitCode": "cycles/s",  
    "observedAt": "2023-01-25T18:57:22Z",  
    "value": 0.31786177757080614  
  },  
  "nominalStaticPressure": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-25T20:44:04Z",  
    "value": 0.9226814968179932  
  },  
  "nominalTotalPressure": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-26T08:36:40Z",  
    "value": 0.7120424039244743  
  },  
  "operationalRiterial": {  
    "type": "Property",  
    "unitCode": "time",  
    "observedAt": "2023-01-25T22:23:39Z",  
    "value": 0.858472652447435  
  },  
  "operationMode": {  
    "type": "Property",  
    "value": "supply"  
  },  
  "operationTemperatureMax": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T17:43:31Z",  
    "value": 0.6990158373086164  
  },  
  "operationTemperatureMin": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T22:43:03Z",  
    "value": 0.070852494560947  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:4e9dc2df-6361-4376-979d-fb3f96ba8a2f"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:d80ed04b-6f2d-45eb-bcf9-f94ed0564d8f"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:e79640ab-b497-40a8-b020-23d2799cdb87"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:9c3ebe76-cc20-45d1-b436-759778c41424"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:b8bb079a-9cb2-4f4e-8f22-2e5ecbc4a37e"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Fan Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Fan 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T01:34:08Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T12:21:35Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Fan"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Fan type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Fan of limited Fan types"  
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
