<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: 코일  
=======<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Coil/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **코일은 혼합되지 않는 매체 간에 열 전달을 제공하는 데 사용되는 장치입니다. 일반적인 예로는 냉각 코일이 있으며, 냉각수, 부동액 또는 냉매를 순환시키는 핀 코일을 사용하여 코일 표면을 가로질러 이동하는 공기의 열을 제거하는 데 사용됩니다. 코일은 가열 또는 냉각 유체를 운반하는 일련의 튜브(코일)를 기류에 배치하여 가열 또는 냉각 용도로 사용할 수 있습니다. 코일은 뱀 모양으로 묶인 튜브 또는 열 전달 표면이 확장된 핀형 튜브로 구성될 수 있습니다.  코일은 바닥 슬래브에 매립하는 등 기류가 흐르지 않는 경우에도 사용할 수 있습니다.**  
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
- `airFlowRateMax[number]`: 최대 허용 공기 유량. 보통 m3/s 단위로 측정됩니다.  - `airFlowRateMin[number]`: 최소 허용 공기 유량. 보통 m3/s 단위로 측정됩니다.  - `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `hasManufacturer[string]`: 엔티티의 제조업체를 식별하는 관계(예: 장치)입니다. 값은 문자열 또는 언어 태그가 포함된 문자열로 예상됩니다.  - `hasModel[string]`: 엔티티의 모델(예: 장치)을 식별하는 관계입니다. 값은 문자열 또는 언어 태그가 포함된 문자열로 예상됩니다.  - `id[*]`: 엔티티의 고유 식별자  - `isContainedInBuildingSpace[*]`: 건물의 물리적 공간을 정의하는 데 사용되는 엔티티입니다. 건물 공간에는 장치 또는 건물 개체가 포함됩니다. (빌딩 공간)  - `isContainedInPhysicalObject[*]`: 적절한 공간 영역을 가진 모든 객체.  (DUL 온톨로지에서 추출한 정의) (PhysicalObject)  - `isSubSystemOf[array]`: 이 피지컬 오브젝트가 속한 시스템에 대한 레퍼런스입니다.  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `nominalLatentCapacity[number]`: 공칭 잠복 용량. 일반적으로 와트(W, J/s) 단위로 측정됩니다.  - `nominalSensibleCapacity[number]`: 공칭 적정 용량. 일반적으로 와트(W, J/s) 단위로 측정됩니다.  - `nominalUa[number]`: 공칭 UA 값  - `operationMode[string]`: 이 코일의 작동 모드  - `operationTemperatureMax[number]`: 허용되는 작동 주변(공기, 유체) 온도 범위. 일반적으로 켈빈(K) 단위로 측정됩니다.  - `operationTemperatureMin[number]`: 허용되는 작동 주변(공기, 유체) 온도 범위. 일반적으로 켈빈(K) 단위로 측정됩니다.  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `placementType[string]`: 장치를 배치하는 방법을 나타냅니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `type[string]`: 코일`과 같아야 합니다.  <!-- /30-PropertiesList -->  
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
Coil:    
  description: 'A coil is a device used to provide heat transfer between non-mixing media. A common example is a cooling coil, which utilizes a finned coil in which circulates chilled water, antifreeze, or refrigerant that is used to remove heat from air moving across the surface of the coil. A coil may be used either for heating or cooling purposes by placing a series of tubes (the coil) carrying a heating or cooling fluid into an airstream. The coil may be constructed from tubes bundled in a serpentine form or from finned tubes that give a extended heat transfer surface.  Coils may also be used for non-airflow cases such as embedded in a floor slab.'    
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
    airFlowRateMin:    
      description: Minimum allowable air flow rate. Usually measured in m3/s    
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
    nominalLatentCapacity:    
      description: 'Nominal latent capacity. Usually measured in Watts (W, J/s)'    
      type: number    
      x-ngsi:    
        type: Property    
    nominalSensibleCapacity:    
      description: 'Nominal sensible capacity. Usually measured in Watts (W, J/s)'    
      type: number    
      x-ngsi:    
        type: Property    
    nominalUa:    
      description: Nominal UA value    
      type: number    
      x-ngsi:    
        type: Property    
    operationMode:    
      description: Operation mode of this coil    
      enum:    
        - cooling    
        - heating    
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
    placementType:    
      description: Indicates how the device is designed to be placed    
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
      description: It must be equal to `Coil`    
      enum:    
        - Coil    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Coil"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Coil/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Coil/schema.json    
  x-model-tags: SAREF Coil    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### 코일 NGSI-v2 키값 예시  
다음은 키-값으로 JSON-LD 형식의 코일의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Coil:180d0665-9242-42c6-b336-d7edcf8fc3b5",  
  "type": "Coil",  
  "airFlowRateMax": 0.22332143818011307,  
  "airFlowRateMin": 0.6369516028350278,  
  "nominalLatentCapacity": 0.9394595315602638,  
  "nominalSensibleCapacity": {  
    "type": 0.8014808985276609,  
    "nominalUa": 0.3738979404823001,  
    "operationMode": "cooling",  
    "operationTemperatureMax": 0.7510713399220631,  
    "operationTemperatureMin": 0.8674252304724047,  
    "placementType": "Money Market Account",  
    "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:c562a0a7-6355-46a0-a528-ebeea1b5af39",  
    "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:7d4df444-5662-45c4-81e8-28dd9e2ab52e",  
    "isSubSystemOf": [  
      "urn:ngsi-ld:System:98486c90-52da-48cf-af50-69449370e3b9",  
      "urn:ngsi-ld:System:afe412c8-8366-4eb1-b834-dc68c1e3d828",  
      "urn:ngsi-ld:System:b851de9e-48bd-4363-9d01-b17ab9469aea"  
    ],  
    "hasManufacturer": "Coil Company Inc.",  
    "hasModel": "Coil 0.1.2",  
    "dateCreated": "2023-01-25T23:02:47Z",  
    "dateModified": "2023-01-26T14:02:17Z",  
    "source": "Import",  
    "name": "Coil",  
    "alternateName": "Coil type 2",  
    "description": "Coil of limited Coil types",  
    "dataProvider": "IFC file"  
  }  
```  
</details>  
#### 코일 NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 코일의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Coil:13d40aef-8b95-4cb2-af1e-483e4c874941",  
  "type": "Coil",  
  "airFlowRateMax": {  
    "type": "Measurement",  
    "value": 0.6477373611080879  
  },  
  "airFlowRateMin": {  
    "type": "Measurement",  
    "value": 0.1367768463223733  
  },  
  "nominalLatentCapacity": {  
    "type": "Measurement",  
    "value": 0.6823953079495582  
  },  
  "nominalSensibleCapacity": {  
    "type": "Measurement",  
    "value": 0.9661532549311025  
  },  
  "nominalUa": {  
    "type": "Measurement",  
    "value": 0.5711236580496344  
  },  
  "operationMode": {  
    "type": "CoilOperationMode",  
    "value": "cooling"  
  },  
  "operationTemperatureMax": {  
    "type": "Measurement",  
    "value": 0.5575891151602635  
  },  
  "operationTemperatureMin": {  
    "type": "Measurement",  
    "value": 0.8396275897283132  
  },  
  "placementType": {  
    "type": "Text",  
    "value": "Buckinghamshire"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:BuildingSpace:1070b255-7508-4019-ba0a-1ce8a03cf3b1"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:PhysicalObject:cef12274-adeb-41a5-aec1-8e254593bb26"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:65b917e6-ec39-4e2e-bce1-a52a52c176bc"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:61834f7f-655f-47f1-828c-755a25e7b026"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:ab77fbe9-a323-477c-81bf-a9923abdf8ea"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Coil Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Coil 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T04:03:32.1629228+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T16:59:28.4436033+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Coil"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Coil type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Coil of limited Coil types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### 코일 NGSI-LD 키값 예시  
다음은 키-값으로 JSON-LD 형식의 코일의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Coil:180d0665-9242-42c6-b336-d7edcf8fc3b5",  
  "type": "Coil",  
  "airFlowRateMax": 0.22332143818011307,  
  "airFlowRateMin": 0.6369516028350278,  
  "nominalLatentCapacity": 0.9394595315602638,  
  "nominalSensibleCapacity": {  
    "type": 0.8014808985276609,  
    "nominalUa": 0.3738979404823001,  
    "operationMode": "cooling",  
    "operationTemperatureMax": 0.7510713399220631,  
    "operationTemperatureMin": 0.8674252304724047,  
    "placementType": "Money Market Account",  
    "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:c562a0a7-6355-46a0-a528-ebeea1b5af39",  
    "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:7d4df444-5662-45c4-81e8-28dd9e2ab52e",  
    "isSubSystemOf": [  
      "urn:ngsi-ld:System:98486c90-52da-48cf-af50-69449370e3b9",  
      "urn:ngsi-ld:System:afe412c8-8366-4eb1-b834-dc68c1e3d828",  
      "urn:ngsi-ld:System:b851de9e-48bd-4363-9d01-b17ab9469aea"  
    ],  
    "hasManufacturer": "Coil Company Inc.",  
    "hasModel": "Coil 0.1.2",  
    "dateCreated": "2023-01-25T23:02:47Z",  
    "dateModified": "2023-01-26T14:02:17Z",  
    "source": "Import",  
    "name": "Coil",  
    "alternateName": "Coil type 2",  
    "description": "Coil of limited Coil types",  
    "dataProvider": "IFC file",  
    "@context": [  
      "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
      "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
  }  
```  
</details>  
#### 코일 NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 코일의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Coil:fcc6fa4b-fa43-42de-af7d-c8be6efda789",  
  "type": "Coil",  
  "airFlowRateMax": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-25T22:00:31Z",  
    "value": 0.461404719601072  
  },  
  "airFlowRateMin": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-26T12:18:55Z",  
    "value": 0.3100905584892091  
  },  
  "nominalLatentCapacity": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-25T15:57:00Z",  
    "value": 0.0859276056343462  
  },  
  "nominalSensibleCapacity": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-25T15:07:49Z",  
    "value": 0.9959034840230547  
  },  
  "nominalUa": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-25T16:07:27Z",  
    "value": 0.03766746157415857  
  },  
  "operationMode": {  
    "type": "Property",  
    "value": "cooling"  
  },  
  "operationTemperatureMax": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T15:22:24Z",  
    "value": 0.18992025947801072  
  },  
  "operationTemperatureMin": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T07:51:42Z",  
    "value": 0.6342100760763256  
  },  
  "placementType": {  
    "type": "Property",  
    "value": "SQL"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:61d397a1-954d-40ec-a4cc-cba2c10a07ca"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:ee042545-32fa-4adb-97e1-5007ccabcd63"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:cab59172-6cb8-443e-94b8-b6270aaa5e60"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:73b9f71e-63bb-49bf-96ef-f6f4922f4245"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:7607ea00-30f7-4271-a0f3-c0b1755be875"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Coil Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Coil 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T04:20:07Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-25T16:46:30Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Coil"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Coil type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Coil of limited Coil types"  
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
