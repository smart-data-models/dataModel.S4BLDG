<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entità: AudioVisualAppliance    
============================<!-- /10-Header -->    
<!-- 15-License -->    
[Licenza aperta](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/AudioVisualAppliance/LICENSE.md)    
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descrizione globale: **Un apparecchio audiovisivo è un dispositivo che visualizza, cattura, trasmette o riceve audio o video.  Le apparecchiature audiovisive possono essere fisse o possono essere spostate da uno spazio all'altro. Possono richiedere un'alimentazione elettrica che può essere fornita da un circuito elettrico o da una batteria locale. Le apparecchiature audiovisive possono essere collegate a circuiti di dati, compresi i circuiti specializzati per scopi esclusivamente audiovisivi.**    
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
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `audioVolume[number]`: Indica i livelli discreti del volume audio e i corrispondenti offset di potenza sonora, se applicabili. I valori mancanti possono essere interpolati. Misurato in watt  - `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `hasManufacturer[string]`: Una relazione che identifica il produttore di un'entità (ad esempio, un dispositivo). Si prevede che il valore sia una stringa o una stringa con tag linguistico  - `hasModel[string]`: Una relazione che identifica il modello di un'entità (ad esempio, un dispositivo). Il valore dovrebbe essere una stringa o una stringa con tag lingua  - `id[*]`: Identificatore univoco dell'entità  - `isContainedInBuildingSpace[*]`: Entità utilizzata per definire gli spazi fisici dell'edificio. Uno spazio dell'edificio contiene dispositivi o oggetti dell'edificio. (Spazio edificio)  - `isContainedInPhysicalObject[*]`: Qualsiasi oggetto che abbia una regione spaziale propria.  (Definizione estratta dall'ontologia DUL) (PhysicalObject)  - `isSubSystemOf[array]`: Un riferimento a uno o più sistemi di cui l'oggetto fisico fa parte.  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `mediaSource[string]`: Indica le sorgenti multimediali e i nomi corrispondenti delle porte (DistributionPort con FlowDirection=SINK e PredefinedType=AUDIOVISUAL) o dei componenti audio/video aggregati (AudioVisualAppliance).  - `name[string]`: Il nome di questo elemento  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `type[string]`: Deve essere uguale a `AudioVisualAppliance`.  <!-- /30-PropertiesList -->    
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
AudioVisualAppliance:      
  description: 'An audio-visual appliance is a device that displays, captures, transmits, or receives audio or video.  Audio-visual appliances may be fixed in place or may be able to be moved from one space to another. They may require an electrical supply that may be supplied either by an electrical circuit or provided from a local battery source. Audio-visual appliances may be connected to data circuits including specialist circuits for audio visual purposes only.'      
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
    audioVolume:      
      description: 'Indicates discrete audio volume levels and corresponding sound power offsets, if applicable. Missing values may be interpolated. Measured in watts'      
      type: number      
      x-ngsi:      
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
    mediaSource:      
      description: Indicates media sources and corresponding names of ports (DistributionPort with FlowDirection=SINK and PredefinedType=AUDIOVISUAL) or aggregated audio/video components (AudioVisualAppliance)      
      type: string      
      x-ngsi:      
        type: Property      
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
    type:      
      description: It must be equal to `AudioVisualAppliance`      
      enum:      
        - AudioVisualAppliance      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:AudioVisualAppliance"      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/AudioVisualAppliance/LICENSE.md      
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/AudioVisualAppliance/schema.json      
  x-model-tags: SAREF AudioVisualAppliance      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Esempi di payload    
#### AudioVisualAppliance Valori chiave NGSI-v2 Esempio    
Ecco un esempio di AudioVisualAppliance in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AudioVisualAppliance:82b14ee9-5b80-497e-bad3-69a107039615",  
  "type": "AudioVisualAppliance",  
  "audioVolume": 0.7567380902263041,  
  "mediaSource": "HDD",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:5389ff9f-388f-4429-8118-01465a26104a",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:aaa7136b-d2f9-494d-ac6a-5b78ce2b423e",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:5c7ba113-3867-4a9a-831f-bab2225d9fa2",  
    "urn:ngsi-ld:System:d74ca22c-580c-4d13-9846-42fbbf1d68e4",  
    "urn:ngsi-ld:System:7655fb65-c336-4d20-8f6b-5c5e515eff24"  
  ],  
  "hasManufacturer": "AudioVisualAppliance Company Inc.",  
  "hasModel": "AudioVisualAppliance 0.1.2",  
  "dateCreated": "2023-01-25T16:14:55Z",  
  "dateModified": "2023-01-26T00:10:16Z",  
  "source": "Import",  
  "name": "AudioVisualAppliance",  
  "alternateName": "AudioVisualAppliance type 2",  
  "description": "AudioVisualAppliance of limited AudioVisualAppliance types",  
  "dataProvider": "IFC file"  
}  
```  
</details>    
#### AudioVisualAppliance NGSI-v2 normalizzato Esempio    
Ecco un esempio di AudioVisualAppliance in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AudioVisualAppliance:9fa87e19-45b4-4d9e-bde2-1a97fd680d44",  
  "type": "AudioVisualAppliance",  
  "audioVolume": {  
    "type": "Number",  
    "value": 0.7152710089989837  
  },  
  "mediaSource": {  
    "type": "Text",  
    "value": "deliver"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:BuildingSpace:395ad84f-d596-466e-95d5-eabc54236844"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:PhysicalObject:9034fa54-28a8-4537-82d0-4c500204f2ac"  
  },  
  "isSubSystemOf": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:System:acd641b3-a81b-4fbb-9435-3ac2910349f3",  
      "urn:ngsi-ld:System:2f600c38-4896-445a-8781-d52bffbbd8dc",  
      "urn:ngsi-ld:System:03fca7e3-0791-4fed-976c-8392d39e187d"  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "AudioVisualAppliance Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "AudioVisualAppliance 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T11:45:27.9326032+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T04:22:01.2237776+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "AudioVisualAppliance"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "AudioVisualAppliance type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "AudioVisualAppliance of limited AudioVisualAppliance types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>    
#### AudioVisualAppliance Valori-chiave NGSI-LD Esempio    
Ecco un esempio di AudioVisualAppliance in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AudioVisualAppliance:a41d1d73-322a-464e-880e-8f2f99f6deb7",  
  "type": "AudioVisualAppliance",  
  "audioVolume": 0.45106111153820727,  
  "mediaSource": "eco-centric",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:8c627932-e06a-4ae9-b789-0021e562a215",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:16c0c4e6-09aa-4086-98ca-5ef2f437274f",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:1729ff5f-82ab-4a44-9cd1-a4c90bf0b4d9",  
    "urn:ngsi-ld:System:0520a884-f15e-44ba-bcee-55ef83c76303",  
    "urn:ngsi-ld:System:a94cf276-f44e-4b67-a98d-de563723f919"  
  ],  
  "hasManufacturer": "AudioVisualAppliance Company Inc.",  
  "hasModel": "AudioVisualAppliance 0.1.2",  
  "dateCreated": "2023-01-25T19:10:42Z",  
  "dateModified": "2023-01-26T02:18:21Z",  
  "source": "Import",  
  "name": "AudioVisualAppliance",  
  "alternateName": "AudioVisualAppliance type 2",  
  "description": "AudioVisualAppliance of limited AudioVisualAppliance types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>    
#### AudioVisualAppliance Esempio normalizzato NGSI-LD    
Ecco un esempio di AudioVisualAppliance in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AudioVisualAppliance:5a3581a9-8282-4896-9b4d-fa504ab5b521",  
  "type": "AudioVisualAppliance",  
  "audioVolume": {  
    "type": "Property",  
    "unitCode": "watts",  
    "observedAt": "2023-01-26T03:27:08Z",  
    "value": 0.5554214508770069  
  },  
  "mediaSource": {  
    "type": "Property",  
    "value": "Cambridgeshire"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:d8d8ebe8-1ace-4416-bd78-27c7da946369"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:63dae1f5-8a50-4827-b54f-e2414f37e25b"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:78a298bd-06b7-463a-9b71-e7639da4a4cd"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:cc6fdf1e-6a7d-4105-9ecc-767efaf48d91"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:5ba5bb3a-f4c8-4070-9135-127d7bd968fe"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "AudioVisualAppliance Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "AudioVisualAppliance 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T18:02:34Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-25T21:12:54Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "AudioVisualAppliance"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "AudioVisualAppliance type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "AudioVisualAppliance of limited AudioVisualAppliance types"  
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
