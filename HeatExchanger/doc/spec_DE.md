<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: HeatExchanger  
======================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/HeatExchanger/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Ein Wärmetauscher ist ein Gerät, das für die Wärmeübertragung zwischen nicht mischenden Medien wie Platten- und Rohrbündelwärmetauschern verwendet wird. HeatExchanger wird üblicherweise in wasserseitigen Verteilungssystemen verwendet, um Energie von einer Flüssigkeit in eine andere Flüssigkeit (in der Regel auf Wasserbasis) zurückzugewinnen, während AirToAirHeatRecovery in der Regel in luftseitigen Verteilungssystemen verwendet wird, um Energie von einem Gas in ein Gas (in der Regel Luft) zurückzugewinnen.**  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `arrangement[string]`: Eigenschaft. Definiert die grundlegenden Strömungsanordnungen für den Wärmetauscher: COUNTERFLOW: Gegenstrom-Wärmetauscheranordnung. CROSSFLOW: Kreuzstrom-Wärmetauscher-Anordnung. PARALLELFLOW: Parallelfluss-Wärmetauscher-Anordnung. MULTIPASS: Wärmetauscheranordnung mit mehreren Durchflüssen. SONSTIGE: Andere, oben nicht definierte Arten von Wärmetauschern mit Durchfluss.  - `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated[string]`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified[string]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description[string]`: Eine Beschreibung dieses Artikels  - `hasManufacturer[string]`: Eigenschaft. Eine Beziehung, die den Hersteller einer Entität (z. B. eines Geräts) identifiziert. Der Wert sollte eine Zeichenkette oder eine Zeichenkette mit Sprachkennzeichen sein.  - `hasModel[string]`: Eigenschaft. Eine Beziehung, die das Modell einer Entität (z. B. eines Geräts) identifiziert. Als Wert wird eine Zeichenkette oder eine Zeichenkette mit Sprachkennzeichen erwartet.  - `id[*]`: Eindeutiger Bezeichner der Entität  - `isContainedInBuildingSpace[*]`: Beziehung. Eine Einheit, die zur Definition der physischen Räume des Gebäudes verwendet wird. Ein Gebäudebereich enthält Geräte oder Gebäudeobjekte. (GebäudeRaum)  - `isContainedInPhysicalObject[*]`: Verwandtschaft. Jedes Objekt, das eine eigene Raumregion hat.  (Definition aus der DUL Ontologie) (PhysicalObject)  - `isSubSystemOf[array]`: Beziehung. Ein Verweis auf ein oder mehrere Systeme, zu denen dieses physische Objekt gehört.  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels.  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Es wird empfohlen, den voll qualifizierten Domänennamen des Quellanbieters oder die URL des Quellobjekts zu verwenden.  - `type[string]`: Eigenschaft. Sie muss gleich `HeatExchanger` sein.  <!-- /30-PropertiesList -->  
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
HeatExchanger:    
  description: 'A heat exchanger is a device used to provide heat transfer between non-mixing media such as plate and shell and tube heat exchangers. HeatExchanger is commonly used on water-side distribution systems to recover energy from a liquid to another liquid (typically water-based), whereas AirToAirHeatRecovery is commonly used on air-side distribution systems to recover energy from a gas to a gas (usually air).'    
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
    arrangement:    
      description: 'Property. Defines the basic flow arrangements for the heat exchanger: COUNTERFLOW: Counterflow heat exchanger arrangement. CROSSFLOW: Crossflow heat exchanger arrangement. PARALLELFLOW: Parallel flow heat exchanger arrangement. MULTIPASS: Multipass flow heat exchanger arrangement. OTHER: Other type of heat exchanger flow arrangement not defined above.'    
      type: string    
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
      anyOf: &heatexchanger_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      anyOf: *heatexchanger_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *heatexchanger_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *heatexchanger_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *heatexchanger_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    type:    
      description: Property. It must be equal to `HeatExchanger`.    
      enum:    
        - HeatExchanger    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:HeatExchanger"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/HeatExchanger/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/HeatExchanger/schema.json    
  x-model-tags: SAREF HeatExchanger    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### HeatExchanger NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für einen Wärmetauscher im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:HeatExchanger:b0f22640-66d7-4a7f-ab63-62b499e7e849",  
  "type": "HeatExchanger",  
  "arrangement": "calculating",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:04ee5ba4-9f7e-43fa-8c45-b756d6bd1b45",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:ca0a85a8-93e8-4cf1-a28b-03eb796f53a3",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:f746caae-43c4-48eb-b7d9-ab95bd858565",  
    "urn:ngsi-ld:System:bf897dfe-ac97-4e1d-8023-bae2465118b9",  
    "urn:ngsi-ld:System:9f9aec4e-7365-49ce-835b-5422973ae19a"  
  ],  
  "hasManufacturer": "HeatExchanger Company Inc.",  
  "hasModel": "HeatExchanger 0.1.2",  
  "dateCreated": "2023-01-26T11:52:54Z",  
  "dateModified": "2023-01-26T05:48:15Z",  
  "source": "Import",  
  "name": "HeatExchanger",  
  "alternateName": "HeatExchanger type 2",  
  "description": "HeatExchanger of limited HeatExchanger types",  
  "dataProvider": "IFC file"  
}  
```  
</details>  
#### HeatExchanger NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen Wärmetauscher im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-v2 kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:HeatExchanger:2fcd41c1-136e-4cff-b439-7c44260bcf66",  
  "type": "HeatExchanger",  
  "arrangement": {  
    "type": "Text",  
    "value": "Assistant"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:BuildingSpace:9ef5478c-5f5f-4d2c-81b3-5cb9317ee70f"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:PhysicalObject:d8a9c2c6-a3e9-414d-a8ac-a69f959d7b70"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:cce1367c-262f-41d6-88ca-6d3032cfb193"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:90db3c34-a2b8-4511-89cb-353fd855fce4"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:3bbddac3-223b-449d-884e-1cc4d04eeb79"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "HeatExchanger Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "HeatExchanger 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T07:35:03.9392521+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T21:26:27.4267913+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "HeatExchanger"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "HeatExchanger type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "HeatExchanger of limited HeatExchanger types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### Wärmetauscher NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen Wärmetauscher im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:HeatExchanger:8eb41206-4a42-4c26-a9ec-6c124d99d9e8",  
  "type": "HeatExchanger",  
  "arrangement": "bus",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:3d853493-b844-4211-b74c-e68b3eb511d3",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:e8054111-5920-4e1d-8832-c33a629673b2",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:46ac40f7-045b-4524-8592-aead52715c98",  
    "urn:ngsi-ld:System:7ec365c9-eef7-43ed-9511-d3aefe39afc4",  
    "urn:ngsi-ld:System:2f3a1c27-a079-4a8d-90f2-ee75c56a1c3e"  
  ],  
  "hasManufacturer": "HeatExchanger Company Inc.",  
  "hasModel": "HeatExchanger 0.1.2",  
  "dateCreated": "2023-01-26T12:05:41Z",  
  "dateModified": "2023-01-25T22:11:27Z",  
  "source": "Import",  
  "name": "HeatExchanger",  
  "alternateName": "HeatExchanger type 2",  
  "description": "HeatExchanger of limited HeatExchanger types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### HeatExchanger NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen Wärmetauscher im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:HeatExchanger:c46c932b-140d-4d0e-8e6c-23a71b24e0f1",  
  "type": "HeatExchanger",  
  "arrangement": {  
    "type": "Property",  
    "value": "Integration"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:c1be2cb8-f889-4ecb-a784-f69890a58887"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:0bd7f4d1-bfea-46a1-96ff-ef8ca5c3a860"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:de5626c3-0724-4126-9891-1a66ac44b329"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:024690f4-219f-4098-a217-bc1c554a7eb7"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:2a908d89-b5f0-4a0f-8b55-eb8433107ca0"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "HeatExchanger Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "HeatExchanger 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T19:13:00Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-25T22:12:50Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "HeatExchanger"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "HeatExchanger type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "HeatExchanger of limited HeatExchanger types"  
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
