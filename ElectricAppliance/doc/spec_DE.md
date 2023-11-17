<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entität: ElectricAppliance    
==========================<!-- /10-Header -->    
<!-- 15-License -->    
[Offene Lizenz](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/ElectricAppliance/LICENSE.md)    
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Globale Beschreibung: **Ein Elektrogerät ist ein für den Verbraucher bestimmtes Gerät, das mit Strom betrieben wird. Elektrogeräte können ortsfest sein oder von einem Ort zum anderen bewegt werden. Elektrische Geräte benötigen eine elektrische Versorgung, die entweder über einen Stromkreis oder über eine lokale Batteriequelle erfolgen kann.**    
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
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `hasManufacturer[string]`: Eine Beziehung zur Identifizierung des Herstellers einer Entität (z. B. eines Geräts). Der Wert sollte eine Zeichenkette oder eine Zeichenkette mit Sprachkennzeichen sein  - `hasModel[string]`: Eine Beziehung, die das Modell einer Entität (z. B. eines Geräts) identifiziert. Als Wert wird eine Zeichenkette oder eine Zeichenkette mit Sprach-Tag erwartet  - `id[*]`: Eindeutiger Bezeichner der Entität  - `isContainedInBuildingSpace[*]`: Eine Einheit, die zur Definition der physischen Räume des Gebäudes verwendet wird. Ein Gebäudebereich enthält Geräte oder Gebäudeobjekte. (GebäudeRaum)  - `isContainedInPhysicalObject[*]`: Jedes Objekt, das eine eigene Raumregion hat.  (Definition entnommen aus der DUL-Ontologie) (PhysicalObject)  - `isSubSystemOf[array]`: Ein Verweis auf ein oder mehrere Systeme, zu denen dieses physische Objekt gehört  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `type[string]`: Sie muss gleich `ElectricAppliance` sein  <!-- /30-PropertiesList -->    
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
ElectricAppliance:      
  description: An electric appliance is a device intended for consumer usage that is powered by electricity. Electric appliances may be fixed in place or may be able to be moved from one space to another. Electric appliances require an electrical supply that may be supplied either by an electrical circuit or provided from a local battery source.      
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
      description: It must be equal to `ElectricAppliance`      
      enum:      
        - ElectricAppliance      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:ElectricAppliance"      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/ElectricAppliance/LICENSE.md      
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/ElectricAppliance/schema.json      
  x-model-tags: SAREF ElectricAppliance      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Beispiel-Nutzlasten    
#### ElektroGeräte NGSI-v2 Schlüsselwerte Beispiel    
Hier ist ein Beispiel für ein Elektrogerät im JSON-LD-Format als Schlüsselwerte. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:ElectricAppliance:6e65c1d1-0ce5-4828-aaeb-fb9e2ef604ad",  
  "type": "ElectricAppliance",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:d4a091f6-b086-4318-88c5-d7b7a244cb28",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:8fbda04a-a5fc-44cd-9854-da6113cfc5f9",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:3d107394-8ee6-41da-aadd-a754c9de429e",  
    "urn:ngsi-ld:System:bfdeb3cd-ed1e-4e1a-8db1-7fb7e1f39bee",  
    "urn:ngsi-ld:System:a2c1fd65-c4e7-45ca-af3e-0dcac93f2465"  
  ],  
  "hasManufacturer": "ElectricAppliance Company Inc.",  
  "hasModel": "ElectricAppliance 0.1.2",  
  "dateCreated": "2023-01-25T19:20:17Z",  
  "dateModified": "2023-01-26T02:11:47Z",  
  "source": "Import",  
  "name": "ElectricAppliance",  
  "alternateName": "ElectricAppliance type 2",  
  "description": "ElectricAppliance of limited ElectricAppliance types",  
  "dataProvider": "IFC file"  
}  
```  
</details>    
#### ElektroGeräte NGSI-v2 normalisiert Beispiel    
Hier ist ein Beispiel für ein Elektrogerät im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:ElectricAppliance:96716a2d-2f29-4743-82df-10d2eca00ede",  
  "type": "ElectricAppliance",  
  "isContainedInBuildingSpace": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:BuildingSpace:01f5ab5b-8e44-41de-b0f7-b5b3f33717b8"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:PhysicalObject:480240b9-9494-4d25-988b-6e52684ef2d1"  
  },  
  "isSubSystemOf": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:System:c561dc1f-70af-4eba-8df2-0b12636d5452",  
      "urn:ngsi-ld:System:b2c80983-473f-4a2e-b7ac-a52ba8fb87a1",  
      "urn:ngsi-ld:System:cad65c54-699e-42d1-92d1-30498917b466"  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "ElectricAppliance Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "ElectricAppliance 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T12:06:23.0239951+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T11:52:29.7829399+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "ElectricAppliance"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "ElectricAppliance type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "ElectricAppliance of limited ElectricAppliance types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>    
#### ElektroGerät NGSI-LD Schlüsselwerte Beispiel    
Hier ist ein Beispiel für ein Elektrogerät im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:ElectricAppliance:d59d2cef-8b46-4096-9529-f69c20153cda",  
  "type": "ElectricAppliance",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:ff56d041-f8c4-45ce-bb80-6640726f99fc",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:9211c842-e092-4c55-b61a-8b7e70b314f0",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:1ca917af-3521-4fa1-9625-107542a9dd84",  
    "urn:ngsi-ld:System:b37bd7ae-e6e6-404b-82c9-c8490d370934",  
    "urn:ngsi-ld:System:7e7cb3ea-44f3-423b-b664-9bc52e2de492"  
  ],  
  "hasManufacturer": "ElectricAppliance Company Inc.",  
  "hasModel": "ElectricAppliance 0.1.2",  
  "dateCreated": "2023-01-26T06:24:09Z",  
  "dateModified": "2023-01-26T10:24:54Z",  
  "source": "Import",  
  "name": "ElectricAppliance",  
  "alternateName": "ElectricAppliance type 2",  
  "description": "ElectricAppliance of limited ElectricAppliance types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>    
#### ElektroGerät NGSI-LD normalisiert Beispiel    
Hier ist ein Beispiel für ein Elektrogerät im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:ElectricAppliance:432b9ede-40de-497c-8018-f1f99a3a83db",  
  "type": "ElectricAppliance",  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:2f3cde5a-5d50-4a7e-9154-03e6ecbe7c76"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:4f82fb66-4142-4fb9-955c-6e96633e5221"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:1f3d76fa-fcea-4e6c-a448-ce031f17c31f"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:a65e461a-cc13-4328-8524-4c3cf19079be"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:8ff7b46e-4446-4682-9421-d6dce91a29b6"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "ElectricAppliance Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "ElectricAppliance 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T20:22:32Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-25T22:18:49Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "ElectricAppliance"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "ElectricAppliance type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "ElectricAppliance of limited ElectricAppliance types"  
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
