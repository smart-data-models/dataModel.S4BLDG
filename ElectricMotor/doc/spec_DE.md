<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: ElektroMotor  
=====================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/ElectricMotor/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Ein Elektromotor ist eine Maschine, die elektrische Energie in mechanische Energie umwandelt.  
Version: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated[string]`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified[string]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description[string]`: Eine Beschreibung dieses Artikels  - `electricMotorEfficiency[number]`: Eigenschaft. Das Verhältnis von Ausgangskapazität zu Aufnahmekapazität.  - `frameSize[string]`: Eigenschaft. Bezeichnung der Rahmengröße entsprechend dem genannten Bereich von Rahmengrößen am Verwendungsort oder nach einer bestimmten Norm.  - `hasManufacturer[string]`: Eigenschaft. Eine Beziehung, die den Hersteller einer Entität (z. B. eines Geräts) identifiziert. Der Wert sollte eine Zeichenkette oder eine Zeichenkette mit Sprachkennzeichen sein.  - `hasModel[string]`: Eigenschaft. Eine Beziehung, die das Modell einer Entität (z. B. eines Geräts) identifiziert. Als Wert wird eine Zeichenkette oder eine Zeichenkette mit Sprachkennzeichen erwartet.  - `hasPartWinding[boolean]`: Eigenschaft. Angabe, ob es sich um einen eintourigen Motor mit einer einzigen Wicklung (= FALSE) oder um einen mehrtourigen Motor mit einer Teilwicklung (= TRUE) handelt.  - `id[*]`: Eindeutiger Bezeichner der Entität  - `isContainedInBuildingSpace[*]`: Beziehung. Eine Einheit, die zur Definition der physischen Räume des Gebäudes verwendet wird. Ein Gebäudebereich enthält Geräte oder Gebäudeobjekte. (GebäudeRaum)  - `isContainedInPhysicalObject[*]`: Verwandtschaft. Jedes Objekt, das eine eigene Raumregion hat.  (Definition aus der DUL Ontologie) (PhysicalObject)  - `isGuarded[boolean]`: Eigenschaft. Angabe, ob das Motorgehäuse bewacht ist (= TRUE) oder nicht (= FALSE).  - `isSubSystemOf[array]`: Beziehung. Ein Verweis auf ein oder mehrere Systeme, zu denen dieses physische Objekt gehört.  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `lockedRotorCurrent[number]`: Eigenschaft. Eingangsstrom, wenn ein Motoranker erregt ist, sich aber nicht dreht. Wird normalerweise in Ampere (A) gemessen.  - `motorEnclosureType[string]`: Eigenschaft. Eine Liste der verfügbaren Typen von Motorgehäusen, aus der der gewünschte Typ ausgewählt werden kann.  - `name[string]`: Der Name dieses Artikels.  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `powerOutputMax[number]`: Eigenschaft. Die maximale Ausgangsleistung des Motors. Wird normalerweise in Watt (W, J/s) gemessen.  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Es wird empfohlen, den voll qualifizierten Domänennamen des Quellanbieters oder die URL des Quellobjekts zu verwenden.  - `startCurrentFactor[number]`: Eigentum. IEC. Der Startstromfaktor legt fest, wie groß der Spitzenanlaufstrom am Motor wird. StartCurrentFactor wird mit NominalCurrent multipliziert und man erhält den Startstrom.  - `startingTime[number]`: Eigenschaft. Die Zeit (in s), die der Motor benötigt, um seine Nenndrehzahl bei angeschlossenem Antriebsaggregat, ausgehend vom Stillstand und bei der an seinen Klemmen angelegten Nennspannung zu erreichen.  - `teTime[number]`: Eigenschaft. Die maximale Zeit (in s), in der der Motor mit blockiertem Rotor laufen könnte, wenn der Motor in einer EX-Umgebung eingesetzt wird. Die Zeit gibt an, dass ein Schutzgerät vor dieser Zeit auslösen sollte, wenn der Anlaufstrom des Motors durch das Gerät verlangsamt wird.  - `type[string]`: Eigenschaft. Sie muss gleich `ElectricMotor` sein.  <!-- /30-PropertiesList -->  
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
ElectricMotor:    
  description: An electric motor is an engine that is a machine for converting electrical energy into mechanical energy.    
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
    electricMotorEfficiency:    
      description: Property. The ratio of output capacity to intake capacity.    
      type: number    
      x-ngsi:    
        type: Property    
    frameSize:    
      description: Property. Designation of the frame size according to the named range of frame sizes designated at the place of use or according to a given standard.    
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
    hasPartWinding:    
      description: 'Property. Indication of whether the motor is single speed, i.e. has a single winding (= FALSE) or multi-speed i.e.has part winding (= TRUE) .'    
      type: boolean    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &electricmotor_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      anyOf: *electricmotor_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *electricmotor_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isGuarded:    
      description: Property. Indication of whether the motor enclosure is guarded (= TRUE) or not (= FALSE).    
      type: boolean    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *electricmotor_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    lockedRotorCurrent:    
      description: Property. Input current when a motor armature is energized but not rotating. Usually measured in Ampere (A).    
      type: number    
      x-ngsi:    
        type: Property    
    motorEnclosureType:    
      description: Property. A list of the available types of motor enclosure from which that required may be selected.    
      type: string    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item.    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *electricmotor_-_properties_-_iscontainedinbuildingspace_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    powerOutputMax:    
      description: 'Property. The maximum output power rating of the engine. Usually measured in Watts (W, J/s).'    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    startCurrentFactor:    
      description: Property. IEC. Start current factor defines how large the peek starting current will become on the engine. StartCurrentFactor is multiplied to NominalCurrent and we get the start current.    
      type: number    
      x-ngsi:    
        type: Property    
    startingTime:    
      description: 'Property. The time (in s) needed for the motor to reach its rated speed with its driven equipment attached, starting from standstill and at the nominal voltage applied at its terminals.'    
      type: number    
      x-ngsi:    
        type: Property    
    teTime:    
      description: Property. The maximum time (in s) at which the motor could run with locked rotor when the motor is used in an EX-environment. The time indicates that a protective device should trip before this time when the starting current of the motor is slowing through the device.    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: Property. It must be equal to `ElectricMotor`.    
      enum:    
        - ElectricMotor    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:ElectricMotor"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/ElectricMotor/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/ElectricMotor/schema.json    
  x-model-tags: SAREF ElectricMotor    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### ElectricMotor NGSI-v2 Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen Elektromotor im JSON-LD-Format als Schlüsselwerte. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:ElectricMotor:ea4bd048-a263-480d-be61-7de297bed540",  
    "type": "ElectricMotor",  
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
    "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:b1cccba1-7a35-422c-aca4-800d8f462b00",  
    "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:a15795e2-b0d9-4ab0-863c-bc40e5e88fc6",  
    "isSubSystemOf": [  
        "urn:ngsi-ld:System:24f05820-a94f-4c53-bd66-bcb5bc451ee4",  
        "urn:ngsi-ld:System:eb6a2613-cf69-4cdc-a958-b8f24903fc46",  
        "urn:ngsi-ld:System:594815c7-5dd7-4910-93ca-ee2579c87739"  
    ],  
    "hasManufacturer": "ElectricMotor Company Inc.",  
    "hasModel": "ElectricMotor 0.1.2",  
    "dateCreated": "2023-01-25T16:58:38Z",  
    "dateModified": "2023-01-25T21:01:09Z",  
    "source": "Import",  
    "name": "ElectricMotor",  
    "alternateName": "ElectricMotor type 2",  
    "description": "ElectricMotor of limited ElectricMotor types",  
    "dataProvider": "IFC file",  
    "nominalFrequency": 0.6643858958243121,  
    "nominalSupplyVoltage": 0.9863230627218449,  
    "nominalSupplyVoltageMin": 0.5073272634060758,  
    "electricGeneratorEfficiency": 0.1422180140007665,  
    "powerOutputMax": 0.5320055721976125,  
    "startCurrentFactor": 0.7921279415808247,  
    "electricMotorEfficiency": 0.36137565435400376,  
    "frameSize": "Awesome",  
    "hasPartWinding": false,  
    "isGuarded": false,  
    "lockedRotorCurrent": 0.4948278478821372,  
    "motorEnclosureType": "target",  
    "startingTime": 0.7237739470818347,  
    "teTime": 0.32577211564738595  
}  
```  
</details>  
#### ElectricMotor NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen Elektromotor im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ElectricMotor:024aea5d-c781-4d5e-9b57-92672c75663d",  
  "type": "ElectricMotor",  
  "electricMotorEfficiency": {  
    "type": "Measurement",  
    "value": 0.14465653517328592  
  },  
  "frameSize": {  
    "type": "Text",  
    "value": "benchmark"  
  },  
  "hasPartWinding": {  
    "type": "Boolean",  
    "value": true  
  },  
  "isGuarded": {  
    "type": "Boolean",  
    "value": false  
  },  
  "lockedRotorCurrent": {  
    "type": "Measurement",  
    "value":  0.7069578753062778  
  },  
  "motorEnclosureType": {  
    "type": "Text",  
    "value": "Cambridgeshire"  
  },  
  "powerOutputMax": {  
    "type": "Measurement",  
    "value": 0.925424003891414  
  },  
  "startCurrentFactor": {  
    "type": "Measurement",  
    "value": 0.27335468276078645  
  },  
  "startingTime": {  
    "type": "Measurement",  
    "value":  0.8955138694697009  
  },  
  "teTime": {  
    "type": "Measurement",  
    "value": 0.024805742901409134  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:BuildingSpace:dec2fd4f-2093-4779-b571-841bac3ec419"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:PhysicalObject:42195e3f-cdb8-4603-952f-d9f52d9749ed"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:System:08a8c968-420c-464d-8458-784dd721cfbe"  
      },  
      {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:System:92362fba-3ddd-47af-a985-de2caf90f298"  
      },  
      {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:System:3033fd90-5610-490c-8b39-6f98c962af41"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "ElectricMotor Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "ElectricMotor 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T20:39:17.5806269+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T18:24:24.0858451+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "ElectricMotor"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "ElectricMotor type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "ElectricMotor of limited ElectricMotor types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### ElectricMotor NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen Elektromotor im JSON-LD-Format als Schlüsselwerte. Dies ist kompatibel mit NGSI-LD, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ElectricMotor:ea4bd048-a263-480d-be61-7de297bed540",  
  "type": "ElectricMotor",  
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
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:b1cccba1-7a35-422c-aca4-800d8f462b00",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:a15795e2-b0d9-4ab0-863c-bc40e5e88fc6",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:24f05820-a94f-4c53-bd66-bcb5bc451ee4",  
    "urn:ngsi-ld:System:eb6a2613-cf69-4cdc-a958-b8f24903fc46",  
    "urn:ngsi-ld:System:594815c7-5dd7-4910-93ca-ee2579c87739"  
  ],  
  "hasManufacturer": "ElectricMotor Company Inc.",  
  "hasModel": "ElectricMotor 0.1.2",  
  "dateCreated": "2023-01-25T16:58:38Z",  
  "dateModified": "2023-01-25T21:01:09Z",  
  "source": "Import",  
  "name": "ElectricMotor",  
  "alternateName": "ElectricMotor type 2",  
  "description": "ElectricMotor of limited ElectricMotor types",  
  "dataProvider": "IFC file",  
  "nominalFrequency": 0.6643858958243121,  
  "nominalSupplyVoltage": 0.9863230627218449,  
  "nominalSupplyVoltageMin": 0.5073272634060758,  
  "electricGeneratorEfficiency": 0.1422180140007665,  
  "powerOutputMax": 0.5320055721976125,  
  "startCurrentFactor": 0.7921279415808247,  
  "electricMotorEfficiency": 0.36137565435400376,  
  "frameSize": "Awesome",  
  "hasPartWinding": false,  
  "isGuarded": false,  
  "lockedRotorCurrent": 0.4948278478821372,  
  "motorEnclosureType": "target",  
  "startingTime": 0.7237739470818347,  
  "teTime": 0.32577211564738595,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### ElectricMotor NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen Elektromotor im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ElectricMotor:c4e91c91-12f4-4dc5-aaae-4c7644c8d9df",  
  "type": "ElectricMotor",  
  "electricMotorEfficiency": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T08:26:24Z",  
    "value": 0.07012980187189011  
  },  
  "frameSize": {  
    "type": "Property",  
    "value": "Saint Martin"  
  },  
  "hasPartWinding": {  
    "type": "Property",  
    "value": false  
  },  
  "isGuarded": {  
    "type": "Property",  
    "value": false  
  },  
  "lockedRotorCurrent": {  
    "type": "Property",  
    "unitCode": "A",  
    "observedAt": "2023-01-26T10:56:17Z",  
    "value": 0.7593092722196552  
  },  
  "motorEnclosureType": {  
    "type": "Property",  
    "value": "Berkshire"  
  },  
  "powerOutputMax": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-26T08:12:29Z",  
    "value": 0.32215622178270653  
  },  
  "startCurrentFactor": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T06:44:33Z",  
    "value": 0.8565155734572442  
  },  
  "startingTime": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T08:12:12Z",  
    "value": 0.7168865515513289  
  },  
  "teTime": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T06:08:56Z",  
    "value": 0.2793471624901087  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:c89167bc-11d5-48cc-8cde-0ea875d76fe3"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:e8206186-a4b3-4030-80dc-a4e5ebe12ab4"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:20c42d2b-4216-458d-9ef0-a0fece28ca92"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:5418d44a-319c-46af-aa8a-83e59fb559e7"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:7baa4e2b-ac2d-4a9b-90a2-ef578b5091a7"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "ElectricMotor Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "ElectricMotor 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T09:43:59Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T14:02:00Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "ElectricMotor"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "ElectricMotor type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "ElectricMotor of limited ElectricMotor types"  
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
