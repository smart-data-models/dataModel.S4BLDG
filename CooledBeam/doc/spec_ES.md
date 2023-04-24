<!-- 10-Header -->
  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entidad: CooledBeam  
===================
<!-- /10-Header -->
  
<!-- 15-License -->
  

[Licencia abierta](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/CooledBeam/LICENSE.md)  

[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->
  
<!-- 20-Description -->
  

Descripción global: **Una viga fría (o viga refrigerante) es un dispositivo utilizado normalmente para enfriar el aire haciendo circular un fluido, como agua fría, a través de tubos con aletas expuestos por encima de un espacio. La viga fría, que suele montarse en el techo o cerca de él, utiliza la convección para enfriar el espacio que tiene debajo actuando como sumidero de calor para el aire caliente que se eleva de forma natural. Una vez enfriado, el aire desciende de forma natural hasta el suelo, donde el ciclo comienza de nuevo.**  

versión: 0.0.2  
<!-- /20-Description -->
  
<!-- 30-PropertiesList -->
  


## Lista de propiedades  


<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.  
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)
- `alternateName[string]`: Un nombre alternativo para este artículo  
- `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)
- `coilLength[number]`: Propiedad. Longitud de la bobina. Suele medirse en milímetros (mm).  
- `coilWidth[number]`: Propiedad. Anchura de la bobina. Suele medirse en milímetros (mm  
- `dataProvider[string]`: Secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  
- `dateCreated[string]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  
- `dateModified[string]`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  
- `description[string]`: Descripción de este artículo  
- `finishColor[string]`: Propiedad. Color de acabado de la viga refrigerada.  
- `hasManufacturer[string]`: Propiedad. Relación que identifica al fabricante de una entidad (por ejemplo, un dispositivo). Se espera que el valor sea una cadena o una cadena con etiqueta de idioma.  
- `hasModel[string]`: Propiedad. Relación que identifica el modelo de una entidad (por ejemplo, dispositivo). Se espera que el valor sea una cadena o una cadena con etiqueta de idioma.  
- `id[*]`: Identificador único de la entidad  
- `integratedLightingType[string]`: Propiedad. Iluminación integrada en viga refrigerada.  
- `isContainedInBuildingSpace[*]`: Relación. Entidad utilizada para definir los espacios físicos del edificio. Un espacio del edificio contiene dispositivos u objetos del edificio. (Espacio del edificio)  
- `isContainedInPhysicalObject[*]`: Relación. Cualquier Objeto que tiene una región espacial propia.  (Definición extraída de la ontología DUL) (PhysicalObject)  
- `isFreeHanging[boolean]`: Propiedad. ¿Es de tipo colgante libre (no está montado en un falso techo)?  
- `isSubSystemOf[array]`: Relación. Referencia a uno o varios sistemas de los que forma parte este objeto físico.  
- `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  
- `name[string]`: El nombre de este artículo.  
- `nominalCoolingCapacity[number]`: Propiedades. Capacidad nominal de refrigeración. Normalmente se mide en vatios (W, J/s).  
- `nominalHeatingCapacity[number]`: Propiedad. Potencia calorífica nominal. Suele medirse en vatios (W, J/s).  
- `nominalReturnWaterTemperatureCooling[number]`: Propiedad. Temperatura nominal del agua de retorno (se refiere a la potencia frigorífica nominal). Normalmente se mide en grados Kelvin (K).  
- `nominalReturnWaterTemperatureHeating[number]`: Propiedad. Temperatura nominal del agua de retorno (se refiere a la potencia nominal de calefacción). Suele medirse en grados Kelvin (K).  
- `nominalSorroundingHumidityCooling[number]`: Propiedad. Humedad ambiental nominal (se refiere a la capacidad nominal de refrigeración). Suele medirse en grados Kelvin (K).  
- `nominalSorroundingTemperatureCooling[number]`: Propiedad. Temperatura ambiente nominal (se refiere a la capacidad nominal de refrigeración). Suele medirse en grados Kelvin (K).  
- `nominalSorroundingTemperatureHeating[number]`: Propiedad. Temperatura ambiente nominal (se refiere a la capacidad nominal de calefacción). Suele medirse en grados Kelvin (K).  
- `nominalSupplyWaterTemperatureCooling[number]`: Propiedad. Temperatura nominal del agua de alimentación (se refiere a la potencia frigorífica nominal). Normalmente se mide en grados Kelvin (K).  
- `nominalSupplyWaterTemperatureHeating[number]`: Propiedad. Temperatura nominal del agua de impulsión (se refiere a la potencia nominal de calefacción). Suele medirse en grados Kelvin (K).  
- `nominalWaterFlowCooling[number]`: Propiedad. Caudal nominal de agua (se refiere a la capacidad nominal de refrigeración). Suele medirse en m3/s.  
- `nominalWaterFlowHeating[number]`: Propiedad. Caudal nominal de agua (se refiere a la potencia nominal de calefacción). Suele medirse en m3/s.  
- `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  
- `pipeConnectionEnum[string]`: Propiedad. La forma en que se realiza la conexión de la tubería a la viga refrigerada.  
- `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  
- `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  
- `type[string]`: Propiedad. Debe ser igual a `CooledBeam`.  
- `waterFlowControlSystemType[string]`: Propiedad. Sistema de control del caudal de agua instalado de fábrica.  
- `waterPressureMax[number]`: Propiedad. Rango de presión de trabajo admisible del circuito de agua. Normalmente se mide en pascales (Pa, N/m2).  
- `waterPressureMin[number]`: Propiedad. Rango de presión de trabajo admisible del circuito de agua. Normalmente se mide en pascales (Pa, N/m2).  
<!-- /30-PropertiesList -->
  
<!-- 35-RequiredProperties -->
  

Propiedades requeridas  
- `id`  
- `type`  
<!-- /35-RequiredProperties -->
  
<!-- 40-RequiredProperties -->
  
<!-- /40-RequiredProperties -->
  
<!-- 50-DataModelHeader -->
  

## Descripción de las propiedades del modelo de datos  

Ordenados alfabéticamente (pulse para más detalles)  
<!-- /50-DataModelHeader -->
  
<!-- 60-ModelYaml -->
  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
CooledBeam:    
  description: 'A cooled beam (or chilled beam) is a device typically used to cool air by circulating a fluid such as chilled water through exposed finned tubes above a space. Typically mounted overhead near or within a ceiling, the cooled beam uses convection to cool the space below it by acting as a heat sink for the naturally rising warm air of the space. Once cooled, the air naturally drops back to the floor where the cycle begins again.'    
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
    coilLength:    
      description: Property. Length of coil. Usually measured in millimeters (mm).    
      type: number    
      x-ngsi:    
        type: Property    
    coilWidth:    
      description: Property. Width of coil. Usually measured in millimeters (mm    
      type: number    
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
    finishColor:    
      description: Property. Finish color for cooled beam.    
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
      anyOf: &cooledbeam_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    integratedLightingType:    
      description: Property. Integrated lighting in cooled beam.    
      type: string    
      x-ngsi:    
        type: Property    
    isContainedInBuildingSpace:    
      anyOf: *cooledbeam_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *cooledbeam_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isFreeHanging:    
      description: 'Property. Is it free hanging type (not mounted in a false ceiling)?'    
      type: boolean    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *cooledbeam_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    nominalCoolingCapacity:    
      description: 'Property. Nominal cooling capacity. Usually measured in Watts (W, J/s).'    
      type: number    
      x-ngsi:    
        type: Property    
    nominalHeatingCapacity:    
      description: 'Property. Nominal heating capacity. Usually measured in Watts (W, J/s).'    
      type: number    
      x-ngsi:    
        type: Property    
    nominalReturnWaterTemperatureCooling:    
      description: Property. Nominal return water temperature (refers to nominal cooling capacity). Usually measured in degrees Kelvin (K).    
      type: number    
      x-ngsi:    
        type: Property    
    nominalReturnWaterTemperatureHeating:    
      description: Property. Nominal return water temperature (refers to nominal heating capacity). Usually measured in degrees Kelvin (K).    
      type: number    
      x-ngsi:    
        type: Property    
    nominalSorroundingHumidityCooling:    
      description: Property. Nominal surrounding humidity (refers to nominal cooling capacity). Usually measured in degrees Kelvin (K).    
      type: number    
      x-ngsi:    
        type: Property    
    nominalSorroundingTemperatureCooling:    
      description: Property. Nominal surrounding temperature (refers to nominal cooling capacity). Usually measured in degrees Kelvin (K).    
      type: number    
      x-ngsi:    
        type: Property    
    nominalSorroundingTemperatureHeating:    
      description: Property. Nominal surrounding temperature (refers to nominal heating capacity). Usually measured in degrees Kelvin (K).    
      type: number    
      x-ngsi:    
        type: Property    
    nominalSupplyWaterTemperatureCooling:    
      description: Property. Nominal supply water temperature (refers to nominal cooling capacity). Usually measured in degrees Kelvin (K).    
      type: number    
      x-ngsi:    
        type: Property    
    nominalSupplyWaterTemperatureHeating:    
      description: Property. Nominal supply water temperature (refers to nominal heating capacity). Usually measured in degrees Kelvin (K).    
      type: number    
      x-ngsi:    
        type: Property    
    nominalWaterFlowCooling:    
      description: Property. Nominal water flow (refers to nominal cooling capacity). Usually measured in m3/s.    
      type: number    
      x-ngsi:    
        type: Property    
    nominalWaterFlowHeating:    
      description: Property. Nominal water flow (refers to nominal heating capacity). Usually measured in m3/s.    
      type: number    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *cooledbeam_-_properties_-_iscontainedinbuildingspace_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    pipeConnectionEnum:    
      description: Property. The manner in which the pipe connection is made to the cooled beam.    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: Property. It must be equal to `CooledBeam`.    
      enum:    
        - CooledBeam    
      type: string    
      x-ngsi:    
        type: Property    
    waterFlowControlSystemType:    
      description: Property. Factory fitted waterflow control system.    
      type: string    
      x-ngsi:    
        type: Property    
    waterPressureMax:    
      description: 'Property. Allowable water circuit working pressure range. Usually measured in Pascals (Pa, N/m2).'    
      type: number    
      x-ngsi:    
        type: Property    
    waterPressureMin:    
      description: 'Property. Allowable water circuit working pressure range. Usually measured in Pascals (Pa, N/m2).'    
      type: number    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:CooledBeam"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/CooledBeam/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/CooledBeam/schema.json    
  x-model-tags: SAREF CooledBeam    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->
  
<!-- 70-MiddleNotes -->
  
<!-- /70-MiddleNotes -->
  
<!-- 80-Examples -->
  

## Ejemplo de carga útil  

#### CooledBeam NGSI-v2 key-values Ejemplo  

Aquí hay un ejemplo de un CooledBeam en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:CooledBeam:82040ca8-778f-478d-a8fd-28485704919f",  
  "type": "CooledBeam",  
  "coilLength": 0.12136965337189098,  
  "coilWidth": 0.9739362570796377,  
  "finishColor": "deposit",  
  "integratedLightingType": "Metrics",  
  "isFreeHanging": false,  
  "nominalCoolingCapacity": 0.25517130161811685,  
  "nominalHeatingCapacity": 0.979299961039553,  
  "nominalReturnWaterTemperatureCooling": 0.8331575990645163,  
  "nominalReturnWaterTemperatureHeating": 0.8257910510708837,  
  "nominalSorroundingHumidityCooling": 0.08831404123432451,  
  "nominalSorroundingTemperatureCooling": 0.8951747110468832,  
  "nominalSorroundingTemperatureHeating": 0.7722529144575002,  
  "nominalSupplyWaterTemperatureCooling": 0.510069259798832,  
  "nominalSupplyWaterTemperatureHeating": 0.9682117435710755,  
  "nominalWaterFlowCooling": 0.640621498291464,  
  "nominalWaterFlowHeating": 0.3754874763938201,  
  "pipeConnectionEnum": "Falls",  
  "waterFlowControlSystemType": "Forks",  
  "waterPressureMax": 0.6809509740238233,  
  "waterPressureMin": 0.3372474470208946,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:29882bc5-9d20-4d25-b276-5bdf4f6981e1",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:13d83cbf-6e67-4d40-85da-46a7032fbde9",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:dfeed4f8-88d6-4475-89b3-71faa705f8a4",  
    "urn:ngsi-ld:System:23813ba9-d7b1-475b-b245-c32d08798cc3",  
    "urn:ngsi-ld:System:daa546ea-d20c-4761-98b2-e17e050b4625"  
  ],  
  "hasManufacturer": "CooledBeam Company Inc.",  
  "hasModel": "CooledBeam 0.1.2",  
  "dateCreated": "2023-01-26T05:29:03Z",  
  "dateModified": "2023-01-26T10:03:56Z",  
  "source": "Import",  
  "name": "CooledBeam",  
  "alternateName": "CooledBeam type 2",  
  "description": "CooledBeam of limited CooledBeam types",  
  "dataProvider": "IFC file"  
}  
```  
</details>  

#### CooledBeam NGSI-v2 normalizado Ejemplo  

He aquí un ejemplo de un CooledBeam en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:CooledBeam:38dcdd25-ae94-441c-8409-218ec91e3006",  
  "type": "CooledBeam",  
  "coilLength": {  
    "type": "Measurement",  
    "value": 0.4277226249853211  
  },  
  "coilWidth": {  
    "type": "Measurement",  
    "value":0.6183775851562611  
  },  
  "finishColor": {  
    "type": "Text",  
    "value": "Associate"  
  },  
  "integratedLightingType": {  
    "type": "Text",  
    "value": "Washington"  
  },  
  "isFreeHanging": {  
    "type": "Boolean",  
    "value": false  
  },  
  "nominalCoolingCapacity": {  
    "type": "Measurement",  
    "value":0.45857043485420457  
  },  
  "nominalHeatingCapacity": {  
    "type": "Measurement",  
    "value":  0.37812382267356337  
  },  
  "nominalReturnWaterTemperatureCooling": {  
    "type": "Measurement",  
    "value":  0.973742767691913  
  },  
  "nominalReturnWaterTemperatureHeating": {  
    "type": "Measurement",  
    "value":  0.6848085584395665  
  },  
  "nominalSorroundingHumidityCooling": {  
    "type": "Measurement",  
    "value":  0.4100986776385609  
  },  
  "nominalSorroundingTemperatureCooling": {  
    "type": "Measurement",  
    "value":  0.039909771141081074  
  },  
  "nominalSorroundingTemperatureHeating": {  
    "type": "Measurement",  
    "value":  0.3023923557796515  
  },  
  "nominalSupplyWaterTemperatureCooling": {  
    "type": "Measurement",  
    "value":  0.7562940127899793  
  },  
  "nominalSupplyWaterTemperatureHeating": {  
    "type": "Measurement",  
    "value":  0.31198678394809454  
  },  
  "nominalWaterFlowCooling": {  
    "type": "Measurement",  
    "value":  0.40924277893308847  
  },  
  "nominalWaterFlowHeating": {  
    "type": "Measurement",  
    "value":  0.9345939456733873  
  },  
  "pipeConnectionEnum": {  
    "type": "Text",  
    "value": "extensible"  
  },  
  "waterFlowControlSystemType": {  
    "type": "Text",  
    "value": "Interactions"  
  },  
  "waterPressureMax": {  
    "type": "Measurement",  
    "value":  0.07837257218461391  
  },  
  "waterPressureMin": {  
    "type": "Measurement",  
    "value": 0.03742669539477306  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:BuildingSpace:3e03fe30-3728-4867-ab51-b147c2d3e63b"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:PhysicalObject:cfd9df05-18b1-44f4-b1ee-da55226255e9"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:a4b0cda0-b373-4ae9-b2c7-e2cff5429e1e"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:216f6f83-8bd1-456f-9bed-36dbec41a3aa"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:d19ccffa-f134-46fc-8f9f-77656bb91649"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "CooledBeam Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "CooledBeam 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T21:51:06.7954024+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T00:15:46.9435362+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "CooledBeam"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "CooledBeam type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "CooledBeam of limited CooledBeam types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  

#### CooledBeam NGSI-LD key-values Ejemplo  

Aquí hay un ejemplo de un CooledBeam en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:CooledBeam:82040ca8-778f-478d-a8fd-28485704919f",  
  "type": "CooledBeam",  
  "coilLength": 0.12136965337189098,  
  "coilWidth": 0.9739362570796377,  
  "finishColor": "deposit",  
  "integratedLightingType": "Metrics",  
  "isFreeHanging": false,  
  "nominalCoolingCapacity": 0.25517130161811685,  
  "nominalHeatingCapacity": 0.979299961039553,  
  "nominalReturnWaterTemperatureCooling": 0.8331575990645163,  
  "nominalReturnWaterTemperatureHeating": 0.8257910510708837,  
  "nominalSorroundingHumidityCooling": 0.08831404123432451,  
  "nominalSorroundingTemperatureCooling": 0.8951747110468832,  
  "nominalSorroundingTemperatureHeating": 0.7722529144575002,  
  "nominalSupplyWaterTemperatureCooling": 0.510069259798832,  
  "nominalSupplyWaterTemperatureHeating": 0.9682117435710755,  
  "nominalWaterFlowCooling": 0.640621498291464,  
  "nominalWaterFlowHeating": 0.3754874763938201,  
  "pipeConnectionEnum": "Falls",  
  "waterFlowControlSystemType": "Forks",  
  "waterPressureMax": 0.6809509740238233,  
  "waterPressureMin": 0.3372474470208946,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:29882bc5-9d20-4d25-b276-5bdf4f6981e1",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:13d83cbf-6e67-4d40-85da-46a7032fbde9",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:dfeed4f8-88d6-4475-89b3-71faa705f8a4",  
    "urn:ngsi-ld:System:23813ba9-d7b1-475b-b245-c32d08798cc3",  
    "urn:ngsi-ld:System:daa546ea-d20c-4761-98b2-e17e050b4625"  
  ],  
  "hasManufacturer": "CooledBeam Company Inc.",  
  "hasModel": "CooledBeam 0.1.2",  
  "dateCreated": "2023-01-26T05:29:03Z",  
  "dateModified": "2023-01-26T10:03:56Z",  
  "source": "Import",  
  "name": "CooledBeam",  
  "alternateName": "CooledBeam type 2",  
  "description": "CooledBeam of limited CooledBeam types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  

#### CooledBeam NGSI-LD normalizado Ejemplo  

He aquí un ejemplo de un CooledBeam en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:CooledBeam:baa66543-6434-4e28-8e85-20b2b260d404",  
  "type": "CooledBeam",  
  "coilLength": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-25T18:59:14Z",  
    "value": 0.45413352830053977  
  },  
  "coilWidth": {  
    "type": "Property",  
    "unitCode": "m",  
    "observedAt": "2023-01-26T07:44:01Z",  
    "value": 0.2692385089640058  
  },  
  "finishColor": {  
    "type": "Property",  
    "value": "indigo"  
  },  
  "integratedLightingType": {  
    "type": "Property",  
    "value": "Graphical User Interface"  
  },  
  "isFreeHanging": {  
    "type": "Property",  
    "value": false  
  },  
  "nominalCoolingCapacity": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-26T09:40:29Z",  
    "value": 0.3030442126473498  
  },  
  "nominalHeatingCapacity": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-26T02:43:04Z",  
    "value": 0.7091959285173477  
  },  
  "nominalReturnWaterTemperatureCooling": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T10:09:02Z",  
    "value": 0.4048762377790246  
  },  
  "nominalReturnWaterTemperatureHeating": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T08:24:33Z",  
    "value": 0.33261295327987683  
  },  
  "nominalSorroundingHumidityCooling": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T12:36:33Z",  
    "value": 0.5632800434491262  
  },  
  "nominalSorroundingTemperatureCooling": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T11:31:42Z",  
    "value": 0.47265451181389695  
  },  
  "nominalSorroundingTemperatureHeating": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T18:37:57Z",  
    "value": 0.18090042184548072  
  },  
  "nominalSupplyWaterTemperatureCooling": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T21:17:20Z",  
    "value": 0.9122743224756777  
  },  
  "nominalSupplyWaterTemperatureHeating": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T17:52:00Z",  
    "value": 0.9207552089629301  
  },  
  "nominalWaterFlowCooling": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-25T15:05:33Z",  
    "value": 0.06592489938443258  
  },  
  "nominalWaterFlowHeating": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-26T13:42:04Z",  
    "value": 0.3446198206084118  
  },  
  "pipeConnectionEnum": {  
    "type": "Property",  
    "value": "SSL"  
  },  
  "waterFlowControlSystemType": {  
    "type": "Property",  
    "value": "supply-chains"  
  },  
  "waterPressureMax": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-25T17:35:39Z",  
    "value": 0.8610847602415933  
  },  
  "waterPressureMin": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-26T03:28:09Z",  
    "value": 0.9088584704707019  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:6689ca11-b361-48b4-950d-07edf1182e97"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:2e350952-8c19-46a2-a2c2-8d30c54d03cb"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:cf124c7e-8f71-424a-93b5-64643c889f30"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:a72f7b54-3f5c-4b66-9463-f20f7127cff6"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:ce488063-f9a9-44c4-ac0f-f79e2977a2d4"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "CooledBeam Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "CooledBeam 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T23:43:55Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-25T20:21:43Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "CooledBeam"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "CooledBeam type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "CooledBeam of limited CooledBeam types"  
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
  
