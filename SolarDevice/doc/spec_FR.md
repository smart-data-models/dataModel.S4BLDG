<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : Dispositif solaire  
===========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/SolarDevice/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Un dispositif solaire convertit le rayonnement solaire en une autre énergie telle que le courant électrique ou l'énergie thermique.  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse postale et qui se trouve dans la région  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La région dans laquelle se trouve la localité et qui se trouve dans le pays  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local.    
	- `postOfficeBoxNumber[string]`: Le numéro de la boîte postale pour les adresses de boîtes postales. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `hasManufacturer[string]`: Relation identifiant le fabricant d'une entité (par exemple, un appareil). La valeur doit être une chaîne de caractères ou une chaîne de caractères avec une balise linguistique  - `hasModel[string]`: Une relation identifiant le modèle d'une entité (par exemple, un appareil). La valeur doit être une chaîne de caractères ou une chaîne de caractères avec une balise de langue  - `id[*]`: Identifiant unique de l'entité  - `isContainedInBuildingSpace[*]`: Entité utilisée pour définir les espaces physiques du bâtiment. Un espace de bâtiment contient des dispositifs ou des objets de bâtiment. (Espace Bâtiment)  - `isContainedInPhysicalObject[*]`: Tout objet qui possède une région spatiale propre.  (Définition extraite de l'ontologie DUL) (PhysicalObject)  - `isSubSystemOf[array]`: Référence au(x) système(s) dont cet objet physique fait partie  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `type[string]`: Il doit être égal à `SolarDevice`  <!-- /30-PropertiesList -->  
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
SolarDevice:    
  description: A solar device converts solar radiation into other energy such as electric current or thermal energy.    
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
      description: It must be equal to `SolarDevice`    
      enum:    
        - SolarDevice    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:SolarDevice"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/SolarDevice/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/SolarDevice/schema.json    
  x-model-tags: SAREF SolarDevice    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### SolarDevice NGSI-v2 key-values Exemple  
Voici un exemple d'un SolarDevice au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SolarDevice:11f3880f-7f05-4a4d-908f-76d1d71d4ca8",  
  "type": "SolarDevice",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:ad61f988-63fb-4140-a060-8db42190b2d3",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:3067c30d-8fd9-4fc2-9373-37dd37771bf5",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:4a64ac85-201c-4c57-8ab9-c3c74bc1d49e",  
    "urn:ngsi-ld:System:319ebac6-32d2-4d42-bf3b-fb07a93cd88a",  
    "urn:ngsi-ld:System:f239edb1-7707-46dd-bc7a-40de65d84bfd"  
  ],  
  "hasManufacturer": "SolarDevice Company Inc.",  
  "hasModel": "SolarDevice 0.1.2",  
  "dateCreated": "2023-01-25T16:52:15Z",  
  "dateModified": "2023-01-25T18:43:20Z",  
  "source": "Import",  
  "name": "SolarDevice",  
  "alternateName": "SolarDevice type 2",  
  "description": "SolarDevice of limited SolarDevice types",  
  "dataProvider": "IFC file"  
}  
```  
</details>  
#### SolarDevice NGSI-v2 normalisé Exemple  
Voici un exemple d'un SolarDevice au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec la norme NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SolarDevice:393f9026-39f9-4046-b396-d5b769cd0294",  
  "type": "SolarDevice",  
  "isContainedInBuildingSpace": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:BuildingSpace:db2a8b32-35f5-4b7a-990d-6a136c8d0b9e"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:PhysicalObject:9243dfaf-6ddc-482b-bba3-e040f331b487"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:3fd752c1-1ec0-4bc9-8a5b-43768df52545"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:8d4a1da4-c92e-497d-861f-68704c9af1e9"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:fa7d2ac0-3c15-46a8-be00-aff4489b32d1"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "SolarDevice Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "SolarDevice 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T03:22:01.6727224+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T02:08:19.888648+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "SolarDevice"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "SolarDevice type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "SolarDevice of limited SolarDevice types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### SolarDevice NGSI-LD key-values Exemple  
Voici un exemple d'un SolarDevice au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SolarDevice:0a31fe75-38bd-4d22-89e3-a92c79345903",  
  "type": "SolarDevice",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:d93dffd9-84c2-488d-8ffd-f94536f804c5",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:7c028af8-992e-4aa4-a732-9b1f645fe9a1",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:f4d59d6a-9a55-41e8-9b74-cb3a77ea7251",  
    "urn:ngsi-ld:System:702c2871-cf14-4b89-9dee-a3848eda3e67",  
    "urn:ngsi-ld:System:71958de6-470b-4195-9b02-8d204b7c7aec"  
  ],  
  "hasManufacturer": "SolarDevice Company Inc.",  
  "hasModel": "SolarDevice 0.1.2",  
  "dateCreated": "2023-01-26T05:35:47Z",  
  "dateModified": "2023-01-25T21:31:55Z",  
  "source": "Import",  
  "name": "SolarDevice",  
  "alternateName": "SolarDevice type 2",  
  "description": "SolarDevice of limited SolarDevice types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### SolarDevice NGSI-LD normalisé Exemple  
Voici un exemple d'un SolarDevice au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SolarDevice:f7b20374-3fff-41d2-96ea-d227a3b458cc",  
  "type": "SolarDevice",  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:a7992d2d-19f4-4e6b-938f-9de8314e6a31"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:cd9cf384-7e05-44b2-816b-9bc094ad8423"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:fea01066-da6c-4823-8331-a7450f139df6"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:4f04da6b-d1c0-47a7-afd9-4455b3cfda01"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:353b9e43-78b1-44b7-a3e4-8f9bc523d7fc"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "SolarDevice Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "SolarDevice 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T09:09:32Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T01:06:29Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "SolarDevice"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "SolarDevice type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "SolarDevice of limited SolarDevice types"  
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
