<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: Torre di raffreddamento  
===============================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/CoolingTower/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Una torre di raffreddamento è un dispositivo che respinge il calore nell'aria ambiente facendo circolare un fluido, come l'acqua, per ridurne la temperatura attraverso una parziale evaporazione.**  
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
- `alternateName[string]`: Un nome alternativo per questa voce  - `ambientDesignDryBulbTemperature[number]`: Temperatura di bulbo secco ambientale di progetto utilizzata per la selezione della torre di raffreddamento. Solitamente misurata in gradi Kelvin (K).  - `ambientDesignWetBulbTemperature[number]`: Temperatura ambiente di progetto a bulbo umido utilizzata per la selezione della torre di raffreddamento. Solitamente misurata in gradi Kelvin (K).  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `basinReserveVolume[number]`: Volume compreso tra i livelli di esercizio e di traboccamento nel bacino della torre di raffreddamento. Solitamente misurato in metri cubi (m3).  - `capacityControl[string]`: Ciclo della ventola: Il ventilatore viene acceso e spento ciclicamente per controllare il funzionamento. TwoSpeedFan: la ventola viene commutata tra bassa e alta velocità per controllare il funzionamento. Ventola a velocità variabile: la velocità della ventola viene variata per controllare il funzionamento. Controllo degli smorzatori: Gli smorzatori modulano il flusso d'aria per controllare il funzionamento. Valvola di bypassControllo: La valvola di bypass modula il flusso dell'acqua per controllare il funzionamento. Pompe serie multiple: Attiva/disattiva le pompe a serie multipla per controllare il funzionamento. Pompa a due velocità: Commutazione tra alta e bassa velocità della pompa per controllare il funzionamento. Pompa a velocità variabile: varia la velocità della pompa per controllare il funzionamento.  - `circuitType[string]`: Circuito aperto: Espone l'acqua direttamente all'atmosfera di raffreddamento. Circuito chiuso: Il fluido è separato dall'atmosfera da uno scambiatore di calore. Umido: Il flusso d'aria o la superficie di scambio termico sono raffreddati per evaporazione. Secco: Nessuna evaporazione nel flusso d'aria. Secco-umido: Una combinazione di torre a secco e torre a umido.  - `controlStrategy[string]`: FixedExitingWaterTemp: la capacità è controllata per mantenere una temperatura fissa dell'acqua in uscita. WetBulbTempReset: Il set-point viene reimpostato in base alla temperatura del bulbo umido.  - `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `flowArrangement[string]`: Controflusso: il flusso d'aria e d'acqua entrano in direzioni diverse. Flusso incrociato: il flusso d'aria e d'acqua sono perpendicolari. Flusso parallelo: il flusso d'aria e d'acqua entrano nelle stesse direzioni.  - `hasManufacturer[string]`: Una relazione che identifica il produttore di un'entità (ad esempio, un dispositivo). Si prevede che il valore sia una stringa o una stringa con tag linguistico  - `hasModel[string]`: Una relazione che identifica il modello di un'entità (ad esempio, un dispositivo). Il valore dovrebbe essere una stringa o una stringa con tag lingua  - `id[*]`: Identificatore univoco dell'entità  - `isContainedInBuildingSpace[*]`: Entità utilizzata per definire gli spazi fisici dell'edificio. Uno spazio dell'edificio contiene dispositivi o oggetti dell'edificio. (Spazio edificio)  - `isContainedInPhysicalObject[*]`: Qualsiasi oggetto che abbia una regione spaziale propria.  (Definizione estratta dall'ontologia DUL) (PhysicalObject)  - `isSubSystemOf[array]`: Un riferimento a uno o più sistemi di cui l'oggetto fisico fa parte.  - `liftElevationDifference[number]`: Differenza di quota tra il pozzetto della torre di raffreddamento e la parte superiore della torre. Solitamente misurata in millimetri (mm).  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento  - `nominalCapacity[number]`: Capacità nominale. Solitamente misurata in Watt (W, J/s).  - `numberOfCells[number]`: Numero di celle in un'unità di torre di raffreddamento  - `operationTemperatureMax[number]`: Intervallo di temperatura ambiente (aria, fluido) consentito per il funzionamento. Solitamente misurata in gradi Kelvin (K).  - `operationTemperatureMin[number]`: Intervallo di temperatura ambiente (aria, fluido) consentito per il funzionamento. Solitamente misurata in gradi Kelvin (K).  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `sprayType[string]`: Spruzzato: L'acqua viene spruzzata nel flusso d'aria. SplashTypeFill: l'acqua scorre a cascata su file successive di barre paraspruzzi. FilmTypeFill: l'acqua scorre in uno strato sottile su fogli strettamente distanziati.  - `type[string]`: Deve essere uguale a `CoolingTower`.  - `waterRequirement[number]`: Fabbisogno di acqua di reintegro. Solitamente misurato in m3/s  <!-- /30-PropertiesList -->  
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
CoolingTower:    
  description: A cooling tower is a device which rejects heat to ambient air by circulating a fluid such as water through it to reduce its temperature by partial evaporation.    
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
    ambientDesignDryBulbTemperature:    
      description: Ambient design dry bulb temperature used for selecting the cooling tower. Usually measured in degrees Kelvin (K)    
      type: number    
      x-ngsi:    
        type: Property    
    ambientDesignWetBulbTemperature:    
      description: Ambient design wet bulb temperature used for selecting the cooling tower. Usually measured in degrees Kelvin (K)    
      type: number    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    basinReserveVolume:    
      description: Volume between operating and overflow levels in cooling tower basin. Usually measured in cubic metre (m3)    
      type: number    
      x-ngsi:    
        type: Property    
    capacityControl:    
      description: 'FanCycling: Fan is cycled on and off to control duty. TwoSpeedFan: Fan is switched between low and high speed to control duty. VariableSpeedFan: Fan speed is varied to control duty. DampersControl: Dampers modulate the air flow to control duty. BypassValveControl: Bypass valve modulates the water flow to control duty. MultipleSeriesPumps: Turn on/off multiple series pump to control duty. TwoSpeedPump: Switch between high/low pump speed to control duty. VariableSpeedPump: vary pump speed to control duty'    
      type: string    
      x-ngsi:    
        type: Property    
    circuitType:    
      description: 'OpenCircuit: Exposes water directly to the cooling atmosphere. CloseCircuit: The fluid is separated from the atmosphere by a heat exchanger. Wet: The air stream or the heat exchange surface is evaporatively cooled. Dry: No evaporation into the air stream. DryWet: A combination of a dry tower and a wet tower'    
      type: string    
      x-ngsi:    
        type: Property    
    controlStrategy:    
      description: 'FixedExitingWaterTemp: The capacity is controlled to maintain a fixed exiting water temperature. WetBulbTempReset: The set-point is reset based on the wet-bulb temperature'    
      type: string    
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
    flowArrangement:    
      description: 'CounterFlow: Air and water flow enter in different directions. CrossFlow: Air and water flow are perpendicular. ParallelFlow: air and water flow enter in same directions'    
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
    liftElevationDifference:    
      description: Elevation difference between cooling tower sump and the top of the tower. Usually measured in millimeters (mm)    
      type: number    
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
    nominalCapacity:    
      description: 'Nominal capacity. Usually measured in Watts (W, J/s)'    
      type: number    
      x-ngsi:    
        type: Property    
    numberOfCells:    
      description: Number of cells in one cooling tower unit    
      type: number    
      x-ngsi:    
        type: Property    
    operationTemperatureMax:    
      description: 'Allowable operation ambient (air, fluid) temperature range. Usually measured in degrees Kelvin (K)'    
      type: number    
      x-ngsi:    
        type: Property    
    operationTemperatureMin:    
      description: 'Allowable operation ambient (air, fluid) temperature range. Usually measured in degrees Kelvin (K)'    
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
    sprayType:    
      description: 'SprayFilled: Water is sprayed into airflow. SplashTypeFill: water cascades over successive rows of splash bars. FilmTypeFill: water flows in a thin layer over closely spaced sheets'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: It must be equal to `CoolingTower`    
      enum:    
        - CoolingTower    
      type: string    
      x-ngsi:    
        type: Property    
    waterRequirement:    
      description: Make-up water requirement. Usually measured in m3/s    
      type: number    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:CoolingTower"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/CoolingTower/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/CoolingTower/schema.json    
  x-model-tags: SAREF CoolingTower    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### CoolingTower NGSI-v2 Esempio di valori chiave  
Ecco un esempio di una torre di raffreddamento in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:CoolingTower:c628d24d-5b25-4b99-838e-35676956d307",  
  "type": "CoolingTower",  
  "ambientDesignDryBulbTemperature": 0.7275209381168831,  
  "ambientDesignWetBulbTemperature": 0.8419497776651206,  
  "basinReserveVolume": 0.9886525691530367,  
  "capacityControl": "Lead",  
  "circuitType": "virtual",  
  "controlStrategy": "Harbors",  
  "flowArrangement": "Extensions",  
  "liftElevationDifference": 0.9337996577856725,  
  "nominalCapacity": 0.8043496896372141,  
  "numberOfCells": 0.03361385186991317,  
  "operationTemperatureMax": 0.7125610456321683,  
  "operationTemperatureMin": 0.3015974804386986,  
  "sprayType": "programming",  
  "waterRequirement": 0.1817597423361893,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:6871b1ec-cfce-4a60-83c2-9f07b13d1703",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:e2a48930-276e-4972-9283-82fbc22faf85",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:aea47887-bc5b-47c3-aeb0-870506d76580",  
    "urn:ngsi-ld:System:2791b628-8fc1-4ec1-91a7-26efbbc892a3",  
    "urn:ngsi-ld:System:c0623c49-ae1f-4772-9323-a94078dbdb86"  
  ],  
  "hasManufacturer": "CoolingTower Company Inc.",  
  "hasModel": "CoolingTower 0.1.2",  
  "dateCreated": "2023-01-26T12:17:43Z",  
  "dateModified": "2023-01-25T16:13:00Z",  
  "source": "Import",  
  "name": "CoolingTower",  
  "alternateName": "CoolingTower type 2",  
  "description": "CoolingTower of limited CoolingTower types",  
  "dataProvider": "IFC file"  
}  
```  
</details>  
#### Esempio normalizzato di CoolingTower NGSI-v2  
Ecco un esempio di CoolingTower in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:CoolingTower:7995c5cf-c8c3-4e42-92db-6dd840796eae",  
  "type": "CoolingTower",  
  "ambientDesignDryBulbTemperature": {  
    "type": "Measurement",  
    "value": 0.36789185492213194  
  },  
  "ambientDesignWetBulbTemperature": {  
    "type": "Measurement",  
    "value": 0.1490037569659941  
  },  
  "basinReserveVolume": {  
    "type": "Measurement",  
    "value": 0.9142388286093716  
  },  
  "capacityControl": {  
    "type": "Text",  
    "value": "next-generation"  
  },  
  "circuitType": {  
    "type": "Text",  
    "value": "morph"  
  },  
  "controlStrategy": {  
    "type": "Text",  
    "value": "Concrete"  
  },  
  "flowArrangement": {  
    "type": "Text",  
    "value": "access"  
  },  
  "liftElevationDifference": {  
    "type": "Measurement",  
    "value": 0.6134421322995507  
  },  
  "nominalCapacity": {  
    "type": "Measurement",  
    "value": 0.14285208313177855  
  },  
  "numberOfCells": {  
    "type": "Float",  
    "value": 0.9307947920697038  
  },  
  "operationTemperatureMax": {  
    "type": "Measurement",  
    "value": 0.33271163839338236  
  },  
  "operationTemperatureMin": {  
    "type": "Measurement",  
    "value": 0.8346930607066967  
  },  
  "sprayType": {  
    "type": "Text",  
    "value": "synthesizing"  
  },  
  "waterRequirement": {  
    "type": "Measurement",  
    "value": 0.6749365729986966  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:BuildingSpace:e1c9dc03-9887-49df-9577-a24218339c39"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:PhysicalObject:d6e1c0cc-a656-4343-8572-21de93d365ba"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:972d1b4b-ab6d-474c-a742-c75822d6c7b8"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:8c7d509c-66b4-4504-ad2e-d7ec82146ba2"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:42d552ca-9fdd-4838-804e-41f34d6f61f7"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "CoolingTower Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "CoolingTower 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T21:28:15.4871264+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T13:03:39.0857574+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "CoolingTower"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "CoolingTower type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "CoolingTower of limited CoolingTower types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### CoolingTower NGSI-LD valori chiave Esempio  
Ecco un esempio di una torre di raffreddamento in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:CoolingTower:c628d24d-5b25-4b99-838e-35676956d307",  
  "type": "CoolingTower",  
  "ambientDesignDryBulbTemperature": 0.7275209381168831,  
  "ambientDesignWetBulbTemperature": 0.8419497776651206,  
  "basinReserveVolume": 0.9886525691530367,  
  "capacityControl": "Lead",  
  "circuitType": "virtual",  
  "controlStrategy": "Harbors",  
  "flowArrangement": "Extensions",  
  "liftElevationDifference": 0.9337996577856725,  
  "nominalCapacity": 0.8043496896372141,  
  "numberOfCells": 0.03361385186991317,  
  "operationTemperatureMax": 0.7125610456321683,  
  "operationTemperatureMin": 0.3015974804386986,  
  "sprayType": "programming",  
  "waterRequirement": 0.1817597423361893,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:6871b1ec-cfce-4a60-83c2-9f07b13d1703",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:e2a48930-276e-4972-9283-82fbc22faf85",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:aea47887-bc5b-47c3-aeb0-870506d76580",  
    "urn:ngsi-ld:System:2791b628-8fc1-4ec1-91a7-26efbbc892a3",  
    "urn:ngsi-ld:System:c0623c49-ae1f-4772-9323-a94078dbdb86"  
  ],  
  "hasManufacturer": "CoolingTower Company Inc.",  
  "hasModel": "CoolingTower 0.1.2",  
  "dateCreated": "2023-01-26T12:17:43Z",  
  "dateModified": "2023-01-25T16:13:00Z",  
  "source": "Import",  
  "name": "CoolingTower",  
  "alternateName": "CoolingTower type 2",  
  "description": "CoolingTower of limited CoolingTower types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### CoolingTower NGSI-LD normalizzato Esempio  
Ecco un esempio di CoolingTower in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si usano le opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:CoolingTower:eb831bd2-82be-42c3-a0c9-a6c0a231e316",  
  "type": "CoolingTower",  
  "ambientDesignDryBulbTemperature": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T08:09:09Z",  
    "value": 0.9762464796853121  
  },  
  "ambientDesignWetBulbTemperature": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T14:29:40Z",  
    "value": 0.3062794162138128  
  },  
  "basinReserveVolume": {  
    "type": "Property",  
    "unitCode": "m3",  
    "observedAt": "2023-01-26T01:28:50Z",  
    "value": 0.9472477891325785  
  },  
  "capacityControl": {  
    "type": "Property",  
    "value": "input"  
  },  
  "circuitType": {  
    "type": "Property",  
    "value": "Mauritania"  
  },  
  "controlStrategy": {  
    "type": "Property",  
    "value": "Investor"  
  },  
  "flowArrangement": {  
    "type": "Property",  
    "value": "Direct"  
  },  
  "liftElevationDifference": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T02:02:47Z",  
    "value": 0.36539365901818843  
  },  
  "nominalCapacity": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-25T22:40:21Z",  
    "value": 0.3624642546775261  
  },  
  "numberOfCells": {  
    "type": "Property",  
    "value": 0.5588013730579288  
  },  
  "operationTemperatureMax": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T23:30:50Z",  
    "value": 0.660338038211496  
  },  
  "operationTemperatureMin": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T23:56:27Z",  
    "value": 0.0877235060077185  
  },  
  "sprayType": {  
    "type": "Property",  
    "value": "Money Market Account"  
  },  
  "waterRequirement": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-25T16:48:25Z",  
    "value": 0.40722633971933253  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:61ad4f84-a577-49d5-a088-aa301efa4ec6"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:f02a5bc4-2f87-4ff7-8dd7-fb61243128a1"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:b9323186-933c-46fd-815f-7f025b04ca80"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:1cea31ba-2978-4af2-b717-5c2a98a431b4"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:13dbe647-863b-4b1f-b10c-1737310d7c51"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "CoolingTower Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "CoolingTower 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T23:05:59Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-25T18:47:19Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "CoolingTower"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "CoolingTower type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "CoolingTower of limited CoolingTower types"  
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
