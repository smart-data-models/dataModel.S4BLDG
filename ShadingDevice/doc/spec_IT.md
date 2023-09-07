<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: ShadingDevice  
=====================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/ShadingDevice/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **I dispositivi di ombreggiamento sono dispositivi costruiti appositamente per proteggere dalla luce solare, dalla luce naturale o per schermare la vista. I dispositivi di ombreggiamento possono far parte della facciata o essere montati all'interno dell'edificio, possono essere fissi o azionabili **.  
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
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `hasManufacturer[string]`: Una relazione che identifica il produttore di un'entità (ad esempio, un dispositivo). Si prevede che il valore sia una stringa o una stringa con tag linguistico  - `hasModel[string]`: Una relazione che identifica il modello di un'entità (ad esempio, un dispositivo). Il valore dovrebbe essere una stringa o una stringa con tag lingua  - `id[*]`: Identificatore univoco dell'entità  - `isContainedInBuildingSpace[*]`: Entità utilizzata per definire gli spazi fisici dell'edificio. Uno spazio dell'edificio contiene dispositivi o oggetti dell'edificio. (Spazio edificio)  - `isContainedInPhysicalObject[*]`: Qualsiasi oggetto che abbia una regione spaziale propria.  (Definizione estratta dall'ontologia DUL) (PhysicalObject)  - `isExternal[boolean]`: Indica se l'elemento è progettato per essere utilizzato all'esterno (VERO) o no (FALSO). Se (VERO) si tratta di un elemento esterno e rivolto verso l'esterno dell'edificio  - `isSubSystemOf[array]`: Un riferimento a uno o più sistemi di cui l'oggetto fisico fa parte.  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `mechanicalOperated[boolean]`: Indica se l'elemento è azionato meccanicamente (TRUE) o meno, cioè manualmente (FALSE).  - `name[string]`: Il nome di questo elemento  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `roughness[string]`: Una misura delle deviazioni verticali della superficie  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `shadingDeviceType[string]`: Specifica il tipo di dispositivo di ombreggiatura  - `solarReflectance[number]`: (Rsol): Il rapporto tra la radiazione solare incidente e quella riflessa da un sistema di schermatura (chiamato anche _e). Si noti la seguente equazione Asol + Rsol + Tsol = 1  - `solarTransmittance[number]`: (Tsol) Il rapporto tra la radiazione solare incidente e quella che passa direttamente attraverso un sistema di schermatura (chiamato anche _e). Si noti la seguente equazione Asol + Rsol + Tsol = 1  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `thermalTransmittance[number]`: Velocità di trasmissione dell'energia attraverso un corpo. Di solito si misura in Watt/m2 Kelvin  - `type[string]`: Deve essere uguale a `ShadingDevice`.  - `visibleLightReflectance[number]`: Frazione della luce visibile che viene riflessa dalla vetrata a incidenza normale. È un valore senza unità di misura  - `visibleLightTransmittance[number]`: Frazione della luce visibile che passa il sistema di ombreggiatura a incidenza normale. È un valore senza unità di misura  <!-- /30-PropertiesList -->  
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
## Esempi di payload  
#### ShadingDevice NGSI-v2 valori-chiave Esempio  
Ecco un esempio di ShadingDevice in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### ShadingDevice NGSI-v2 normalizzato Esempio  
Ecco un esempio di ShadingDevice in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
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
    "type": "Measurement",  
    "value": 0.23462582512353236  
  },  
  "solarTransmittance": {  
    "type": "Measurement",  
    "value": 0.569468324137257  
  },  
  "thermalTransmittance": {  
    "type": "Measurement",  
    "value": 0.315308180363743  
  },  
  "visibleLightReflectance": {  
    "type": "Measurement",  
    "value": 0.6167477347282538  
  },  
  "visibleLightTransmittance": {  
    "type": "Measurement",  
    "value": 0.27849116636487137  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:BuildingSpace:6d6d4b35-2d0f-4590-bd7d-1e5cdc1d71fe"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:PhysicalObject:ff501e6f-1fbf-4dd4-9537-b3b6668f156b"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:6d7f1004-c306-4d6b-8b95-d661e62087df"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:9eedb406-9b0a-466e-99bf-d8b4721af694"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:c485e374-da84-4bff-8a79-7d35bdcd0dab"  
      }  
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
#### ShadingDevice Valori-chiave NGSI-LD Esempio  
Ecco un esempio di ShadingDevice in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### ShadingDevice NGSI-LD normalizzato Esempio  
Ecco un esempio di ShadingDevice in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si usano opzioni e restituisce i dati di contesto di una singola entità.  
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
