<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entität: DuctSilencer    
=====================<!-- /10-Header -->    
<!-- 15-License -->    
[Offene Lizenz](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/DuctSilencer/LICENSE.md)    
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Globale Beschreibung: **Ein Kanalschalldämpfer ist eine Vorrichtung, die in der Regel in einem Kanalverteilungssystem installiert wird, um den Geräuschpegel von Luftbewegungen, Lüftergeräuschen usw. im angrenzenden Raum oder stromabwärts des Kanalschalldämpfers zu verringern.**    
Version: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste der Eigenschaften    
<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.    
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel, Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: Die Ortschaft, in der sich die Adresse befindet, und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: Die Region, in der sich der Ort befindet, und die auf dem Land liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird.      
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: Die Straßenanschrift  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `airFlowRateMax[number]`: Maximal zulässiger Luftdurchsatz. Üblicherweise gemessen in m3/s  - `airFlowRateMin[number]`: Zulässiger Mindestluftdurchsatz. Üblicherweise gemessen in m3/s  - `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `hasExteriorInsulation[boolean]`: TRUE, wenn der Schalldämpfer eine Außenisolierung hat. FALSE, wenn er keine hat  - `hasManufacturer[string]`: Eine Beziehung zur Identifizierung des Herstellers einer Entität (z. B. eines Geräts). Der Wert sollte eine Zeichenkette oder eine Zeichenkette mit Sprachkennzeichen sein  - `hasModel[string]`: Eine Beziehung, die das Modell einer Entität (z. B. eines Geräts) identifiziert. Als Wert wird eine Zeichenkette oder eine Zeichenkette mit Sprach-Tag erwartet  - `hydraulicDiameter[number]`: Hydraulischer Durchmesser. Normalerweise in Millimetern (mm) gemessen.  - `id[*]`: Eindeutiger Bezeichner der Entität  - `isContainedInBuildingSpace[*]`: Eine Einheit, die zur Definition der physischen Räume des Gebäudes verwendet wird. Ein Gebäudebereich enthält Geräte oder Gebäudeobjekte. (GebäudeRaum)  - `isContainedInPhysicalObject[*]`: Jedes Objekt, das eine eigene Raumregion hat.  (Definition entnommen aus der DUL-Ontologie) (PhysicalObject)  - `isSubSystemOf[array]`: Ein Verweis auf ein oder mehrere Systeme, zu denen dieses physische Objekt gehört  - `length[number]`: Die fertige Länge des Geräts. Wird normalerweise in Millimetern (mm) gemessen.  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels  - `operationTemperatureMax[number]`: Zulässiger Temperaturbereich der Betriebsumgebung (Luft, Flüssigkeit). Gewöhnlich gemessen in Grad Kelvin (K)  - `operationTemperatureMin[number]`: Zulässiger Temperaturbereich der Betriebsumgebung (Luft, Flüssigkeit). Gewöhnlich gemessen in Grad Kelvin (K)  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `type[string]`: Er muss gleich `DuctSilencer` sein  - `weight[number]`: Das Gewicht des Geräts. Wird normalerweise in Kilogramm (kg) oder Gramm (g) gemessen.  - `workingPressureMax[number]`: Maximaler Arbeitsdruck. Üblicherweise gemessen in Pascal (Pa, N/m2)  - `workingPressureMin[number]`: Zulässiger Mindestbetriebsdruck (bezogen auf den Umgebungsdruck). Wird normalerweise in Pascal (Pa, N/m2) gemessen.  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Erforderliche Eigenschaften    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Datenmodell Beschreibung der Eigenschaften    
Alphabetisch sortiert (für Details anklicken)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
DuctSilencer:      
  description: 'A duct silencer is a device that is typically installed inside a duct distribution system for the purpose of reducing the noise levels from air movement, fan noise, etc. in the adjacent space or downstream of the duct silencer device.'      
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
    airFlowRateMax:      
      description: Maximum allowable air flow rate. Usually measured in m3/s      
      type: number      
      x-ngsi:      
        type: Property      
    airFlowRateMin:      
      description: Minimum allowable air flow rate. Usually measured in m3/s      
      type: number      
      x-ngsi:      
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
    hasExteriorInsulation:      
      description: TRUE if the silencer has exterior insulation. FALSE if it does not      
      type: boolean      
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
    hydraulicDiameter:      
      description: Hydraulic diameter. Usually measured in millimeters (mm)      
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
    length:      
      description: The finished length of the device. Usually measured in millimeters (mm)      
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
    type:      
      description: It must be equal to `DuctSilencer`      
      enum:      
        - DuctSilencer      
      type: string      
      x-ngsi:      
        type: Property      
    weight:      
      description: The weight of the device. Usually measured in kilograms (kg) or grams (g)      
      type: number      
      x-ngsi:      
        type: Property      
    workingPressureMax:      
      description: 'Maximum working pressure. Usually measured in Pascals (Pa, N/m2)'      
      type: number      
      x-ngsi:      
        type: Property      
    workingPressureMin:      
      description: 'Allowable minimum working pressure (relative to ambient pressure). Usually measured in Pascals (Pa, N/m2)'      
      type: number      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:DuctSilencer"      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/DuctSilencer/LICENSE.md      
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/DuctSilencer/schema.json      
  x-model-tags: SAREF DuctSilencer      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Beispiel-Nutzlasten    
#### DuctSilencer NGSI-v2 key-values Beispiel    
Hier ist ein Beispiel für einen DuctSilencer im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:DuctSilencer:439e7a92-6ff4-4b8b-94fa-cefa9b8cc9a2",  
  "type": "DuctSilencer",  
  "airFlowRateMax": 0.1608748792870458,  
  "airFlowRateMin": 0.5144201035637935,  
  "hasExteriorInsulation": true,  
  "hydraulicDiameter": 0.655988670157379,  
  "length": 0.6761801102701772,  
  "operationTemperatureMax": 0.9108707788637439,  
  "operationTemperatureMin": 0.38034850956825317,  
  "weight": 0.3440451194010431,  
  "workingPressureMax": 0.4689060124065172,  
  "workingPressureMin": 0.6786833167445696,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:35cd1a8e-8ad6-4cd0-9a0c-4270a9cf8680",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:3ba75bf1-2b1d-4988-bf7d-2000b44b87ab",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:7dd27551-56f1-4c2b-b094-f490114a721e",  
    "urn:ngsi-ld:System:b6550f33-a522-4632-81e4-dcd4c08d3229",  
    "urn:ngsi-ld:System:68691c7c-07b2-4009-ae84-c326a9e32071"  
  ],  
  "hasManufacturer": "DuctSilencer Company Inc.",  
  "hasModel": "DuctSilencer 0.1.2",  
  "dateCreated": "2023-01-26T11:03:15Z",  
  "dateModified": "2023-01-26T06:10:02Z",  
  "source": "Import",  
  "name": "DuctSilencer",  
  "alternateName": "DuctSilencer type 2",  
  "description": "DuctSilencer of limited DuctSilencer types",  
  "dataProvider": "IFC file"  
}  
```  
</details>    
#### DuctSilencer NGSI-v2 normalisiert Beispiel    
Hier ist ein Beispiel für einen DuctSilencer im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:DuctSilencer:354bc2c9-fe84-4b86-870e-b4bb0f421e14",  
  "type": "DuctSilencer",  
  "airFlowRateMax": {  
    "type": "Number",  
    "value": 0.42241788558074733  
  },  
  "airFlowRateMin": {  
    "type": "Number",  
    "value": 0.3750532258722393  
  },  
  "hasExteriorInsulation": {  
    "type": "Boolean",  
    "value": false  
  },  
  "hydraulicDiameter": {  
    "type": "Number",  
    "value": 0.28893264554968967  
  },  
  "length": {  
    "type": "Number",  
    "value": 0.8546214350560009  
  },  
  "operationTemperatureMax": {  
    "type": "Number",  
    "value": 0.5534860278496251  
  },  
  "operationTemperatureMin": {  
    "type": "Number",  
    "value": 0.8929827048351656  
  },  
  "weight": {  
    "type": "Number",  
    "value": 0.6856055430291446  
  },  
  "workingPressureMax": {  
    "type": "Number",  
    "value": 0.28889395933436934  
  },  
  "workingPressureMin": {  
    "type": "Number",  
    "value": 0.5603647437955193  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:BuildingSpace:2e17ab63-5c61-4d14-90a2-6d9c2f96681d"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:PhysicalObject:edc1a584-5b19-4244-b872-001cf887a7d7"  
  },  
  "isSubSystemOf": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:System:749d1fd1-6e00-4d22-96f6-aec2dda0e494",  
      "urn:ngsi-ld:System:6e1df1b9-fdec-4c73-9a85-f28b88014ec8",  
      "urn:ngsi-ld:System:b6ffa288-5b86-40d9-90d7-5fb8b8dc7f02"  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "DuctSilencer Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "DuctSilencer 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T14:45:14.4588565+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T11:59:21.5030067+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "DuctSilencer"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "DuctSilencer type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "DuctSilencer of limited DuctSilencer types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>    
#### DuctSilencer NGSI-LD key-values Beispiel    
Hier ist ein Beispiel für einen DuctSilencer im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:DuctSilencer:439e7a92-6ff4-4b8b-94fa-cefa9b8cc9a2",  
  "type": "DuctSilencer",  
  "airFlowRateMax": 0.1608748792870458,  
  "airFlowRateMin": 0.5144201035637935,  
  "hasExteriorInsulation": true,  
  "hydraulicDiameter": 0.655988670157379,  
  "length": 0.6761801102701772,  
  "operationTemperatureMax": 0.9108707788637439,  
  "operationTemperatureMin": 0.38034850956825317,  
  "weight": 0.3440451194010431,  
  "workingPressureMax": 0.4689060124065172,  
  "workingPressureMin": 0.6786833167445696,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:35cd1a8e-8ad6-4cd0-9a0c-4270a9cf8680",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:3ba75bf1-2b1d-4988-bf7d-2000b44b87ab",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:7dd27551-56f1-4c2b-b094-f490114a721e",  
    "urn:ngsi-ld:System:b6550f33-a522-4632-81e4-dcd4c08d3229",  
    "urn:ngsi-ld:System:68691c7c-07b2-4009-ae84-c326a9e32071"  
  ],  
  "hasManufacturer": "DuctSilencer Company Inc.",  
  "hasModel": "DuctSilencer 0.1.2",  
  "dateCreated": "2023-01-26T11:03:15Z",  
  "dateModified": "2023-01-26T06:10:02Z",  
  "source": "Import",  
  "name": "DuctSilencer",  
  "alternateName": "DuctSilencer type 2",  
  "description": "DuctSilencer of limited DuctSilencer types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>    
#### DuctSilencer NGSI-LD normalisiert Beispiel    
Hier ist ein Beispiel für einen DuctSilencer im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:DuctSilencer:f2f44b77-d3ee-4ab4-bd1a-1c476f674549",  
  "type": "DuctSilencer",  
  "airFlowRateMax": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-25T19:54:39Z",  
    "value": 0.5746033930246481  
  },  
  "airFlowRateMin": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-25T21:24:51Z",  
    "value": 0.6010968836956997  
  },  
  "hasExteriorInsulation": {  
    "type": "Property",  
    "value": true  
  },  
  "hydraulicDiameter": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-25T17:57:38Z",  
    "value": 0.6623416028707915  
  },  
  "length": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-25T15:21:41Z",  
    "value": 0.9676732407508329  
  },  
  "operationTemperatureMax": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T11:39:38Z",  
    "value": 0.56707910867758  
  },  
  "operationTemperatureMin": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T09:06:00Z",  
    "value": 0.7219158816538178  
  },  
  "weight": {  
    "type": "Property",  
    "unitCode": "g",  
    "observedAt": "2023-01-25T21:05:44Z",  
    "value": 0.6644043164355533  
  },  
  "workingPressureMax": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-26T04:07:57Z",  
    "value": 0.058329572403388985  
  },  
  "workingPressureMin": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-25T23:17:06Z",  
    "value": 0.10711886041657781  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:0addac31-ddff-4a11-97a1-e9411907e554"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:ac4f9960-3415-4943-a490-81859df172a4"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:a182c79d-ec15-4bfb-9b22-b0db74eac23e"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:f429ad1b-2285-441f-9305-8de0017d3b4c"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:d1dfe74b-ef79-4c61-be03-d1617663f8c4"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "DuctSilencer Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "DuctSilencer 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T01:07:55Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T12:16:22Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "DuctSilencer"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "DuctSilencer type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "DuctSilencer of limited DuctSilencer types"  
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
