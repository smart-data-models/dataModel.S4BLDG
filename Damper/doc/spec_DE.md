<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: Dämpfer  
================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Damper/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Eine Klappe ist in der Regel Teil eines HVAC-Kanalverteilungssystems und wird zur Steuerung oder Modulation des Luftstroms verwendet.**  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)- `airFlowRateMax[number]`: Eigenschaft. Maximal zulässiger Luftdurchsatz. Wird normalerweise in m3/s gemessen.  - `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `bladeAction[string]`: Eigenschaft. Klingen-Aktion.  - `bladeEdge[string]`: Eigenschaft. Schneide der Klinge.  - `bladeShape[string]`: Eigenschaft. Form der Klinge. Flach bedeutet dreifache V-Nut.  - `bladeThickness[number]`: Eigenschaft. Die Dicke des Dämpferblattes. Wird normalerweise in Millimetern (mm) gemessen.  - `closeOffRating[number]`: Eigenschaft. Abschaltvermögen. Wird normalerweise in Pascal (Pa, N/m2) gemessen.  - `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated[string]`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified[string]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description[string]`: Eine Beschreibung dieses Artikels  - `faceArea[number]`: Eigenschaft. Zur Luftströmung offene Fläche. Wird normalerweise in Quadratmetern (m2) gemessen.  - `frameDepth[number]`: Eigenschaft. Die Länge (oder Tiefe) des Dämpferrahmens. Wird normalerweise in Millimetern (mm) gemessen.  - `frameThickness[number]`: Eigenschaft. Die Dicke des Materials des Dämpferrahmens. Wird normalerweise in Millimetern (mm) gemessen.  - `frameType[string]`: Eigenschaft. Der von der Klappe verwendete Rahmentyp (z. B. Standard, Einfacher Flansch, Einfacher umgekehrter Flansch, Doppelter Flansch, usw.).  - `hasManufacturer[string]`: Eigenschaft. Eine Beziehung, die den Hersteller einer Entität (z. B. eines Geräts) identifiziert. Der Wert sollte eine Zeichenkette oder eine Zeichenkette mit Sprachkennzeichen sein.  - `hasModel[string]`: Eigenschaft. Eine Beziehung, die das Modell einer Entität (z. B. eines Geräts) identifiziert. Als Wert wird eine Zeichenkette oder eine Zeichenkette mit Sprachkennzeichen erwartet.  - `id[*]`: Eindeutiger Bezeichner der Entität  - `isContainedInBuildingSpace[*]`: Beziehung. Eine Einheit, die zur Definition der physischen Räume des Gebäudes verwendet wird. Ein Gebäudebereich enthält Geräte oder Gebäudeobjekte. (GebäudeRaum)  - `isContainedInPhysicalObject[*]`: Verwandtschaft. Jedes Objekt, das eine eigene Raumregion hat.  (Definition aus der DUL Ontologie) (PhysicalObject)  - `isSubSystemOf[array]`: Beziehung. Ein Verweis auf ein oder mehrere Systeme, zu denen dieses physische Objekt gehört.  - `leakageFullyClosed[number]`: Eigenschaft. Leckage bei vollständiger Schließung. Wird normalerweise in m3/s gemessen.  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels.  - `nominalAirFlowRate[number]`: Eigenschaft. Nominale Luftdurchflussrate. Wird normalerweise in m3/s gemessen.  - `numberOfBlades[number]`: Eigenschaft. Anzahl der Klingen.  - `openPressureDrop[number]`: Eigenschaft. Gesamtdruckabfall über der Klappe. Wird normalerweise in Pascal (Pa, N/m2) gemessen.  - `operation[string]`: Eigenschaft. Der Betriebsmechanismus für den Betrieb der Klappe.  - `operationMode[string]`: Eigenschaft. Betriebsart dieser Klappe.  - `operationTemperatureMax[number]`: Eigenschaft. Zulässiger Temperaturbereich der Betriebsumgebung (Luft, Flüssigkeit). Wird normalerweise in Grad Kelvin (K) gemessen.  - `operationTemperatureMin[number]`: Eigenschaft. Zulässiger Temperaturbereich der Betriebsumgebung (Luft, Flüssigkeit). Wird normalerweise in Grad Kelvin (K) gemessen.  - `orientation[string]`: Eigenschaft. Die vom Hersteller angegebene vorgesehene Ausrichtung des Dämpfers.  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Es wird empfohlen, den voll qualifizierten Domänennamen des Quellanbieters oder die URL des Quellobjekts zu verwenden.  - `temperatureRating[number]`: Eigenschaft. Temperaturklasse. Wird normalerweise in Grad Kelvin (K) gemessen.  - `type[string]`: Eigenschaft. Sie muss gleich `Damper` sein.  - `workingPressureMax[number]`: Eigenschaft. Maximaler Arbeitsdruck. Wird normalerweise in Pascal (Pa, N/m2) gemessen.  <!-- /30-PropertiesList -->  
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
Damper:    
  description: A damper typically participates in an HVAC duct distribution system and is used to control or modulate the flow of air.    
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
    airFlowRateMax:    
      description: Property. Maximum allowable air flow rate. Usually measured in m3/s.    
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
    bladeAction:    
      description: Property. Blade action.    
      type: string    
      x-ngsi:    
        type: Property    
    bladeEdge:    
      description: Property. Blade edge.    
      type: string    
      x-ngsi:    
        type: Property    
    bladeShape:    
      description: Property. Blade shape. Flat means triple V-groove.    
      type: string    
      x-ngsi:    
        type: Property    
    bladeThickness:    
      description: Property. The thickness of the damper blade. Usually measured in millimeters (mm).    
      type: number    
      x-ngsi:    
        type: Property    
    closeOffRating:    
      description: 'Property. Close off rating. Usually measured in Pascals (Pa, N/m2).'    
      type: number    
      x-ngsi:    
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
    faceArea:    
      description: Property. Face area open to the airstream. Usually measured in square metre (m2).    
      type: number    
      x-ngsi:    
        type: Property    
    frameDepth:    
      description: Property. The length (or depth) of the damper frame. Usually measured in millimeters (mm).    
      type: number    
      x-ngsi:    
        type: Property    
    frameThickness:    
      description: Property. The thickness of the damper frame material. Usually measured in millimeters (mm).    
      type: number    
      x-ngsi:    
        type: Property    
    frameType:    
      description: 'Property. The type of frame used by the damper (e.g., Standard, Single Flange, Single Reversed Flange, Double Flange, etc.).'    
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
    id:    
      anyOf: &damper_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      anyOf: *damper_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *damper_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *damper_-_properties_-_iscontainedinbuildingspace_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Relationship    
    leakageFullyClosed:    
      description: Property. Leakage when fully closed. Usually measured in m3/s.    
      type: number    
      x-ngsi:    
        type: Property    
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
    nominalAirFlowRate:    
      description: Property. Nominal rate of air flow. Usually measured in m3/s.    
      type: number    
      x-ngsi:    
        type: Property    
    numberOfBlades:    
      description: Property. Number of blades.    
      type: number    
      x-ngsi:    
        type: Property    
    openPressureDrop:    
      description: 'Property. Total pressure drop across damper. Usually measured in Pascals (Pa, N/m2).'    
      type: number    
      x-ngsi:    
        type: Property    
    operation:    
      description: Property. The operational mechanism for the damper operation.    
      type: string    
      x-ngsi:    
        type: Property    
    operationMode:    
      description: Property. Operation mode of this damper.    
      enum:    
        - supply    
        - exhaust    
      type: string    
      x-ngsi:    
        type: Property    
    operationTemperatureMax:    
      description: 'Property. Allowable operation ambient (air, fluid) temperature range. Usually measured in degrees Kelvin (K).'    
      type: number    
      x-ngsi:    
        type: Property    
    operationTemperatureMin:    
      description: 'Property. Allowable operation ambient (air, fluid) temperature range. Usually measured in degrees Kelvin (K).'    
      type: number    
      x-ngsi:    
        type: Property    
    orientation:    
      description: Property. The intended orientation for the damper as specified by the manufacturer.    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *damper_-_properties_-_iscontainedinbuildingspace_-_anyof    
        description: Property. Unique identifier of the entity    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    temperatureRating:    
      description: Property. Temperature rating. Usually measured in degrees Kelvin (K).    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: Property. It must be equal to `Damper`.    
      enum:    
        - Damper    
      type: string    
      x-ngsi:    
        type: Property    
    workingPressureMax:    
      description: 'Property. Maximum working pressure. Usually measured in Pascals (Pa, N/m2).'    
      type: number    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Damper"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Damper/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Damper/schema.json    
  x-model-tags: SAREF Damper SMART DATA MODELS    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### Dämpfer NGSI-v2 Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen Damper im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Damper:65c94159-bfe6-416d-b02c-283479048fe3",  
  "type": "Damper",  
  "airFlowRateMax": 0.5927918101987754,  
  "bladeAction": "Belize Dollar",  
  "bladeEdge": "frictionless",  
  "bladeShape": "intermediate",  
  "bladeThickness": 0.5665758025960763,  
  "closeOffRating": 0.8924252696459434,  
  "faceArea": 0.45839947738381925,  
  "frameDepth": 0.6687870848219263,  
  "frameThickness": 0.6594470368135407,  
  "frameType": "Ergonomic",  
  "leakageFullyClosed": 0.052627216627954665,  
  "nominalAirFlowRate": 0.7333602290466408,  
  "numberOfBlades": 0.3476917428528077,  
  "openPressureDrop": 0.8991384789588308,  
  "operation": "Implemented",  
  "operationMode": "supply",  
  "operationTemperatureMax": 0.07772736087657628,  
  "operationTemperatureMin": 0.4857292385786113,  
  "orientation": "reboot",  
  "temperatureRating": 0.4909792118139581,  
  "workingPressureMax": 0.10839736205746486,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:c25bebe3-d546-4942-be72-9468ce218070",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:326da1c1-440d-4200-b598-a84e3bf5fdc1",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:007e61a9-027a-4662-a7a0-1e9e48f57886",  
    "urn:ngsi-ld:System:59945456-4e66-4c84-b637-7c771479a9f3",  
    "urn:ngsi-ld:System:023e0706-8d3d-411b-9e97-994a870341cd"  
  ],  
  "hasManufacturer": "Damper Company Inc.",  
  "hasModel": "Damper 0.1.2",  
  "dateCreated": "2023-01-25T18:10:59Z",  
  "dateModified": "2023-01-26T07:49:53Z",  
  "source": "Import",  
  "name": "Damper",  
  "alternateName": "Damper type 2",  
  "description": "Damper of limited Damper types",  
  "dataProvider": "IFC file"  
}  
```  
</details>  
#### Dämpfer NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen Dämpfer im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Damper:30830dab-6aa5-4dd1-9e48-d6ac7e24e4bf",  
  "type": "Damper",  
  "airFlowRateMax": {  
    "type": "Measurement",  
    "value":  0.13813389168852752  
  },  
  "bladeAction": {  
    "type": "Text",  
    "value": "Spur"  
  },  
  "bladeEdge": {  
    "type": "Text",  
    "value": "Personal Loan Account"  
  },  
  "bladeShape": {  
    "type": "Text",  
    "value": "Human"  
  },  
  "bladeThickness": {  
    "type": "Measurement",  
    "value":  0.35230461364031296  
  },  
  "closeOffRating": {  
    "type": "Measurement",  
    "value":  0.171775838539866  
  },  
  "faceArea": {  
    "type": "Measurement",  
    "value": 0.4212393478883142  
  },  
  "frameDepth": {  
    "type": "Measurement",  
    "value": 0.8035081586701794  
  },  
  "frameThickness": {  
    "type": "Measurement",  
    "value":  0.28946308913206176  
  },  
  "frameType": {  
    "type": "Text",  
    "value": "Balanced"  
  },  
  "leakageFullyClosed": {  
    "type": "Measurement",  
    "value":  0.44075236436472953  
  },  
  "nominalAirFlowRate": {  
    "type": "Measurement",  
    "value":0.47305378645729657  
  },  
  "numberOfBlades": {  
    "type": "Float",  
    "value": 0.8083872561368712  
  },  
  "openPressureDrop": {  
    "type": "Measurement",  
    "value": 0.9106213284285767  
  },  
  "operation": {  
    "type": "Text",  
    "value": "Handcrafted Concrete Computer"  
  },  
  "operationMode": {  
    "type": "DamperOperationMode",  
    "value": "supply"  
  },  
  "operationTemperatureMax": {  
    "type": "Measurement",  
    "value":  0.87576324331876  
  },  
  "operationTemperatureMin": {  
    "type": "Measurement",  
    "value":  0.3952529455728351  
  },  
  "orientation": {  
    "type": "Text",  
    "value": "Mozambique"  
  },  
  "temperatureRating": {  
    "type": "Measurement",  
    "value":  0.43326401348250587  
  },  
  "workingPressureMax": {  
    "type": "Measurement",  
    "value":  0.2695729035947665  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:BuildingSpace:f19ff450-12f4-472a-985e-40b163530ccd"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:PhysicalObject:ee6c23f3-7261-4807-b3e3-703588646f02"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:a8f8f637-52c0-491d-890e-2806ffbdc6cd"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:7f5f939e-9a41-4ca6-95ff-4ece8ffec42c"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:ff7924ea-c532-40c9-a1ac-449c76216073"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Damper Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Damper 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T15:13:23.9679787+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T16:00:58.1902016+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Damper"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Damper type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Damper of limited Damper types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### Dämpfer NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen Damper im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Damper:65c94159-bfe6-416d-b02c-283479048fe3",  
  "type": "Damper",  
  "airFlowRateMax": 0.5927918101987754,  
  "bladeAction": "Belize Dollar",  
  "bladeEdge": "frictionless",  
  "bladeShape": "intermediate",  
  "bladeThickness": 0.5665758025960763,  
  "closeOffRating": 0.8924252696459434,  
  "faceArea": 0.45839947738381925,  
  "frameDepth": 0.6687870848219263,  
  "frameThickness": 0.6594470368135407,  
  "frameType": "Ergonomic",  
  "leakageFullyClosed": 0.052627216627954665,  
  "nominalAirFlowRate": 0.7333602290466408,  
  "numberOfBlades": 0.3476917428528077,  
  "openPressureDrop": 0.8991384789588308,  
  "operation": "Implemented",  
  "operationMode": "supply",  
  "operationTemperatureMax": 0.07772736087657628,  
  "operationTemperatureMin": 0.4857292385786113,  
  "orientation": "reboot",  
  "temperatureRating": 0.4909792118139581,  
  "workingPressureMax": 0.10839736205746486,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:c25bebe3-d546-4942-be72-9468ce218070",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:326da1c1-440d-4200-b598-a84e3bf5fdc1",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:007e61a9-027a-4662-a7a0-1e9e48f57886",  
    "urn:ngsi-ld:System:59945456-4e66-4c84-b637-7c771479a9f3",  
    "urn:ngsi-ld:System:023e0706-8d3d-411b-9e97-994a870341cd"  
  ],  
  "hasManufacturer": "Damper Company Inc.",  
  "hasModel": "Damper 0.1.2",  
  "dateCreated": "2023-01-25T18:10:59Z",  
  "dateModified": "2023-01-26T07:49:53Z",  
  "source": "Import",  
  "name": "Damper",  
  "alternateName": "Damper type 2",  
  "description": "Damper of limited Damper types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### Dämpfer NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen Dämpfer im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Damper:99cb9b35-5f17-4e4d-89bb-e9d7bb88c2ba",  
  "type": "Damper",  
  "airFlowRateMax": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-26T10:15:08Z",  
    "value": 0.46010915943742847  
  },  
  "bladeAction": {  
    "type": "Property",  
    "value": "microchip"  
  },  
  "bladeEdge": {  
    "type": "Property",  
    "value": "Village"  
  },  
  "bladeShape": {  
    "type": "Property",  
    "value": "Netherlands Antillian Guilder"  
  },  
  "bladeThickness": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-25T21:36:37Z",  
    "value": 0.5214778377905084  
  },  
  "closeOffRating": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-25T18:21:40Z",  
    "value": 0.8241451329002358  
  },  
  "faceArea": {  
    "type": "Property",  
    "unitCode": "m2",  
    "observedAt": "2023-01-25T20:36:04Z",  
    "value": 0.6197704906516315  
  },  
  "frameDepth": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T14:05:58Z",  
    "value": 0.19371235604272175  
  },  
  "frameThickness": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-25T21:48:43Z",  
    "value": 0.630746648821536  
  },  
  "frameType": {  
    "type": "Property",  
    "value": "SAS"  
  },  
  "leakageFullyClosed": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-25T21:59:27Z",  
    "value": 0.8430168839934075  
  },  
  "nominalAirFlowRate": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-26T06:30:50Z",  
    "value": 0.8419372074040988  
  },  
  "numberOfBlades": {  
    "type": "Property",  
    "value": 0.2730424937241438  
  },  
  "openPressureDrop": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-26T04:03:50Z",  
    "value": 0.25493844227297535  
  },  
  "operation": {  
    "type": "Property",  
    "value": "partnerships"  
  },  
  "operationMode": {  
    "type": "Property",  
    "value": "exhaust"  
  },  
  "operationTemperatureMax": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T22:15:50Z",  
    "value": 0.4402985682699154  
  },  
  "operationTemperatureMin": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T11:49:40Z",  
    "value": 0.0015019955460002787  
  },  
  "orientation": {  
    "type": "Property",  
    "value": "Metrics"  
  },  
  "temperatureRating": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T16:28:22Z",  
    "value": 0.6012606116766228  
  },  
  "workingPressureMax": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-26T09:39:16Z",  
    "value": 0.320862748056973  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:573f5e7a-806c-4deb-878c-365ef09fe4d2"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:0cbecfb0-1008-4c54-99f6-510fba847457"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:972e3b8b-9613-4b3a-a798-f3e56587d999"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:0d09725f-1468-4352-92e9-39d0b647a683"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:0c5bf106-93a0-4eb9-a15d-a0d834088c94"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Damper Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Damper 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T10:37:53Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T10:42:54Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Damper"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Damper type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Damper of limited Damper types"  
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
