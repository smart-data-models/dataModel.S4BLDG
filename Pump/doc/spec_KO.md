<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: 펌프  
=======<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Pump/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **펌프는 유체 또는 슬러리에 기계적 작업을 가하여 채널 또는 파이프 라인을 통해 이동시키는 장치입니다. 펌프의 일반적인 용도는 건물 서비스 분배 시스템에서 냉수 또는 난방 온수를 순환시키는 것입니다.  
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
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `connectionSize[number]`: 펌프와 펌프 사이의 연결 크기입니다. 일반적으로 밀리미터(mm) 단위로 측정됩니다.  - `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `flowResistanceMax[number]`: 유체가 펌핑되는 마찰 저항의 허용 범위입니다. 일반적으로 파스칼(Pa, N/m2) 단위로 측정됩니다.  - `flowResistanceMin[number]`: 유체가 펌핑되는 마찰 저항의 허용 범위입니다. 일반적으로 파스칼(Pa, N/m2) 단위로 측정됩니다.  - `hasManufacturer[string]`: 엔티티의 제조업체를 식별하는 관계(예: 장치)입니다. 값은 문자열 또는 언어 태그가 포함된 문자열로 예상됩니다.  - `hasModel[string]`: 엔티티의 모델(예: 장치)을 식별하는 관계입니다. 값은 문자열 또는 언어 태그가 포함된 문자열로 예상됩니다.  - `id[*]`: 엔티티의 고유 식별자  - `isContainedInBuildingSpace[*]`: 건물의 물리적 공간을 정의하는 데 사용되는 엔티티입니다. 건물 공간에는 장치 또는 건물 개체가 포함됩니다. (빌딩 공간)  - `isContainedInPhysicalObject[*]`: 적절한 공간 영역을 가진 모든 객체.  (DUL 온톨로지에서 추출한 정의) (PhysicalObject)  - `isSubSystemOf[array]`: 이 피지컬 오브젝트가 속한 시스템에 대한 레퍼런스입니다.  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `netPositiveSuctionHead[number]`: 캐비테이션을 방지하기 위한 펌프 입구의 최소 액체 압력입니다. 일반적으로 파스칼(Pa, N/m2) 단위로 측정됩니다.  - `nomminalRotationSpeed[number]`: 공칭 조건에서의 펌프 회전 속도. 일반적으로 사이클/초 단위로 측정됩니다.  - `operationTemperatureMax[number]`: 허용되는 작동 주변(공기, 유체) 온도 범위. 일반적으로 켈빈(K) 단위로 측정됩니다.  - `operationTemperatureMin[number]`: 허용되는 작동 주변(공기, 유체) 온도 범위. 일반적으로 켈빈(K) 단위로 측정됩니다.  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `pumpFlowRateMax[number]`: 지정된 저항에 대해 펌핑되는 유체 부피의 허용 범위입니다. 일반적으로 kg/s 단위로 측정됩니다.  - `pumpFlowRateMin[number]`: 지정된 저항에 대해 펌핑되는 유체 부피의 허용 범위입니다. 일반적으로 kg/s 단위로 측정됩니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `type[string]`: 펌프`와 같아야 합니다.  <!-- /30-PropertiesList -->  
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
Pump:    
  description: A pump is a device which imparts mechanical work on fluids or slurries to move them through a channel or pipeline. A typical use of a pump is to circulate chilled water or heating hot water in a building services distribution system.    
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
    connectionSize:    
      description: The connection size of the to and from the pump. Usually measured in millimeters (mm)    
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
    flowResistanceMax:    
      description: 'Allowable range of frictional resistance against which the fluid is being pumped. Usually measured in Pascals (Pa, N/m2)'    
      type: number    
      x-ngsi:    
        type: Property    
    flowResistanceMin:    
      description: 'Allowable range of frictional resistance against which the fluid is being pumped. Usually measured in Pascals (Pa, N/m2)'    
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
    netPositiveSuctionHead:    
      description: 'Minimum liquid pressure at the pump inlet to prevent cavitation. Usually measured in Pascals (Pa, N/m2)'    
      type: number    
      x-ngsi:    
        type: Property    
    nomminalRotationSpeed:    
      description: Pump rotational speed under nominal conditions. Usually measured in cycles/s    
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
    pumpFlowRateMax:    
      description: Allowable range of volume of fluid being pumped against the resistance specified. Usually measured in kg/s    
      type: number    
      x-ngsi:    
        type: Property    
    pumpFlowRateMin:    
      description: Allowable range of volume of fluid being pumped against the resistance specified. Usually measured in kg/s    
      type: number    
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
      description: It must be equal to `Pump`    
      enum:    
        - Pump    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Pump"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Pump/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Pump/schema.json    
  x-model-tags: SAREF Pump    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### 펌프 NGSI-v2 키값 예시  
다음은 키값으로 JSON-LD 형식의 펌프의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Pump:5c6aa613-0829-405e-aeb6-ef000e26fea1",  
    "type": "Pump",  
    "connectionSize": 0.0736674796470771,  
    "flowResistanceMax": 0.5763414622833901,  
    "flowResistanceMin": 0.23194313125611832,  
    "netPositiveSuctionHead": 0.9430406136976697,  
    "nomminalRotationSpeed": 0.49997837892806263,  
    "operationTemperatureMax": 0.016630756942512148,  
    "operationTemperatureMin": 0.7235008225786019,  
    "pumpFlowRateMax": 0.2126600766557486,  
    "pumpFlowRateMin": 0.8849029838139153,  
    "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:13846972-f593-4662-96b5-92cefbbe8219",  
    "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:54ecdd7e-4ab8-4c41-b56b-47bb45c572f8",  
    "isSubSystemOf": [  
        "urn:ngsi-ld:System:092c5cb0-1b8e-4bc9-88ee-ce226a23061f",  
        "urn:ngsi-ld:System:053dc8a9-bbb7-402c-8d99-522b8626091d",  
        "urn:ngsi-ld:System:60e0c6c5-ebd6-4460-aa78-442698c8204c"  
    ],  
    "hasManufacturer": "Pump Company Inc.",  
    "hasModel": "Pump 0.1.2",  
    "dateCreated": "2023-01-26T00:41:42Z",  
    "dateModified": "2023-01-26T10:20:35Z",  
    "source": "Import",  
    "name": "Pump",  
    "alternateName": "Pump type 2",  
    "description": "Pump of limited Pump types",  
    "dataProvider": "IFC file"  
}  
```  
</details>  
#### 펌프 NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 펌프의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Pump:068a2569-0602-4845-8ed3-8ddb200bdcac",  
  "type": "Pump",  
  "connectionSize": {  
    "type": "Measurement",  
    "value": 0.8537944550916271  
  },  
  "flowResistanceMax": {  
    "type": "Measurement",  
    "value": 0.934151218696693  
  },  
  "flowResistanceMin": {  
    "type": "Measurement",  
    "value": 0.5798733223282941  
  },  
  "netPositiveSuctionHead": {  
    "type": "Measurement",  
    "value": 0.9236791362464654  
  },  
  "nomminalRotationSpeed": {  
    "type": "Measurement",  
    "value": 0.9434212309119704  
  },  
  "operationTemperatureMax": {  
    "type": "Measurement",  
    "value": 0.40126909555034673  
  },  
  "operationTemperatureMin": {  
    "type": "Measurement",  
    "value": 0.49855896547412504  
  },  
  "pumpFlowRateMax": {  
    "type": "Measurement",  
    "value": 0.8126244460338075  
  },  
  "pumpFlowRateMin": {  
    "type": "Measurement",  
    "value":  0.4387979987462379  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:BuildingSpace:30823ddd-b24b-4307-917c-72134cf789aa"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:PhysicalObject:f57afcb5-61fd-4e18-b9e0-4c246e0ed2c2"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:93229da7-6aa4-42ad-8d91-7d529267dafd"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:cd14cc46-1a6c-4058-ad6c-07b62d4944c0"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:1dcc7d2b-1886-4006-970f-4c44a5213211"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Pump Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Pump 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T09:00:15.8186104+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T18:30:43.9565309+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Pump"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Pump type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Pump of limited Pump types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### 펌프 NGSI-LD 키 값 예시  
다음은 키 값으로 JSON-LD 형식의 펌프의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Pump:5c6aa613-0829-405e-aeb6-ef000e26fea1",  
  "type": "Pump",  
  "connectionSize": 0.0736674796470771,  
  "flowResistanceMax": 0.5763414622833901,  
  "flowResistanceMin": 0.23194313125611832,  
  "netPositiveSuctionHead": 0.9430406136976697,  
  "nomminalRotationSpeed": 0.49997837892806263,  
  "operationTemperatureMax": 0.016630756942512148,  
  "operationTemperatureMin": 0.7235008225786019,  
  "pumpFlowRateMax": 0.2126600766557486,  
  "pumpFlowRateMin": 0.8849029838139153,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:13846972-f593-4662-96b5-92cefbbe8219",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:54ecdd7e-4ab8-4c41-b56b-47bb45c572f8",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:092c5cb0-1b8e-4bc9-88ee-ce226a23061f",  
    "urn:ngsi-ld:System:053dc8a9-bbb7-402c-8d99-522b8626091d",  
    "urn:ngsi-ld:System:60e0c6c5-ebd6-4460-aa78-442698c8204c"  
  ],  
  "hasManufacturer": "Pump Company Inc.",  
  "hasModel": "Pump 0.1.2",  
  "dateCreated": "2023-01-26T00:41:42Z",  
  "dateModified": "2023-01-26T10:20:35Z",  
  "source": "Import",  
  "name": "Pump",  
  "alternateName": "Pump type 2",  
  "description": "Pump of limited Pump types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### 펌프 NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 펌프의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Pump:7ed480ca-f64d-42fd-9d2e-a792829d1467",  
  "type": "Pump",  
  "connectionSize": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T01:56:40Z",  
    "value": 0.439871049852415  
  },  
  "flowResistanceMax": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-26T10:30:54Z",  
    "value": 0.70272326323097  
  },  
  "flowResistanceMin": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-26T11:23:10Z",  
    "value": 0.748100252355086  
  },  
  "netPositiveSuctionHead": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-25T23:42:12Z",  
    "value": 0.4372375818125598  
  },  
  "nomminalRotationSpeed": {  
    "type": "Property",  
    "unitCode": "cycles/s",  
    "observedAt": "2023-01-25T16:47:26Z",  
    "value": 0.9055473204179818  
  },  
  "operationTemperatureMax": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T23:01:07Z",  
    "value": 0.19255105886794588  
  },  
  "operationTemperatureMin": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T02:59:51Z",  
    "value": 0.014765641352581182  
  },  
  "pumpFlowRateMax": {  
    "type": "Property",  
    "unitCode": "kg/s",  
    "observedAt": "2023-01-26T10:06:49Z",  
    "value": 0.2765428009146871  
  },  
  "pumpFlowRateMin": {  
    "type": "Property",  
    "unitCode": "kg/s",  
    "observedAt": "2023-01-26T00:29:22Z",  
    "value": 0.691611788348768  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:00bec903-1682-4d39-9164-6b6635d717c7"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:cf20b915-721e-4f55-b736-af772bdc68c2"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:08e18090-a9f4-4837-a6aa-3d218b14721c"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:646f75aa-9900-4722-98ce-b3811440d0ce"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:00fb7f96-ff82-4b41-8b6e-1e3d2d8b66c3"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Pump Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Pump 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T13:30:12Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-25T15:53:32Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Pump"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Pump type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Pump of limited Pump types"  
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
