<!-- 10-Header -->
  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entità: Recupero calore da aria ad aria  
=======================================
<!-- /10-Header -->
  
<!-- 15-License -->
  

[Licenza aperta](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/AirToAirHeatRecovery/LICENSE.md)  

[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->
  
<!-- 20-Description -->
  

Descrizione globale: **Un dispositivo di recupero di calore aria-aria impiega uno scambiatore di calore in controcorrente tra il flusso d'aria in entrata e quello in uscita. In genere viene utilizzato per trasferire il calore dall'aria più calda in una camera all'aria più fredda nella seconda camera (cioè, in genere viene utilizzato per recuperare il calore dall'aria condizionata che viene espulsa e dall'aria esterna che viene immessa in un edificio), con conseguente risparmio energetico grazie alla riduzione dei requisiti di riscaldamento (o raffreddamento)**.  

versione: 0.0.1  
<!-- /20-Description -->
  
<!-- 30-PropertiesList -->
  


## Elenco delle proprietà  


<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)
- `alternateName[string]`: Un nome alternativo per questa voce  
- `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)
- `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  
- `dateCreated[string]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  
- `dateModified[string]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  
- `description[string]`: Descrizione dell'articolo  
- `hasDefrost[boolean]`: Proprietà. Se lo scambiatore di calore ha o meno la funzione di sbrinamento.  
- `hasManufacturer[string]`: Proprietà. Una relazione che identifica il produttore di un'entità (ad esempio, un dispositivo). Il valore dovrebbe essere una stringa o una stringa con un tag di lingua.  
- `hasModel[string]`: Proprietà. Una relazione che identifica il modello di un'entità (ad esempio, un dispositivo). Il valore dovrebbe essere una stringa o una stringa con un tag di lingua.  
- `heatTransferTypeEnum[string]`: Proprietà. Tipo di trasferimento di calore tra i due flussi d'aria.  
- `id[*]`: Identificatore univoco dell'entità  
- `isContainedInBuildingSpace[*]`: Relazione. Un'entità utilizzata per definire gli spazi fisici dell'edificio. Uno spazio dell'edificio contiene dispositivi o oggetti dell'edificio. (Spazio edificio)  
- `isContainedInPhysicalObject[*]`: Relazione. Qualsiasi oggetto che abbia una regione spaziale appropriata.  (Definizione estratta dall'ontologia DUL) (PhysicalObject)  
- `isSubSystemOf[array]`: Relazione. Un riferimento a uno o più sistemi di cui questo Oggetto fisico fa parte.  
- `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  
- `name[string]`: Il nome di questo elemento.  
- `operationTemperatureMax[object]`: Proprietà. Intervallo di temperatura ambiente (aria, fluido) consentito per il funzionamento. Di solito si misura in gradi Kelvin (K).  
- `operationTemperatureMin[object]`: Proprietà. Intervallo di temperatura ambiente (aria, fluido) consentito per il funzionamento. Di solito si misura in gradi Kelvin (K).  
- `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  
- `primaryAirFlowRateMax[object]`: Proprietà. Flusso d'aria primario massimo erogabile. Di solito si misura in m3/s.  
- `primaryAirFlowRateMin[object]`: Proprietà. Flusso d'aria primario minimo che può essere erogato. Di solito si misura in m3/s.  
- `secondaryAirFlowRateMax[object]`: Proprietà. Flusso d'aria secondario massimo erogabile. Di solito si misura in Pascal (Pa, N/m2).  
- `secondaryAirFlowRateMin[object]`: Proprietà. Flusso d'aria secondario massimo erogabile. Di solito si misura in Pascal (Pa, N/m2).  
- `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  
- `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  
- `type[string]`: Proprietà. Deve essere uguale a `AirToAirHeatRecovery`.  
<!-- /30-PropertiesList -->
  
<!-- 35-RequiredProperties -->
  

Proprietà richieste  
- `id`  
- `type`  
<!-- /35-RequiredProperties -->
  
<!-- 40-RequiredProperties -->
  
<!-- /40-RequiredProperties -->
  
<!-- 50-DataModelHeader -->
  

## Modello di dati descrizione delle proprietà  

Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->
  
<!-- 60-ModelYaml -->
  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
AirToAirHeatRecovery:    
  description: 'An air-to-air heat recovery device employs a counter-flow heat exchanger between inbound and outbound air flow. It is typically used to transfer heat from warmer air in one chamber to cooler air in the second chamber (i.e., typically used to recover heat from the conditioned air being exhausted and the outside air being supplied to a building), resulting in energy savings from reduced heating (or cooling) requirements.'    
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
    hasDefrost:    
      description: Property. Whether the heat exchanger has defrost function or not.    
      type: boolean    
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
    heatTransferTypeEnum:    
      description: Property. Type of heat transfer between the two air streams.    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &airtoairheatrecovery_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      anyOf: *airtoairheatrecovery_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *airtoairheatrecovery_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *airtoairheatrecovery_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      description: 'Property. Allowable operation ambient (air, fluid) temperature range. Usually measured in degrees Kelvin (K).'    
      properties: &airtoairheatrecovery_-_properties_-_operationtemperaturemin_-_properties    
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
      type: object    
      x-ngsi:    
        type: Property    
    operationTemperatureMin:    
      description: 'Property. Allowable operation ambient (air, fluid) temperature range. Usually measured in degrees Kelvin (K).'    
      properties: *airtoairheatrecovery_-_properties_-_operationtemperaturemin_-_properties    
      type: object    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *airtoairheatrecovery_-_properties_-_iscontainedinbuildingspace_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    primaryAirFlowRateMax:    
      description: Property. Maximum primary airflow that can be delivered. Usually measured in m3/s.    
      properties: *airtoairheatrecovery_-_properties_-_operationtemperaturemin_-_properties    
      type: object    
      x-ngsi:    
        type: Property    
    primaryAirFlowRateMin:    
      description: Property. Minimum primary airflow that can be delivered. Usually measured in m3/s.    
      properties: *airtoairheatrecovery_-_properties_-_operationtemperaturemin_-_properties    
      type: object    
      x-ngsi:    
        type: Property    
    secondaryAirFlowRateMax:    
      description: 'Property. Maximum secondary airflow that can be delivered. Usually measured in Pascals (Pa, N/m2).'    
      properties: *airtoairheatrecovery_-_properties_-_operationtemperaturemin_-_properties    
      type: object    
      x-ngsi:    
        type: Property    
    secondaryAirFlowRateMin:    
      description: 'Property. Maximum secondary airflow that can be delivered. Usually measured in Pascals (Pa, N/m2).'    
      properties: *airtoairheatrecovery_-_properties_-_operationtemperaturemin_-_properties    
      type: object    
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
      description: Property. It must be equal to `AirToAirHeatRecovery`.    
      enum:    
        - AirToAirHeatRecovery    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:AirToAirHeatRecovery"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/AirToAirHeatRecovery/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/AirToAirHeatRecovery/schema.json    
  x-model-tags: SAREF AirToAirHeatRecovery    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->
  
<!-- 70-MiddleNotes -->
  
<!-- /70-MiddleNotes -->
  
<!-- 80-Examples -->
  

## Esempi di payload  

#### Valori chiave di AirToAirHeatRecovery NGSI-v2 Esempio  

Ecco un esempio di recupero di calore AirToAirHeatRecovery in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:AirToAirHeatRecovery:8c59d316-ed05-4b56-bec3-886379421239",  
  "type": "AirToAirHeatRecovery",  
  "hasDefrost": false,  
  "heatTransferTypeEnum": "24/7",  
  "operationTemperatureMax": {  
    "unitCode": "K",  
    "observedAt": "2023-01-26T04:36:47Z",  
    "value": 0.8198825347384565  
  },  
  "operationTemperatureMin": {  
    "unitCode": "K",  
    "observedAt": "2023-01-25T14:46:06Z",  
    "value": 0.505815040579818  
  },  
  "primaryAirFlowRateMax": {  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-25T20:09:42Z",  
    "value": 0.2511282384018223  
  },  
  "primaryAirFlowRateMin": {  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-25T23:44:23Z",  
    "value": 0.8540184208518826  
  },  
  "secondaryAirFlowRateMax": {  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-26T11:38:58Z",  
    "value": 0.913617698002923  
  },  
  "secondaryAirFlowRateMin": {  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-25T17:25:01Z",  
    "value": 0.17456040773539583  
  },  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:018e6821-b097-4029-9cbb-207ae7e5ddca",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:ad795f1c-0754-4877-acc2-2dcc3b337edd",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:c92bd8da-e37f-4f64-989b-6007925a053b",  
    "urn:ngsi-ld:System:5642f604-3a36-49c3-b178-3e7b99eca071",  
    "urn:ngsi-ld:System:2f04039b-ef4e-4d61-8232-e786a220b927"  
  ],  
  "hasManufacturer": "AirToAirHeatRecovery Company Inc.",  
  "hasModel": "AirToAirHeatRecovery 0.1.2",  
  "dateCreated": "2023-01-25T18:33:19Z",  
  "dateModified": "2023-01-25T17:11:08Z",  
  "source": "Import",  
  "name": "AirToAirHeatRecovery",  
  "alternateName": "AirToAirHeatRecovery type 2",  
  "description": "AirToAirHeatRecovery of limited AirToAirHeatRecovery types",  
  "dataProvider": "IFC file"  
}  
```  
</details>  

#### Recupero aria-aria-riscaldamento NGSI-v2 normalizzato Esempio  

Ecco un esempio di recupero di calore AirToAirHeatRecovery in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:AirToAirHeatRecovery:a732b90e-0296-47c9-ab0f-34f6de5edfb4",  
  "type": "AirToAirHeatRecovery",  
  "hasDefrost": {  
    "type": "Boolean",  
    "value": true  
  },  
  "heatTransferTypeEnum": {  
    "type": "Text",  
    "value": "Future"  
  },  
  "operationTemperatureMax": {  
    "type": "Measurement",  
    "value": {  
      "unitCode": "K",  
      "observedAt": "2023-01-26T07:59:34Z",  
      "value": 0.9053685058368695  
    }  
  },  
  "operationTemperatureMin": {  
    "type": "Measurement",  
    "value": {  
      "unitCode": "K",  
      "observedAt": "2023-01-26T08:16:23Z",  
      "value": 0.0225751895192714  
    }  
  },  
  "primaryAirFlowRateMax": {  
    "type": "Measurement",  
    "value": {  
      "unitCode": "m3/s",  
      "observedAt": "2023-01-25T19:33:24Z",  
      "value": 0.6828734611896666  
    }  
  },  
  "primaryAirFlowRateMin": {  
    "type": "Measurement",  
    "value": {  
      "unitCode": "m3/s",  
      "observedAt": "2023-01-25T22:42:55Z",  
      "value": 0.48874342661652126  
    }  
  },  
  "secondaryAirFlowRateMax": {  
    "type": "Measurement",  
    "value": {  
      "unitCode": "N/m2",  
      "observedAt": "2023-01-26T11:44:17Z",  
      "value": 0.36804021603434756  
    }  
  },  
  "secondaryAirFlowRateMin": {  
    "type": "Measurement",  
    "value": {  
      "unitCode": "N/m2",  
      "observedAt": "2023-01-26T01:16:14Z",  
      "value": 0.28401066550404996  
    }  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:BuildingSpace:2058c38a-eb2e-4001-af3f-9a93effd41ac"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:PhysicalObject:ea1b1b2c-cb04-429d-bf2c-ca99e7f3f005"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:System:123d10ff-2c3a-40f4-9fd0-07851a7d7a3c"  
      },  
      {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:System:90a762d4-7eed-4d5a-8a0d-a4676773917f"  
      },  
      {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:System:b9899a7a-dc77-43a1-a0df-5a4134af3004"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "AirToAirHeatRecovery Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "AirToAirHeatRecovery 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T00:34:42.9211606+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T13:58:25.8715515+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "AirToAirHeatRecovery"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "AirToAirHeatRecovery type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "AirToAirHeatRecovery of limited AirToAirHeatRecovery types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  

#### Recupero di calore AirToAirHeatRecovery Valori chiave NGSI-LD Esempio  

Ecco un esempio di recupero di calore AirToAirHeatRecovery in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:AirToAirHeatRecovery:8c59d316-ed05-4b56-bec3-886379421239",  
  "type": "AirToAirHeatRecovery",  
  "hasDefrost": false,  
  "heatTransferTypeEnum": "24/7",  
  "operationTemperatureMax": {  
    "unitCode": "K",  
    "observedAt": "2023-01-26T04:36:47Z",  
    "value": 0.8198825347384565  
  },  
  "operationTemperatureMin": {  
    "unitCode": "K",  
    "observedAt": "2023-01-25T14:46:06Z",  
    "value": 0.505815040579818  
  },  
  "primaryAirFlowRateMax": {  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-25T20:09:42Z",  
    "value": 0.2511282384018223  
  },  
  "primaryAirFlowRateMin": {  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-25T23:44:23Z",  
    "value": 0.8540184208518826  
  },  
  "secondaryAirFlowRateMax": {  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-26T11:38:58Z",  
    "value": 0.913617698002923  
  },  
  "secondaryAirFlowRateMin": {  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-25T17:25:01Z",  
    "value": 0.17456040773539583  
  },  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:018e6821-b097-4029-9cbb-207ae7e5ddca",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:ad795f1c-0754-4877-acc2-2dcc3b337edd",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:c92bd8da-e37f-4f64-989b-6007925a053b",  
    "urn:ngsi-ld:System:5642f604-3a36-49c3-b178-3e7b99eca071",  
    "urn:ngsi-ld:System:2f04039b-ef4e-4d61-8232-e786a220b927"  
  ],  
  "hasManufacturer": "AirToAirHeatRecovery Company Inc.",  
  "hasModel": "AirToAirHeatRecovery 0.1.2",  
  "dateCreated": "2023-01-25T18:33:19Z",  
  "dateModified": "2023-01-25T17:11:08Z",  
  "source": "Import",  
  "name": "AirToAirHeatRecovery",  
  "alternateName": "AirToAirHeatRecovery type 2",  
  "description": "AirToAirHeatRecovery of limited AirToAirHeatRecovery types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  

#### Recupero di calore da aria ad aria NGSI-LD normalizzato Esempio  

Ecco un esempio di recupero di calore AirToAirHeatRecovery in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:AirToAirHeatRecovery:a8cd6aa9-dd5f-48bf-ba9f-3db11843b050",  
  "type": "AirToAirHeatRecovery",  
  "hasDefrost": {  
    "type": "Property",  
    "value": false  
  },  
  "heatTransferTypeEnum": {  
    "type": "Property",  
    "value": "Street"  
  },  
  "operationTemperatureMax": {  
    "type": "Property",  
    "value": {  
      "unitCode": "K",  
      "observedAt": "2023-01-26T02:03:09Z",  
      "value": 0.09206773488147657  
    }  
  },  
  "operationTemperatureMin": {  
    "type": "Property",  
    "value": {  
      "unitCode": "K",  
      "observedAt": "2023-01-26T09:23:23Z",  
      "value": 0.04773015112848933  
    }  
  },  
  "primaryAirFlowRateMax": {  
    "type": "Property",  
    "value": {  
      "unitCode": "m3/s",  
      "observedAt": "2023-01-25T15:19:05Z",  
      "value": 0.04143347387591234  
    }  
  },  
  "primaryAirFlowRateMin": {  
    "type": "Property",  
    "value": {  
      "unitCode": "m3/s",  
      "observedAt": "2023-01-26T00:05:48Z",  
      "value": 0.9113949488212527  
    }  
  },  
  "secondaryAirFlowRateMax": {  
    "type": "Property",  
    "value": {  
      "unitCode": "N/m2",  
      "observedAt": "2023-01-26T02:57:23Z",  
      "value": 0.391335331160202  
    }  
  },  
  "secondaryAirFlowRateMin": {  
    "type": "Property",  
    "value": {  
      "unitCode": "N/m2",  
      "observedAt": "2023-01-26T08:54:29Z",  
      "value": 0.9115616360325159  
    }  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:f9f09bbc-27ef-4bd0-991f-6dd8720f5e7b"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:79a8986d-8526-4608-b216-ea4eb2d147ac"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:fae709e8-6311-4179-acfd-7b79e92d095c"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:4c06efa1-0d47-4a8a-a38c-d0783a106972"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:a3120479-fd3a-4a34-915c-418000e05d2b"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "AirToAirHeatRecovery Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "AirToAirHeatRecovery 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-25T23:15:35Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-26T07:30:02Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "AirToAirHeatRecovery"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "AirToAirHeatRecovery type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "AirToAirHeatRecovery of limited AirToAirHeatRecovery types"  
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
  
