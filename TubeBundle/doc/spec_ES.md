<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entidad: TubeBundle    
===================<!-- /10-Header -->    
<!-- 15-License -->    
[Licencia abierta](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/TubeBundle/LICENSE.md)    
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descripción global: **Un haz de tubos es un dispositivo formado por tubos y haces de tubos utilizados para la transferencia de calor y contenidos normalmente dentro de otros dispositivos de conversión de energía, como una enfriadora o un serpentín.**    
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
- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `description[string]`: Descripción de este artículo  - `foulingFactor[number]`: Factor de ensuciamiento de los tubos en el haz tubular. Suele medirse en m2 Kelvin/Watio.  - `hasManufacturer[string]`: Relación que identifica al fabricante de una entidad (por ejemplo, un dispositivo). Se espera que el valor sea una cadena o una cadena con etiqueta de idioma  - `hasModel[string]`: Relación que identifica el modelo de una entidad (por ejemplo, un dispositivo). Se espera que el valor sea una cadena o una cadena con etiqueta de idioma  - `hasTurbulator[boolean]`: TRUE si el tubo tiene turbulador, FALSE si no lo tiene  - `horizontalSpacing[number]`: Separación horizontal entre los tubos del haz tubular. Suele medirse en milímetros (mm).  - `id[*]`: Identificador único de la entidad  - `inLineRowSpacing[number]`: Distancia entre filas de tubos en línea. Suele medirse en milímetros (mm).  - `insideDiameter[number]`: Diámetro interior real del tubo en el haz de tubos. Suele medirse en milímetros (mm).  - `isContainedInBuildingSpace[*]`: Entidad utilizada para definir los espacios físicos del edificio. Un espacio del edificio contiene dispositivos u objetos del edificio. (Espacio del edificio)  - `isContainedInPhysicalObject[*]`: Cualquier Objeto que tiene una región espacial propia.  (Definición extraída de la ontología DUL) (PhysicalObject)  - `isSubSystemOf[array]`: Referencia al sistema o sistemas de los que forma parte este objeto físico.  - `length[number]`: La longitud final del dispositivo. Suele medirse en milímetros (mm).  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `name[string]`: El nombre de este artículo  - `nominalDiameter[number]`: Diámetro nominal o anchura de los tubos del haz tubular. Suele medirse en milímetros (mm).  - `numberOfCircuits[number]`: Número de circuitos paralelos de tubos de fluido  - `numberOfRows[number]`: Número de filas de tubos en el conjunto del haz de tubos  - `outsideDiameter[number]`: Diámetro exterior real del tubo en el haz de tubos. Suele medirse en milímetros (mm).  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `staggeredRowSpacing[number]`: Distancia entre hileras de tubos escalonadas. Suele medirse en milímetros (mm).  - `thermalConductivity[number]`: Factor de ensuciamiento de los tubos en el haz tubular. Suele medirse en m2 Kelvin/Watio.  - `type[string]`: Debe ser igual a `TubeBundle`.  - `verticalSpacing[number]`: Separación vertical entre los tubos del haz de tubos, medida normalmente en milímetros (mm).  - `volumen[number]`: Volumen total de fluido en los tubos y sus cabeceras. Suele medirse en metros cúbicos (m3).  <!-- /30-PropertiesList -->    
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
TubeBundle:      
  description: 'A tube bundle is a device consisting of tubes and bundles of tubes used for heat transfer and contained typically within other energy conversion devices, such as a chiller or coil.'      
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
    foulingFactor:      
      description: Fouling factor of the tubes in the tube bundle. Usually measured in m2 Kelvin/Watt      
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
    hasTurbulator:      
      description: 'TRUE if the tube has a turbulator, FALSE if it does not'      
      type: boolean      
      x-ngsi:      
        type: Property      
    horizontalSpacing:      
      description: Horizontal spacing between tubes in the tube bundle. Usually measured in millimeters (mm)      
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
    inLineRowSpacing:      
      description: In-line tube row spacing. Usually measured in millimeters (mm)      
      type: number      
      x-ngsi:      
        type: Property      
    insideDiameter:      
      description: Actual inner diameter of the tube in the tube bundle. Usually measured in millimeters (mm)      
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
    length:      
      description: The finished length of the device. Usually measured in millimeters (mm)      
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
    nominalDiameter:      
      description: Nominal diameter or width of the tubes in the tube bundle. Usually measured in millimeters (mm)      
      type: number      
      x-ngsi:      
        type: Property      
    numberOfCircuits:      
      description: Number of parallel fluid tube circuits      
      type: number      
      x-ngsi:      
        type: Property      
    numberOfRows:      
      description: Number of tube rows in the tube bundle assembly      
      type: number      
      x-ngsi:      
        type: Property      
    outsideDiameter:      
      description: Actual outside diameter of the tube in the tube bundle. Usually measured in millimeters (mm)      
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
    staggeredRowSpacing:      
      description: Staggered tube row spacing. Usually measured in millimeters (mm)      
      type: number      
      x-ngsi:      
        type: Property      
    thermalConductivity:      
      description: Fouling factor of the tubes in the tube bundle. Usually measured in m2 Kelvin/Watt      
      type: number      
      x-ngsi:      
        type: Property      
    type:      
      description: It must be equal to `TubeBundle`      
      enum:      
        - TubeBundle      
      type: string      
      x-ngsi:      
        type: Property      
    verticalSpacing:      
      description: Vertical spacing between tubes in the tube bundle.Usually measured in millimeters (mm)      
      type: number      
      x-ngsi:      
        type: Property      
    volumen:      
      description: Total volume of fluid in the tubes and their headers. Usually measured in cubic metre (m3)      
      type: number      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:TubeBundle"      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/TubeBundle/LICENSE.md      
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/TubeBundle/schema.json      
  x-model-tags: SAREF TubeBundle      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Ejemplo de carga útil    
#### TubeBundle NGSI-v2 key-values Ejemplo    
He aquí un ejemplo de TubeBundle en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:TubeBundle:ce27cf16-c4dc-4b93-a7e5-021f38a5a0b8",  
  "type": "TubeBundle",  
  "foulingFactor": 0.8435912145074106,  
  "hasTurbulator": true,  
  "horizontalSpacing": 0.45432121749623355,  
  "inLineRowSpacing": 0.9076815444305774,  
  "insideDiameter": 0.9701449888350496,  
  "length": 0.38222174657550045,  
  "nominalDiameter": 0.0408320640034282,  
  "numberOfCircuits": 0.7792295738277125,  
  "numberOfRows": 0.2682132970916634,  
  "outsideDiameter": 0.7194081859650397,  
  "staggeredRowSpacing": 0.31167087959205464,  
  "thermalConductivity": 0.9198905188483331,  
  "verticalSpacing": 0.8194554788890942,  
  "volumen": 0.7779813380010603,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:a13d415e-6116-43c4-a668-24f7dbf86bc1",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:6946c181-2515-406c-82f2-6bad063d7f8b",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:8f497d54-7104-4546-8fa1-51c409c2b446",  
    "urn:ngsi-ld:System:adfb1f0e-a324-45c4-be4c-1127ac06e4ed",  
    "urn:ngsi-ld:System:614b0bb1-d2d9-425f-a7b1-4063e2ba74fa"  
  ],  
  "hasManufacturer": "TubeBundle Company Inc.",  
  "hasModel": "TubeBundle 0.1.2",  
  "dateCreated": "2023-01-26T00:58:36Z",  
  "dateModified": "2023-01-26T10:38:11Z",  
  "source": "Import",  
  "name": "TubeBundle",  
  "alternateName": "TubeBundle type 2",  
  "description": "TubeBundle of limited TubeBundle types",  
  "dataProvider": "IFC file"  
}  
```  
</details>    
#### TubeBundle NGSI-v2 normalizado Ejemplo    
He aquí un ejemplo de TubeBundle en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:TubeBundle:75ab66ce-2623-41a5-884f-ed9b90bde563",  
  "type": "TubeBundle",  
  "foulingFactor": {  
    "type": "Number",  
    "value": 0.10691025901902518  
  },  
  "hasTurbulator": {  
    "type": "Boolean",  
    "value": false  
  },  
  "horizontalSpacing": {  
    "type": "Number",  
    "value": 0.5021481278695225  
  },  
  "inLineRowSpacing": {  
    "type": "Number",  
    "value": 0.7015738944986649  
  },  
  "insideDiameter": {  
    "type": "Number",  
    "value": 0.47609748066140833  
  },  
  "length": {  
    "type": "Number",  
    "value": 0.6920310151935178  
  },  
  "nominalDiameter": {  
    "type": "Number",  
    "value": 0.7019643160884628  
  },  
  "numberOfCircuits": {  
    "type": "Number",  
    "value": 0.2146661280911759  
  },  
  "numberOfRows": {  
    "type": "Number",  
    "value": 0.7182471012018697  
  },  
  "outsideDiameter": {  
    "type": "Number",  
    "value": 0.41939698462727526  
  },  
  "staggeredRowSpacing": {  
    "type": "Number",  
    "value": 0.39127220946141616  
  },  
  "thermalConductivity": {  
    "type": "Number",  
    "value": 0.9507857927588059  
  },  
  "verticalSpacing": {  
    "type": "Number",  
    "value": 0.08491295072422345  
  },  
  "volumen": {  
    "type": "Number",  
    "value": 0.16253433369725145  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:BuildingSpace:e03ce9ef-23a6-4ad9-a533-a960cec73dbe"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:PhysicalObject:1c71e6d7-68ef-4a8d-9fde-985758f88344"  
  },  
  "isSubSystemOf": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:System:c9a9c176-b562-42b7-ad80-cc8db2093faa",  
      "urn:ngsi-ld:System:63e522a0-7de4-4bd9-9f94-094efdf565dc",  
      "urn:ngsi-ld:System:0eebd7dc-010a-4f91-a4d1-da8b2a153b7b"  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "TubeBundle Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "TubeBundle 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T11:52:01.9956382+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T07:18:26.9100211+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "TubeBundle"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "TubeBundle type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "TubeBundle of limited TubeBundle types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>    
#### TubeBundle NGSI-LD key-values Ejemplo    
He aquí un ejemplo de TubeBundle en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:TubeBundle:ce27cf16-c4dc-4b93-a7e5-021f38a5a0b8",  
  "type": "TubeBundle",  
  "foulingFactor": 0.8435912145074106,  
  "hasTurbulator": true,  
  "horizontalSpacing": 0.45432121749623355,  
  "inLineRowSpacing": 0.9076815444305774,  
  "insideDiameter": 0.9701449888350496,  
  "length": 0.38222174657550045,  
  "nominalDiameter": 0.0408320640034282,  
  "numberOfCircuits": 0.7792295738277125,  
  "numberOfRows": 0.2682132970916634,  
  "outsideDiameter": 0.7194081859650397,  
  "staggeredRowSpacing": 0.31167087959205464,  
  "thermalConductivity": 0.9198905188483331,  
  "verticalSpacing": 0.8194554788890942,  
  "volumen": 0.7779813380010603,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:a13d415e-6116-43c4-a668-24f7dbf86bc1",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:6946c181-2515-406c-82f2-6bad063d7f8b",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:8f497d54-7104-4546-8fa1-51c409c2b446",  
    "urn:ngsi-ld:System:adfb1f0e-a324-45c4-be4c-1127ac06e4ed",  
    "urn:ngsi-ld:System:614b0bb1-d2d9-425f-a7b1-4063e2ba74fa"  
  ],  
  "hasManufacturer": "TubeBundle Company Inc.",  
  "hasModel": "TubeBundle 0.1.2",  
  "dateCreated": "2023-01-26T00:58:36Z",  
  "dateModified": "2023-01-26T10:38:11Z",  
  "source": "Import",  
  "name": "TubeBundle",  
  "alternateName": "TubeBundle type 2",  
  "description": "TubeBundle of limited TubeBundle types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>    
#### TubeBundle NGSI-LD normalizado Ejemplo    
He aquí un ejemplo de TubeBundle en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:TubeBundle:e896fec0-f21f-4fa6-a73b-274bb42fb0fe",  
  "type": "TubeBundle",  
  "foulingFactor": {  
    "type": "Property",  
    "unitCode": "Kelvin/Watt",  
    "observedAt": "2023-01-25T15:34:45Z",  
    "value": 0.7896142805113859  
  },  
  "hasTurbulator": {  
    "type": "Property",  
    "value": false  
  },  
  "horizontalSpacing": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-25T18:38:27Z",  
    "value": 0.9299315212283089  
  },  
  "inLineRowSpacing": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T04:15:23Z",  
    "value": 0.12680136540868248  
  },  
  "insideDiameter": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T12:46:46Z",  
    "value": 0.9063711005346757  
  },  
  "length": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-25T15:58:18Z",  
    "value": 0.5121996408910179  
  },  
  "nominalDiameter": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T05:13:10Z",  
    "value": 0.8209837702761213  
  },  
  "numberOfCircuits": {  
    "type": "Property",  
    "value": 0.253153343197542  
  },  
  "numberOfRows": {  
    "type": "Property",  
    "value": 0.69547957104902  
  },  
  "outsideDiameter": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T07:32:26Z",  
    "value": 0.7479684351740756  
  },  
  "staggeredRowSpacing": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T08:06:42Z",  
    "value": 0.2757631103143954  
  },  
  "thermalConductivity": {  
    "type": "Property",  
    "unitCode": "Kelvin/Watt",  
    "observedAt": "2023-01-25T15:39:27Z",  
    "value": 0.28193770602031487  
  },  
  "verticalSpacing": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T06:27:04Z",  
    "value": 0.7886025280565963  
  },  
  "volumen": {  
    "type": "Property",  
    "unitCode": "m3",  
    "observedAt": "2023-01-26T05:29:35Z",  
    "value": 0.6238667384353597  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:4943f440-65d7-4fe4-834f-140d786124af"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:6b66c26d-c9a9-4e59-ba5f-5a17174fa9da"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:721e7dae-913a-4e6e-989b-30d545a7ec3d"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:c6a87a94-a7c7-4c31-9b33-6f3ad7861cd0"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:205f1bbb-6bff-422a-9121-4c30a002dfe3"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "TubeBundle Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "TubeBundle 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T21:28:33Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T00:41:51Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "TubeBundle"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "TubeBundle type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "TubeBundle of limited TubeBundle types"  
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
