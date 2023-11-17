<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entità: Serbatoio    
=================<!-- /10-Header -->    
<!-- 15-License -->    
[Licenza aperta](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Tank/LICENSE.md)    
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descrizione globale: **Un serbatoio è un recipiente o un contenitore in cui viene immagazzinato un fluido o un gas per un uso successivo.    
versione: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Elenco delle proprietà    
<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.    
- `accessType[string]`: Definisce i tipi di accesso (o copertura) a un serbatoio che possono essere specificati. Si noti che le coperture sono generalmente specificate per i serbatoi rettangolari. Per i serbatoi cilindrici, l'accesso avviene normalmente tramite un pozzetto.  - `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestita dal governo locale.      
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `effectiveCapacity[number]`: La capacità volumetrica totale effettiva o reale del serbatoio. Solitamente misurata in metri cubi (m3).B3  - `endShapeType[string]`: Definisce i tipi di forme di estremità che possono essere utilizzate per i serbatoi preformati. La convenzione per la lettura di questi valori enumerati è che per un cilindro verticale, il primo valore è la base e il secondo è la sommità per un cilindro orizzontale, l'ordine di lettura deve essere da sinistra a destra. Per un serbatoio sferico, si deve utilizzare il valore UNSET.B5  - `firstCurvatureRadius[number]`: FirstCurvatureRadius deve essere definito come il valore del raggio di curvatura della base o del lato sinistro. Di solito viene misurato in millimetri (mm).  - `hasManufacturer[string]`: Una relazione che identifica il produttore di un'entità (ad esempio, un dispositivo). Si prevede che il valore sia una stringa o una stringa con tag linguistico  - `hasModel[string]`: Una relazione che identifica il modello di un'entità (ad esempio, un dispositivo). Il valore dovrebbe essere una stringa o una stringa con tag lingua  - `id[*]`: Identificatore univoco dell'entità  - `isContainedInBuildingSpace[*]`: Entità utilizzata per definire gli spazi fisici dell'edificio. Uno spazio dell'edificio contiene dispositivi o oggetti dell'edificio. (Spazio edificio)  - `isContainedInPhysicalObject[*]`: Qualsiasi oggetto che abbia una regione spaziale propria.  (Definizione estratta dall'ontologia DUL) (PhysicalObject)  - `isSubSystemOf[array]`: Un riferimento a uno o più sistemi di cui l'oggetto fisico fa parte.  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento  - `nominalDepth[number]`: Profondità nominale del serbatoio. Nota: non è richiesta per i serbatoi cilindrici orizzontali. Solitamente misurata in millimetri (mm).  - `nominalLengthOrDiameter[number]`: La lunghezza nominale o, nel caso di un serbatoio cilindrico verticale, il diametro nominale del serbatoio. Di solito si misura in millimetri (mm).  - `nominalVolumetricCapacity[number]`: La capacità volumetrica totale nominale o di progetto del serbatoio. Di solito viene misurata in metri cubi (m3).  - `nominalWidthOrDiameter[number]`: La larghezza nominale o, nel caso di un serbatoio cilindrico orizzontale, il diametro nominale del serbatoio. Nota: non è richiesta per i serbatoi cilindrici verticali. Di solito si misura in millimetri (mm).  - `numberOfSections[number]`: Numero di sezioni utilizzate  - `operatingWeight[number]`: Peso operativo del serbatoio, compreso tutto il suo contenuto. Solitamente misurato in chilogrammi (kg) o grammi (g).  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `patternType[string]`: Definisce i tipi di modello (o forma di serbatoio) che possono essere specificati  - `secondCurvatureRadius[number]`: SecondCurvatureRadius deve essere definito come il valore del raggio di curvatura superiore o destro. Di solito viene misurato in millimetri (mm).  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `storageType[string]`: Definisce la categoria generale di materiale che si intende stoccare.  - `type[string]`: Deve essere uguale a `Tank`.  <!-- /30-PropertiesList -->    
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
## Esempi di payload    
#### Valori chiave del serbatoio NGSI-v2 Esempio    
Ecco un esempio di un serbatoio in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
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
#### Serbatoio NGSI-v2 normalizzato Esempio    
Ecco un esempio di un serbatoio in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.    
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
#### Valori chiave del serbatoio NGSI-LD Esempio    
Ecco un esempio di un serbatoio in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
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
#### Serbatoio NGSI-LD normalizzato Esempio    
Ecco un esempio di un serbatoio in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.    
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
