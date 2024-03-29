<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entità: Refrigeratore    
=====================<!-- /10-Header -->    
<!-- 15-License -->    
[Licenza aperta](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Chiller/LICENSE.md)    
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descrizione globale: **Un refrigeratore è un dispositivo utilizzato per rimuovere il calore da un liquido attraverso un ciclo di refrigerazione a compressione di vapore o ad assorbimento per raffreddare un fluido, tipicamente acqua o una miscela di acqua e glicole. Il fluido refrigerato viene quindi utilizzato per raffreddare e deumidificare l'aria in un edificio.**    
versione: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Elenco delle proprietà    
<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.    
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestita dal governo locale.      
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `hasManufacturer[string]`: Una relazione che identifica il produttore di un'entità (ad esempio, un dispositivo). Si prevede che il valore sia una stringa o una stringa con tag linguistico  - `hasModel[string]`: Una relazione che identifica il modello di un'entità (ad esempio, un dispositivo). Il valore dovrebbe essere una stringa o una stringa con tag lingua  - `id[*]`: Identificatore univoco dell'entità  - `isContainedInBuildingSpace[*]`: Entità utilizzata per definire gli spazi fisici dell'edificio. Uno spazio dell'edificio contiene dispositivi o oggetti dell'edificio. (Spazio edificio)  - `isContainedInPhysicalObject[*]`: Qualsiasi oggetto che abbia una regione spaziale propria.  (Definizione estratta dall'ontologia DUL) (PhysicalObject)  - `isSubSystemOf[array]`: Un riferimento a uno o più sistemi di cui l'oggetto fisico fa parte.  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento  - `nominalCapacity[number]`: Capacità nominale. Solitamente misurata in Watt (W, J/s).  - `nominalCondensingTemperature[number]`: Temperatura di condensazione del refrigeratore. Solitamente misurata in gradi Kelvin (K).  - `nominalEfficiency[number]`: Efficienza nominale del refrigeratore in condizioni nominali.  - `nominalEvaporatingTemmperature[number]`: Temperatura di evaporazione del refrigeratore, solitamente misurata in gradi Kelvin (K).  - `nominalHeatRejectionRate[number]`: Somma dell'effetto di refrigerazione e dell'equivalente termico della potenza assorbita dal compressore. Solitamente misurato in Watt (W, J/s).  - `nominalPowerConsumption[number]`: Consumo totale nominale di energia. Solitamente misurato in Watt (W, J/s).  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `type[string]`: Deve essere uguale a `Chiller`.  <!-- /30-PropertiesList -->    
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
Chiller:      
  description: 'A chiller is a device used to remove heat from a liquid via a vapor-compression or absorption refrigeration cycle to cool a fluid, typically water or a mixture of water and glycol. The chilled fluid is then used to cool and dehumidify air in a building.'      
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
    nominalCapacity:      
      description: 'Nominal capacity. Usually measured in Watts (W, J/s)'      
      type: number      
      x-ngsi:      
        type: Property      
    nominalCondensingTemperature:      
      description: Chiller condensing temperature. Usually measured in degrees Kelvin (K)      
      type: number      
      x-ngsi:      
        type: Property      
    nominalEfficiency:      
      description: 'Nominal chiller efficiency under nominal conditions. '      
      type: number      
      x-ngsi:      
        type: Property      
    nominalEvaporatingTemmperature:      
      description: Chiller evaporating temperature.Usually measured in degrees Kelvin (K)      
      type: number      
      x-ngsi:      
        type: Property      
    nominalHeatRejectionRate:      
      description: 'Sum of the refrigeration effect and the heat equivalent of the power input to the compressor. Usually measured in Watts (W, J/s)'      
      type: number      
      x-ngsi:      
        type: Property      
    nominalPowerConsumption:      
      description: 'Nominal total power consumption. Usually measured in Watts (W, J/s)'      
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
    type:      
      description: It must be equal to `Chiller`      
      enum:      
        - Chiller      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Chiller"      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Chiller/LICENSE.md      
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Chiller/schema.json      
  x-model-tags: SAREF Chiller      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Esempi di payload    
#### Chiller NGSI-v2 valori-chiave Esempio    
Ecco un esempio di Chiller in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Chiller:ba7497f8-4fd6-4ec0-8dd8-00ed95bd51fc",  
  "type": "Chiller",  
  "nominalCapacity": 0.09475720530736764,  
  "nominalCondensingTemperature": 0.20516492572831713,  
  "nominalEfficiency": 0.9467840743079621,  
  "nominalEvaporatingTemmperature": 0.9391249200926837,  
  "nominalHeatRejectionRate": 0.6781215261931568,  
  "nominalPowerConsumption": 0.7316060776442138,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:53b1b818-f2bf-4bbf-9ba6-e3d431a11173",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:5d06c867-dc48-4267-b194-60642a22f0af",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:8c79471f-dea7-474b-985e-e5072ea36369",  
    "urn:ngsi-ld:System:e2e46075-3c25-46c4-80b4-da4b79faef4e",  
    "urn:ngsi-ld:System:9eea4295-8a6c-4efb-833e-1d6941c97754"  
  ],  
  "hasManufacturer": "Chiller Company Inc.",  
  "hasModel": "Chiller 0.1.2",  
  "dateCreated": "2023-01-25T19:42:28Z",  
  "dateModified": "2023-01-25T19:48:46Z",  
  "source": "Import",  
  "name": "Chiller",  
  "alternateName": "Chiller type 2",  
  "description": "Chiller of limited Chiller types",  
  "dataProvider": "IFC file"  
}  
```  
</details>    
#### Chiller NGSI-v2 normalizzato Esempio    
Ecco un esempio di un Chiller in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Chiller:fbbc813e-29ac-4462-9996-5a3d73d1ce98",  
  "type": "Chiller",  
  "nominalCapacity": {  
    "type": "Number",  
    "value": 0.0740819212946876  
  },  
  "nominalCondensingTemperature": {  
    "type": "Number",  
    "value": 0.5010709006481944  
  },  
  "nominalEfficiency": {  
    "type": "Number",  
    "value": 0.05897827362979524  
  },  
  "nominalEvaporatingTemmperature": {  
    "type": "Number",  
    "value": 0.0556993113916634  
  },  
  "nominalHeatRejectionRate": {  
    "type": "Number",  
    "value": 0.756236294011522  
  },  
  "nominalPowerConsumption": {  
    "type": "Number",  
    "value": 0.8474333854169832  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:BuildingSpace:0a2b8ec3-70d9-483f-8df0-dc7bbfa27d29"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:PhysicalObject:18da6c4b-5520-4b19-b3ee-2a91993c19de"  
  },  
  "isSubSystemOf": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:System:b48e7b0c-7d5e-4087-89d4-c40a87ae78be",  
      "urn:ngsi-ld:System:d9a20a72-def1-447e-ba8a-f601965fc681",  
      "urn:ngsi-ld:System:474efe4e-7d74-4985-ac14-792dcb6b9d76"  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Chiller Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Chiller 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T05:24:59.314133+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T04:27:01.3524196+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Chiller"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Chiller type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Chiller of limited Chiller types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>    
#### Chiller NGSI-LD valori-chiave Esempio    
Ecco un esempio di Chiller in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Chiller:ba7497f8-4fd6-4ec0-8dd8-00ed95bd51fc",  
  "type": "Chiller",  
  "nominalCapacity": 0.09475720530736764,  
  "nominalCondensingTemperature": 0.20516492572831713,  
  "nominalEfficiency": 0.9467840743079621,  
  "nominalEvaporatingTemmperature": 0.9391249200926837,  
  "nominalHeatRejectionRate": 0.6781215261931568,  
  "nominalPowerConsumption": 0.7316060776442138,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:53b1b818-f2bf-4bbf-9ba6-e3d431a11173",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:5d06c867-dc48-4267-b194-60642a22f0af",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:8c79471f-dea7-474b-985e-e5072ea36369",  
    "urn:ngsi-ld:System:e2e46075-3c25-46c4-80b4-da4b79faef4e",  
    "urn:ngsi-ld:System:9eea4295-8a6c-4efb-833e-1d6941c97754"  
  ],  
  "hasManufacturer": "Chiller Company Inc.",  
  "hasModel": "Chiller 0.1.2",  
  "dateCreated": "2023-01-25T19:42:28Z",  
  "dateModified": "2023-01-25T19:48:46Z",  
  "source": "Import",  
  "name": "Chiller",  
  "alternateName": "Chiller type 2",  
  "description": "Chiller of limited Chiller types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>    
#### Refrigeratore NGSI-LD normalizzato Esempio    
Ecco un esempio di un Chiller in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Chiller:1a99f350-0e1d-4466-8579-912c1f3c9b8f",  
  "type": "Chiller",  
  "nominalCapacity": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-26T09:47:03Z",  
    "value": 0.22554187711659102  
  },  
  "nominalCondensingTemperature": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T14:43:34Z",  
    "value": 0.1507511254687508  
  },  
  "nominalEfficiency": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T03:46:03Z",  
    "value": 0.3248755291390478  
  },  
  "nominalEvaporatingTemmperature": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T02:17:21Z",  
    "value": 0.13438649176620343  
  },  
  "nominalHeatRejectionRate": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-26T06:04:17Z",  
    "value": 0.0564283340666325  
  },  
  "nominalPowerConsumption": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-26T10:26:02Z",  
    "value": 0.8546772522263915  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:d78af157-a55d-46b9-8c56-d6c0eda32745"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:4748763d-3b35-487c-a6ad-3a9dfa510820"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:29fc2747-3753-44b5-8d88-3ae91cd4bc89"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:7a9aa253-a2eb-42ce-aeee-6130d158d18f"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:72503e97-5805-42a7-a24b-891925d2a999"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Chiller Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Chiller 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T10:57:45Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T04:43:33Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Chiller"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Chiller type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Chiller of limited Chiller types"  
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
