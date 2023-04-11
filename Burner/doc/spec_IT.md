<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: Bruciatore  
==================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Burner/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Un bruciatore è un dispositivo che converte il combustibile in calore attraverso la combustione. Comprende bruciatori a gas, a olio e a legna **.  
versione: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated[string]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateModified[string]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `description[string]`: Descrizione dell'articolo  - `energySource[string]`: Proprietà. La fonte di energia. Enumerazione che definisce la fonte di energia o il combustibile bruciato per generare calore.  - `hasManufacturer[string]`: Proprietà. Una relazione che identifica il produttore di un'entità (ad esempio, un dispositivo). Il valore dovrebbe essere una stringa o una stringa con un tag di lingua.  - `hasModel[string]`: Proprietà. Una relazione che identifica il modello di un'entità (ad esempio, un dispositivo). Il valore dovrebbe essere una stringa o una stringa con un tag di lingua.  - `id[*]`: Identificatore univoco dell'entità  - `isContainedInBuildingSpace[*]`: Relazione. Un'entità utilizzata per definire gli spazi fisici dell'edificio. Uno spazio dell'edificio contiene dispositivi o oggetti dell'edificio. (Spazio edificio)  - `isContainedInPhysicalObject[*]`: Relazione. Qualsiasi oggetto che abbia una regione spaziale appropriata.  (Definizione estratta dall'ontologia DUL) (PhysicalObject)  - `isSubSystemOf[array]`: Relazione. Un riferimento a uno o più sistemi di cui questo Oggetto fisico fa parte.  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento.  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `type[string]`: Proprietà. Deve essere uguale a `Burner`.  <!-- /30-PropertiesList -->  
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
Burner:    
  description: 'A burner is a device that converts fuel into heat through combustion. It includes gas, oil, and wood burners.'    
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
    energySource:    
      description: Property. The source of energy. Enumeration defining the energy source or fuel combusted to generate heat.    
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
      anyOf: &burner_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      anyOf: *burner_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *burner_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *burner_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
        anyOf: *burner_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      description: Property. It must be equal to `Burner`.    
      enum:    
        - Burner    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Burner"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Burner/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Burner/schema.json    
  x-model-tags: SAREF Burner    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### Bruciatore NGSI-v2 valori-chiave Esempio  
Ecco un esempio di un masterizzatore in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Burner:57ee4f97-e73f-42b7-a5d1-abadac0160df",  
  "type": "Burner",  
  "energySource": "Hawaii",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:b7a42278-ecad-4219-bcfb-61044ba28feb",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:05c6475a-3aae-489b-8379-516e0d24d950",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:abc190c6-e33a-4e70-9538-de5fb54a53dd",  
    "urn:ngsi-ld:System:6311081e-c999-45a0-8856-510f4d756c8b",  
    "urn:ngsi-ld:System:30f0aac4-ce5a-465a-97d7-f261767bff28"  
  ],  
  "hasManufacturer": "Burner Company Inc.",  
  "hasModel": "Burner 0.1.2",  
  "dateCreated": "2023-01-26T11:10:49Z",  
  "dateModified": "2023-01-26T04:11:49Z",  
  "source": "Import",  
  "name": "Burner",  
  "alternateName": "Burner type 2",  
  "description": "Burner of limited Burner types",  
  "dataProvider": "IFC file"  
}  
```  
</details>  
#### Bruciatore NGSI-v2 normalizzato Esempio  
Ecco un esempio di un masterizzatore in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Burner:13aa97b0-0dea-4c18-91e3-bdd384861b75",  
  "type": "Burner",  
  "energySource": {  
    "type": "Text",  
    "value": "Creative"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:BuildingSpace:86af140b-763f-4bd0-93cc-91a0d601ad28"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:PhysicalObject:925b1db4-c39f-4a17-94db-7914d7eb703e"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:System:f5f4b44d-9071-4234-b20a-56cb3e28aa26"  
      },  
      {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:System:0686ff8c-1c6e-4a06-a955-4e3f17bbe9ee"  
      },  
      {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:System:5e7341dd-71a3-445c-9623-98331d97c002"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Burner Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Burner 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T14:50:18.0448295+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T22:03:55.6685756+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Burner"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Burner type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Burner of limited Burner types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### Bruciatore NGSI-LD valori chiave Esempio  
Ecco un esempio di un masterizzatore in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Burner:f3031bdd-1200-46ef-a4fd-d4cf75e7fc40",  
  "type": "Burner",  
  "energySource": "payment",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:69fbb678-74eb-4e22-bcbf-573de85bb807",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:30c80727-7e04-404d-bed6-173f7e64fad9",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:5057e5dd-a9aa-4068-baef-b145976f42a6",  
    "urn:ngsi-ld:System:371ac047-54b4-4ad0-83ee-3737918a4ac2",  
    "urn:ngsi-ld:System:cb261821-28ed-4fc8-9651-1017dba293b0"  
  ],  
  "hasManufacturer": "Burner Company Inc.",  
  "hasModel": "Burner 0.1.2",  
  "dateCreated": "2023-01-26T09:15:49Z",  
  "dateModified": "2023-01-26T05:16:31Z",  
  "source": "Import",  
  "name": "Burner",  
  "alternateName": "Burner type 2",  
  "description": "Burner of limited Burner types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### Bruciatore NGSI-LD normalizzato Esempio  
Ecco un esempio di un masterizzatore in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si usano le opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Burner:160a0bcf-c82a-46bd-b7d6-376fdc4fe4ee",  
  "type": "Burner",  
  "energySource": {  
    "type": "Property",  
    "value": "Texas"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:ec0a854e-9aeb-43c1-b7ea-a07cf7945d4c"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:f2b2b100-fa4b-4e5c-ae2a-c987d75c5807"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:7fa89a63-7d50-4eee-bbad-50e57f37555c"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:d258fa75-ee4a-4cca-95dc-6483203ed4ff"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:4224343e-8cbb-445a-8df3-e36e24fdcff1"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Burner Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Burner 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T19:58:22Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T06:56:25Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Burner"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Burner type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Burner of limited Burner types"  
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
