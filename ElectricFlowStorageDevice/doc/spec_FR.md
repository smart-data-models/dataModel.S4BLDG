<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : Dispositif de stockage à flux électrique  
=================================================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/ElectricFlowStorageDevice/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Un dispositif de stockage de flux électrique est un dispositif dans lequel l'énergie électrique est stockée et à partir duquel l'énergie peut être progressivement libérée**.  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Date de création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage.  - `dateModified[string]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage.  - `description[string]`: Une description de l'article  - `hasManufacturer[string]`: Propriété. Une relation identifiant le fabricant d'une entité (par exemple, un appareil). La valeur doit être une chaîne de caractères ou une chaîne de caractères avec une étiquette de langue.  - `hasModel[string]`: Propriété. Une relation identifiant le modèle d'une entité (par exemple, un appareil). La valeur doit être une chaîne de caractères ou une chaîne de caractères avec une balise de langue.  - `id[*]`: Identifiant unique de l'entité  - `isContainedInBuildingSpace[*]`: Relations. Entité utilisée pour définir les espaces physiques du bâtiment. Un espace de bâtiment contient des appareils ou des objets de bâtiment. (Espace Bâtiment)  - `isContainedInPhysicalObject[*]`: Relation. Tout objet qui possède une région spatiale propre.  (Définition extraite de l'ontologie DUL) (PhysicalObject)  - `isSubSystemOf[array]`: Relation. Référence à un ou plusieurs systèmes dont cet objet physique fait partie.  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément.  - `nominalFrequency[number]`: Propriété. La fréquence nominale de l'alimentation. Généralement mesurée en cycles/s ou en Hertz (Hz).  - `nominalSupplyVoltage[number]`: Propriété. La tension nominale de l'alimentation. Généralement mesurée en Volts (V, W/A).  - `nominalSupplyVoltageMin[number]`: Propriété. La tension maximale et minimale autorisée de l'alimentation, par exemple les limites de 380V/440V peuvent être appliquées pour une tension nominale de 400V.  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `type[string]`: Propriété. Elle doit être égale à `ElectricFlowStorageDevice`.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modèle de données description des propriétés  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ElectricFlowStorageDevice:    
  description: An electric flow storage device is a device in which electrical energy is stored and from which energy may be progressively released.    
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
      anyOf: &electricflowstoragedevice_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      anyOf: *electricflowstoragedevice_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *electricflowstoragedevice_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *electricflowstoragedevice_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    nominalFrequency:    
      description: Property. The nominal frequency of the supply. Usually measured in cycles/s or Hertz (Hz).    
      type: number    
      x-ngsi:    
        type: Property    
    nominalSupplyVoltage:    
      description: 'Property. The nominal voltage of the supply. Usually measured in Volts (V, W/A).'    
      type: number    
      x-ngsi:    
        type: Property    
    nominalSupplyVoltageMin:    
      description: Property. The maximum and minimum allowed voltage of the supply e.g. boundaries of 380V/440V may be applied for a nominal voltage of 400V.    
      type: number    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *electricflowstoragedevice_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      description: Property. It must be equal to `ElectricFlowStorageDevice`.    
      enum:    
        - ElectricFlowStorageDevice    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:ElectricFlowStorageDevice"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/ElectricFlowStorageDevice/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/ElectricFlowStorageDevice/schema.json    
  x-model-tags: SAREF ElectricFlowStorageDevice    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### ElectricFlowStorageDevice Valeurs clés NGSI-v2 Exemple  
Voici un exemple d'ElectricFlowStorageDevice au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ElectricFlowStorageDevice:60491652-ea6b-4e3c-8c4d-b0ae10defbda",  
  "type": "ElectricFlowStorageDevice",  
  "nominalFrequency": 0.6643858958243121,  
  "nominalSupplyVoltage": 0.9863230627218449,  
  "nominalSupplyVoltageMin": 0.5073272634060758,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:783aa5ff-fb6a-4fd8-863d-82a133f5d062",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:2602e1ee-c225-4703-9046-53bad81695f9",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:7aa13a80-05f1-4b1e-b973-4a4c88b729e8",  
    "urn:ngsi-ld:System:c34c6ce4-1336-4a37-a951-7710dd32550f",  
    "urn:ngsi-ld:System:dfeb61ff-fb62-4890-b453-918fe7a49b98"  
  ],  
  "hasManufacturer": "ElectricFlowStorageDevice Company Inc.",  
  "hasModel": "ElectricFlowStorageDevice 0.1.2",  
  "dateCreated": "2023-01-25T18:29:30Z",  
  "dateModified": "2023-01-25T14:18:54Z",  
  "source": "Import",  
  "name": "ElectricFlowStorageDevice",  
  "alternateName": "ElectricFlowStorageDevice type 2",  
  "description": "ElectricFlowStorageDevice of limited ElectricFlowStorageDevice types",  
  "dataProvider": "IFC file"  
}  
```  
</details>  
#### ElectricFlowStorageDevice NGSI-v2 normalisé Exemple  
Voici un exemple d'ElectricFlowStorageDevice au format JSON-LD tel que normalisé. Ce format est compatible avec l'INSG-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ElectricFlowStorageDevice:4596f0a6-514a-4513-a666-3b9ade359305",  
  "type": "ElectricFlowStorageDevice",  
  "nominalFrequency": {  
    "type": "Measurement",  
    "value":  0.42581504045433194  
  },  
  "nominalSupplyVoltage": {  
    "type": "Measurement",  
    "value":  0.025200397292739596  
  },  
  "nominalSupplyVoltageMin": {  
    "type": "Measurement",  
    "value": 0.05204546916613961  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:BuildingSpace:235bfb6d-5039-45ea-95f9-094db1283634"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:PhysicalObject:9b54ca95-3f90-4be8-b32a-b585f8a9f867"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:0292e70d-da07-4d14-b8d8-c81c27c44683"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:6dce885f-2c53-414b-b0b2-9f2b88f0376d"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:a52f7099-5638-4b97-98c6-d24acc53edc6"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "ElectricFlowStorageDevice Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "ElectricFlowStorageDevice 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T09:43:01.2422472+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T15:38:19.0396796+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "ElectricFlowStorageDevice"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "ElectricFlowStorageDevice type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "ElectricFlowStorageDevice of limited ElectricFlowStorageDevice types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### ElectricFlowStorageDevice Valeurs clés NGSI-LD Exemple  
Voici un exemple d'ElectricFlowStorageDevice au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ElectricFlowStorageDevice:60491652-ea6b-4e3c-8c4d-b0ae10defbda",  
  "type": "ElectricFlowStorageDevice",  
  "nominalFrequency": 0.6643858958243121,  
  "nominalSupplyVoltage": 0.9863230627218449,  
  "nominalSupplyVoltageMin": 0.5073272634060758,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:783aa5ff-fb6a-4fd8-863d-82a133f5d062",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:2602e1ee-c225-4703-9046-53bad81695f9",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:7aa13a80-05f1-4b1e-b973-4a4c88b729e8",  
    "urn:ngsi-ld:System:c34c6ce4-1336-4a37-a951-7710dd32550f",  
    "urn:ngsi-ld:System:dfeb61ff-fb62-4890-b453-918fe7a49b98"  
  ],  
  "hasManufacturer": "ElectricFlowStorageDevice Company Inc.",  
  "hasModel": "ElectricFlowStorageDevice 0.1.2",  
  "dateCreated": "2023-01-25T18:29:30Z",  
  "dateModified": "2023-01-25T14:18:54Z",  
  "source": "Import",  
  "name": "ElectricFlowStorageDevice",  
  "alternateName": "ElectricFlowStorageDevice type 2",  
  "description": "ElectricFlowStorageDevice of limited ElectricFlowStorageDevice types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### ElectricFlowStorageDevice NGSI-LD normalisé Exemple  
Voici un exemple d'ElectricFlowStorageDevice au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ElectricFlowStorageDevice:88efe032-f0b1-4d6b-9ff0-d3955cdcd6e7",  
  "type": "ElectricFlowStorageDevice",  
  "nominalFrequency": {  
    "type": "Property",  
    "unitCode": "Hz",  
    "observedAt": "2023-01-25T19:08:38Z",  
    "value": 0.6604645004424095  
  },  
  "nominalSupplyVoltage": {  
    "type": "Property",  
    "unitCode": "W/A",  
    "observedAt": "2023-01-26T06:40:20Z",  
    "value": 0.7889839353290103  
  },  
  "nominalSupplyVoltageMin": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T13:04:38Z",  
    "value": 0.5759276076424262  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:8d1a4801-d77d-48ce-8fdb-6b0e6bf737f2"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:42136020-035a-4946-8a49-99cbfde581e2"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:d553b00a-f3fe-4293-922d-8b665ed69e0d"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:7d32b669-8e92-4b94-9807-effabcb49391"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:242276cc-61da-4555-8b5f-769fd606ae0f"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "ElectricFlowStorageDevice Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "ElectricFlowStorageDevice 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T04:39:29Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-25T22:59:03Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "ElectricFlowStorageDevice"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "ElectricFlowStorageDevice type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "ElectricFlowStorageDevice of limited ElectricFlowStorageDevice types"  
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
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
