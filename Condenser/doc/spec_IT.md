<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entità: Condensatore    
====================<!-- /10-Header -->    
<!-- 15-License -->    
[Licenza aperta](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Condenser/LICENSE.md)    
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descrizione globale: **Un condensatore è un dispositivo che viene utilizzato per dissipare il calore, in genere condensando una sostanza come un refrigerante dallo stato gassoso a quello liquido.**    
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
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `externalSurfaceArea[number]`: Superficie esterna (sia primaria che secondaria). Solitamente misurata in metri quadrati (m2).  - `hasManufacturer[string]`: Una relazione che identifica il produttore di un'entità (ad esempio, un dispositivo). Si prevede che il valore sia una stringa o una stringa con tag linguistico  - `hasModel[string]`: Una relazione che identifica il modello di un'entità (ad esempio, un dispositivo). Il valore dovrebbe essere una stringa o una stringa con tag lingua  - `id[*]`: Identificatore univoco dell'entità  - `internalRefrigerantVolume[number]`: Volume interno dell'evaporatore (lato refrigerante). Solitamente misurato in metri cubi (m3).  - `internalSurfaceArea[number]`: Superficie interna. Solitamente misurata in metri quadrati (m2).  - `internalWaterVolume[number]`: Volume interno dell'evaporatore (lato acqua). Solitamente misurato in metri cubi (m3).  - `isContainedInBuildingSpace[*]`: Entità utilizzata per definire gli spazi fisici dell'edificio. Uno spazio dell'edificio contiene dispositivi o oggetti dell'edificio. (Spazio edificio)  - `isContainedInPhysicalObject[*]`: Qualsiasi oggetto che abbia una regione spaziale propria.  (Definizione estratta dall'ontologia DUL) (PhysicalObject)  - `isSubSystemOf[array]`: Un riferimento a uno o più sistemi di cui l'oggetto fisico fa parte.  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento  - `nominalHeatTransferArea[number]`: Superficie nominale di trasferimento del calore associata al coefficiente nominale di trasferimento del calore complessivo. Di solito viene misurata in metri quadrati (m2).  - `nominalHeatTransferCoefficient[number]`: Coefficiente nominale di trasferimento del calore complessivo associato all'area nominale di trasferimento del calore. Solitamente misurato in Watt/m2 Kelvin  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `refrigerantClass[string]`: Classe di refrigerante utilizzata dal compressore. CFC: Clorofluorocarburi. HCFC: Idroclorofluorocarburi. HFC: Idrofluorocarburi.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `type[string]`: Deve essere uguale a "Condensatore".  <!-- /30-PropertiesList -->    
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
Condenser:      
  description: 'A condenser is a device that is used to dissipate heat, typically by condensing a substance such as a refrigerant from its gaseous to its liquid state.'      
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
    externalSurfaceArea:      
      description: External surface area (both primary and secondary area). Usually measured in square metre (m2)      
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
    internalRefrigerantVolume:      
      description: Internal volume of evaporator (refrigerant side). Usually measured in cubic metre (m3)      
      type: number      
      x-ngsi:      
        type: Property      
    internalSurfaceArea:      
      description: Internal surface area. Usually measured in square metre (m2)      
      type: number      
      x-ngsi:      
        type: Property      
    internalWaterVolume:      
      description: Internal volume of evaporator (water side). Usually measured in cubic metre (m3)      
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
    nominalHeatTransferArea:      
      description: Nominal heat transfer surface area associated with nominal overall heat transfer coefficient. Usually measured in square metre (m2)      
      type: number      
      x-ngsi:      
        type: Property      
    nominalHeatTransferCoefficient:      
      description: Nominal overall heat transfer coefficient associated with nominal heat transfer area. Usually measured in Watts/m2 Kelvin      
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
    refrigerantClass:      
      description: 'Refrigerant class used by the compressor. CFC: Chlorofluorocarbons. HCFC: Hydrochlorofluorocarbons. HFC: Hydrofluorocarbons'      
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    type:      
      description: It must be equal to `Condenser`      
      enum:      
        - Condenser      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Condenser"      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Condenser/LICENSE.md      
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Condenser/schema.json      
  x-model-tags: SAREF Condenser      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Esempi di payload    
#### Condensatore NGSI-v2 valori-chiave Esempio    
Ecco un esempio di Condensatore in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Condenser:2adcb166-23ce-4061-8062-952d5f2402b9",  
  "type": "Condenser",  
  "externalSurfaceArea": 0.18804655027013273,  
  "internalRefrigerantVolume": 0.1588694072031649,  
  "internalSurfaceArea": 0.884829655411807,  
  "internalWaterVolume": 0.7576300292464242,  
  "nominalHeatTransferArea": 0.04220384603580274,  
  "nominalHeatTransferCoefficient": 0.4901767947128819,  
  "refrigerantClass": "Barbados",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:7ba37c8a-b348-4fc5-8191-22dbe255c23e",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:f9999243-09ea-40b2-892a-63bfd9062a09",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:374a6c1e-348f-46a2-824d-616554f66351",  
    "urn:ngsi-ld:System:0bd6a865-18bc-40a2-b1cf-64af77762cee",  
    "urn:ngsi-ld:System:e8c3da85-a230-40e1-832c-e03b342a1160"  
  ],  
  "hasManufacturer": "Condenser Company Inc.",  
  "hasModel": "Condenser 0.1.2",  
  "dateCreated": "2023-01-25T15:55:59Z",  
  "dateModified": "2023-01-26T06:49:28Z",  
  "source": "Import",  
  "name": "Condenser",  
  "alternateName": "Condenser type 2",  
  "description": "Condenser of limited Condenser types",  
  "dataProvider": "IFC file"  
}  
```  
</details>    
#### Condensatore NGSI-v2 normalizzato Esempio    
Ecco un esempio di Condensatore in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Condenser:e22782fc-5392-4dd2-b891-29b5fbf683cd",  
  "type": "Condenser",  
  "externalSurfaceArea": {  
    "type": "Number",  
    "value": 0.1255332761606085  
  },  
  "internalRefrigerantVolume": {  
    "type": "Number",  
    "value": 0.5305579766612258  
  },  
  "internalSurfaceArea": {  
    "type": "Number",  
    "value": 0.7094627719374283  
  },  
  "internalWaterVolume": {  
    "type": "Number",  
    "value": 0.3123303218703414  
  },  
  "nominalHeatTransferArea": {  
    "type": "Number",  
    "value": 0.4444793909507544  
  },  
  "nominalHeatTransferCoefficient": {  
    "type": "Number",  
    "value": 0.6428769642448905  
  },  
  "refrigerantClass": {  
    "type": "Text",  
    "value": "Ergonomic Fresh Pants"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:BuildingSpace:ae10b0d7-9929-45cc-bf0c-3e3ab5380c1a"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:PhysicalObject:a3e1362f-7a17-46e9-a997-fd763290b5a2"  
  },  
  "isSubSystemOf": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:System:47267553-d21a-42f8-b1b9-b24ec529e8ad",  
      "urn:ngsi-ld:System:878dd196-c9af-43d7-8d36-344fa19ca56f",  
      "urn:ngsi-ld:System:366cc386-314f-4591-9f3f-4099890c74e7"  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Condenser Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Condenser 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T23:40:11.0211053+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T22:43:21.3342982+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Condenser"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Condenser type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Condenser of limited Condenser types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>    
#### Condensatore NGSI-LD valori chiave Esempio    
Ecco un esempio di Condensatore in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Condenser:2adcb166-23ce-4061-8062-952d5f2402b9",  
  "type": "Condenser",  
  "externalSurfaceArea": 0.18804655027013273,  
  "internalRefrigerantVolume": 0.1588694072031649,  
  "internalSurfaceArea": 0.884829655411807,  
  "internalWaterVolume": 0.7576300292464242,  
  "nominalHeatTransferArea": 0.04220384603580274,  
  "nominalHeatTransferCoefficient": 0.4901767947128819,  
  "refrigerantClass": "Barbados",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:7ba37c8a-b348-4fc5-8191-22dbe255c23e",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:f9999243-09ea-40b2-892a-63bfd9062a09",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:374a6c1e-348f-46a2-824d-616554f66351",  
    "urn:ngsi-ld:System:0bd6a865-18bc-40a2-b1cf-64af77762cee",  
    "urn:ngsi-ld:System:e8c3da85-a230-40e1-832c-e03b342a1160"  
  ],  
  "hasManufacturer": "Condenser Company Inc.",  
  "hasModel": "Condenser 0.1.2",  
  "dateCreated": "2023-01-25T15:55:59Z",  
  "dateModified": "2023-01-26T06:49:28Z",  
  "source": "Import",  
  "name": "Condenser",  
  "alternateName": "Condenser type 2",  
  "description": "Condenser of limited Condenser types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>    
#### Condensatore NGSI-LD normalizzato Esempio    
Ecco un esempio di Condensatore in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Condenser:290f1265-1ded-4706-b549-43d7ddcaa239",  
  "type": "Condenser",  
  "externalSurfaceArea": {  
    "type": "Property",  
    "unitCode": "m2",  
    "observedAt": "2023-01-26T11:04:44Z",  
    "value": 0.3471102075551651  
  },  
  "internalRefrigerantVolume": {  
    "type": "Property",  
    "unitCode": "m3",  
    "observedAt": "2023-01-26T10:30:09Z",  
    "value": 0.696994206179287  
  },  
  "internalSurfaceArea": {  
    "type": "Property",  
    "unitCode": "m2",  
    "observedAt": "2023-01-25T14:42:31Z",  
    "value": 0.7522617883905902  
  },  
  "internalWaterVolume": {  
    "type": "Property",  
    "unitCode": "m3",  
    "observedAt": "2023-01-26T09:25:42Z",  
    "value": 0.5807649609435256  
  },  
  "nominalHeatTransferArea": {  
    "type": "Property",  
    "unitCode": "m2",  
    "observedAt": "2023-01-26T05:15:12Z",  
    "value": 0.6105994546410142  
  },  
  "nominalHeatTransferCoefficient": {  
    "type": "Property",  
    "unitCode": "Kelvin",  
    "observedAt": "2023-01-25T14:28:56Z",  
    "value": 0.17023310849677553  
  },  
  "refrigerantClass": {  
    "type": "Property",  
    "value": "Generic Metal Pants"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:b7d758c3-cd93-4ce4-a414-28e5a714b67c"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:9d98233b-6df5-418e-b43c-5f98c921296f"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:6ba8c28a-2ebf-4a11-ba34-b7d778896bf9"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:3f480247-b6e3-4cc3-89e1-5c1f88507e48"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:645beb56-0f95-4b35-a0ed-56d848e575f1"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Condenser Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Condenser 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T22:14:26Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T02:56:43Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Condenser"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Condenser type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Condenser of limited Condenser types"  
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
