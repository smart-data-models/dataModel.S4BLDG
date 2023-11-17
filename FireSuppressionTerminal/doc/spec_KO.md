<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: 화재 진압 터미널    
==============<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/FireSuppressionTerminal/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: **화재 진압 터미널은 화재를 진압할 유체(가스 또는 액체)를 전달하는 것을 목적으로 합니다.  화재 진압 터미널은 배관 시스템에 연결되어 화재를 진압하는 역할을 하는 모든 형태의 스프링클러, 살포기 및 기타 형태의 터미널을 제공합니다.**    
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
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `hasManufacturer[string]`: 엔티티의 제조업체를 식별하는 관계(예: 장치)입니다. 값은 문자열 또는 언어 태그가 포함된 문자열로 예상됩니다.  - `hasModel[string]`: 엔티티의 모델(예: 장치)을 식별하는 관계입니다. 값은 문자열 또는 언어 태그가 포함된 문자열로 예상됩니다.  - `id[*]`: 엔티티의 고유 식별자  - `isContainedInBuildingSpace[*]`: 건물의 물리적 공간을 정의하는 데 사용되는 엔티티입니다. 건물 공간에는 장치 또는 건물 개체가 포함됩니다. (빌딩 공간)  - `isContainedInPhysicalObject[*]`: 적절한 공간 영역을 가진 모든 객체.  (DUL 온톨로지에서 추출한 정의) (PhysicalObject)  - `isSubSystemOf[array]`: 이 피지컬 오브젝트가 속한 시스템에 대한 레퍼런스입니다.  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `type[string]`: FireSuppressionTerminal`과 같아야 합니다.  <!-- /30-PropertiesList -->    
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
FireSuppressionTerminal:      
  description: 'A fire suppression terminal has the purpose of delivering a fluid (gas or liquid) that will suppress a fire.  A fire suppression terminal provides for all forms of sprinkler, spreader and other form of terminal that is connected to a pipework system and intended to act in the role of suppressing a fire.'      
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
    type:      
      description: It must be equal to `FireSuppressionTerminal`      
      enum:      
        - FireSuppressionTerminal      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:FireSuppressionTerminal"      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/FireSuppressionTerminal/LICENSE.md      
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/FireSuppressionTerminal/schema.json      
  x-model-tags: SAREF FireSuppressionTerminal      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 페이로드 예시    
#### FireSuppressionTerminal NGSI-v2 키 값 예시    
다음은 키-값으로 JSON-LD 형식의 FireSuppressionTerminal의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:FireSuppressionTerminal:46b595ee-54b5-40c5-a24e-4e3c5c1bb5ba",  
  "type": "FireSuppressionTerminal",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:f537e09c-8ef7-4f98-9b0b-1c59f8462648",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:b1c88eee-f678-49b4-b622-674b16e499f0",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:9aa3f554-6ce7-49db-a32d-07bf807d7763",  
    "urn:ngsi-ld:System:7102f790-fd82-402a-ba60-5c5a79d3fc3d",  
    "urn:ngsi-ld:System:cb8023a6-5b92-4c80-8cf3-c5ec46c64e57"  
  ],  
  "hasManufacturer": "FireSuppressionTerminal Company Inc.",  
  "hasModel": "FireSuppressionTerminal 0.1.2",  
  "dateCreated": "2023-01-25T21:23:42Z",  
  "dateModified": "2023-01-26T02:53:39Z",  
  "source": "Import",  
  "name": "FireSuppressionTerminal",  
  "alternateName": "FireSuppressionTerminal type 2",  
  "description": "FireSuppressionTerminal of limited FireSuppressionTerminal types",  
  "dataProvider": "IFC file"  
}  
```  
</details>    
#### FireSuppressionTerminal NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 FireSuppressionTerminal의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:FireSuppressionTerminal:f45acb30-c282-460f-95b0-5c14d69923d9",  
  "type": "FireSuppressionTerminal",  
  "isContainedInBuildingSpace": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:BuildingSpace:45f2a673-b419-4a10-bfda-16623713dc37"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:PhysicalObject:75c6b864-e882-4b7d-8794-8936df8f7deb"  
  },  
  "isSubSystemOf": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:System:99be813e-a877-4b55-aa0b-7bf449c3f3ea",  
      "urn:ngsi-ld:System:8358c738-4053-4787-b9a8-d3b98d95e1e9",  
      "urn:ngsi-ld:System:116d5ed2-34ca-4b99-8ea3-d6fea2d6acea"  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "FireSuppressionTerminal Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "FireSuppressionTerminal 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T22:17:42.4115636+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T04:01:40.8529856+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "FireSuppressionTerminal"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "FireSuppressionTerminal type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "FireSuppressionTerminal of limited FireSuppressionTerminal types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>    
#### FireSuppressionTerminal NGSI-LD 키 값 예시    
다음은 키-값으로 JSON-LD 형식의 FireSuppressionTerminal의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:FireSuppressionTerminal:c202a2c3-79a9-48a0-8492-169aa9d113e6",  
  "type": "FireSuppressionTerminal",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:d8c18c4d-f60d-429d-bfda-44689825a2df",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:b2875a65-7e00-4d62-a629-8231df841f27",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:a792de28-61ae-48d5-b846-600e2f5a2677",  
    "urn:ngsi-ld:System:95e1f552-83c1-44ff-b2a9-ca60dca852c4",  
    "urn:ngsi-ld:System:640d2741-287f-4634-a2b5-70ad4056c298"  
  ],  
  "hasManufacturer": "FireSuppressionTerminal Company Inc.",  
  "hasModel": "FireSuppressionTerminal 0.1.2",  
  "dateCreated": "2023-01-26T10:29:38Z",  
  "dateModified": "2023-01-26T10:34:00Z",  
  "source": "Import",  
  "name": "FireSuppressionTerminal",  
  "alternateName": "FireSuppressionTerminal type 2",  
  "description": "FireSuppressionTerminal of limited FireSuppressionTerminal types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>    
#### FireSuppressionTerminal NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 FireSuppressionTerminal의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:FireSuppressionTerminal:252e5c25-8b52-438a-afba-8be31e98e272",  
  "type": "FireSuppressionTerminal",  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:114ef098-ce1a-4472-9dde-920ce363a235"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:368214d7-9133-43b9-a039-cfc29a776bd3"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:b021ab2b-22e3-4138-8476-ec6b4cc3f50d"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:6463b606-5b54-4d7f-9e94-6cfd6fc02f65"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:ada26427-12e2-4d5b-ab7b-0756e7a0ab09"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "FireSuppressionTerminal Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "FireSuppressionTerminal 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T00:18:51Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T10:04:54Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "FireSuppressionTerminal"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "FireSuppressionTerminal type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "FireSuppressionTerminal of limited FireSuppressionTerminal types"  
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
