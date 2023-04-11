<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: Bobina  
==============<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Coil/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Una serpentina è un dispositivo utilizzato per garantire il trasferimento di calore tra mezzi non mescolanti. Un esempio comune è la serpentina di raffreddamento, che utilizza una serpentina alettata in cui circola acqua refrigerata, antigelo o refrigerante che viene utilizzato per rimuovere il calore dall'aria che si muove sulla superficie della serpentina. Una serpentina può essere utilizzata sia per il riscaldamento che per il raffreddamento, collocando una serie di tubi (la serpentina) che trasportano un fluido riscaldante o raffreddante in un flusso d'aria. La serpentina può essere costituita da tubi a forma di serpentina o da tubi alettati che offrono una superficie di trasferimento del calore più estesa.  Le serpentine possono essere utilizzate anche per i casi in cui non c'è flusso d'aria, come nel caso in cui siano incassate in una soletta del pavimento **.  
versione: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)- `airFlowRateMax[object]`: Proprietà. Portata d'aria massima consentita. Di solito si misura in m3/s.  - `airFlowRateMin[object]`: Proprietà. Portata d'aria minima consentita. Solitamente misurata in m3/s.  - `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated[string]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateModified[string]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `description[string]`: Descrizione dell'articolo  - `hasManufacturer[string]`: Proprietà. Una relazione che identifica il produttore di un'entità (ad esempio, un dispositivo). Il valore dovrebbe essere una stringa o una stringa con un tag di lingua.  - `hasModel[string]`: Proprietà. Una relazione che identifica il modello di un'entità (ad esempio, un dispositivo). Il valore dovrebbe essere una stringa o una stringa con un tag di lingua.  - `id[*]`: Identificatore univoco dell'entità  - `isContainedInBuildingSpace[*]`: Relazione. Un'entità utilizzata per definire gli spazi fisici dell'edificio. Uno spazio dell'edificio contiene dispositivi o oggetti dell'edificio. (Spazio edificio)  - `isContainedInPhysicalObject[*]`: Relazione. Qualsiasi oggetto che abbia una regione spaziale appropriata.  (Definizione estratta dall'ontologia DUL) (PhysicalObject)  - `isSubSystemOf[array]`: Relazione. Un riferimento a uno o più sistemi di cui questo Oggetto fisico fa parte.  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento.  - `nominalLatentCapacity[object]`: Proprietà. Capacità latente nominale. Solitamente misurata in Watt (W, J/s).  - `nominalSensibleCapacity[object]`: Proprietà. Capacità sensibile nominale. Solitamente misurata in Watt (W, J/s).  - `nominalUa[object]`: Proprietà. Valore nominale UA.  - `operationMode[string]`: Proprietà. Modalità di funzionamento di questa bobina.  - `operationTemperatureMax[object]`: Proprietà. Intervallo di temperatura ambiente (aria, fluido) consentito per il funzionamento. Di solito si misura in gradi Kelvin (K).  - `operationTemperatureMin[object]`: Proprietà. Intervallo di temperatura ambiente (aria, fluido) consentito per il funzionamento. Di solito si misura in gradi Kelvin (K).  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `placementType[string]`: Proprietà. Indica il modo in cui il dispositivo è stato progettato per essere collocato.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `type[string]`: Proprietà. Deve essere uguale a `Coil`.  <!-- /30-PropertiesList -->  
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
Coil:    
  description: 'A coil is a device used to provide heat transfer between non-mixing media. A common example is a cooling coil, which utilizes a finned coil in which circulates chilled water, antifreeze, or refrigerant that is used to remove heat from air moving across the surface of the coil. A coil may be used either for heating or cooling purposes by placing a series of tubes (the coil) carrying a heating or cooling fluid into an airstream. The coil may be constructed from tubes bundled in a serpentine form or from finned tubes that give a extended heat transfer surface.  Coils may also be used for non-airflow cases such as embedded in a floor slab.'    
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
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: Property. Maximum allowable air flow rate. Usually measured in m3/s.    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: &coil_-_properties_-_airflowratemin_-_properties    
        observedAt:    
          description: Property. A relationship stating the timestamp of an entity (e.g. a measurement).    
          format: date-time    
          type: string    
        unitCode:    
          description: Property. A relationship identifying the unit of measure used for a certain entity.    
          type: string    
        value:    
          description: 'Property. A relationship defining the value of a certain property, e.g., energy or power. Note that, even if numeric values are expected to enable reasoning, measurement values could use other datatypes.'    
          type: number    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    airFlowRateMin:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: Property. Minimum allowable air flow rate. Usually measured in m3/s.    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *coil_-_properties_-_airflowratemin_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
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
      anyOf: &coil_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      anyOf: *coil_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *coil_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *coil_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    nominalLatentCapacity:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: 'Property. Nominal latent capacity. Usually measured in Watts (W, J/s).'    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *coil_-_properties_-_airflowratemin_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    nominalSensibleCapacity:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: 'Property. Nominal sensible capacity. Usually measured in Watts (W, J/s).'    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *coil_-_properties_-_airflowratemin_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    nominalUa:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: Property. Nominal UA value.    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *coil_-_properties_-_airflowratemin_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    operationMode:    
      description: Property. Operation mode of this coil.    
      enum:    
        - cooling    
        - heating    
      type: string    
      x-ngsi:    
        type: Property    
    operationTemperatureMax:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: 'Property. Allowable operation ambient (air, fluid) temperature range. Usually measured in degrees Kelvin (K).'    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *coil_-_properties_-_airflowratemin_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    operationTemperatureMin:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: 'Property. Allowable operation ambient (air, fluid) temperature range. Usually measured in degrees Kelvin (K).'    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *coil_-_properties_-_airflowratemin_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *coil_-_properties_-_iscontainedinbuildingspace_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    placementType:    
      description: Property. Indicates how the device is designed to be placed.    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: Property. It must be equal to `Coil`.    
      enum:    
        - Coil    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Coil"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Coil/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Coil/schema.json    
  x-model-tags: SAREF Coil SMART DATA MODELS    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### Bobina NGSI-v2 valori-chiave Esempio  
Ecco un esempio di una bobina in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Coil:180d0665-9242-42c6-b336-d7edcf8fc3b5",  
  "type": "Coil",  
  "airFlowRateMax": 0.22332143818011307,  
  "airFlowRateMin": 0.6369516028350278,  
  "nominalLatentCapacity": 0.9394595315602638,  
  "nominalSensibleCapacity": {  
    "type": 0.8014808985276609,  
    "nominalUa": 0.3738979404823001,  
    "operationMode": "cooling",  
    "operationTemperatureMax": 0.7510713399220631,  
    "operationTemperatureMin": 0.8674252304724047,  
    "placementType": "Money Market Account",  
    "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:c562a0a7-6355-46a0-a528-ebeea1b5af39",  
    "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:7d4df444-5662-45c4-81e8-28dd9e2ab52e",  
    "isSubSystemOf": [  
      "urn:ngsi-ld:System:98486c90-52da-48cf-af50-69449370e3b9",  
      "urn:ngsi-ld:System:afe412c8-8366-4eb1-b834-dc68c1e3d828",  
      "urn:ngsi-ld:System:b851de9e-48bd-4363-9d01-b17ab9469aea"  
    ],  
    "hasManufacturer": "Coil Company Inc.",  
    "hasModel": "Coil 0.1.2",  
    "dateCreated": "2023-01-25T23:02:47Z",  
    "dateModified": "2023-01-26T14:02:17Z",  
    "source": "Import",  
    "name": "Coil",  
    "alternateName": "Coil type 2",  
    "description": "Coil of limited Coil types",  
    "dataProvider": "IFC file"  
  }  
```  
</details>  
#### Bobina NGSI-v2 normalizzata Esempio  
Ecco un esempio di Coil in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si usano le opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Coil:13d40aef-8b95-4cb2-af1e-483e4c874941",  
  "type": "Coil",  
  "airFlowRateMax": {  
    "type": "Measurement",  
    "value": 0.6477373611080879  
  },  
  "airFlowRateMin": {  
    "type": "Measurement",  
    "value": 0.1367768463223733  
  },  
  "nominalLatentCapacity": {  
    "type": "Measurement",  
    "value": 0.6823953079495582  
  },  
  "nominalSensibleCapacity": {  
    "type": "Measurement",  
    "value": 0.9661532549311025  
  },  
  "nominalUa": {  
    "type": "Measurement",  
    "value": 0.5711236580496344  
  },  
  "operationMode": {  
    "type": "CoilOperationMode",  
    "value": "cooling"  
  },  
  "operationTemperatureMax": {  
    "type": "Measurement",  
    "value": 0.5575891151602635  
  },  
  "operationTemperatureMin": {  
    "type": "Measurement",  
    "value": 0.8396275897283132  
  },  
  "placementType": {  
    "type": "Text",  
    "value": "Buckinghamshire"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:BuildingSpace:1070b255-7508-4019-ba0a-1ce8a03cf3b1"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:PhysicalObject:cef12274-adeb-41a5-aec1-8e254593bb26"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:System:65b917e6-ec39-4e2e-bce1-a52a52c176bc"  
      },  
      {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:System:61834f7f-655f-47f1-828c-755a25e7b026"  
      },  
      {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:System:ab77fbe9-a323-477c-81bf-a9923abdf8ea"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Coil Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Coil 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T04:03:32.1629228+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T16:59:28.4436033+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Coil"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Coil type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Coil of limited Coil types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### Bobina Valori chiave NGSI-LD Esempio  
Ecco un esempio di una bobina in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Coil:180d0665-9242-42c6-b336-d7edcf8fc3b5",  
  "type": "Coil",  
  "airFlowRateMax": 0.22332143818011307,  
  "airFlowRateMin": 0.6369516028350278,  
  "nominalLatentCapacity": 0.9394595315602638,  
  "nominalSensibleCapacity": {  
    "type": 0.8014808985276609,  
    "nominalUa": 0.3738979404823001,  
    "operationMode": "cooling",  
    "operationTemperatureMax": 0.7510713399220631,  
    "operationTemperatureMin": 0.8674252304724047,  
    "placementType": "Money Market Account",  
    "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:c562a0a7-6355-46a0-a528-ebeea1b5af39",  
    "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:7d4df444-5662-45c4-81e8-28dd9e2ab52e",  
    "isSubSystemOf": [  
      "urn:ngsi-ld:System:98486c90-52da-48cf-af50-69449370e3b9",  
      "urn:ngsi-ld:System:afe412c8-8366-4eb1-b834-dc68c1e3d828",  
      "urn:ngsi-ld:System:b851de9e-48bd-4363-9d01-b17ab9469aea"  
    ],  
    "hasManufacturer": "Coil Company Inc.",  
    "hasModel": "Coil 0.1.2",  
    "dateCreated": "2023-01-25T23:02:47Z",  
    "dateModified": "2023-01-26T14:02:17Z",  
    "source": "Import",  
    "name": "Coil",  
    "alternateName": "Coil type 2",  
    "description": "Coil of limited Coil types",  
    "dataProvider": "IFC file",  
    "@context": [  
      "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
      "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
  }  
```  
</details>  
#### Bobina NGSI-LD normalizzata Esempio  
Ecco un esempio di una bobina in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Coil:fcc6fa4b-fa43-42de-af7d-c8be6efda789",  
  "type": "Coil",  
  "airFlowRateMax": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-25T22:00:31Z",  
    "value": 0.461404719601072  
  },  
  "airFlowRateMin": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-26T12:18:55Z",  
    "value": 0.3100905584892091  
  },  
  "nominalLatentCapacity": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-25T15:57:00Z",  
    "value": 0.0859276056343462  
  },  
  "nominalSensibleCapacity": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-25T15:07:49Z",  
    "value": 0.9959034840230547  
  },  
  "nominalUa": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-25T16:07:27Z",  
    "value": 0.03766746157415857  
  },  
  "operationMode": {  
    "type": "Property",  
    "value": "cooling"  
  },  
  "operationTemperatureMax": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T15:22:24Z",  
    "value": 0.18992025947801072  
  },  
  "operationTemperatureMin": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T07:51:42Z",  
    "value": 0.6342100760763256  
  },  
  "placementType": {  
    "type": "Property",  
    "value": "SQL"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:61d397a1-954d-40ec-a4cc-cba2c10a07ca"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:ee042545-32fa-4adb-97e1-5007ccabcd63"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:cab59172-6cb8-443e-94b8-b6270aaa5e60"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:73b9f71e-63bb-49bf-96ef-f6f4922f4245"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:7607ea00-30f7-4271-a0f3-c0b1755be875"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Coil Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Coil 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T04:20:07Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-25T16:46:30Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Coil"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Coil type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Coil of limited Coil types"  
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
