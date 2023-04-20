<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: Raffreddatore evaporativo  
=================================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/EvaporativeCooler/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Un raffreddatore evaporativo è un dispositivo che raffredda l'aria saturandola di vapore acqueo.  
versione: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated[string]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateModified[string]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `description[string]`: Descrizione dell'articolo  - `flowArrangement[string]`: Proprietà. Controflusso: il flusso d'aria e d'acqua entrano in direzioni diverse. Flusso incrociato: il flusso d'aria e d'acqua sono perpendicolari. Flusso parallelo: il flusso d'aria e d'acqua entrano nelle stesse direzioni.  - `hasManufacturer[string]`: Proprietà. Una relazione che identifica il produttore di un'entità (ad esempio, un dispositivo). Il valore dovrebbe essere una stringa o una stringa con un tag di lingua.  - `hasModel[string]`: Proprietà. Una relazione che identifica il modello di un'entità (ad esempio, un dispositivo). Il valore dovrebbe essere una stringa o una stringa con un tag di lingua.  - `heatExchangeArea[object]`: Proprietà. Area di scambio termico. Solitamente misurata in metri quadrati (m2).  - `id[*]`: Identificatore univoco dell'entità  - `isContainedInBuildingSpace[*]`: Relazione. Un'entità utilizzata per definire gli spazi fisici dell'edificio. Uno spazio dell'edificio contiene dispositivi o oggetti dell'edificio. (Spazio edificio)  - `isContainedInPhysicalObject[*]`: Relazione. Qualsiasi oggetto che abbia una regione spaziale appropriata.  (Definizione estratta dall'ontologia DUL) (PhysicalObject)  - `isSubSystemOf[array]`: Relazione. Un riferimento a uno o più sistemi di cui questo Oggetto fisico fa parte.  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento.  - `operationTemperatureMax[object]`: Proprietà. Intervallo di temperatura ambiente (aria, fluido) consentito per il funzionamento. Di solito si misura in gradi Kelvin (K).  - `operationTemperatureMin[object]`: Proprietà. Intervallo di temperatura ambiente (aria, fluido) consentito per il funzionamento. Di solito si misura in gradi Kelvin (K).  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `type[string]`: Proprietà. Deve essere uguale a `EvaporativeCooler`.  - `waterRequirement[object]`: Proprietà. Fabbisogno di acqua di reintegro. Di solito si misura in m3/s.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
EvaporativeCooler:    
  description: An evaporative cooler is a device that cools air by saturating it with water vapor.    
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
    flowArrangement:    
      description: 'Property. CounterFlow: Air and water flow enter in different directions. CrossFlow: Air and water flow are perpendicular. ParallelFlow: air and water flow enter in same directions.'    
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
    heatExchangeArea:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: Property. Heat exchange area. Usually measured in square metre (m2).    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: &evaporativecooler_-_properties_-_operationtemperaturemax_-_properties    
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
    id:    
      anyOf: &evaporativecooler_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    isContainedInBuildingSpace:    
      anyOf: *evaporativecooler_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *evaporativecooler_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *evaporativecooler_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    operationTemperatureMax:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: 'Property. Allowable operation ambient (air, fluid) temperature range. Usually measured in degrees Kelvin (K).'    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *evaporativecooler_-_properties_-_operationtemperaturemax_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    operationTemperatureMin:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: 'Property. Allowable operation ambient (air, fluid) temperature range. Usually measured in degrees Kelvin (K).'    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *evaporativecooler_-_properties_-_operationtemperaturemax_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *evaporativecooler_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      description: Property. It must be equal to `EvaporativeCooler`.    
      enum:    
        - EvaporativeCooler    
      type: string    
      x-ngsi:    
        type: Property    
    waterRequirement:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: Property. Make-up water requirement. Usually measured in m3/s.    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *evaporativecooler_-_properties_-_operationtemperaturemax_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:EvaporativeCooler"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/EvaporativeCooler/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/EvaporativeCooler/schema.json    
  x-model-tags: SAREF EvaporativeCooler    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### EvaporativeCooler NGSI-v2 valori-chiave Esempio  
Ecco un esempio di EvaporativeCooler in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:EvaporativeCooler:54b020f5-a24c-4e78-af69-ab730287a7fb",  
    "type": "EvaporativeCooler",  
    "flowArrangement": "Walk",  
    "heatExchangeArea": 0.0154798489699417,  
    "operationTemperatureMax": 0.8076614358257233,  
    "operationTemperatureMin": 0.05752519637609499,  
    "waterRequirement": 0.48344490145201957,  
    "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:b2cc75eb-3d85-44ce-b594-0c9c036f5f20",  
    "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:76419a51-5245-4bbe-b246-b2d4278d8c91",  
    "isSubSystemOf": [  
        "urn:ngsi-ld:System:ad240648-fa46-4518-82b1-4f4baa6d5de7",  
        "urn:ngsi-ld:System:3f9f73d3-72a5-4538-8869-c17a4b9df476",  
        "urn:ngsi-ld:System:ec373deb-a7d7-4b21-9e0e-9adffd16c74c"  
    ],  
    "hasManufacturer": "EvaporativeCooler Company Inc.",  
    "hasModel": "EvaporativeCooler 0.1.2",  
    "dateCreated": "2023-01-26T11:22:41Z",  
    "dateModified": "2023-01-26T09:06:31Z",  
    "source": "Import",  
    "name": "EvaporativeCooler",  
    "alternateName": "EvaporativeCooler type 2",  
    "description": "EvaporativeCooler of limited EvaporativeCooler types",  
    "dataProvider": "IFC file"  
}  
```  
</details>  
#### Raffreddatore evaporativo NGSI-v2 normalizzato Esempio  
Ecco un esempio di EvaporativeCooler in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:EvaporativeCooler:0a346c54-49ed-4047-a778-8db06579e512",  
  "type": "EvaporativeCooler",  
  "flowArrangement": {  
    "type": "Text",  
    "value": "Music"  
  },  
  "heatExchangeArea": {  
    "type": "Measurement",  
    "value": 0.7281726107323353  
  },  
  "operationTemperatureMax": {  
    "type": "Measurement",  
    "value": 0.6966196068493681  
  },  
  "operationTemperatureMin": {  
    "type": "Measurement",  
    "value": 0.2633641809598216  
  },  
  "waterRequirement": {  
    "type": "Measurement",  
    "value": 0.34619924829877713  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:BuildingSpace:09f6bb8b-789e-4410-a7d4-8927eea55d49"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:PhysicalObject:d4b8632d-7fad-4de8-901e-4efd140dbd98"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:0dd5150e-9430-493e-aba8-3843ca28c5e9"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:c101e62e-699a-4ac8-82c9-271f229e05ba"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:8dea165b-31d9-40ac-900e-eced972e318d"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "EvaporativeCooler Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "EvaporativeCooler 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T19:12:10.9508051+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T07:18:26.9847952+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "EvaporativeCooler"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "EvaporativeCooler type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "EvaporativeCooler of limited EvaporativeCooler types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### Raffreddatore evaporativo Valori chiave NGSI-LD Esempio  
Ecco un esempio di EvaporativeCooler in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:EvaporativeCooler:54b020f5-a24c-4e78-af69-ab730287a7fb",  
  "type": "EvaporativeCooler",  
  "flowArrangement": "Walk",  
  "heatExchangeArea": 0.0154798489699417,  
  "operationTemperatureMax": 0.8076614358257233,  
  "operationTemperatureMin": 0.05752519637609499,  
  "waterRequirement": 0.48344490145201957,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:b2cc75eb-3d85-44ce-b594-0c9c036f5f20",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:76419a51-5245-4bbe-b246-b2d4278d8c91",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:ad240648-fa46-4518-82b1-4f4baa6d5de7",  
    "urn:ngsi-ld:System:3f9f73d3-72a5-4538-8869-c17a4b9df476",  
    "urn:ngsi-ld:System:ec373deb-a7d7-4b21-9e0e-9adffd16c74c"  
  ],  
  "hasManufacturer": "EvaporativeCooler Company Inc.",  
  "hasModel": "EvaporativeCooler 0.1.2",  
  "dateCreated": "2023-01-26T11:22:41Z",  
  "dateModified": "2023-01-26T09:06:31Z",  
  "source": "Import",  
  "name": "EvaporativeCooler",  
  "alternateName": "EvaporativeCooler type 2",  
  "description": "EvaporativeCooler of limited EvaporativeCooler types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### Raffreddatore evaporativo NGSI-LD normalizzato Esempio  
Ecco un esempio di EvaporativeCooler in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:EvaporativeCooler:1eca9015-b483-4e0b-9f5c-eda9902c092d",  
  "type": "EvaporativeCooler",  
  "flowArrangement": {  
    "type": "Property",  
    "value": "COM"  
  },  
  "heatExchangeArea": {  
    "type": "Property",  
    "unitCode": "m2",  
    "observedAt": "2023-01-25T17:08:28Z",  
    "value": 0.7584250696633893  
  },  
  "operationTemperatureMax": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T18:14:01Z",  
    "value": 0.692516512025741  
  },  
  "operationTemperatureMin": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T20:42:27Z",  
    "value": 0.7188097385031748  
  },  
  "waterRequirement": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-26T08:51:16Z",  
    "value": 0.11534754798971114  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:73720b9e-732d-4566-91b8-7155f46be5ce"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:b0b36411-8e0e-460e-9e23-b05ab337d6b5"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:b0207455-4fc3-4b08-bdcf-9b605a3c4ca5"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:7ed66c88-e9d3-4b03-8cb8-a3a5cac78535"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:6c3a2470-0188-4b7f-b870-9cd359fd4111"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "EvaporativeCooler Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "EvaporativeCooler 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T00:32:51Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T12:51:38Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "EvaporativeCooler"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "EvaporativeCooler type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "EvaporativeCooler of limited EvaporativeCooler types"  
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
