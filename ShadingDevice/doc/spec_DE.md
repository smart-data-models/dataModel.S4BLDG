<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entität: ShadingDevice    
======================<!-- /10-Header -->    
<!-- 15-License -->    
[Offene Lizenz](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/ShadingDevice/LICENSE.md)    
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Globale Beschreibung: **Beschattungsvorrichtungen sind zweckmäßige Vorrichtungen zum Schutz vor Sonnenlicht, vor natürlichem Licht oder als Sichtschutz. Beschattungsvorrichtungen können Teil der Fassade sein oder im Inneren des Gebäudes angebracht werden, sie können fest oder beweglich sein.**    
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
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `hasManufacturer[string]`: Eine Beziehung zur Identifizierung des Herstellers einer Entität (z. B. eines Geräts). Der Wert sollte eine Zeichenkette oder eine Zeichenkette mit Sprachkennzeichen sein  - `hasModel[string]`: Eine Beziehung, die das Modell einer Entität (z. B. eines Geräts) identifiziert. Als Wert wird eine Zeichenkette oder eine Zeichenkette mit Sprach-Tag erwartet  - `id[*]`: Eindeutiger Bezeichner der Entität  - `isContainedInBuildingSpace[*]`: Eine Einheit, die zur Definition der physischen Räume des Gebäudes verwendet wird. Ein Gebäudebereich enthält Geräte oder Gebäudeobjekte. (GebäudeRaum)  - `isContainedInPhysicalObject[*]`: Jedes Objekt, das eine eigene Raumregion hat.  (Definition entnommen aus der DUL-Ontologie) (PhysicalObject)  - `isExternal[boolean]`: Angabe, ob das Element für die Verwendung im Außenbereich vorgesehen ist (TRUE) oder nicht (FALSE). Wenn (TRUE) es sich um ein Außenelement handelt und es nach außen gerichtet ist  - `isSubSystemOf[array]`: Ein Verweis auf ein oder mehrere Systeme, zu denen dieses physische Objekt gehört  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `mechanicalOperated[boolean]`: Angabe, ob das Element maschinell (TRUE) oder nicht, d.h. manuell (FALSE) bedient wird  - `name[string]`: Der Name dieses Artikels  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `roughness[string]`: Ein Maß für die vertikalen Abweichungen der Oberfläche  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `shadingDeviceType[string]`: Gibt den Typ der Beschattungseinrichtung an  - `solarReflectance[number]`: (Rsol): Der Anteil der einfallenden Sonnenstrahlung, der von einem Beschattungssystem reflektiert wird (auch _e genannt). Beachten Sie die folgende Gleichung Asol + Rsol + Tsol = 1  - `solarTransmittance[number]`: (Tsol) Der Anteil der einfallenden Sonnenstrahlung, der direkt durch ein Beschattungssystem geht (auch _e genannt). Beachten Sie die folgende Gleichung Asol + Rsol + Tsol = 1  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `thermalTransmittance[number]`: Geschwindigkeit, mit der Energie durch einen Körper übertragen wird. Wird normalerweise in Watt/m2 Kelvin gemessen.  - `type[string]`: Es muss gleich `ShadingDevice` sein  - `visibleLightReflectance[number]`: Anteil des sichtbaren Lichts, der bei normalem Lichteinfall von der Verglasung reflektiert wird. Es ist ein Wert ohne Einheit  - `visibleLightTransmittance[number]`: Anteil des sichtbaren Lichts, der das Schattierungssystem bei normalem Einfall passiert. Es ist ein Wert ohne Einheit  <!-- /30-PropertiesList -->    
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
ShadingDevice:      
  description: 'Shading devices are purpose built devices to protect from the sunlight, from natural light, or screening them from view. Shading devices can form part of the facade or can be mounted inside the building, they can be fixed or operable.'      
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
    isExternal:      
      description: Indication whether the element is designed for use in the exterior (TRUE) or not (FALSE). If (TRUE) it is an external element and faces the outside of the building      
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
    mechanicalOperated:      
      description: 'Indication whether the element is operated machanically (TRUE) or not, i.e. manually (FALSE)'      
      type: boolean      
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
    roughness:      
      description: A measure of the vertical deviations of the surface      
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
    shadingDeviceType:      
      description: Specifies the type of shading device      
      type: string      
      x-ngsi:      
        type: Property      
    solarReflectance:      
      description: '(Rsol): The ratio of incident solar radiation that is reflected by a shading system (also named _e). Note the following equation Asol + Rsol + Tsol = 1'      
      type: number      
      x-ngsi:      
        type: Property      
    solarTransmittance:      
      description: (Tsol) The ratio of incident solar radiation that directly passes through a shading system (also named _e). Note the following equation Asol + Rsol + Tsol = 1      
      type: number      
      x-ngsi:      
        type: Property      
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    thermalTransmittance:      
      description: Rate at which energy is transmitted through a body. Usually measured in Watts/m2 Kelvin      
      type: number      
      x-ngsi:      
        type: Property      
    type:      
      description: It must be equal to `ShadingDevice`      
      enum:      
        - ShadingDevice      
      type: string      
      x-ngsi:      
        type: Property      
    visibleLightReflectance:      
      description: Fraction of the visible light that is reflected by the glazing at normal incidence. It is a value without unit      
      type: number      
      x-ngsi:      
        type: Property      
    visibleLightTransmittance:      
      description: Fraction of the visible light that passes the shading system at normal incidence. It is a value without unit      
      type: number      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:ShadingDevice"      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/ShadingDevice/LICENSE.md      
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/ShadingDevice/schema.json      
  x-model-tags: SAREF ShadingDevice      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Beispiel-Nutzlasten    
#### ShadingDevice NGSI-v2 key-values Beispiel    
Hier ist ein Beispiel für ein ShadingDevice im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:ShadingDevice:03281d48-cb47-4061-9208-b2a380b3d7cd",  
  "type": "ShadingDevice",  
  "isExternal": false,  
  "mechanicalOperated": true,  
  "roughness": "Executive",  
  "shadingDeviceType": "client-driven",  
  "solarReflectance": 0.7901767410172098,  
  "solarTransmittance": 0.5537106205704284,  
  "thermalTransmittance": 0.9786915841160174,  
  "visibleLightReflectance": 0.7194478774053882,  
  "visibleLightTransmittance": 0.8973320246848571,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:3f4442cb-0f79-4dad-81ba-69879612f561",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:de04c9b6-2d78-491f-987a-085ea71f747b",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:fd063381-99e7-4b7d-8936-cd66932ba1e7",  
    "urn:ngsi-ld:System:5bfac8cc-a08e-4bc8-a9e8-474e8db84d73",  
    "urn:ngsi-ld:System:a4eef133-5e5d-4051-8b37-bf89e468f019"  
  ],  
  "hasManufacturer": "ShadingDevice Company Inc.",  
  "hasModel": "ShadingDevice 0.1.2",  
  "dateCreated": "2023-01-26T07:18:28Z",  
  "dateModified": "2023-01-26T08:58:08Z",  
  "source": "Import",  
  "name": "ShadingDevice",  
  "alternateName": "ShadingDevice type 2",  
  "description": "ShadingDevice of limited ShadingDevice types",  
  "dataProvider": "IFC file"  
}  
```  
</details>    
#### ShadingDevice NGSI-v2 normalisiert Beispiel    
Hier ist ein Beispiel für ein ShadingDevice im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:ShadingDevice:b3c3bd8f-6f5a-400a-b43c-99c32bf7d036",  
  "type": "ShadingDevice",  
  "isExternal": {  
    "type": "Boolean",  
    "value": true  
  },  
  "mechanicalOperated": {  
    "type": "Boolean",  
    "value": false  
  },  
  "roughness": {  
    "type": "Text",  
    "value": "Home Loan Account"  
  },  
  "shadingDeviceType": {  
    "type": "Text",  
    "value": "program"  
  },  
  "solarReflectance": {  
    "type": "Number",  
    "value": 0.23462582512353236  
  },  
  "solarTransmittance": {  
    "type": "Number",  
    "value": 0.569468324137257  
  },  
  "thermalTransmittance": {  
    "type": "Number",  
    "value": 0.315308180363743  
  },  
  "visibleLightReflectance": {  
    "type": "Number",  
    "value": 0.6167477347282538  
  },  
  "visibleLightTransmittance": {  
    "type": "Number",  
    "value": 0.27849116636487137  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:BuildingSpace:6d6d4b35-2d0f-4590-bd7d-1e5cdc1d71fe"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:PhysicalObject:ff501e6f-1fbf-4dd4-9537-b3b6668f156b"  
  },  
  "isSubSystemOf": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:System:6d7f1004-c306-4d6b-8b95-d661e62087df",  
      "urn:ngsi-ld:System:9eedb406-9b0a-466e-99bf-d8b4721af694",  
      "urn:ngsi-ld:System:c485e374-da84-4bff-8a79-7d35bdcd0dab"  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "ShadingDevice Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "ShadingDevice 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T15:18:47.9518072+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T11:03:03.3618393+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "ShadingDevice"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "ShadingDevice type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "ShadingDevice of limited ShadingDevice types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>    
#### ShadingDevice NGSI-LD key-values Beispiel    
Hier ist ein Beispiel für ein ShadingDevice im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:ShadingDevice:03281d48-cb47-4061-9208-b2a380b3d7cd",  
  "type": "ShadingDevice",  
  "isExternal": false,  
  "mechanicalOperated": true,  
  "roughness": "Executive",  
  "shadingDeviceType": "client-driven",  
  "solarReflectance": 0.7901767410172098,  
  "solarTransmittance": 0.5537106205704284,  
  "thermalTransmittance": 0.9786915841160174,  
  "visibleLightReflectance": 0.7194478774053882,  
  "visibleLightTransmittance": 0.8973320246848571,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:3f4442cb-0f79-4dad-81ba-69879612f561",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:de04c9b6-2d78-491f-987a-085ea71f747b",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:fd063381-99e7-4b7d-8936-cd66932ba1e7",  
    "urn:ngsi-ld:System:5bfac8cc-a08e-4bc8-a9e8-474e8db84d73",  
    "urn:ngsi-ld:System:a4eef133-5e5d-4051-8b37-bf89e468f019"  
  ],  
  "hasManufacturer": "ShadingDevice Company Inc.",  
  "hasModel": "ShadingDevice 0.1.2",  
  "dateCreated": "2023-01-26T07:18:28Z",  
  "dateModified": "2023-01-26T08:58:08Z",  
  "source": "Import",  
  "name": "ShadingDevice",  
  "alternateName": "ShadingDevice type 2",  
  "description": "ShadingDevice of limited ShadingDevice types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>    
#### ShadingDevice NGSI-LD normalisiert Beispiel    
Hier ist ein Beispiel für ein ShadingDevice im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:ShadingDevice:98dd5d05-db70-4ebb-a39c-e286063cb137",  
  "type": "ShadingDevice",  
  "isExternal": {  
    "type": "Property",  
    "value": true  
  },  
  "mechanicalOperated": {  
    "type": "Property",  
    "value": true  
  },  
  "roughness": {  
    "type": "Property",  
    "value": "Practical Rubber Cheese"  
  },  
  "shadingDeviceType": {  
    "type": "Property",  
    "value": "parsing"  
  },  
  "solarReflectance": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T03:37:18Z",  
    "value": 0.378910710384914  
  },  
  "solarTransmittance": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T09:24:57Z",  
    "value": 0.9404860966072789  
  },  
  "thermalTransmittance": {  
    "type": "Property",  
    "unitCode": "Kelvin",  
    "observedAt": "2023-01-26T12:37:04Z",  
    "value": 0.471443015298326  
  },  
  "visibleLightReflectance": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T06:09:46Z",  
    "value": 0.7789148596577641  
  },  
  "visibleLightTransmittance": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T05:43:18Z",  
    "value": 0.9110422065316075  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:0bfda01f-c7bd-4db3-9a81-cfeb051cf629"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:53171831-ae73-45fa-8f15-b1c034e5b2af"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:b9d614e5-32c2-47cd-b5ba-23b2c8ed67ea"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:6048cde5-df44-4963-b770-29ace8711405"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:e2c351bf-c825-4bc9-a7ca-dc96552b8e38"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "ShadingDevice Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "ShadingDevice 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T15:37:39Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-25T17:44:25Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "ShadingDevice"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "ShadingDevice type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "ShadingDevice of limited ShadingDevice types"  
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
