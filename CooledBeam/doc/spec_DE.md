<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entität: CooledBeam    
===================<!-- /10-Header -->    
<!-- 15-License -->    
[Offene Lizenz](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/CooledBeam/LICENSE.md)    
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Globale Beschreibung: **Ein Kühlbalken (oder Kühlbalken) ist ein Gerät, das in der Regel zur Kühlung von Luft verwendet wird, indem eine Flüssigkeit wie z. B. gekühltes Wasser durch freiliegende Rippenrohre über einem Raum zirkuliert. Der Kühlbalken wird in der Regel über Kopf in der Nähe der Decke oder in der Decke montiert und nutzt die Konvektion, um den Raum darunter zu kühlen, indem er als Wärmesenke für die natürlich aufsteigende warme Luft des Raums dient. Sobald die Luft abgekühlt ist, fällt sie auf natürliche Weise zum Boden zurück, wo der Kreislauf von neuem beginnt.**    
Version: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste der Eigenschaften    
<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.    
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel, Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: Die Ortschaft, in der sich die Adresse befindet, und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: Die Region, in der sich der Ort befindet, und die auf dem Lande liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird.      
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: Die Straßenanschrift  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `coilLength[number]`: Länge der Spule. Normalerweise in Millimetern (mm) gemessen.  - `coilWidth[number]`: Breite der Spule. Normalerweise in Millimetern (mm) gemessen.  - `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `finishColor[string]`: Oberflächenfarbe für gekühlten Balken  - `hasManufacturer[string]`: Eine Beziehung zur Identifizierung des Herstellers einer Entität (z. B. eines Geräts). Der Wert sollte eine Zeichenkette oder eine Zeichenkette mit Sprachkennzeichen sein  - `hasModel[string]`: Eine Beziehung, die das Modell einer Entität (z. B. eines Geräts) identifiziert. Als Wert wird eine Zeichenkette oder eine Zeichenkette mit Sprach-Tag erwartet  - `id[*]`: Eindeutiger Bezeichner der Entität  - `integratedLightingType[string]`: Integrierte Beleuchtung im gekühlten Strahl  - `isContainedInBuildingSpace[*]`: Eine Einheit, die zur Definition der physischen Räume des Gebäudes verwendet wird. Ein Gebäudebereich enthält Geräte oder Gebäudeobjekte. (GebäudeRaum)  - `isContainedInPhysicalObject[*]`: Jedes Objekt, das eine eigene Raumregion hat.  (Definition entnommen aus der DUL-Ontologie) (PhysicalObject)  - `isFreeHanging[boolean]`: Handelt es sich um einen frei hängenden Typ (nicht in einer Zwischendecke montiert)?  - `isSubSystemOf[array]`: Ein Verweis auf ein oder mehrere Systeme, zu denen dieses physische Objekt gehört  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels  - `nominalCoolingCapacity[number]`: Nominale Kühlleistung. Wird normalerweise in Watt (W, J/s) gemessen.  - `nominalHeatingCapacity[number]`: Nominale Heizleistung. Wird normalerweise in Watt (W, J/s) gemessen.  - `nominalReturnWaterTemperatureCooling[number]`: Nenntemperatur des Rücklaufwassers (bezieht sich auf die Nennkühlleistung). Normalerweise gemessen in Grad Kelvin (K)  - `nominalReturnWaterTemperatureHeating[number]`: Nenntemperatur des Rücklaufwassers (bezieht sich auf die Nennheizleistung). Wird normalerweise in Grad Kelvin (K) gemessen.  - `nominalSorroundingHumidityCooling[number]`: Nominale Umgebungsfeuchte (bezieht sich auf die nominale Kühlleistung). Üblicherweise gemessen in Grad Kelvin (K)  - `nominalSorroundingTemperatureCooling[number]`: Nominale Umgebungstemperatur (bezieht sich auf die nominale Kühlleistung). Wird normalerweise in Grad Kelvin (K) gemessen.  - `nominalSorroundingTemperatureHeating[number]`: Nenn-Umgebungstemperatur (bezieht sich auf die Nenn-Heizleistung). Wird normalerweise in Grad Kelvin (K) gemessen.  - `nominalSupplyWaterTemperatureCooling[number]`: Nominale Vorlaufwassertemperatur (bezieht sich auf die nominale Kühlleistung). Wird normalerweise in Grad Kelvin (K) gemessen.  - `nominalSupplyWaterTemperatureHeating[number]`: Nenntemperatur des Vorlaufwassers (bezieht sich auf die Nennheizleistung). Wird normalerweise in Grad Kelvin (K) gemessen.  - `nominalWaterFlowCooling[number]`: Nennwasserdurchfluss (bezieht sich auf die Nennkühlleistung). Üblicherweise gemessen in m3/s  - `nominalWaterFlowHeating[number]`: Nennwasserdurchfluss (bezieht sich auf die Nennheizleistung). Üblicherweise gemessen in m3/s  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `pipeConnectionEnum[string]`: Die Art und Weise, wie das Rohr an den gekühlten Balken angeschlossen wird  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `type[string]`: Er muss gleich `CooledBeam` sein  - `waterFlowControlSystemType[string]`: Werkseitig eingebautes Wasserdurchflusskontrollsystem  - `waterPressureMax[number]`: Zulässiger Betriebsdruckbereich des Wasserkreislaufs. Üblicherweise gemessen in Pascal (Pa, N/m2)  - `waterPressureMin[number]`: Zulässiger Betriebsdruckbereich des Wasserkreislaufs. Üblicherweise gemessen in Pascal (Pa, N/m2)  <!-- /30-PropertiesList -->    
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
CooledBeam:      
  description: 'A cooled beam (or chilled beam) is a device typically used to cool air by circulating a fluid such as chilled water through exposed finned tubes above a space. Typically mounted overhead near or within a ceiling, the cooled beam uses convection to cool the space below it by acting as a heat sink for the naturally rising warm air of the space. Once cooled, the air naturally drops back to the floor where the cycle begins again.'      
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
    coilLength:      
      description: Length of coil. Usually measured in millimeters (mm)      
      type: number      
      x-ngsi:      
        type: Property      
    coilWidth:      
      description: Width of coil. Usually measured in millimeters (mm      
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
    finishColor:      
      description: Finish color for cooled beam      
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
    integratedLightingType:      
      description: Integrated lighting in cooled beam      
      type: string      
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
    isFreeHanging:      
      description: 'Is it free hanging type (not mounted in a false ceiling)?'      
      type: boolean      
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
    nominalCoolingCapacity:      
      description: 'Nominal cooling capacity. Usually measured in Watts (W, J/s)'      
      type: number      
      x-ngsi:      
        type: Property      
    nominalHeatingCapacity:      
      description: 'Nominal heating capacity. Usually measured in Watts (W, J/s)'      
      type: number      
      x-ngsi:      
        type: Property      
    nominalReturnWaterTemperatureCooling:      
      description: Nominal return water temperature (refers to nominal cooling capacity). Usually measured in degrees Kelvin (K)      
      type: number      
      x-ngsi:      
        type: Property      
    nominalReturnWaterTemperatureHeating:      
      description: Nominal return water temperature (refers to nominal heating capacity). Usually measured in degrees Kelvin (K)      
      type: number      
      x-ngsi:      
        type: Property      
    nominalSorroundingHumidityCooling:      
      description: Nominal surrounding humidity (refers to nominal cooling capacity). Usually measured in degrees Kelvin (K)      
      type: number      
      x-ngsi:      
        type: Property      
    nominalSorroundingTemperatureCooling:      
      description: Nominal surrounding temperature (refers to nominal cooling capacity). Usually measured in degrees Kelvin (K)      
      type: number      
      x-ngsi:      
        type: Property      
    nominalSorroundingTemperatureHeating:      
      description: Nominal surrounding temperature (refers to nominal heating capacity). Usually measured in degrees Kelvin (K)      
      type: number      
      x-ngsi:      
        type: Property      
    nominalSupplyWaterTemperatureCooling:      
      description: Nominal supply water temperature (refers to nominal cooling capacity). Usually measured in degrees Kelvin (K)      
      type: number      
      x-ngsi:      
        type: Property      
    nominalSupplyWaterTemperatureHeating:      
      description: Nominal supply water temperature (refers to nominal heating capacity). Usually measured in degrees Kelvin (K)      
      type: number      
      x-ngsi:      
        type: Property      
    nominalWaterFlowCooling:      
      description: Nominal water flow (refers to nominal cooling capacity). Usually measured in m3/s      
      type: number      
      x-ngsi:      
        type: Property      
    nominalWaterFlowHeating:      
      description: Nominal water flow (refers to nominal heating capacity). Usually measured in m3/s      
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
    pipeConnectionEnum:      
      description: The manner in which the pipe connection is made to the cooled beam      
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
      description: It must be equal to `CooledBeam`      
      enum:      
        - CooledBeam      
      type: string      
      x-ngsi:      
        type: Property      
    waterFlowControlSystemType:      
      description: Factory fitted waterflow control system      
      type: string      
      x-ngsi:      
        type: Property      
    waterPressureMax:      
      description: 'Allowable water circuit working pressure range. Usually measured in Pascals (Pa, N/m2)'      
      type: number      
      x-ngsi:      
        type: Property      
    waterPressureMin:      
      description: 'Allowable water circuit working pressure range. Usually measured in Pascals (Pa, N/m2)'      
      type: number      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:CooledBeam"      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/CooledBeam/LICENSE.md      
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/CooledBeam/schema.json      
  x-model-tags: SAREF CooledBeam      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Beispiel-Nutzlasten    
#### CooledBeam NGSI-v2 key-values Beispiel    
Hier ist ein Beispiel für einen CooledBeam im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:CooledBeam:82040ca8-778f-478d-a8fd-28485704919f",  
  "type": "CooledBeam",  
  "coilLength": 0.12136965337189098,  
  "coilWidth": 0.9739362570796377,  
  "finishColor": "deposit",  
  "integratedLightingType": "Metrics",  
  "isFreeHanging": false,  
  "nominalCoolingCapacity": 0.25517130161811685,  
  "nominalHeatingCapacity": 0.979299961039553,  
  "nominalReturnWaterTemperatureCooling": 0.8331575990645163,  
  "nominalReturnWaterTemperatureHeating": 0.8257910510708837,  
  "nominalSorroundingHumidityCooling": 0.08831404123432451,  
  "nominalSorroundingTemperatureCooling": 0.8951747110468832,  
  "nominalSorroundingTemperatureHeating": 0.7722529144575002,  
  "nominalSupplyWaterTemperatureCooling": 0.510069259798832,  
  "nominalSupplyWaterTemperatureHeating": 0.9682117435710755,  
  "nominalWaterFlowCooling": 0.640621498291464,  
  "nominalWaterFlowHeating": 0.3754874763938201,  
  "pipeConnectionEnum": "Falls",  
  "waterFlowControlSystemType": "Forks",  
  "waterPressureMax": 0.6809509740238233,  
  "waterPressureMin": 0.3372474470208946,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:29882bc5-9d20-4d25-b276-5bdf4f6981e1",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:13d83cbf-6e67-4d40-85da-46a7032fbde9",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:dfeed4f8-88d6-4475-89b3-71faa705f8a4",  
    "urn:ngsi-ld:System:23813ba9-d7b1-475b-b245-c32d08798cc3",  
    "urn:ngsi-ld:System:daa546ea-d20c-4761-98b2-e17e050b4625"  
  ],  
  "hasManufacturer": "CooledBeam Company Inc.",  
  "hasModel": "CooledBeam 0.1.2",  
  "dateCreated": "2023-01-26T05:29:03Z",  
  "dateModified": "2023-01-26T10:03:56Z",  
  "source": "Import",  
  "name": "CooledBeam",  
  "alternateName": "CooledBeam type 2",  
  "description": "CooledBeam of limited CooledBeam types",  
  "dataProvider": "IFC file"  
}  
```  
</details>    
#### CooledBeam NGSI-v2 normalisiert Beispiel    
Hier ist ein Beispiel für einen CooledBeam im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:CooledBeam:38dcdd25-ae94-441c-8409-218ec91e3006",  
  "type": "CooledBeam",  
  "coilLength": {  
    "type": "Number",  
    "value": 0.4277226249853211  
  },  
  "coilWidth": {  
    "type": "Number",  
    "value": 0.6183775851562611  
  },  
  "finishColor": {  
    "type": "Text",  
    "value": "Associate"  
  },  
  "integratedLightingType": {  
    "type": "Text",  
    "value": "Washington"  
  },  
  "isFreeHanging": {  
    "type": "Boolean",  
    "value": false  
  },  
  "nominalCoolingCapacity": {  
    "type": "Number",  
    "value": 0.45857043485420457  
  },  
  "nominalHeatingCapacity": {  
    "type": "Number",  
    "value": 0.37812382267356337  
  },  
  "nominalReturnWaterTemperatureCooling": {  
    "type": "Number",  
    "value": 0.973742767691913  
  },  
  "nominalReturnWaterTemperatureHeating": {  
    "type": "Number",  
    "value": 0.6848085584395665  
  },  
  "nominalSorroundingHumidityCooling": {  
    "type": "Number",  
    "value": 0.4100986776385609  
  },  
  "nominalSorroundingTemperatureCooling": {  
    "type": "Number",  
    "value": 0.039909771141081074  
  },  
  "nominalSorroundingTemperatureHeating": {  
    "type": "Number",  
    "value": 0.3023923557796515  
  },  
  "nominalSupplyWaterTemperatureCooling": {  
    "type": "Number",  
    "value": 0.7562940127899793  
  },  
  "nominalSupplyWaterTemperatureHeating": {  
    "type": "Number",  
    "value": 0.31198678394809454  
  },  
  "nominalWaterFlowCooling": {  
    "type": "Number",  
    "value": 0.40924277893308847  
  },  
  "nominalWaterFlowHeating": {  
    "type": "Number",  
    "value": 0.9345939456733873  
  },  
  "pipeConnectionEnum": {  
    "type": "Text",  
    "value": "extensible"  
  },  
  "waterFlowControlSystemType": {  
    "type": "Text",  
    "value": "Interactions"  
  },  
  "waterPressureMax": {  
    "type": "Number",  
    "value": 0.07837257218461391  
  },  
  "waterPressureMin": {  
    "type": "Number",  
    "value": 0.03742669539477306  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:BuildingSpace:3e03fe30-3728-4867-ab51-b147c2d3e63b"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:PhysicalObject:cfd9df05-18b1-44f4-b1ee-da55226255e9"  
  },  
  "isSubSystemOf": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:System:a4b0cda0-b373-4ae9-b2c7-e2cff5429e1e",  
      "urn:ngsi-ld:System:216f6f83-8bd1-456f-9bed-36dbec41a3aa",  
      "urn:ngsi-ld:System:d19ccffa-f134-46fc-8f9f-77656bb91649"  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "CooledBeam Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "CooledBeam 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T21:51:06.7954024+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T00:15:46.9435362+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "CooledBeam"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "CooledBeam type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "CooledBeam of limited CooledBeam types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>    
#### CooledBeam NGSI-LD key-values Beispiel    
Hier ist ein Beispiel für einen CooledBeam im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:CooledBeam:82040ca8-778f-478d-a8fd-28485704919f",  
  "type": "CooledBeam",  
  "coilLength": 0.12136965337189098,  
  "coilWidth": 0.9739362570796377,  
  "finishColor": "deposit",  
  "integratedLightingType": "Metrics",  
  "isFreeHanging": false,  
  "nominalCoolingCapacity": 0.25517130161811685,  
  "nominalHeatingCapacity": 0.979299961039553,  
  "nominalReturnWaterTemperatureCooling": 0.8331575990645163,  
  "nominalReturnWaterTemperatureHeating": 0.8257910510708837,  
  "nominalSorroundingHumidityCooling": 0.08831404123432451,  
  "nominalSorroundingTemperatureCooling": 0.8951747110468832,  
  "nominalSorroundingTemperatureHeating": 0.7722529144575002,  
  "nominalSupplyWaterTemperatureCooling": 0.510069259798832,  
  "nominalSupplyWaterTemperatureHeating": 0.9682117435710755,  
  "nominalWaterFlowCooling": 0.640621498291464,  
  "nominalWaterFlowHeating": 0.3754874763938201,  
  "pipeConnectionEnum": "Falls",  
  "waterFlowControlSystemType": "Forks",  
  "waterPressureMax": 0.6809509740238233,  
  "waterPressureMin": 0.3372474470208946,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:29882bc5-9d20-4d25-b276-5bdf4f6981e1",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:13d83cbf-6e67-4d40-85da-46a7032fbde9",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:dfeed4f8-88d6-4475-89b3-71faa705f8a4",  
    "urn:ngsi-ld:System:23813ba9-d7b1-475b-b245-c32d08798cc3",  
    "urn:ngsi-ld:System:daa546ea-d20c-4761-98b2-e17e050b4625"  
  ],  
  "hasManufacturer": "CooledBeam Company Inc.",  
  "hasModel": "CooledBeam 0.1.2",  
  "dateCreated": "2023-01-26T05:29:03Z",  
  "dateModified": "2023-01-26T10:03:56Z",  
  "source": "Import",  
  "name": "CooledBeam",  
  "alternateName": "CooledBeam type 2",  
  "description": "CooledBeam of limited CooledBeam types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>    
#### CooledBeam NGSI-LD normalisiert Beispiel    
Hier ist ein Beispiel für einen CooledBeam im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:CooledBeam:baa66543-6434-4e28-8e85-20b2b260d404",  
  "type": "CooledBeam",  
  "coilLength": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-25T18:59:14Z",  
    "value": 0.45413352830053977  
  },  
  "coilWidth": {  
    "type": "Property",  
    "unitCode": "m",  
    "observedAt": "2023-01-26T07:44:01Z",  
    "value": 0.2692385089640058  
  },  
  "finishColor": {  
    "type": "Property",  
    "value": "indigo"  
  },  
  "integratedLightingType": {  
    "type": "Property",  
    "value": "Graphical User Interface"  
  },  
  "isFreeHanging": {  
    "type": "Property",  
    "value": false  
  },  
  "nominalCoolingCapacity": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-26T09:40:29Z",  
    "value": 0.3030442126473498  
  },  
  "nominalHeatingCapacity": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-26T02:43:04Z",  
    "value": 0.7091959285173477  
  },  
  "nominalReturnWaterTemperatureCooling": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T10:09:02Z",  
    "value": 0.4048762377790246  
  },  
  "nominalReturnWaterTemperatureHeating": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T08:24:33Z",  
    "value": 0.33261295327987683  
  },  
  "nominalSorroundingHumidityCooling": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T12:36:33Z",  
    "value": 0.5632800434491262  
  },  
  "nominalSorroundingTemperatureCooling": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T11:31:42Z",  
    "value": 0.47265451181389695  
  },  
  "nominalSorroundingTemperatureHeating": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T18:37:57Z",  
    "value": 0.18090042184548072  
  },  
  "nominalSupplyWaterTemperatureCooling": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T21:17:20Z",  
    "value": 0.9122743224756777  
  },  
  "nominalSupplyWaterTemperatureHeating": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T17:52:00Z",  
    "value": 0.9207552089629301  
  },  
  "nominalWaterFlowCooling": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-25T15:05:33Z",  
    "value": 0.06592489938443258  
  },  
  "nominalWaterFlowHeating": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-26T13:42:04Z",  
    "value": 0.3446198206084118  
  },  
  "pipeConnectionEnum": {  
    "type": "Property",  
    "value": "SSL"  
  },  
  "waterFlowControlSystemType": {  
    "type": "Property",  
    "value": "supply-chains"  
  },  
  "waterPressureMax": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-25T17:35:39Z",  
    "value": 0.8610847602415933  
  },  
  "waterPressureMin": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-26T03:28:09Z",  
    "value": 0.9088584704707019  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:6689ca11-b361-48b4-950d-07edf1182e97"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:2e350952-8c19-46a2-a2c2-8d30c54d03cb"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:cf124c7e-8f71-424a-93b5-64643c889f30"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:a72f7b54-3f5c-4b66-9463-f20f7127cff6"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:ce488063-f9a9-44c4-ac0f-f79e2977a2d4"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "CooledBeam Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "CooledBeam 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T23:43:55Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-25T20:21:43Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "CooledBeam"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "CooledBeam type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "CooledBeam of limited CooledBeam types"  
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
