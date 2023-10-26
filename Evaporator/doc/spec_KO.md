<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: 증발기  
========<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Evaporator/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **증발기는 액체 냉매를 기화시켜 주변 유체로부터 열을 흡수하는 장치입니다**.  
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
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `evaporationCoolant[string]`: 증발기의 냉각수에 사용되는 유체  - `evaporationMediumType[string]`: ColdLiquid: 증발기는 냉매와 열을 교환하기 위해 액체 형태의 유체를 사용합니다. ColdAir: 증발기는 공기를 사용하여 냉매와 열을 교환합니다.  - `externalSurfaceArea[number]`: 외부 표면적(기본 및 보조 면적 모두). 일반적으로 평방미터(m2) 단위로 측정됩니다.  - `hasManufacturer[string]`: 엔티티의 제조업체를 식별하는 관계(예: 장치)입니다. 값은 문자열 또는 언어 태그가 포함된 문자열로 예상됩니다.  - `hasModel[string]`: 엔티티의 모델(예: 장치)을 식별하는 관계입니다. 값은 문자열 또는 언어 태그가 포함된 문자열로 예상됩니다.  - `id[*]`: 엔티티의 고유 식별자  - `internalRefrigerantVolume[number]`: 증발기의 내부 부피(냉매 측). 일반적으로 입방미터(m3) 단위로 측정됩니다.  - `internalSurfaceArea[number]`: 내부 표면적. 보통 평방미터(m2) 단위로 측정됩니다.  - `internalWaterVolume[number]`: 증발기 내부 부피(물 쪽). 일반적으로 입방미터(m3) 단위로 측정됩니다.  - `isContainedInBuildingSpace[*]`: 건물의 물리적 공간을 정의하는 데 사용되는 엔티티입니다. 건물 공간에는 장치 또는 건물 개체가 포함됩니다. (빌딩 공간)  - `isContainedInPhysicalObject[*]`: 적절한 공간 영역을 가진 모든 객체.  (DUL 온톨로지에서 추출한 정의) (PhysicalObject)  - `isSubSystemOf[array]`: 이 피지컬 오브젝트가 속한 시스템에 대한 레퍼런스입니다.  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `nominalHeatTransferArea[number]`: 공칭 전체 열전달 계수와 관련된 공칭 열전달 표면적. 일반적으로 평방미터(m2) 단위로 측정됩니다.  - `nominalHeatTransferCoefficient[number]`: 공칭 열전달 면적과 관련된 공칭 전체 열전달 계수입니다. 일반적으로 와트/m2 켈빈 단위로 측정됩니다.  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `refrigerantClass[string]`: 컴프레서에 사용되는 냉매 등급입니다. CFC: 염화불화탄소. HCFC: 수소염화불화탄소. HFC: 수소불화탄소  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `type[string]`: 증발기`와 같아야 합니다.  <!-- /30-PropertiesList -->  
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
Evaporator:    
  description: An evaporator is a device in which a liquid refrigerent is vaporized and absorbs heat from the surrounding fluid.    
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
    evaporationCoolant:    
      description: The fluid used for the coolant in the evaporator    
      type: string    
      x-ngsi:    
        type: Property    
    evaporationMediumType:    
      description: 'ColdLiquid: Evaporator is using liquid type of fluid to exchange heat with refrigerant. ColdAir: Evaporator is using air to exchange heat with refrigerant'    
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
      description: It must be equal to `Evaporator`    
      enum:    
        - Evaporator    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Evaporator"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Evaporator/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Evaporator/schema.json    
  x-model-tags: SAREF Evaporator    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### 증발기 NGSI-v2 키값 예시  
다음은 키-값으로 JSON-LD 형식의 증발기 예제입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Evaporator:052fc49c-111f-420b-a8e2-51fe3338d2b1",  
  "type": "Evaporator",  
  "evaporationCoolant": "Martinique",  
  "evaporationMediumType": "e-markets",  
  "externalSurfaceArea": 0.5908980288694448,  
  "internalRefrigerantVolume": 0.6284120974003947,  
  "internalSurfaceArea": 0.9343787028327242,  
  "internalWaterVolume": 0.6490547902275666,  
  "nominalHeatTransferArea": 0.4294965931834158,  
  "nominalHeatTransferCoefficient": 0.8081650097718576,  
  "refrigerantClass": "Jewelery, Music & Games",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:51c0dbf1-adcc-4d2c-b3ea-90aa62cb494f",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:c5bac51f-5e2b-4152-9eb1-96959129eb27",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:67f3cbde-6a56-4f0b-9085-ddcee5f7e9fa",  
    "urn:ngsi-ld:System:3e056ae8-5498-4141-9bca-6f9b2eb03b67",  
    "urn:ngsi-ld:System:6692437c-d2c6-4ba0-9386-3a7e0f49d10d"  
  ],  
  "hasManufacturer": "Evaporator Company Inc.",  
  "hasModel": "Evaporator 0.1.2",  
  "dateCreated": "2023-01-26T00:54:03Z",  
  "dateModified": "2023-01-25T16:56:18Z",  
  "source": "Import",  
  "name": "Evaporator",  
  "alternateName": "Evaporator type 2",  
  "description": "Evaporator of limited Evaporator types",  
  "dataProvider": "IFC file"  
}  
```  
</details>  
#### 증발기 NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 증발기 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Evaporator:c9337df1-e99a-43a3-9f15-425e35abf54a",  
  "type": "Evaporator",  
  "evaporationCoolant": {  
    "type": "Text",  
    "value": "seamless"  
  },  
  "evaporationMediumType": {  
    "type": "Text",  
    "value": "Pike"  
  },  
  "externalSurfaceArea": {  
    "type": "Measurement",  
    "value": 0.07191726989654268  
  },  
  "internalRefrigerantVolume": {  
    "type": "Measurement",  
    "value":  0.20250063780044392  
  },  
  "internalSurfaceArea": {  
    "type": "Measurement",  
    "value":  0.33350088977343506  
  },  
  "internalWaterVolume": {  
    "type": "Measurement",  
    "value":  0.8525147046941662  
  },  
  "nominalHeatTransferArea": {  
    "type": "Measurement",  
    "value":  0.7335123054536791  
  },  
  "nominalHeatTransferCoefficient": {  
    "type": "Measurement",  
    "value":  0.23696481410868975  
  },  
  "refrigerantClass": {  
    "type": "Text",  
    "value": "Incredible"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:BuildingSpace:1d3c18d5-3c73-4b33-ac02-be885911a9c2"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:PhysicalObject:c2a99f87-20d2-4a3e-8869-9ccb703023f7"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:9905fd33-a0dd-465c-821e-7179621c4cd2"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:912b3134-8a54-4576-9e70-68f7d814a681"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:46197de5-7d87-4a26-9d32-4e62dd387c93"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Evaporator Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Evaporator 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T19:39:32.5598858+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T02:08:29.4163966+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Evaporator"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Evaporator type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Evaporator of limited Evaporator types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### 증발기 NGSI-LD 키값 예시  
다음은 키-값으로 JSON-LD 형식의 증발기 예제입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Evaporator:052fc49c-111f-420b-a8e2-51fe3338d2b1",  
  "type": "Evaporator",  
  "evaporationCoolant": "Martinique",  
  "evaporationMediumType": "e-markets",  
  "externalSurfaceArea": 0.5908980288694448,  
  "internalRefrigerantVolume": 0.6284120974003947,  
  "internalSurfaceArea": 0.9343787028327242,  
  "internalWaterVolume": 0.6490547902275666,  
  "nominalHeatTransferArea": 0.4294965931834158,  
  "nominalHeatTransferCoefficient": 0.8081650097718576,  
  "refrigerantClass": "Jewelery, Music & Games",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:51c0dbf1-adcc-4d2c-b3ea-90aa62cb494f",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:c5bac51f-5e2b-4152-9eb1-96959129eb27",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:67f3cbde-6a56-4f0b-9085-ddcee5f7e9fa",  
    "urn:ngsi-ld:System:3e056ae8-5498-4141-9bca-6f9b2eb03b67",  
    "urn:ngsi-ld:System:6692437c-d2c6-4ba0-9386-3a7e0f49d10d"  
  ],  
  "hasManufacturer": "Evaporator Company Inc.",  
  "hasModel": "Evaporator 0.1.2",  
  "dateCreated": "2023-01-26T00:54:03Z",  
  "dateModified": "2023-01-25T16:56:18Z",  
  "source": "Import",  
  "name": "Evaporator",  
  "alternateName": "Evaporator type 2",  
  "description": "Evaporator of limited Evaporator types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### 증발기 NGSI-LD 정규화 예시  
다음은 정규화된 JSON-LD 형식의 증발기 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Evaporator:012ce978-0915-4322-82cf-64be00f886e6",  
  "type": "Evaporator",  
  "evaporationCoolant": {  
    "type": "Property",  
    "value": "Generic"  
  },  
  "evaporationMediumType": {  
    "type": "Property",  
    "value": "ROI"  
  },  
  "externalSurfaceArea": {  
    "type": "Property",  
    "unitCode": "m2",  
    "observedAt": "2023-01-26T01:26:06Z",  
    "value": 0.40305559655625467  
  },  
  "internalRefrigerantVolume": {  
    "type": "Property",  
    "unitCode": "m3",  
    "observedAt": "2023-01-26T04:37:57Z",  
    "value": 0.9165377999786634  
  },  
  "internalSurfaceArea": {  
    "type": "Property",  
    "unitCode": "m2",  
    "observedAt": "2023-01-26T07:59:30Z",  
    "value": 0.11705017875360657  
  },  
  "internalWaterVolume": {  
    "type": "Property",  
    "unitCode": "m3",  
    "observedAt": "2023-01-26T13:18:36Z",  
    "value": 0.6445386560470906  
  },  
  "nominalHeatTransferArea": {  
    "type": "Property",  
    "unitCode": "m2",  
    "observedAt": "2023-01-25T18:46:49Z",  
    "value": 0.20771410507872068  
  },  
  "nominalHeatTransferCoefficient": {  
    "type": "Property",  
    "unitCode": "Kelvin",  
    "observedAt": "2023-01-26T11:33:53Z",  
    "value": 0.029467682176717913  
  },  
  "refrigerantClass": {  
    "type": "Property",  
    "value": "Directives"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:09942ed6-b0b8-4968-a57d-e48b8fd062f9"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:9f7d6071-a0a0-4b9d-9707-b59804cef5a8"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:cb2ff8f9-5b3a-48f2-a576-c7a632297517"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:c9865d23-d9da-47f2-875a-1f0beb5bbf09"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:18016c6a-4548-4adc-a84c-c62c94e34393"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Evaporator Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Evaporator 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T06:49:33Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T02:39:15Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Evaporator"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Evaporator type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Evaporator of limited Evaporator types"  
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
