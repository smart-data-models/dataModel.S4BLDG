<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: 댐퍼  
=======<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Damper/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **댐퍼는 일반적으로 HVAC 덕트 분배 시스템에 참여하며 공기의 흐름을 제어하거나 조절하는 데 사용됩니다.**  
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
- `airFlowRateMax[number]`: 최대 허용 공기 유량. 보통 m3/s 단위로 측정됩니다.  - `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `bladeAction[string]`: 블레이드 액션  - `bladeEdge[string]`: 블레이드 가장자리  - `bladeShape[string]`: 블레이드 모양. 플랫은 트리플 V 홈을 의미합니다.  - `bladeThickness[number]`: 댐퍼 블레이드의 두께입니다. 일반적으로 밀리미터(mm) 단위로 측정됩니다.  - `closeOffRating[number]`: 마감 등급. 일반적으로 파스칼(Pa, N/m2) 단위로 측정됩니다.  - `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `faceArea[number]`: 기류에 개방된 얼굴 면적. 보통 평방미터(m2) 단위로 측정됩니다.  - `frameDepth[number]`: 댐퍼 프레임의 길이(또는 깊이)입니다. 일반적으로 밀리미터(mm) 단위로 측정됩니다.  - `frameThickness[number]`: 댐퍼 프레임 소재의 두께입니다. 일반적으로 밀리미터(mm) 단위로 측정됩니다.  - `frameType[string]`: 댐퍼에 사용되는 프레임 유형(예: 표준, 싱글 플랜지, 싱글 리버스 플랜지, 더블 플랜지 등)  - `hasManufacturer[string]`: 엔티티의 제조업체를 식별하는 관계(예: 장치)입니다. 값은 문자열 또는 언어 태그가 포함된 문자열로 예상됩니다.  - `hasModel[string]`: 엔티티의 모델(예: 장치)을 식별하는 관계입니다. 값은 문자열 또는 언어 태그가 포함된 문자열로 예상됩니다.  - `id[*]`: 엔티티의 고유 식별자  - `isContainedInBuildingSpace[*]`: 건물의 물리적 공간을 정의하는 데 사용되는 엔티티입니다. 건물 공간에는 장치 또는 건물 개체가 포함됩니다. (빌딩 공간)  - `isContainedInPhysicalObject[*]`: 적절한 공간 영역을 가진 모든 객체.  (DUL 온톨로지에서 추출한 정의) (PhysicalObject)  - `isSubSystemOf[array]`: 이 피지컬 오브젝트가 속한 시스템에 대한 레퍼런스입니다.  - `leakageFullyClosed[number]`: 완전히 닫혔을 때의 누출량. 보통 m3/s 단위로 측정됩니다.  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `nominalAirFlowRate[number]`: 공칭 공기 흐름 속도. 보통 m3/s 단위로 측정됩니다.  - `numberOfBlades[number]`: 블레이드 개수  - `openPressureDrop[number]`: 댐퍼 전체에 걸친 총 압력 강하. 일반적으로 파스칼(Pa, N/m2) 단위로 측정됩니다.  - `operation[string]`: 댐퍼 작동을 위한 작동 메커니즘  - `operationMode[string]`: 이 댐퍼의 작동 모드  - `operationTemperatureMax[number]`: 허용되는 작동 주변(공기, 유체) 온도 범위. 일반적으로 켈빈(K) 단위로 측정됩니다.  - `operationTemperatureMin[number]`: 허용되는 작동 주변(공기, 유체) 온도 범위. 일반적으로 켈빈(K) 단위로 측정됩니다.  - `orientation[string]`: 제조업체에서 지정한 댐퍼의 의도된 방향  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `temperatureRating[number]`: 온도 등급. 일반적으로 켈빈(K) 단위로 측정됩니다.  - `type[string]`: 댐퍼`와 같아야 합니다.  - `workingPressureMax[number]`: 최대 작동 압력. 일반적으로 파스칼(Pa, N/m2) 단위로 측정됩니다.  <!-- /30-PropertiesList -->  
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
Damper:    
  description: A damper typically participates in an HVAC duct distribution system and is used to control or modulate the flow of air.    
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
    airFlowRateMax:    
      description: Maximum allowable air flow rate. Usually measured in m3/s    
      type: number    
      x-ngsi:    
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
    bladeAction:    
      description: Blade action    
      type: string    
      x-ngsi:    
        type: Property    
    bladeEdge:    
      description: Blade edge    
      type: string    
      x-ngsi:    
        type: Property    
    bladeShape:    
      description: Blade shape. Flat means triple V-groove    
      type: string    
      x-ngsi:    
        type: Property    
    bladeThickness:    
      description: The thickness of the damper blade. Usually measured in millimeters (mm)    
      type: number    
      x-ngsi:    
        type: Property    
    closeOffRating:    
      description: 'Close off rating. Usually measured in Pascals (Pa, N/m2)'    
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
    faceArea:    
      description: Face area open to the airstream. Usually measured in square metre (m2)    
      type: number    
      x-ngsi:    
        type: Property    
    frameDepth:    
      description: The length (or depth) of the damper frame. Usually measured in millimeters (mm)    
      type: number    
      x-ngsi:    
        type: Property    
    frameThickness:    
      description: The thickness of the damper frame material. Usually measured in millimeters (mm)    
      type: number    
      x-ngsi:    
        type: Property    
    frameType:    
      description: 'The type of frame used by the damper (e.g., Standard, Single Flange, Single Reversed Flange, Double Flange, etc.)'    
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
    leakageFullyClosed:    
      description: Leakage when fully closed. Usually measured in m3/s    
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
    nominalAirFlowRate:    
      description: Nominal rate of air flow. Usually measured in m3/s    
      type: number    
      x-ngsi:    
        type: Property    
    numberOfBlades:    
      description: Number of blades    
      type: number    
      x-ngsi:    
        type: Property    
    openPressureDrop:    
      description: 'Total pressure drop across damper. Usually measured in Pascals (Pa, N/m2)'    
      type: number    
      x-ngsi:    
        type: Property    
    operation:    
      description: The operational mechanism for the damper operation    
      type: string    
      x-ngsi:    
        type: Property    
    operationMode:    
      description: Operation mode of this damper    
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
    orientation:    
      description: The intended orientation for the damper as specified by the manufacturer    
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
    temperatureRating:    
      description: Temperature rating. Usually measured in degrees Kelvin (K)    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: It must be equal to `Damper`    
      enum:    
        - Damper    
      type: string    
      x-ngsi:    
        type: Property    
    workingPressureMax:    
      description: 'Maximum working pressure. Usually measured in Pascals (Pa, N/m2)'    
      type: number    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Damper"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Damper/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Damper/schema.json    
  x-model-tags: SAREF Damper    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### 댐퍼 NGSI-v2 키값 예시  
다음은 JSON-LD 형식의 댐퍼를 키값으로 반환하는 예제입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Damper:65c94159-bfe6-416d-b02c-283479048fe3",  
  "type": "Damper",  
  "airFlowRateMax": 0.5927918101987754,  
  "bladeAction": "Belize Dollar",  
  "bladeEdge": "frictionless",  
  "bladeShape": "intermediate",  
  "bladeThickness": 0.5665758025960763,  
  "closeOffRating": 0.8924252696459434,  
  "faceArea": 0.45839947738381925,  
  "frameDepth": 0.6687870848219263,  
  "frameThickness": 0.6594470368135407,  
  "frameType": "Ergonomic",  
  "leakageFullyClosed": 0.052627216627954665,  
  "nominalAirFlowRate": 0.7333602290466408,  
  "numberOfBlades": 0.3476917428528077,  
  "openPressureDrop": 0.8991384789588308,  
  "operation": "Implemented",  
  "operationMode": "supply",  
  "operationTemperatureMax": 0.07772736087657628,  
  "operationTemperatureMin": 0.4857292385786113,  
  "orientation": "reboot",  
  "temperatureRating": 0.4909792118139581,  
  "workingPressureMax": 0.10839736205746486,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:c25bebe3-d546-4942-be72-9468ce218070",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:326da1c1-440d-4200-b598-a84e3bf5fdc1",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:007e61a9-027a-4662-a7a0-1e9e48f57886",  
    "urn:ngsi-ld:System:59945456-4e66-4c84-b637-7c771479a9f3",  
    "urn:ngsi-ld:System:023e0706-8d3d-411b-9e97-994a870341cd"  
  ],  
  "hasManufacturer": "Damper Company Inc.",  
  "hasModel": "Damper 0.1.2",  
  "dateCreated": "2023-01-25T18:10:59Z",  
  "dateModified": "2023-01-26T07:49:53Z",  
  "source": "Import",  
  "name": "Damper",  
  "alternateName": "Damper type 2",  
  "description": "Damper of limited Damper types",  
  "dataProvider": "IFC file"  
}  
```  
</details>  
#### 댐퍼 NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 댐퍼의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Damper:30830dab-6aa5-4dd1-9e48-d6ac7e24e4bf",  
  "type": "Damper",  
  "airFlowRateMax": {  
    "type": "Measurement",  
    "value":  0.13813389168852752  
  },  
  "bladeAction": {  
    "type": "Text",  
    "value": "Spur"  
  },  
  "bladeEdge": {  
    "type": "Text",  
    "value": "Personal Loan Account"  
  },  
  "bladeShape": {  
    "type": "Text",  
    "value": "Human"  
  },  
  "bladeThickness": {  
    "type": "Measurement",  
    "value":  0.35230461364031296  
  },  
  "closeOffRating": {  
    "type": "Measurement",  
    "value":  0.171775838539866  
  },  
  "faceArea": {  
    "type": "Measurement",  
    "value": 0.4212393478883142  
  },  
  "frameDepth": {  
    "type": "Measurement",  
    "value": 0.8035081586701794  
  },  
  "frameThickness": {  
    "type": "Measurement",  
    "value":  0.28946308913206176  
  },  
  "frameType": {  
    "type": "Text",  
    "value": "Balanced"  
  },  
  "leakageFullyClosed": {  
    "type": "Measurement",  
    "value":  0.44075236436472953  
  },  
  "nominalAirFlowRate": {  
    "type": "Measurement",  
    "value":0.47305378645729657  
  },  
  "numberOfBlades": {  
    "type": "Float",  
    "value": 0.8083872561368712  
  },  
  "openPressureDrop": {  
    "type": "Measurement",  
    "value": 0.9106213284285767  
  },  
  "operation": {  
    "type": "Text",  
    "value": "Handcrafted Concrete Computer"  
  },  
  "operationMode": {  
    "type": "DamperOperationMode",  
    "value": "supply"  
  },  
  "operationTemperatureMax": {  
    "type": "Measurement",  
    "value":  0.87576324331876  
  },  
  "operationTemperatureMin": {  
    "type": "Measurement",  
    "value":  0.3952529455728351  
  },  
  "orientation": {  
    "type": "Text",  
    "value": "Mozambique"  
  },  
  "temperatureRating": {  
    "type": "Measurement",  
    "value":  0.43326401348250587  
  },  
  "workingPressureMax": {  
    "type": "Measurement",  
    "value":  0.2695729035947665  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:BuildingSpace:f19ff450-12f4-472a-985e-40b163530ccd"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:PhysicalObject:ee6c23f3-7261-4807-b3e3-703588646f02"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:a8f8f637-52c0-491d-890e-2806ffbdc6cd"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:7f5f939e-9a41-4ca6-95ff-4ece8ffec42c"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:ff7924ea-c532-40c9-a1ac-449c76216073"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Damper Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Damper 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T15:13:23.9679787+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T16:00:58.1902016+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Damper"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Damper type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Damper of limited Damper types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### 댐퍼 NGSI-LD 키 값 예시  
다음은 JSON-LD 형식의 댐퍼를 키값으로 사용한 예시입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Damper:65c94159-bfe6-416d-b02c-283479048fe3",  
  "type": "Damper",  
  "airFlowRateMax": 0.5927918101987754,  
  "bladeAction": "Belize Dollar",  
  "bladeEdge": "frictionless",  
  "bladeShape": "intermediate",  
  "bladeThickness": 0.5665758025960763,  
  "closeOffRating": 0.8924252696459434,  
  "faceArea": 0.45839947738381925,  
  "frameDepth": 0.6687870848219263,  
  "frameThickness": 0.6594470368135407,  
  "frameType": "Ergonomic",  
  "leakageFullyClosed": 0.052627216627954665,  
  "nominalAirFlowRate": 0.7333602290466408,  
  "numberOfBlades": 0.3476917428528077,  
  "openPressureDrop": 0.8991384789588308,  
  "operation": "Implemented",  
  "operationMode": "supply",  
  "operationTemperatureMax": 0.07772736087657628,  
  "operationTemperatureMin": 0.4857292385786113,  
  "orientation": "reboot",  
  "temperatureRating": 0.4909792118139581,  
  "workingPressureMax": 0.10839736205746486,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:c25bebe3-d546-4942-be72-9468ce218070",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:326da1c1-440d-4200-b598-a84e3bf5fdc1",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:007e61a9-027a-4662-a7a0-1e9e48f57886",  
    "urn:ngsi-ld:System:59945456-4e66-4c84-b637-7c771479a9f3",  
    "urn:ngsi-ld:System:023e0706-8d3d-411b-9e97-994a870341cd"  
  ],  
  "hasManufacturer": "Damper Company Inc.",  
  "hasModel": "Damper 0.1.2",  
  "dateCreated": "2023-01-25T18:10:59Z",  
  "dateModified": "2023-01-26T07:49:53Z",  
  "source": "Import",  
  "name": "Damper",  
  "alternateName": "Damper type 2",  
  "description": "Damper of limited Damper types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### 댐퍼 NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 댐퍼의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Damper:99cb9b35-5f17-4e4d-89bb-e9d7bb88c2ba",  
  "type": "Damper",  
  "airFlowRateMax": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-26T10:15:08Z",  
    "value": 0.46010915943742847  
  },  
  "bladeAction": {  
    "type": "Property",  
    "value": "microchip"  
  },  
  "bladeEdge": {  
    "type": "Property",  
    "value": "Village"  
  },  
  "bladeShape": {  
    "type": "Property",  
    "value": "Netherlands Antillian Guilder"  
  },  
  "bladeThickness": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-25T21:36:37Z",  
    "value": 0.5214778377905084  
  },  
  "closeOffRating": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-25T18:21:40Z",  
    "value": 0.8241451329002358  
  },  
  "faceArea": {  
    "type": "Property",  
    "unitCode": "m2",  
    "observedAt": "2023-01-25T20:36:04Z",  
    "value": 0.6197704906516315  
  },  
  "frameDepth": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T14:05:58Z",  
    "value": 0.19371235604272175  
  },  
  "frameThickness": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-25T21:48:43Z",  
    "value": 0.630746648821536  
  },  
  "frameType": {  
    "type": "Property",  
    "value": "SAS"  
  },  
  "leakageFullyClosed": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-25T21:59:27Z",  
    "value": 0.8430168839934075  
  },  
  "nominalAirFlowRate": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-26T06:30:50Z",  
    "value": 0.8419372074040988  
  },  
  "numberOfBlades": {  
    "type": "Property",  
    "value": 0.2730424937241438  
  },  
  "openPressureDrop": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-26T04:03:50Z",  
    "value": 0.25493844227297535  
  },  
  "operation": {  
    "type": "Property",  
    "value": "partnerships"  
  },  
  "operationMode": {  
    "type": "Property",  
    "value": "exhaust"  
  },  
  "operationTemperatureMax": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T22:15:50Z",  
    "value": 0.4402985682699154  
  },  
  "operationTemperatureMin": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T11:49:40Z",  
    "value": 0.0015019955460002787  
  },  
  "orientation": {  
    "type": "Property",  
    "value": "Metrics"  
  },  
  "temperatureRating": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T16:28:22Z",  
    "value": 0.6012606116766228  
  },  
  "workingPressureMax": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-26T09:39:16Z",  
    "value": 0.320862748056973  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:573f5e7a-806c-4deb-878c-365ef09fe4d2"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:0cbecfb0-1008-4c54-99f6-510fba847457"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:972e3b8b-9613-4b3a-a798-f3e56587d999"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:0d09725f-1468-4352-92e9-39d0b647a683"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:0c5bf106-93a0-4eb9-a15d-a0d834088c94"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Damper Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Damper 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T10:37:53Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T10:42:54Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Damper"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Damper type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Damper of limited Damper types"  
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
