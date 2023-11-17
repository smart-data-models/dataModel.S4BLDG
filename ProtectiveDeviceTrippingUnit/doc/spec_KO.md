<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: 보호 장치 트리핑 유닛    
=================<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/ProtectiveDeviceTrippingUnit/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: **보호 장치 트립 장치는 장치를 통과하는 규정 전류를 초과할 경우 별도의 차단 장치에서 전기 회로를 차단합니다.**    
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
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `hasManufacturer[string]`: 엔티티의 제조업체를 식별하는 관계(예: 장치)입니다. 값은 문자열 또는 언어 태그가 포함된 문자열로 예상됩니다.  - `hasModel[string]`: 엔티티의 모델(예: 장치)을 식별하는 관계입니다. 값은 문자열 또는 언어 태그가 포함된 문자열로 예상됩니다.  - `id[*]`: 엔티티의 고유 식별자  - `isContainedInBuildingSpace[*]`: 건물의 물리적 공간을 정의하는 데 사용되는 엔티티입니다. 건물 공간에는 장치 또는 건물 개체가 포함됩니다. (빌딩 공간)  - `isContainedInPhysicalObject[*]`: 적절한 공간 영역을 가진 모든 객체.  (DUL 온톨로지에서 추출한 정의) (PhysicalObject)  - `isSubSystemOf[array]`: 이 피지컬 오브젝트가 속한 시스템에 대한 레퍼런스입니다.  - `limitingTerminalSize[number]`: 장치의 최대 터미널 크기 용량입니다. 일반적으로 평방미터(m2) 단위로 측정됩니다.  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `standard[string]`: 단위의 특성을 정의하는 데 적용되는 표준 지정  - `type[string]`: 보호 장치 트리핑 유닛`과 같아야 합니다.  <!-- /30-PropertiesList -->    
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
ProtectiveDeviceTrippingUnit:      
  description: A protective device tripping unit breaks an electrical circuit at a separate breaking unit when a stated electric current that passes through the unit is exceeded.      
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
    limitingTerminalSize:      
      description: The maximum terminal size capacity of the device. Usually measured in square metre (m2)      
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
    standard:      
      description: The designation of the standard applicable for the definition of the characteristics of the unit      
      type: string      
      x-ngsi:      
        type: Property      
    type:      
      description: It must be equal to `ProtectiveDeviceTrippingUnit`      
      enum:      
        - ProtectiveDeviceTrippingUnit      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:ProtectiveDeviceTrippingUnit"      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/ProtectiveDeviceTrippingUnit/LICENSE.md      
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/ProtectiveDeviceTrippingUnit/schema.json      
  x-model-tags: SAREF ProtectiveDeviceTrippingUnit      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 페이로드 예시    
#### ProtectiveDeviceTrippingUnit NGSI-v2 키 값 예시    
다음은 키-값으로 JSON-LD 형식의 보호 장치 트리핑 유닛의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:ProtectiveDeviceTrippingUnit:a9978d1d-ff56-4285-ab6f-75c7ea9d9366",  
  "type": "ProtectiveDeviceTrippingUnit",  
  "limitingTerminalSize": 0.007349040029648757,  
  "standard": "transmit",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:0ab75dd1-ffd5-45b9-b82a-581cdc354a9a",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:c94d5308-85dc-4feb-a469-6e5fc8dd9e64",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:13b21daf-60e6-490b-883f-24f5e9439662",  
    "urn:ngsi-ld:System:6223a07f-c00a-40eb-b519-1260b420a8a4",  
    "urn:ngsi-ld:System:9dafd28f-9eb5-461d-a82d-2ddcbe017a87"  
  ],  
  "hasManufacturer": "ProtectiveDeviceTrippingUnit Company Inc.",  
  "hasModel": "ProtectiveDeviceTrippingUnit 0.1.2",  
  "dateCreated": "2023-01-26T07:35:56Z",  
  "dateModified": "2023-01-26T00:18:37Z",  
  "source": "Import",  
  "name": "ProtectiveDeviceTrippingUnit",  
  "alternateName": "ProtectiveDeviceTrippingUnit type 2",  
  "description": "ProtectiveDeviceTrippingUnit of limited ProtectiveDeviceTrippingUnit types",  
  "dataProvider": "IFC file"  
}  
```  
</details>    
#### ProtectiveDeviceTrippingUnit NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 보호 장치 트리핑 유닛의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:ProtectiveDeviceTrippingUnit:d0ceff43-b934-4f8b-9a61-ac3fb2d00ca0",  
  "type": "ProtectiveDeviceTrippingUnit",  
  "limitingTerminalSize": {  
    "type": "Number",  
    "value": 0.6188844647188521  
  },  
  "standard": {  
    "type": "Text",  
    "value": "alarm"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:BuildingSpace:9e090bad-e15b-4d58-98aa-fb3603aa29a9"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:PhysicalObject:6c1269e4-0729-42b5-a7c3-626c97c5e6f1"  
  },  
  "isSubSystemOf": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:System:90583732-ca11-440d-88a8-c8dfd68ba350",  
      "urn:ngsi-ld:System:fc4ff579-32de-4fb7-95a3-ef9fa07b0dc5",  
      "urn:ngsi-ld:System:68ddbc79-587d-4866-ae6d-3d9efcac6ac5"  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "ProtectiveDeviceTrippingUnit Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "ProtectiveDeviceTrippingUnit 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T07:05:39.1899219+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T16:04:21.3598466+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "ProtectiveDeviceTrippingUnit"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "ProtectiveDeviceTrippingUnit type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "ProtectiveDeviceTrippingUnit of limited ProtectiveDeviceTrippingUnit types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>    
#### ProtectiveDeviceTrippingUnit NGSI-LD 키 값 예시    
다음은 키 값으로 JSON-LD 형식의 보호 장치 트리핑 유닛의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:ProtectiveDeviceTrippingUnit:41659f5e-fe2b-4bb2-8ec4-ed401727e57d",  
  "type": "ProtectiveDeviceTrippingUnit",  
  "limitingTerminalSize": 0.37033727779383474,  
  "standard": "Sports, Games & Baby",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:d344d393-7664-4070-8f2f-e61396544c25",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:3dec837c-37b9-4f90-9c4f-4a1fe790b3bd",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:2599cb04-f959-4b4f-b3fc-bcaf4d989af1",  
    "urn:ngsi-ld:System:46b06cab-817c-4eda-8966-bd94e0be6ba8",  
    "urn:ngsi-ld:System:922d0ea6-fe00-4164-870b-541b868e838e"  
  ],  
  "hasManufacturer": "ProtectiveDeviceTrippingUnit Company Inc.",  
  "hasModel": "ProtectiveDeviceTrippingUnit 0.1.2",  
  "dateCreated": "2023-01-25T17:38:53Z",  
  "dateModified": "2023-01-26T01:14:24Z",  
  "source": "Import",  
  "name": "ProtectiveDeviceTrippingUnit",  
  "alternateName": "ProtectiveDeviceTrippingUnit type 2",  
  "description": "ProtectiveDeviceTrippingUnit of limited ProtectiveDeviceTrippingUnit types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>    
#### ProtectiveDeviceTrippingUnit NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 보호 장치 트리핑 유닛의 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:ProtectiveDeviceTrippingUnit:f10ca3f9-0120-45ce-9758-c7d87ff88556",  
  "type": "ProtectiveDeviceTrippingUnit",  
  "limitingTerminalSize": {  
    "type": "Property",  
    "unitCode": "m2",  
    "observedAt": "2023-01-25T16:18:32Z",  
    "value": 0.5988374624361508  
  },  
  "standard": {  
    "type": "Property",  
    "value": "turquoise"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:b4596d63-a279-46bd-9f55-787ea3bfea0c"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:be93a21f-cf03-446e-8bc6-3caf4d92fae9"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:386d031a-d13b-4b5f-a022-1aab55cc9bd5"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:2d9aeff1-a0f8-4cad-96a0-b01d99938948"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:9a4c8d68-59b1-4bf7-833d-871d2d835564"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "ProtectiveDeviceTrippingUnit Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "ProtectiveDeviceTrippingUnit 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T08:37:55Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T07:20:44Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "ProtectiveDeviceTrippingUnit"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "ProtectiveDeviceTrippingUnit type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "ProtectiveDeviceTrippingUnit of limited ProtectiveDeviceTrippingUnit types"  
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
