<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: 인터셉터  
=========<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Interceptor/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **인터셉터는 정상적인 하수 또는 액체는 중력에 의해 수거 시스템으로 배출되도록 허용하면서 유해하거나 위험하거나 바람직하지 않은 물질을 분리 및 보유하기 위해 설계 및 설치된 장치입니다.**.  
버전: 0.0.  
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
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `coverLength[number]`: 로컬 좌표계에서 x축을 따라 측정한 길이 또는 오일 차단기 덮개의 반경(평면에서 원형인 경우)입니다. 일반적으로 밀리미터(mm) 단위로 측정됩니다.  - `coverWidth[number]`: 오일 차단기 커버의 로컬 좌표계에서 x축을 따라 측정된 길이입니다. 일반적으로 밀리미터(mm) 단위로 측정됩니다.  - `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `hasManufacturer[string]`: 엔티티의 제조업체를 식별하는 관계(예: 장치)입니다. 값은 문자열 또는 언어 태그가 포함된 문자열로 예상됩니다.  - `hasModel[string]`: 엔티티의 모델(예: 장치)을 식별하는 관계입니다. 값은 문자열 또는 언어 태그가 포함된 문자열로 예상됩니다.  - `id[*]`: 엔티티의 고유 식별자  - `inletConnectionSize[number]`: 입구 연결의 크기입니다. 일반적으로 밀리미터(mm) 단위로 측정됩니다.  - `isContainedInBuildingSpace[*]`: 건물의 물리적 공간을 정의하는 데 사용되는 엔티티입니다. 건물 공간에는 장치 또는 건물 개체가 포함됩니다. (빌딩 공간)  - `isContainedInPhysicalObject[*]`: 적절한 공간 영역을 가진 모든 객체.  (DUL 온톨로지에서 추출한 정의) (PhysicalObject)  - `isSubSystemOf[array]`: 이 피지컬 오브젝트가 속한 시스템에 대한 레퍼런스입니다.  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `nominalBodyDepth[number]`: 공칭 또는 따옴표로 묶인 =길이는 객체의 로컬 좌표계의 z축을 따라 객체 몸체의 길이를 측정합니다. 일반적으로 밀리미터(mm) 단위로 측정됩니다.  - `nominalBodyLength[number]`: 객체의 로컬 좌표계의 x축을 따라 측정된 객체 몸체의 공칭 또는 인용된 길이입니다. 일반적으로 밀리미터(mm) 단위로 측정됩니다.  - `nominalBodyWidth[number]`: 객체의 로컬 좌표계의 y축을 따라 측정된 객체 몸체의 공칭 또는 인용된 길이입니다. 일반적으로 밀리미터(mm) 단위로 측정됩니다.  - `outletConnectionSize[number]`: 콘센트 연결의 크기. 보통 밀리미터(mm) 단위로 측정됩니다.  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `type[string]`: 인터셉터`와 같아야 합니다.  - `ventilatingPipeSize[number]`: 환기 파이프의 크기. 일반적으로 밀리미터(mm) 단위로 측정됩니다.  <!-- /30-PropertiesList -->  
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
Interceptor:    
  description: 'An interceptor is a device designed and installed in order to separate and retain deleterious, hazardous or undesirable matter while permitting normal sewage or liquids to discharge into a collection system by gravity.'    
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
    coverLength:    
      description: The length measured along the x-axis in the local coordinate system or the radius (in the case of a circular shape in plan) of the cover of the oil interceptor. Usually measured in millimeters (mm)    
      type: number    
      x-ngsi:    
        type: Property    
    coverWidth:    
      description: The length measured along the x-axis in the local coordinate system of the cover of the oil interceptor. Usually measured in millimeters (mm)    
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
    inletConnectionSize:    
      description: Size of the inlet connection. Usually measured in millimeters (mm)    
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
    nominalBodyDepth:    
      description: 'Nominal or quoted =length, measured along the z-axis of the local coordinate system of the object, of the body of the object. Usually measured in millimeters (mm)'    
      type: number    
      x-ngsi:    
        type: Property    
    nominalBodyLength:    
      description: 'Nominal or quoted length, measured along the x-axis of the local coordinate system of the object, of the body of the object. Usually measured in millimeters (mm)'    
      type: number    
      x-ngsi:    
        type: Property    
    nominalBodyWidth:    
      description: 'Nominal or quoted length, measured along the y-axis of the local coordinate system of the object, of the body of the object. Usually measured in millimeters (mm)'    
      type: number    
      x-ngsi:    
        type: Property    
    outletConnectionSize:    
      description: Size of the outlet connection. Usually measured in millimeters (mm)    
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
      description: It must be equal to `Interceptor`    
      enum:    
        - Interceptor    
      type: string    
      x-ngsi:    
        type: Property    
    ventilatingPipeSize:    
      description: Size of the ventilating pipe(s). Usually measured in millimeters (mm)    
      type: number    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Interceptor"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Interceptor/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Interceptor/schema.json    
  x-model-tags: SAREF Interceptor    
  x-version: 0.0.    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### 인터셉터 NGSI-v2 키-값 예시  
다음은 키-값으로 JSON-LD 형식의 인터셉터 예제입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Interceptor:e70382d2-800a-4b96-be2e-03cfbe37ea51",  
    "type": "Interceptor",  
    "coverLength": 0.637563278020405,  
    "coverWidth": 0.39657091750888485,  
    "inletConnectionSize": 0.19141372654068167,  
    "nominalBodyDepth": 0.14989240074077315,  
    "nominalBodyLength": 0.06135027876899957,  
    "nominalBodyWidth": 0.7029889791860054,  
    "outletConnectionSize": 0.7108703974241664,  
    "ventilatingPipeSize": 0.5746572805545043,  
    "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:5a19b47d-28c9-43f1-9dc1-5970e15117e5",  
    "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:676f81a5-820d-474d-991e-2b87d2acd734",  
    "isSubSystemOf": [  
        "urn:ngsi-ld:System:5661f227-2a9c-49ce-a1e6-b0ac6fffdf71",  
        "urn:ngsi-ld:System:c9571a2a-2f4a-4c46-b931-0fe3489aaf15",  
        "urn:ngsi-ld:System:67c475d5-808d-4419-8c5f-1cdf158221f1"  
    ],  
    "hasManufacturer": "Interceptor Company Inc.",  
    "hasModel": "Interceptor 0.1.2",  
    "dateCreated": "2023-01-25T20:11:18Z",  
    "dateModified": "2023-01-26T02:38:35Z",  
    "source": "Import",  
    "name": "Interceptor",  
    "alternateName": "Interceptor type 2",  
    "description": "Interceptor of limited Interceptor types",  
    "dataProvider": "IFC file"  
}  
```  
</details>  
#### 인터셉터 NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 인터셉터 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Interceptor:e45ced8f-6d99-4b1e-a32b-d9e525d9429f",  
  "type": "Interceptor",  
  "coverLength": {  
    "type": "Measurement",  
    "value":  0.44339547398234425  
  },  
  "coverWidth": {  
    "type": "Measurement",  
    "value":0.8009891082993085  
  },  
  "inletConnectionSize": {  
    "type": "Measurement",  
    "value": 0.041004126787857476  
  },  
  "nominalBodyDepth": {  
    "type": "Measurement",  
    "value":  0.29190715678427104   
  },  
  "nominalBodyLength": {  
    "type": "Measurement",  
    "value":  0.3879109279352648    
  },  
  "nominalBodyWidth": {  
    "type": "Measurement",  
    "value":  0.41258224275422206   
  },  
  "outletConnectionSize": {  
    "type": "Measurement",  
    "value": 0.45113395263374134  
  },  
  "ventilatingPipeSize": {  
    "type": "Measurement",  
    "value": 0.9955414515835173  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:BuildingSpace:6e19661e-cc0d-40a9-a678-77eb09dbec66"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:PhysicalObject:ab4d138b-d0c3-4d88-96fa-9326f23e5946"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:284ae13c-0f10-4ade-bde1-84335db0e9c3"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:01933b47-4ff0-4a28-a3c1-ccda5080a98d"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:e0b79043-7cc6-45b0-a28a-8368751e98b8"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Interceptor Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Interceptor 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T19:09:02.6826601+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T23:45:53.2581226+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Interceptor"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Interceptor type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Interceptor of limited Interceptor types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### 인터셉터 NGSI-LD 키-값 예시  
다음은 키-값으로 JSON-LD 형식의 인터셉터 예시입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Interceptor:e70382d2-800a-4b96-be2e-03cfbe37ea51",  
  "type": "Interceptor",  
  "coverLength": 0.637563278020405,  
  "coverWidth": 0.39657091750888485,  
  "inletConnectionSize": 0.19141372654068167,  
  "nominalBodyDepth": 0.14989240074077315,  
  "nominalBodyLength": 0.06135027876899957,  
  "nominalBodyWidth": 0.7029889791860054,  
  "outletConnectionSize": 0.7108703974241664,  
  "ventilatingPipeSize": 0.5746572805545043,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:5a19b47d-28c9-43f1-9dc1-5970e15117e5",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:676f81a5-820d-474d-991e-2b87d2acd734",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:5661f227-2a9c-49ce-a1e6-b0ac6fffdf71",  
    "urn:ngsi-ld:System:c9571a2a-2f4a-4c46-b931-0fe3489aaf15",  
    "urn:ngsi-ld:System:67c475d5-808d-4419-8c5f-1cdf158221f1"  
  ],  
  "hasManufacturer": "Interceptor Company Inc.",  
  "hasModel": "Interceptor 0.1.2",  
  "dateCreated": "2023-01-25T20:11:18Z",  
  "dateModified": "2023-01-26T02:38:35Z",  
  "source": "Import",  
  "name": "Interceptor",  
  "alternateName": "Interceptor type 2",  
  "description": "Interceptor of limited Interceptor types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### 인터셉터 NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 인터셉터 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Interceptor:06f8171e-55bb-4229-ab9e-d558b4512982",  
  "type": "Interceptor",  
  "coverLength": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T04:52:13Z",  
    "value": 0.7541861378948772  
  },  
  "coverWidth": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T13:23:50Z",  
    "value": 0.18581009233424606  
  },  
  "inletConnectionSize": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T06:33:28Z",  
    "value": 0.5362664253813387  
  },  
  "nominalBodyDepth": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T01:38:01Z",  
    "value": 0.8646722014120122  
  },  
  "nominalBodyLength": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-25T14:16:38Z",  
    "value": 0.9860672918739783  
  },  
  "nominalBodyWidth": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-25T19:51:23Z",  
    "value": 0.8127360894676557  
  },  
  "outletConnectionSize": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T04:47:21Z",  
    "value": 0.5311465588349177  
  },  
  "ventilatingPipeSize": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T08:31:47Z",  
    "value": 0.7111321417760854  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:21622424-25f8-4e51-b604-713fb47019ac"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:69c1fa2f-3885-434a-b3dd-b7eb481dc4be"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:ddff37fe-7866-4af8-8fb2-2961e751ede0"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:9f5fd945-9540-4ddf-8af6-9e3f51f39f90"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:f007bebb-144c-4490-975b-b14698f42f2a"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Interceptor Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Interceptor 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T18:44:42Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-25T17:19:12Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Interceptor"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Interceptor type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Interceptor of limited Interceptor types"  
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
