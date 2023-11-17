<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entidad: Tanque    
===============<!-- /10-Header -->    
<!-- 15-License -->    
[Licencia abierta](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Tank/LICENSE.md)    
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descripción global: **Un depósito es un recipiente o contenedor en el que se almacena un fluido o gas para su uso posterior.**    
versión: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Lista de propiedades    
<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.    
- `accessType[string]`: Define los tipos de acceso (o cubierta) a un depósito que pueden especificarse. Tenga en cuenta que las cubiertas suelen especificarse para los tanques rectangulares. En el caso de los depósitos cilíndricos, el acceso se realiza normalmente a través de una boca de inspección.  - `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: El país. Por ejemplo, España  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La localidad en la que se encuentra la dirección postal, y que está en la región  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La región en la que se encuentra la localidad, y que está en el país  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distrito es un tipo de división administrativa que, en algunos países, gestiona el gobierno local      
	- `postOfficeBoxNumber[string]`: El número del apartado de correos para las direcciones de apartados postales. Por ejemplo, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: El código postal. Por ejemplo, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: La dirección  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `description[string]`: Descripción de este artículo  - `effectiveCapacity[number]`: Capacidad volumétrica total efectiva o real del depósito. Suele medirse en metros cúbicos (m3).B3  - `endShapeType[string]`: Define los tipos de formas finales que pueden utilizarse para los depósitos preformados. La convención para leer estos valores enumerados es que para un cilindro vertical, el primer valor es la base y el segundo es la parte superior para un cilindro horizontal, el orden de lectura debe ser de izquierda a derecha. Para un tanque esférico, debe utilizarse el valor UNSET.B5  - `firstCurvatureRadius[number]`: FirstCurvatureRadius debe definirse como el valor del radio de curvatura de la base o del lado izquierdo. Normalmente se mide en milímetros (mm)  - `hasManufacturer[string]`: Relación que identifica al fabricante de una entidad (por ejemplo, un dispositivo). Se espera que el valor sea una cadena o una cadena con etiqueta de idioma  - `hasModel[string]`: Relación que identifica el modelo de una entidad (por ejemplo, un dispositivo). Se espera que el valor sea una cadena o una cadena con etiqueta de idioma  - `id[*]`: Identificador único de la entidad  - `isContainedInBuildingSpace[*]`: Entidad utilizada para definir los espacios físicos del edificio. Un espacio del edificio contiene dispositivos u objetos del edificio. (Espacio del edificio)  - `isContainedInPhysicalObject[*]`: Cualquier Objeto que tiene una región espacial propia.  (Definición extraída de la ontología DUL) (PhysicalObject)  - `isSubSystemOf[array]`: Referencia al sistema o sistemas de los que forma parte este objeto físico.  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `name[string]`: El nombre de este artículo  - `nominalDepth[number]`: La profundidad nominal del depósito. Nota: No se requiere para un depósito cilíndrico horizontal. Suele medirse en milímetros (mm).  - `nominalLengthOrDiameter[number]`: La longitud nominal o, en el caso de un depósito cilíndrico vertical, el diámetro nominal del depósito. Suele medirse en milímetros (mm).  - `nominalVolumetricCapacity[number]`: Capacidad volumétrica total nominal o de diseño del depósito. Suele medirse en metros cúbicos (m3).  - `nominalWidthOrDiameter[number]`: La anchura nominal o, en el caso de un depósito cilíndrico horizontal, el diámetro nominal del depósito. Nota: No es necesario para un depósito cilíndrico vertical. Suele medirse en milímetros (mm).  - `numberOfSections[number]`: Número de secciones utilizadas  - `operatingWeight[number]`: Peso operativo del depósito, incluido todo su contenido. Suele medirse en kilogramos (kg) o gramos (g).  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `patternType[string]`: Define los tipos de patrón (o forma de un depósito que se pueden especificar  - `secondCurvatureRadius[number]`: SecondCurvatureRadius debe definirse como el valor del radio de curvatura superior o del lado derecho. Normalmente se mide en milímetros (mm)  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `storageType[string]`: Define la categoría general de material que se pretende almacenar  - `type[string]`: Debe ser igual a `Tank`  <!-- /30-PropertiesList -->    
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
Tank:      
  description: A tank is a vessel or container in which a fluid or gas is stored for later use.      
  properties:      
    accessType:      
      description: 'Defines the types of access (or cover) to a tank that may be specified. Note that covers are generally specified for rectangular tanks. For cylindrical tanks, access will normally be via a manhole'      
      type: string      
      x-ngsi:      
        type: Property      
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
    effectiveCapacity:      
      description: The total effective or actual volumetric capacity of the tank. Usually measured in cubic metre (m3).B3      
      type: number      
      x-ngsi:      
        type: Property      
    endShapeType:      
      description: 'Defines the types of end shapes that can be used for preformed tanks. The convention for reading these enumerated values is that for a vertical cylinder, the first value is the base and the second is the top for a horizontal cylinder, the order of reading should be left to right. For a speherical tank, the value UNSET should be used.B5'      
      type: string      
      x-ngsi:      
        type: Property      
    firstCurvatureRadius:      
      description: FirstCurvatureRadius should be defined as the base or left side radius of curvature value. Usually measured in millimeters (mm)      
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
    nominalDepth:      
      description: 'The nominal depth of the tank. Note: Not required for a horizontal cylindrical tank. Usually measured in millimeters (mm)'      
      type: number      
      x-ngsi:      
        type: Property      
    nominalLengthOrDiameter:      
      description: 'The nominal length or, in the case of a vertical cylindrical tank, the nominal diameter of the tank. Usually measured in millimeters (mm)'      
      type: number      
      x-ngsi:      
        type: Property      
    nominalVolumetricCapacity:      
      description: The total nominal or design volumetric capacity of the tank. Usually measured in cubic metre (m3)      
      type: number      
      x-ngsi:      
        type: Property      
    nominalWidthOrDiameter:      
      description: 'The nominal width or, in the case of a horizontal cylindrical tank, the nominal diameter of the tank. Note: Not required for a vertical cylindrical tank. Usually measured in millimeters (mm)'      
      type: number      
      x-ngsi:      
        type: Property      
    numberOfSections:      
      description: Number of sections used      
      type: number      
      x-ngsi:      
        type: Property      
    operatingWeight:      
      description: Operating weight of the tank including all of its contents. Usually measured in kilograms (kg) or grams (g)      
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
    patternType:      
      description: Defines the types of pattern (or shape of a tank that may be specified      
      type: string      
      x-ngsi:      
        type: Property      
    secondCurvatureRadius:      
      description: SecondCurvatureRadius should be defined as the top or right side radius of curvature value. Usually measured in millimeters (mm)      
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
    storageType:      
      description: Defines the general material category intended to be stored      
      type: string      
      x-ngsi:      
        type: Property      
    type:      
      description: It must be equal to `Tank`      
      enum:      
        - Tank      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Tank"      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Tank/LICENSE.md      
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Tank/schema.json      
  x-model-tags: SAREF Tank      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Ejemplo de carga útil    
#### Tanque NGSI-v2 key-values Ejemplo    
He aquí un ejemplo de un Tanque en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Tank:7a5293bf-87b8-4768-8c25-56bcbfa91649",  
  "type": "Tank",  
  "accessType": "Auto Loan Account",  
  "effectiveCapacity": 0.6627329008534851,  
  "endShapeType": "Union",  
  "firstCurvatureRadius": 0.6799132713266423,  
  "nominalDepth": 0.07530609187652448,  
  "nominalLengthOrDiameter": 0.1950493997985394,  
  "nominalVolumetricCapacity": 0.6494794060427406,  
  "nominalWidthOrDiameter": 0.2734692629974923,  
  "numberOfSections": 0.3094855572354859,  
  "operatingWeight": 0.3055837938759739,  
  "patternType": "Investment Account",  
  "secondCurvatureRadius": 0.0019846058153857316,  
  "storageType": "Investor",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:ffcd7e11-7c74-45f3-8f5a-3310ababddc8",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:c2540316-a0c2-4363-93b7-e49ab5ed3b2f",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:aae7e0b6-0256-4c58-a3ee-4989bdc205da",  
    "urn:ngsi-ld:System:857551fc-8a05-4052-9269-8193f148ff2c",  
    "urn:ngsi-ld:System:e4e88c0a-d78a-4bfd-a76b-af72e518a66e"  
  ],  
  "hasManufacturer": "Tank Company Inc.",  
  "hasModel": "Tank 0.1.2",  
  "dateCreated": "2023-01-26T12:03:34Z",  
  "dateModified": "2023-01-25T16:27:50Z",  
  "source": "Import",  
  "name": "Tank",  
  "alternateName": "Tank type 2",  
  "description": "Tank of limited Tank types",  
  "dataProvider": "IFC file"  
}  
```  
</details>    
#### Tanque NGSI-v2 normalizado Ejemplo    
He aquí un ejemplo de un Tanque en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Tank:dc341150-16f1-4fa1-a674-36714ed2565c",  
  "type": "Tank",  
  "accessType": {  
    "type": "Text",  
    "value": "Benin"  
  },  
  "effectiveCapacity": {  
    "type": "Number",  
    "value": 0.34988329549654584  
  },  
  "endShapeType": {  
    "type": "Text",  
    "value": "Lari"  
  },  
  "firstCurvatureRadius": {  
    "type": "Number",  
    "value": 0.9159778495815387  
  },  
  "nominalDepth": {  
    "type": "Number",  
    "value": 0.8630341610754986  
  },  
  "nominalLengthOrDiameter": {  
    "type": "Number",  
    "value": 0.8867523503955448  
  },  
  "nominalVolumetricCapacity": {  
    "type": "Number",  
    "value": 0.27704062609207425  
  },  
  "nominalWidthOrDiameter": {  
    "type": "Number",  
    "value": 0.6770082270929979  
  },  
  "numberOfSections": {  
    "type": "Number",  
    "value": 0.7169194499582789  
  },  
  "operatingWeight": {  
    "type": "Number",  
    "value": 0.23947734710245394  
  },  
  "patternType": {  
    "type": "Text",  
    "value": "Ergonomic Cotton Ball"  
  },  
  "secondCurvatureRadius": {  
    "type": "Number",  
    "value": 0.11478790270153483  
  },  
  "storageType": {  
    "type": "Text",  
    "value": "gold"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:BuildingSpace:431e892c-1029-409d-b7b8-b9cad9a0a9e5"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:PhysicalObject:fd304ea2-572f-4b66-b8ad-d9d84c870fa1"  
  },  
  "isSubSystemOf": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:System:b3336716-b468-40f1-be04-9f7ffedcc418",  
      "urn:ngsi-ld:System:05bac9cd-2c56-4046-a70a-b2415e810f43",  
      "urn:ngsi-ld:System:2344579c-27b3-4c5d-9db3-0fd9b46fb7e7"  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Tank Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Tank 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T00:00:57.3062284+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T06:50:59.7051893+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Tank"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Tank type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Tank of limited Tank types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>    
#### Tanque NGSI-LD key-values Ejemplo    
He aquí un ejemplo de un Tanque en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Tank:7a5293bf-87b8-4768-8c25-56bcbfa91649",  
  "type": "Tank",  
  "accessType": "Auto Loan Account",  
  "effectiveCapacity": 0.6627329008534851,  
  "endShapeType": "Union",  
  "firstCurvatureRadius": 0.6799132713266423,  
  "nominalDepth": 0.07530609187652448,  
  "nominalLengthOrDiameter": 0.1950493997985394,  
  "nominalVolumetricCapacity": 0.6494794060427406,  
  "nominalWidthOrDiameter": 0.2734692629974923,  
  "numberOfSections": 0.3094855572354859,  
  "operatingWeight": 0.3055837938759739,  
  "patternType": "Investment Account",  
  "secondCurvatureRadius": 0.0019846058153857316,  
  "storageType": "Investor",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:ffcd7e11-7c74-45f3-8f5a-3310ababddc8",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:c2540316-a0c2-4363-93b7-e49ab5ed3b2f",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:aae7e0b6-0256-4c58-a3ee-4989bdc205da",  
    "urn:ngsi-ld:System:857551fc-8a05-4052-9269-8193f148ff2c",  
    "urn:ngsi-ld:System:e4e88c0a-d78a-4bfd-a76b-af72e518a66e"  
  ],  
  "hasManufacturer": "Tank Company Inc.",  
  "hasModel": "Tank 0.1.2",  
  "dateCreated": "2023-01-26T12:03:34Z",  
  "dateModified": "2023-01-25T16:27:50Z",  
  "source": "Import",  
  "name": "Tank",  
  "alternateName": "Tank type 2",  
  "description": "Tank of limited Tank types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>    
#### Tanque NGSI-LD normalizado Ejemplo    
He aquí un ejemplo de un Tanque en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Tank:3d8b578c-7201-4bf4-bd7f-4aa1d9f5d298",  
  "type": "Tank",  
  "accessType": {  
    "type": "Property",  
    "value": "solid state"  
  },  
  "effectiveCapacity": {  
    "type": "Property",  
    "unitCode": "m3.B",  
    "observedAt": "2023-01-26T08:12:59Z",  
    "value": 0.30258616298480145  
  },  
  "endShapeType": {  
    "type": "Property",  
    "value": "Well"  
  },  
  "firstCurvatureRadius": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T08:09:31Z",  
    "value": 0.1755132773764223  
  },  
  "nominalDepth": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T09:14:29Z",  
    "value": 0.005463727391297302  
  },  
  "nominalLengthOrDiameter": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-25T17:31:47Z",  
    "value": 0.1263533877303663  
  },  
  "nominalVolumetricCapacity": {  
    "type": "Property",  
    "unitCode": "m3",  
    "observedAt": "2023-01-26T01:49:01Z",  
    "value": 0.26912875201450304  
  },  
  "nominalWidthOrDiameter": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-25T23:31:21Z",  
    "value": 0.7148569363985878  
  },  
  "numberOfSections": {  
    "type": "Property",  
    "value": 0.4947989850793809  
  },  
  "operatingWeight": {  
    "type": "Property",  
    "unitCode": "g",  
    "observedAt": "2023-01-26T07:09:35Z",  
    "value": 0.3475732824316351  
  },  
  "patternType": {  
    "type": "Property",  
    "value": "Checking Account"  
  },  
  "secondCurvatureRadius": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T05:30:46Z",  
    "value": 0.16951688752044902  
  },  
  "storageType": {  
    "type": "Property",  
    "value": "generate"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:862ca318-44c7-49b8-b0ca-74e1a829af60"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:4b8fd30b-21ae-4587-beaa-21783322f1a8"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:b8611055-a97b-4d01-8cd6-dd7f7931aa2a"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:1f9ab32d-3414-46a9-9bc9-b3f1d1b2c750"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:30979e9d-79b3-4285-ab23-addd0bdb63ef"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Tank Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Tank 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T19:22:34Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-25T19:58:46Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Tank"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Tank type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Tank of limited Tank types"  
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
