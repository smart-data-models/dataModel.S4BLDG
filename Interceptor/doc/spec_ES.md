<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: Interceptor  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Interceptor/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Un interceptor es un dispositivo diseñado e instalado con el fin de separar y retener materias deletéreas, peligrosas o indeseables, permitiendo al mismo tiempo que las aguas residuales o líquidos normales se descarguen en un sistema colector por gravedad.**  
versión: 0.0.  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.  
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `coverLength[object]`: Propiedad. La longitud medida a lo largo del eje x en el sistema de coordenadas local o el radio (en el caso de una forma circular en planta) de la cubierta del interceptor de aceite. Suele medirse en milímetros (mm).  - `coverWidth[object]`: Propiedad. Longitud medida a lo largo del eje x en el sistema de coordenadas local de la cubierta del interceptor de aceite. Normalmente se mide en milímetros (mm).  - `dataProvider[string]`: Secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated[string]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `dateModified[string]`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description[string]`: Descripción de este artículo  - `hasManufacturer[string]`: Propiedad. Relación que identifica al fabricante de una entidad (por ejemplo, un dispositivo). Se espera que el valor sea una cadena o una cadena con etiqueta de idioma.  - `hasModel[string]`: Propiedad. Relación que identifica el modelo de una entidad (por ejemplo, dispositivo). Se espera que el valor sea una cadena o una cadena con etiqueta de idioma.  - `id[*]`: Identificador único de la entidad  - `inletConnectionSize[object]`: Propiedad. Tamaño de la conexión de entrada. Suele medirse en milímetros (mm).  - `isContainedInBuildingSpace[*]`: Relación. Entidad utilizada para definir los espacios físicos del edificio. Un espacio del edificio contiene dispositivos u objetos del edificio. (Espacio del edificio)  - `isContainedInPhysicalObject[*]`: Relación. Cualquier Objeto que tiene una región espacial propia.  (Definición extraída de la ontología DUL) (PhysicalObject)  - `isSubSystemOf[array]`: Relación. Referencia a uno o varios sistemas de los que forma parte este objeto físico.  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `name[string]`: El nombre de este artículo.  - `nominalBodyDepth[object]`: Propiedad. Nominal o citada =longitud, medida a lo largo del eje z del sistema de coordenadas local del objeto, del cuerpo del objeto. Suele medirse en milímetros (mm).  - `nominalBodyLength[object]`: Propiedad. Longitud nominal o cotizada, medida a lo largo del eje x del sistema de coordenadas local del objeto, del cuerpo del objeto. Suele medirse en milímetros (mm).  - `nominalBodyWidth[object]`: Propiedad. Longitud nominal o cotizada, medida a lo largo del eje y del sistema de coordenadas local del objeto, del cuerpo del objeto. Suele medirse en milímetros (mm).  - `outletConnectionSize[object]`: Propiedad. Tamaño de la conexión de salida. Suele medirse en milímetros (mm).  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `type[string]`: Propiedad. Debe ser igual a `Interceptor`.  - `ventilatingPipeSize[object]`: Propiedad. Tamaño del tubo o tubos de ventilación. Suele medirse en milímetros (mm).  <!-- /30-PropertiesList -->  
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
Interceptor:    
  description: 'An interceptor is a device designed and installed in order to separate and retain deleterious, hazardous or undesirable matter while permitting normal sewage or liquids to discharge into a collection system by gravity.'    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government.'    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
        streetNr:    
          description: Number identifying a specific property on a public street.    
          type: string    
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
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: Property. The length measured along the x-axis in the local coordinate system or the radius (in the case of a circular shape in plan) of the cover of the oil interceptor. Usually measured in millimeters (mm).    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: &interceptor_-_properties_-_coverwidth_-_properties    
        observedAt:    
          description: Property. A relationship stating the timestamp of an entity (e.g. a measurement).    
          format: date-time    
          type: string    
        unitCode:    
          description: Property. A relationship identifying the unit of measure used for a certain entity.    
          type: string    
        value:    
          description: 'Property. A relationship defining the value of a certain property, e.g., energy or power. Note that, even if numeric values are expected to enable reasoning, measurement values could use other datatypes.'    
          type: number    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    coverWidth:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: Property. The length measured along the x-axis in the local coordinate system of the cover of the oil interceptor. Usually measured in millimeters (mm).    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *interceptor_-_properties_-_coverwidth_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity.    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.    
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
      description: 'Property. A relationship identifying the manufacturer of an entity (e.g., device). The value is expected to be a string or a string with language tag.'    
      type: string    
      x-ngsi:    
        type: Property    
    hasModel:    
      description: 'Property. A relationship identifying the model of an entity (e.g., device). The value is expected to be a string or a string with language tag.'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &interceptor_-_properties_-_iscontainedinbuildingspace_-_anyof    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    inletConnectionSize:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: Property. Size of the inlet connection. Usually measured in millimeters (mm).    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *interceptor_-_properties_-_coverwidth_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    isContainedInBuildingSpace:    
      anyOf: *interceptor_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *interceptor_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *interceptor_-_properties_-_iscontainedinbuildingspace_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Relationship    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: GeoProperty. Geojson reference to the item. Point    
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
        - description: GeoProperty. Geojson reference to the item. LineString    
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
        - description: GeoProperty. Geojson reference to the item. Polygon    
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
        - description: GeoProperty. Geojson reference to the item. MultiPoint    
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
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
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
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
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
    name:    
      description: The name of this item.    
      type: string    
      x-ngsi:    
        type: Property    
    nominalBodyDepth:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: 'Property. Nominal or quoted =length, measured along the z-axis of the local coordinate system of the object, of the body of the object. Usually measured in millimeters (mm).'    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *interceptor_-_properties_-_coverwidth_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    nominalBodyLength:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: 'Property. Nominal or quoted length, measured along the x-axis of the local coordinate system of the object, of the body of the object. Usually measured in millimeters (mm).'    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *interceptor_-_properties_-_coverwidth_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    nominalBodyWidth:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: 'Property. Nominal or quoted length, measured along the y-axis of the local coordinate system of the object, of the body of the object. Usually measured in millimeters (mm).'    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *interceptor_-_properties_-_coverwidth_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    outletConnectionSize:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: Property. Size of the outlet connection. Usually measured in millimeters (mm).    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *interceptor_-_properties_-_coverwidth_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *interceptor_-_properties_-_iscontainedinbuildingspace_-_anyof    
        description: Property. Unique identifier of the entity    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: Property. It must be equal to `Interceptor`.    
      enum:    
        - Interceptor    
      type: string    
      x-ngsi:    
        type: Property    
    ventilatingPipeSize:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: Property. Size of the ventilating pipe(s). Usually measured in millimeters (mm).    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *interceptor_-_properties_-_coverwidth_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
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
## Ejemplo de carga útil  
#### Interceptor NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un Interceptor en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### Interceptor NGSI-v2 normalizado Ejemplo  
He aquí un ejemplo de un interceptor en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Interceptor:e45ced8f-6d99-4b1e-a32b-d9e525d9429f",  
  "type": "Interceptor",  
  "coverLength": {  
    "type": "Measurement",  
    "value":  0.44339547398234425  
    }  
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
    }  
  },  
  "ventilatingPipeSize": {  
    "type": "Measurement",  
    "value": 0.9955414515835173  
    }  
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
#### Interceptor NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un Interceptor en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### Interceptor NGSI-LD normalizado Ejemplo  
He aquí un ejemplo de un interceptor en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
