<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entidad: VibrationIsolator    
==========================<!-- /10-Header -->    
<!-- 15-License -->    
[Licencia abierta](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/VibrationIsolator/LICENSE.md)    
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descripción global: **Un aislante de vibraciones es un dispositivo utilizado para minimizar los efectos de la transmisibilidad de las vibraciones en un edificio.**    
versión: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Lista de propiedades    
<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.    
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: El país. Por ejemplo, España  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La localidad en la que se encuentra la dirección postal, y que está en la región  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La región en la que se encuentra la localidad, y que está en el país  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distrito es un tipo de división administrativa que, en algunos países, gestiona el gobierno local      
	- `postOfficeBoxNumber[string]`: El número del apartado de correos para las direcciones de apartados postales. Por ejemplo, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: El código postal. Por ejemplo, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: La dirección  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `description[string]`: Descripción de este artículo  - `hasManufacturer[string]`: Relación que identifica al fabricante de una entidad (por ejemplo, un dispositivo). Se espera que el valor sea una cadena o una cadena con etiqueta de idioma  - `hasModel[string]`: Relación que identifica el modelo de una entidad (por ejemplo, un dispositivo). Se espera que el valor sea una cadena o una cadena con etiqueta de idioma  - `height[number]`: Altura del aislante antivibratorio antes de la aplicación de la carga. Suele medirse en milímetros (mm).  - `id[*]`: Identificador único de la entidad  - `isContainedInBuildingSpace[*]`: Entidad utilizada para definir los espacios físicos del edificio. Un espacio del edificio contiene dispositivos u objetos del edificio. (Espacio del edificio)  - `isContainedInPhysicalObject[*]`: Cualquier Objeto que tiene una región espacial propia.  (Definición extraída de la ontología DUL) (PhysicalObject)  - `isSubSystemOf[array]`: Referencia al sistema o sistemas de los que forma parte este objeto físico.  - `isolatorCompressibility[number]`: La compresibilidad del aislante antivibratorio  - `isolatorStaticDeflection[number]`: Deflexión estática del aislante antivibratorio. Suele medirse en milímetros (mm).  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `name[string]`: El nombre de este artículo  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `supportedWeightMax[number]`: El peso máximo que puede soportar el aislador de vibraciones. Suele medirse en kilogramos (kg) o gramos (g).  - `type[string]`: Debe ser igual a `VibrationIsolator`.  - `vibrationTransmissibility[number]`: El porcentaje de transmisibilidad de las vibraciones  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propiedades requeridas    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Descripción de las propiedades del modelo de datos    
Ordenados alfabéticamente (pulse para más detalles)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
VibrationIsolator:      
  description: A vibration isolator is a device used to minimize the effects of vibration transmissibility in a building.      
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
    height:      
      description: Height of the vibration isolator before tha application of load. Usually measured in millimeters (mm)      
      type: number      
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
    isolatorCompressibility:      
      description: The compressibility of the vibration isolator      
      type: number      
      x-ngsi:      
        type: Property      
    isolatorStaticDeflection:      
      description: Static deflection of the vibration isolator. Usually measured in millimeters (mm)      
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
    supportedWeightMax:      
      description: The maximum weight that can be carried by the vibration isolator. Usually measured in kilograms (kg) or grams (g)      
      type: number      
      x-ngsi:      
        type: Property      
    type:      
      description: It must be equal to `VibrationIsolator`      
      enum:      
        - VibrationIsolator      
      type: string      
      x-ngsi:      
        type: Property      
    vibrationTransmissibility:      
      description: The vibration transmissibility percentage      
      type: number      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:VibrationIsolator"      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/VibrationIsolator/LICENSE.md      
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/VibrationIsolator/schema.json      
  x-model-tags: SAREF VibrationIsolator      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Ejemplo de carga útil    
#### VibrationIsolator NGSI-v2 key-values Ejemplo    
Aquí hay un ejemplo de un VibrationIsolator en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:VibrationIsolator:cd36687d-d862-4b70-b8ed-789a16b2afec",  
  "type": "VibrationIsolator",  
  "height": 0.38014362681889713,  
  "isolatorCompressibility": 0.7634523319144405,  
  "isolatorStaticDeflection": 0.7887792629834026,  
  "supportedWeightMax": 0.32346503665487614,  
  "vibrationTransmissibility": 0.0735805434874115,  
  "hasManufacturer": "VibrationIsolator Company Inc.",  
  "hasModel": "VibrationIsolator 0.1.2",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:e78215e8-4265-4a20-abd0-a19cbe803047",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:30fd3d36-dbea-4994-a312-a061f283886a",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:a9cb3141-21d1-41f9-882d-4e7eb5ca0538",  
    "urn:ngsi-ld:System:d34a3962-d8fc-4d65-a0d8-57d881ec9279",  
    "urn:ngsi-ld:System:c23095d2-a7c8-4920-b237-e7ae47f03451"  
  ],  
  "dateCreated": "2023-01-26T13:07:56Z",  
  "dateModified": "2023-01-26T06:35:21Z",  
  "source": "Import",  
  "name": "VibrationIsolator",  
  "alternateName": "VibrationIsolator type 2",  
  "description": "VibrationIsolator of limited VibrationIsolator types",  
  "dataProvider": "IFC file"  
}  
```  
</details>    
#### VibrationIsolator NGSI-v2 normalizado Ejemplo    
Aquí hay un ejemplo de un VibrationIsolator en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:VibrationIsolator:c808c7ae-06ec-4022-8405-3a2031703303",  
  "type": "VibrationIsolator",  
  "height": {  
    "type": "Number",  
    "value": 0.4519574730782471  
  },  
  "isolatorCompressibility": {  
    "type": "Number",  
    "value": 0.11287489586954691  
  },  
  "isolatorStaticDeflection": {  
    "type": "Number",  
    "value": 0.44640431539803016  
  },  
  "supportedWeightMax": {  
    "type": "Number",  
    "value": 0.9957664703512201  
  },  
  "vibrationTransmissibility": {  
    "type": "Number",  
    "value": 0.045745566367183965  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "VibrationIsolator Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "VibrationIsolator 0.1.2"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:BuildingSpace:35215bc5-6e3e-4794-ab50-6a3a56149e98"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:PhysicalObject:e97a7737-8516-4038-b9c3-a6bc22bc3228"  
  },  
  "isSubSystemOf": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:System:4491af0e-5aaf-494e-a7c2-7d62f7e18db5",  
      "urn:ngsi-ld:System:18b4c438-10ee-4916-9d1d-b6e4dbc3bd7f",  
      "urn:ngsi-ld:System:541cc5f6-fade-4136-a18a-784f97ebe6c4"  
    ]  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T04:34:02.6856577+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T21:20:11.0544578+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "VibrationIsolator"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "VibrationIsolator type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "VibrationIsolator of limited VibrationIsolator types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>    
#### VibrationIsolator NGSI-LD key-values Ejemplo    
Aquí hay un ejemplo de un VibrationIsolator en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:VibrationIsolator:cd36687d-d862-4b70-b8ed-789a16b2afec",  
  "type": "VibrationIsolator",  
  "height": 0.38014362681889713,  
  "isolatorCompressibility": 0.7634523319144405,  
  "isolatorStaticDeflection": 0.7887792629834026,  
  "supportedWeightMax": 0.32346503665487614,  
  "vibrationTransmissibility": 0.0735805434874115,  
  "hasManufacturer": "VibrationIsolator Company Inc.",  
  "hasModel": "VibrationIsolator 0.1.2",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:e78215e8-4265-4a20-abd0-a19cbe803047",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:30fd3d36-dbea-4994-a312-a061f283886a",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:a9cb3141-21d1-41f9-882d-4e7eb5ca0538",  
    "urn:ngsi-ld:System:d34a3962-d8fc-4d65-a0d8-57d881ec9279",  
    "urn:ngsi-ld:System:c23095d2-a7c8-4920-b237-e7ae47f03451"  
  ],  
  "dateCreated": "2023-01-26T13:07:56Z",  
  "dateModified": "2023-01-26T06:35:21Z",  
  "source": "Import",  
  "name": "VibrationIsolator",  
  "alternateName": "VibrationIsolator type 2",  
  "description": "VibrationIsolator of limited VibrationIsolator types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>    
#### VibrationIsolator NGSI-LD normalizado Ejemplo    
He aquí un ejemplo de VibrationIsolator en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:VibrationIsolator:3fef599e-57dd-4ead-b1f1-1be1acec4ed4",  
  "type": "VibrationIsolator",  
  "height": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T00:57:35Z",  
    "value": 0.5291676326164039  
  },  
  "isolatorCompressibility": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T13:38:20Z",  
    "value": 0.0633806140666543  
  },  
  "isolatorStaticDeflection": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T05:45:32Z",  
    "value": 0.7015963366033574  
  },  
  "supportedWeightMax": {  
    "type": "Property",  
    "unitCode": "g",  
    "observedAt": "2023-01-26T11:46:41Z",  
    "value": 0.22821941593534223  
  },  
  "vibrationTransmissibility": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T02:32:45Z",  
    "value": 0.5811208596388945  
  },  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "VibrationIsolator Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "VibrationIsolator 0.1.2"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:fd49449a-d970-42ca-b1fc-76498db2246a"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:928afd04-5e3b-4626-a746-e15f82d1dd27"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:ef621e1c-9c02-4f58-9460-e9792c709c3c"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:d166189e-cc79-40a9-ad8d-9874487d095f"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:5dface3a-d991-4c63-a878-87fc9194c2a8"  
    }  
  ],  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T22:43:59Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T12:00:10Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "VibrationIsolator"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "VibrationIsolator type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "VibrationIsolator of limited VibrationIsolator types"  
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
