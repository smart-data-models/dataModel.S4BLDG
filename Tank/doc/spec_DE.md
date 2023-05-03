<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: Tank  
=============<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Tank/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Ein Tank ist ein Gefäß oder Behälter, in dem eine Flüssigkeit oder ein Gas zur späteren Verwendung gelagert wird.**  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
- `accessType[string]`: Eigenschaft. Definiert die Arten des Zugangs (oder der Abdeckung) zu einem Tank, die angegeben werden können. Beachten Sie, dass Abdeckungen im Allgemeinen für rechteckige Tanks angegeben werden. Bei zylindrischen Tanks erfolgt der Zugang normalerweise über ein Mannloch.  - `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated[string]`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified[string]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description[string]`: Eine Beschreibung dieses Artikels  - `effectiveCapacity[number]`: Eigenschaft. Der gesamte effektive oder tatsächliche Fassungsraum des Tanks. Wird normalerweise in Kubikmetern (m3) gemessen.B3  - `endShapeType[string]`: Eigenschaft. Definiert die Arten von Endformen, die für vorgeformte Tanks verwendet werden können. Die Konvention für das Ablesen dieser Aufzählungswerte ist, dass bei einem vertikalen Zylinder der erste Wert die Basis und der zweite die Oberseite ist, bei einem horizontalen Zylinder ist die Reihenfolge des Ablesens von links nach rechts. Für einen kugelförmigen Tank sollte der Wert UNSET verwendet werden.B5  - `firstCurvatureRadius[number]`: Eigenschaft. FirstCurvatureRadius sollte als Basis- oder linksseitiger Krümmungsradiuswert definiert werden. Wird normalerweise in Millimetern (mm) gemessen.  - `hasManufacturer[string]`: Eigenschaft. Eine Beziehung, die den Hersteller einer Entität (z. B. eines Geräts) identifiziert. Der Wert sollte eine Zeichenkette oder eine Zeichenkette mit Sprachkennzeichen sein.  - `hasModel[string]`: Eigenschaft. Eine Beziehung, die das Modell einer Entität (z. B. eines Geräts) identifiziert. Als Wert wird eine Zeichenkette oder eine Zeichenkette mit Sprachkennzeichen erwartet.  - `id[*]`: Eindeutiger Bezeichner der Entität  - `isContainedInBuildingSpace[*]`: Beziehung. Eine Einheit, die zur Definition der physischen Räume des Gebäudes verwendet wird. Ein Gebäudebereich enthält Geräte oder Gebäudeobjekte. (GebäudeRaum)  - `isContainedInPhysicalObject[*]`: Verwandtschaft. Jedes Objekt, das eine eigene Raumregion hat.  (Definition aus der DUL Ontologie) (PhysicalObject)  - `isSubSystemOf[array]`: Beziehung. Ein Verweis auf ein oder mehrere Systeme, zu denen dieses physische Objekt gehört.  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels.  - `nominalDepth[number]`: Eigenschaft. Die Nenntiefe des Tanks. Hinweis: Nicht erforderlich für einen liegenden zylindrischen Tank. Wird normalerweise in Millimetern (mm) gemessen.  - `nominalLengthOrDiameter[number]`: Eigenschaft. Die Nennlänge oder, im Falle eines stehenden zylindrischen Tanks, der Nenndurchmesser des Tanks. Wird normalerweise in Millimetern (mm) gemessen.  - `nominalVolumetricCapacity[number]`: Eigenschaft. Das gesamte Nenn- oder Auslegungsvolumen des Tanks. Wird normalerweise in Kubikmetern (m3) gemessen.  - `nominalWidthOrDiameter[number]`: Eigenschaft. Die Nennbreite oder, bei liegenden zylindrischen Tanks, der Nenndurchmesser des Tanks. Anmerkung: Nicht erforderlich für einen stehenden zylindrischen Tank. Wird normalerweise in Millimetern (mm) gemessen.  - `numberOfSections[number]`: Eigenschaft. Anzahl der verwendeten Abschnitte.  - `operatingWeight[number]`: Eigenschaft. Betriebsgewicht des Tanks einschließlich seines gesamten Inhalts. Wird normalerweise in Kilogramm (kg) oder Gramm (g) gemessen.  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `patternType[string]`: Eigenschaft. Definiert die Arten von Mustern (oder die Form eines Tanks), die angegeben werden können.  - `secondCurvatureRadius[number]`: Eigenschaft. SecondCurvatureRadius sollte als Wert für den oberen oder rechten Krümmungsradius definiert werden. Wird normalerweise in Millimetern (mm) gemessen.  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `storageType[string]`: Eigenschaft. Definiert die allgemeine Materialkategorie, die gelagert werden soll.  - `type[string]`: Eigenschaft. Sie muss gleich `Tank` sein.  <!-- /30-PropertiesList -->  
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
Tank:    
  description: A tank is a vessel or container in which a fluid or gas is stored for later use.    
  properties:    
    accessType:    
      description: 'Property. Defines the types of access (or cover) to a tank that may be specified. Note that covers are generally specified for rectangular tanks. For cylindrical tanks, access will normally be via a manhole.'    
      type: string    
      x-ngsi:    
        type: Property    
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
    effectiveCapacity:    
      description: Property. The total effective or actual volumetric capacity of the tank. Usually measured in cubic metre (m3).B3    
      type: number    
      x-ngsi:    
        type: Property    
    endShapeType:    
      description: 'Property. Defines the types of end shapes that can be used for preformed tanks. The convention for reading these enumerated values is that for a vertical cylinder, the first value is the base and the second is the top for a horizontal cylinder, the order of reading should be left to right. For a speherical tank, the value UNSET should be used.B5'    
      type: string    
      x-ngsi:    
        type: Property    
    firstCurvatureRadius:    
      description: Property. FirstCurvatureRadius should be defined as the base or left side radius of curvature value. Usually measured in millimeters (mm).    
      type: number    
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
    id:    
      anyOf: &tank_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      anyOf: *tank_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *tank_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *tank_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    nominalDepth:    
      description: 'Property. The nominal depth of the tank. Note: Not required for a horizontal cylindrical tank. Usually measured in millimeters (mm).'    
      type: number    
      x-ngsi:    
        type: Property    
    nominalLengthOrDiameter:    
      description: 'Property. The nominal length or, in the case of a vertical cylindrical tank, the nominal diameter of the tank. Usually measured in millimeters (mm).'    
      type: number    
      x-ngsi:    
        type: Property    
    nominalVolumetricCapacity:    
      description: Property. The total nominal or design volumetric capacity of the tank. Usually measured in cubic metre (m3).    
      type: number    
      x-ngsi:    
        type: Property    
    nominalWidthOrDiameter:    
      description: 'Property. The nominal width or, in the case of a horizontal cylindrical tank, the nominal diameter of the tank. Note: Not required for a vertical cylindrical tank. Usually measured in millimeters (mm).'    
      type: number    
      x-ngsi:    
        type: Property    
    numberOfSections:    
      description: Property. Number of sections used.    
      type: number    
      x-ngsi:    
        type: Property    
    operatingWeight:    
      description: Property. Operating weight of the tank including all of its contents. Usually measured in kilograms (kg) or grams (g).    
      type: number    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *tank_-_properties_-_iscontainedinbuildingspace_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    patternType:    
      description: Property. Defines the types of pattern (or shape of a tank that may be specified.    
      type: string    
      x-ngsi:    
        type: Property    
    secondCurvatureRadius:    
      description: Property. SecondCurvatureRadius should be defined as the top or right side radius of curvature value. Usually measured in millimeters (mm).    
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
    storageType:    
      description: Property. Defines the general material category intended to be stored.    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: Property. It must be equal to `Tank`.    
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
## Beispiel-Nutzlasten  
#### Tank NGSI-v2 Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen Tank im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird, und liefert die Kontextdaten einer einzelnen Entität.  
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
#### Tank NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen Tank im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
    "type": "Measurement",  
    "value":  0.34988329549654584  
  },  
  "endShapeType": {  
    "type": "Text",  
    "value": "Lari"  
  },  
  "firstCurvatureRadius": {  
    "type": "Measurement",  
    "value": 0.9159778495815387  
  },  
  "nominalDepth": {  
    "type": "Measurement",  
    "value": 0.8630341610754986  
  },  
  "nominalLengthOrDiameter": {  
    "type": "Measurement",  
    "value":  0.8867523503955448  
  },  
  "nominalVolumetricCapacity": {  
    "type": "Measurement",  
    "value":  0.27704062609207425  
  },  
  "nominalWidthOrDiameter": {  
    "type": "Measurement",  
    "value":  0.6770082270929979  
  },  
  "numberOfSections": {  
    "type": "Float",  
    "value": 0.7169194499582789  
  },  
  "operatingWeight": {  
    "type": "Measurement",  
    "value": 0.23947734710245394  
  },  
  "patternType": {  
    "type": "Text",  
    "value": "Ergonomic Cotton Ball"  
  },  
  "secondCurvatureRadius": {  
    "type": "Measurement",  
    "value": 0.11478790270153483  
  },  
  "storageType": {  
    "type": "Text",  
    "value": "gold"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:BuildingSpace:431e892c-1029-409d-b7b8-b9cad9a0a9e5"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:PhysicalObject:fd304ea2-572f-4b66-b8ad-d9d84c870fa1"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:b3336716-b468-40f1-be04-9f7ffedcc418"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:05bac9cd-2c56-4046-a70a-b2415e810f43"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:2344579c-27b3-4c5d-9db3-0fd9b46fb7e7"  
      }  
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
#### Tank NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen Tank im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
#### Tank NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen Tank im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
