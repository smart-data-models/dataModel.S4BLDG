<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entidad: Caldera    
================<!-- /10-Header -->    
<!-- 15-License -->    
[Licencia abierta](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Boiler/LICENSE.md)    
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descripción global: **Una caldera es un recipiente cerrado a presión en el que se calienta agua u otro fluido utilizando una fuente de energía como el gas natural, el gasóleo de calefacción o la electricidad. El fluido contenido en el recipiente se hace circular fuera de la caldera para su uso en diversos procesos o aplicaciones de calefacción.**.    
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
- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `description[string]`: Descripción de este artículo  - `energySource[string]`: La fuente de energía. Enumeración que define la fuente de energía o el combustible quemado para generar calor.  - `hasManufacturer[string]`: Relación que identifica al fabricante de una entidad (por ejemplo, un dispositivo). Se espera que el valor sea una cadena o una cadena con etiqueta de idioma  - `hasModel[string]`: Relación que identifica el modelo de una entidad (por ejemplo, un dispositivo). Se espera que el valor sea una cadena o una cadena con etiqueta de idioma  - `heatTransferSurfaceArea[number]`: Superficie total de transferencia de calor del recipiente. Suele medirse en metros cuadrados (m2).  - `id[*]`: Identificador único de la entidad  - `isContainedInBuildingSpace[*]`: Entidad utilizada para definir los espacios físicos del edificio. Un espacio del edificio contiene dispositivos u objetos del edificio. (Espacio del edificio)  - `isContainedInPhysicalObject[*]`: Cualquier Objeto que tiene una región espacial propia.  (Definición extraída de la ontología DUL) (PhysicalObject)  - `isSubSystemOf[array]`: Referencia al sistema o sistemas de los que forma parte este objeto físico.  - `isWaterStorageHeater[boolean]`: Se utiliza para identificar si la caldera tiene capacidad de almacenamiento (TRUE). Si es FALSE, la caldera no tiene capacidad de acumulación, como un calentador de agua instantáneo.  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `name[string]`: El nombre de este artículo  - `nominalEnergyConsumption[number]`: Tasa nominal de consumo de combustible necesaria para producir la potencia calorífica total de la caldera. Suele medirse en vatios (W, J/s).  - `nominalPartLoadRatio[number]`: Rango de carga parcial admisible  - `operatingMode[string]`: Identifica el modo de funcionamiento de la caldera  - `outletTemperatureMax[number]`: Temperatura de salida admisible del agua o del vapor. Suele medirse en grados Kelvin (K).  - `outletTemperatureMin[number]`: Temperatura de salida admisible del agua o del vapor. Suele medirse en grados Kelvin (K).  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `pressureRating[number]`: Presión nominal de la caldera según la clasificación del organismo competente. Normalmente se mide en pascales (Pa, N/m2).  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `type[string]`: Debe ser igual a "Caldera".  - `waterInletTemperatureMax[number]`: Rango admisible de temperatura de entrada del agua. Suele medirse en grados Kelvin (K).  - `waterInletTemperatureMin[number]`: Rango admisible de temperatura de entrada del agua. Suele medirse en grados Kelvin (K).  - `waterStorageCapacity[number]`: Capacidad de almacenamiento de agua. Suele medirse en metros cúbicos (m3).  <!-- /30-PropertiesList -->    
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
Boiler:      
  description: 'A boiler is a closed, pressure-rated vessel in which water or other fluid is heated using an energy source such as natural gas, heating oil, or electricity. The fluid in the vessel is then circulated out of the boiler for use in various processes or heating applications.'      
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
    energySource:      
      description: The source of energy. Enumeration defining the energy source or fuel combusted to generate heat      
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
    heatTransferSurfaceArea:      
      description: Total heat transfer area of the vessel. Usually measured in square metre (m2)      
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
    isWaterStorageHeater:      
      description: 'This is used to identify if the boiler has storage capacity (TRUE). If FALSE, then there is no storage capacity built into the boiler, such as an instantaneous hot water heater'      
      type: boolean      
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
    nominalEnergyConsumption:      
      description: 'Nominal fuel consumption rate required to produce the total boiler heat output. Usually measured in Watts (W, J/s)'      
      type: number      
      x-ngsi:      
        type: Property      
    nominalPartLoadRatio:      
      description: Allowable part load ratio range      
      type: number      
      x-ngsi:      
        type: Property      
    operatingMode:      
      description: Identifies the operating mode of the boiler      
      type: string      
      x-ngsi:      
        type: Property      
    outletTemperatureMax:      
      description: Allowable outlet temperature of either the water or the steam. Usually measured in degrees Kelvin (K)      
      type: number      
      x-ngsi:      
        type: Property      
    outletTemperatureMin:      
      description: Allowable outlet temperature of either the water or the steam. Usually measured in degrees Kelvin (K)      
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
    pressureRating:      
      description: 'Nominal pressure rating of the boiler as rated by the agency having jurisdiction. Usually measured in Pascals (Pa, N/m2)'      
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
      description: It must be equal to `Boiler`      
      enum:      
        - Boiler      
      type: string      
      x-ngsi:      
        type: Property      
    waterInletTemperatureMax:      
      description: Allowable water inlet temperature range. Usually measured in degrees Kelvin (K)      
      type: number      
      x-ngsi:      
        type: Property      
    waterInletTemperatureMin:      
      description: Allowable water inlet temperature range. Usually measured in degrees Kelvin (K)      
      type: number      
      x-ngsi:      
        type: Property      
    waterStorageCapacity:      
      description: Water storage capacity. Usually measured in cubic metre (m3)      
      type: number      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Boiler"      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Boiler/LICENSE.md      
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Boiler/schema.json      
  x-model-tags: 'SAREF, building'      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Ejemplo de carga útil    
#### Ejemplo de valores clave de la caldera NGSI-v2    
He aquí un ejemplo de una caldera en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Boiler:724c2f67-e55e-4971-8e74-55d6ecfa19c9",  
  "type": "Boiler",  
  "energySource": "United States of America",  
  "heatTransferSurfaceArea": 0.7853344933267346,  
  "isWaterStorageHeater": false,  
  "nominalEnergyConsumption": 0.6203749662936422,  
  "nominalPartLoadRatio": 0.8015670647257737,  
  "operatingMode": "systems",  
  "outletTemperatureMax": 0.16008580907721015,  
  "outletTemperatureMin": 0.04227267769006804,  
  "pressureRating": 0.5113599213422801,  
  "waterInletTemperatureMax": 0.9011788947791837,  
  "waterInletTemperatureMin": 0.24858493133262038,  
  "waterStorageCapacity": 0.5276371515431508,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:50afbc21-cf0f-4f69-b48a-47af5a287d38",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:f2bfaa08-a201-40bd-b1b3-fe5a4ba5d291",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:1cfd3123-93fa-408a-a750-dd5a6f0edcae",  
    "urn:ngsi-ld:System:fec748f9-6ee5-49af-93a4-5bffcc20e73c",  
    "urn:ngsi-ld:System:5ee8058b-c872-4237-9c94-82f22172c39e"  
  ],  
  "hasManufacturer": "Boiler Company Inc.",  
  "hasModel": "Boiler 0.1.2",  
  "dateCreated": "2023-01-26T09:03:19Z",  
  "dateModified": "2023-01-25T16:09:21Z",  
  "source": "Import",  
  "name": "Boiler",  
  "alternateName": "Boiler type 2",  
  "description": "Boiler of limited Boiler types",  
  "dataProvider": "IFC file"  
}  
```  
</details>    
#### Caldera NGSI-v2 normalizada Ejemplo    
He aquí un ejemplo de una caldera en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Boiler:554e6cfc-a12b-466b-bdb5-251db87de147",  
  "type": "Boiler",  
  "energySource": {  
    "type": "Text",  
    "value": "Coordinator"  
  },  
  "heatTransferSurfaceArea": {  
    "type": "Number",  
    "value": 0.054241651152424186  
  },  
  "isWaterStorageHeater": {  
    "type": "Boolean",  
    "value": false  
  },  
  "nominalEnergyConsumption": {  
    "type": "Number",  
    "value": 0.015349430439582035  
  },  
  "nominalPartLoadRatio": {  
    "type": "Number",  
    "value": 0.15224995605259972  
  },  
  "operatingMode": {  
    "type": "Text",  
    "value": "bypass"  
  },  
  "outletTemperatureMax": {  
    "type": "Number",  
    "value": 0.6702304071347284  
  },  
  "outletTemperatureMin": {  
    "type": "Number",  
    "value": 0.5096152218274909  
  },  
  "pressureRating": {  
    "type": "Number",  
    "value": 0.5974774605306619  
  },  
  "waterInletTemperatureMax": {  
    "type": "Number",  
    "value": 0.9398884749677864  
  },  
  "waterInletTemperatureMin": {  
    "type": "Number",  
    "value": 0.4089735417040705  
  },  
  "waterStorageCapacity": {  
    "type": "Number",  
    "value": 0.9413886423074906  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:BuildingSpace:ab8a7d6f-040b-4eb8-b6ea-f238a2ccc065"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:PhysicalObject:668e5ccf-c66c-43ea-ad8d-fca6862f3d04"  
  },  
  "isSubSystemOf": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:System:2c2904e8-d4fa-4191-8b1b-4e06eaed77ff",  
      "urn:ngsi-ld:System:820d0fb3-9cb6-4bc4-b706-515d91e3343f",  
      "urn:ngsi-ld:System:a0370269-07a5-4bad-a6c0-15a382a279ce"  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Boiler Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Boiler 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T10:00:09.4580486+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T18:35:13.9392676+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Boiler"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Boiler type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Boiler of limited Boiler types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>    
#### Ejemplo de valores clave de la caldera NGSI-LD    
He aquí un ejemplo de una caldera en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Boiler:724c2f67-e55e-4971-8e74-55d6ecfa19c9",  
  "type": "Boiler",  
  "energySource": "United States of America",  
  "heatTransferSurfaceArea": 0.7853344933267346,  
  "isWaterStorageHeater": false,  
  "nominalEnergyConsumption": 0.6203749662936422,  
  "nominalPartLoadRatio": 0.8015670647257737,  
  "operatingMode": "systems",  
  "outletTemperatureMax": 0.16008580907721015,  
  "outletTemperatureMin": 0.04227267769006804,  
  "pressureRating": 0.5113599213422801,  
  "waterInletTemperatureMax": 0.9011788947791837,  
  "waterInletTemperatureMin": 0.24858493133262038,  
  "waterStorageCapacity": 0.5276371515431508,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:50afbc21-cf0f-4f69-b48a-47af5a287d38",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:f2bfaa08-a201-40bd-b1b3-fe5a4ba5d291",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:1cfd3123-93fa-408a-a750-dd5a6f0edcae",  
    "urn:ngsi-ld:System:fec748f9-6ee5-49af-93a4-5bffcc20e73c",  
    "urn:ngsi-ld:System:5ee8058b-c872-4237-9c94-82f22172c39e"  
  ],  
  "hasManufacturer": "Boiler Company Inc.",  
  "hasModel": "Boiler 0.1.2",  
  "dateCreated": "2023-01-26T09:03:19Z",  
  "dateModified": "2023-01-25T16:09:21Z",  
  "source": "Import",  
  "name": "Boiler",  
  "alternateName": "Boiler type 2",  
  "description": "Boiler of limited Boiler types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>    
#### Caldera NGSI-LD normalizada Ejemplo    
He aquí un ejemplo de una caldera en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Boiler:4f7a4533-13d0-4de0-b5e9-72dee067176a",  
  "type": "Boiler",  
  "energySource": {  
    "type": "Property",  
    "value": "Sri Lanka"  
  },  
  "heatTransferSurfaceArea": {  
    "type": "Property",  
    "unitCode": "m2",  
    "observedAt": "2023-01-25T19:16:12Z",  
    "value": 0.4182368568397056  
  },  
  "isWaterStorageHeater": {  
    "type": "Property",  
    "value": false  
  },  
  "nominalEnergyConsumption": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-25T23:06:57Z",  
    "value": 0.5252685918504294  
  },  
  "nominalPartLoadRatio": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-25T22:37:37Z",  
    "value": 0.481958764350527  
  },  
  "operatingMode": {  
    "type": "Property",  
    "value": "Auto Loan Account"  
  },  
  "outletTemperatureMax": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T17:03:10Z",  
    "value": 0.2786304815176084  
  },  
  "outletTemperatureMin": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T02:55:50Z",  
    "value": 0.4041488945350036  
  },  
  "pressureRating": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-25T18:00:19Z",  
    "value": 0.5561857737231611  
  },  
  "waterInletTemperatureMax": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T03:34:53Z",  
    "value": 0.242404197934733  
  },  
  "waterInletTemperatureMin": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T04:06:01Z",  
    "value": 0.46028861347866734  
  },  
  "waterStorageCapacity": {  
    "type": "Property",  
    "unitCode": "m3",  
    "observedAt": "2023-01-26T10:18:01Z",  
    "value": 0.22263600675421202  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:cfc926aa-ae2a-411e-b3d4-c315d7d19d9b"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:5e682b37-bcc1-441a-ad19-80615c70a84f"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:ba691c15-807f-48fb-b963-99961fd81a95"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:227bcf8f-170f-41ff-a88d-1e1cb67da411"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:7868b4ac-6685-4b3e-85ef-6494c909409c"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Boiler Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Boiler 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T17:50:43Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-25T23:43:57Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Boiler"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Boiler type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Boiler of limited Boiler types"  
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
