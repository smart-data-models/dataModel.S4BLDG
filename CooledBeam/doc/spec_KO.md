<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: CooledBeam    
===============<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/CooledBeam/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: **냉각 빔(또는 냉각 빔)은 일반적으로 공간 위의 노출된 핀 튜브를 통해 냉각수와 같은 유체를 순환시켜 공기를 냉각하는 데 사용되는 장치입니다. 일반적으로 천장 근처 또는 천장 내부에 설치되는 냉각 빔은 대류를 이용해 자연적으로 상승하는 공간의 따뜻한 공기에 방열판 역할을 함으로써 그 아래 공간을 냉각시킵니다. 냉각된 공기는 자연스럽게 바닥으로 떨어지면서 사이클이 다시 시작됩니다.**    
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
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `coilLength[number]`: 코일의 길이. 보통 밀리미터(mm) 단위로 측정됩니다.  - `coilWidth[number]`: 코일의 너비. 보통 밀리미터(mm) 단위로 측정합니다.  - `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `finishColor[string]`: 냉각 빔의 마감 색상  - `hasManufacturer[string]`: 엔티티의 제조업체를 식별하는 관계(예: 장치)입니다. 값은 문자열 또는 언어 태그가 포함된 문자열로 예상됩니다.  - `hasModel[string]`: 엔티티의 모델(예: 장치)을 식별하는 관계입니다. 값은 문자열 또는 언어 태그가 포함된 문자열로 예상됩니다.  - `id[*]`: 엔티티의 고유 식별자  - `integratedLightingType[string]`: 냉각식 빔에 통합 조명  - `isContainedInBuildingSpace[*]`: 건물의 물리적 공간을 정의하는 데 사용되는 엔티티입니다. 건물 공간에는 장치 또는 건물 개체가 포함됩니다. (빌딩 공간)  - `isContainedInPhysicalObject[*]`: 적절한 공간 영역을 가진 모든 객체.  (DUL 온톨로지에서 추출한 정의) (PhysicalObject)  - `isFreeHanging[boolean]`: 프리 행잉 타입인가요(가천장에 설치되지 않음)?  - `isSubSystemOf[array]`: 이 피지컬 오브젝트가 속한 시스템에 대한 레퍼런스입니다.  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `nominalCoolingCapacity[number]`: 공칭 냉각 용량. 일반적으로 와트(W, J/s) 단위로 측정됩니다.  - `nominalHeatingCapacity[number]`: 공칭 난방 용량. 일반적으로 와트(W, J/s) 단위로 측정됩니다.  - `nominalReturnWaterTemperatureCooling[number]`: 공칭 회수 수온(공칭 냉각 용량 참조). 일반적으로 켈빈(K) 단위로 측정됩니다.  - `nominalReturnWaterTemperatureHeating[number]`: 공칭 회수 수온(공칭 난방 용량 참조). 일반적으로 켈빈(K) 단위로 측정됩니다.  - `nominalSorroundingHumidityCooling[number]`: 공칭 주변 습도(공칭 냉각 용량 참조). 일반적으로 켈빈(K) 단위로 측정됩니다.  - `nominalSorroundingTemperatureCooling[number]`: 공칭 주변 온도(공칭 냉각 용량 참조). 일반적으로 켈빈(K) 단위로 측정됩니다.  - `nominalSorroundingTemperatureHeating[number]`: 공칭 주변 온도(공칭 난방 용량 참조). 일반적으로 켈빈(K) 단위로 측정됩니다.  - `nominalSupplyWaterTemperatureCooling[number]`: 공칭 공급수 온도(공칭 냉각 용량 참조). 일반적으로 켈빈(K) 단위로 측정됩니다.  - `nominalSupplyWaterTemperatureHeating[number]`: 공칭 공급수 온도(공칭 난방 용량 참조). 일반적으로 켈빈(K) 단위로 측정됩니다.  - `nominalWaterFlowCooling[number]`: 공칭 물 흐름(공칭 냉각 용량 참조). 일반적으로 m3/s 단위로 측정  - `nominalWaterFlowHeating[number]`: 공칭 물 흐름(공칭 난방 용량 참조). 일반적으로 m3/s 단위로 측정  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `pipeConnectionEnum[string]`: 냉각된 빔에 파이프가 연결되는 방식  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `type[string]`: CooledBeam`과 같아야 합니다.  - `waterFlowControlSystemType[string]`: 공장에서 장착된 물 흐름 제어 시스템  - `waterPressureMax[number]`: 허용되는 물 회로 작동 압력 범위. 일반적으로 파스칼(Pa, N/m2) 단위로 측정됩니다.  - `waterPressureMin[number]`: 허용되는 물 회로 작동 압력 범위. 일반적으로 파스칼(Pa, N/m2) 단위로 측정됩니다.  <!-- /30-PropertiesList -->    
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
CooledBeam:      
  description: 'A cooled beam (or chilled beam) is a device typically used to cool air by circulating a fluid such as chilled water through exposed finned tubes above a space. Typically mounted overhead near or within a ceiling, the cooled beam uses convection to cool the space below it by acting as a heat sink for the naturally rising warm air of the space. Once cooled, the air naturally drops back to the floor where the cycle begins again.'      
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
    coilLength:      
      description: Length of coil. Usually measured in millimeters (mm)      
      type: number      
      x-ngsi:      
        type: Property      
    coilWidth:      
      description: Width of coil. Usually measured in millimeters (mm      
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
    finishColor:      
      description: Finish color for cooled beam      
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
    integratedLightingType:      
      description: Integrated lighting in cooled beam      
      type: string      
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
    isFreeHanging:      
      description: 'Is it free hanging type (not mounted in a false ceiling)?'      
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
    nominalCoolingCapacity:      
      description: 'Nominal cooling capacity. Usually measured in Watts (W, J/s)'      
      type: number      
      x-ngsi:      
        type: Property      
    nominalHeatingCapacity:      
      description: 'Nominal heating capacity. Usually measured in Watts (W, J/s)'      
      type: number      
      x-ngsi:      
        type: Property      
    nominalReturnWaterTemperatureCooling:      
      description: Nominal return water temperature (refers to nominal cooling capacity). Usually measured in degrees Kelvin (K)      
      type: number      
      x-ngsi:      
        type: Property      
    nominalReturnWaterTemperatureHeating:      
      description: Nominal return water temperature (refers to nominal heating capacity). Usually measured in degrees Kelvin (K)      
      type: number      
      x-ngsi:      
        type: Property      
    nominalSorroundingHumidityCooling:      
      description: Nominal surrounding humidity (refers to nominal cooling capacity). Usually measured in degrees Kelvin (K)      
      type: number      
      x-ngsi:      
        type: Property      
    nominalSorroundingTemperatureCooling:      
      description: Nominal surrounding temperature (refers to nominal cooling capacity). Usually measured in degrees Kelvin (K)      
      type: number      
      x-ngsi:      
        type: Property      
    nominalSorroundingTemperatureHeating:      
      description: Nominal surrounding temperature (refers to nominal heating capacity). Usually measured in degrees Kelvin (K)      
      type: number      
      x-ngsi:      
        type: Property      
    nominalSupplyWaterTemperatureCooling:      
      description: Nominal supply water temperature (refers to nominal cooling capacity). Usually measured in degrees Kelvin (K)      
      type: number      
      x-ngsi:      
        type: Property      
    nominalSupplyWaterTemperatureHeating:      
      description: Nominal supply water temperature (refers to nominal heating capacity). Usually measured in degrees Kelvin (K)      
      type: number      
      x-ngsi:      
        type: Property      
    nominalWaterFlowCooling:      
      description: Nominal water flow (refers to nominal cooling capacity). Usually measured in m3/s      
      type: number      
      x-ngsi:      
        type: Property      
    nominalWaterFlowHeating:      
      description: Nominal water flow (refers to nominal heating capacity). Usually measured in m3/s      
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
    pipeConnectionEnum:      
      description: The manner in which the pipe connection is made to the cooled beam      
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
      description: It must be equal to `CooledBeam`      
      enum:      
        - CooledBeam      
      type: string      
      x-ngsi:      
        type: Property      
    waterFlowControlSystemType:      
      description: Factory fitted waterflow control system      
      type: string      
      x-ngsi:      
        type: Property      
    waterPressureMax:      
      description: 'Allowable water circuit working pressure range. Usually measured in Pascals (Pa, N/m2)'      
      type: number      
      x-ngsi:      
        type: Property      
    waterPressureMin:      
      description: 'Allowable water circuit working pressure range. Usually measured in Pascals (Pa, N/m2)'      
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
  x-model-tags: SAREF CooledBeam      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 페이로드 예시    
#### CooledBeam NGSI-v2 키값 예시    
다음은 키-값으로 JSON-LD 형식의 CooledBeam의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
#### CooledBeam NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 CooledBeam의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:CooledBeam:38dcdd25-ae94-441c-8409-218ec91e3006",  
  "type": "CooledBeam",  
  "coilLength": {  
    "type": "Number",  
    "value": 0.4277226249853211  
  },  
  "coilWidth": {  
    "type": "Number",  
    "value": 0.6183775851562611  
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
    "type": "Number",  
    "value": 0.45857043485420457  
  },  
  "nominalHeatingCapacity": {  
    "type": "Number",  
    "value": 0.37812382267356337  
  },  
  "nominalReturnWaterTemperatureCooling": {  
    "type": "Number",  
    "value": 0.973742767691913  
  },  
  "nominalReturnWaterTemperatureHeating": {  
    "type": "Number",  
    "value": 0.6848085584395665  
  },  
  "nominalSorroundingHumidityCooling": {  
    "type": "Number",  
    "value": 0.4100986776385609  
  },  
  "nominalSorroundingTemperatureCooling": {  
    "type": "Number",  
    "value": 0.039909771141081074  
  },  
  "nominalSorroundingTemperatureHeating": {  
    "type": "Number",  
    "value": 0.3023923557796515  
  },  
  "nominalSupplyWaterTemperatureCooling": {  
    "type": "Number",  
    "value": 0.7562940127899793  
  },  
  "nominalSupplyWaterTemperatureHeating": {  
    "type": "Number",  
    "value": 0.31198678394809454  
  },  
  "nominalWaterFlowCooling": {  
    "type": "Number",  
    "value": 0.40924277893308847  
  },  
  "nominalWaterFlowHeating": {  
    "type": "Number",  
    "value": 0.9345939456733873  
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
    "type": "Number",  
    "value": 0.07837257218461391  
  },  
  "waterPressureMin": {  
    "type": "Number",  
    "value": 0.03742669539477306  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:BuildingSpace:3e03fe30-3728-4867-ab51-b147c2d3e63b"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:PhysicalObject:cfd9df05-18b1-44f4-b1ee-da55226255e9"  
  },  
  "isSubSystemOf": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:System:a4b0cda0-b373-4ae9-b2c7-e2cff5429e1e",  
      "urn:ngsi-ld:System:216f6f83-8bd1-456f-9bed-36dbec41a3aa",  
      "urn:ngsi-ld:System:d19ccffa-f134-46fc-8f9f-77656bb91649"  
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
#### CooledBeam NGSI-LD 키 값 예시    
다음은 키-값으로 JSON-LD 형식의 CooledBeam의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
#### CooledBeam NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 CooledBeam의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
