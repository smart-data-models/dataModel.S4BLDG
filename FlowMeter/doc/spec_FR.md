<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : Débitmètre  
===================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/FlowMeter/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Un débitmètre est un dispositif utilisé pour mesurer le débit dans un système**.  
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
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `hasManufacturer[string]`: Relation identifiant le fabricant d'une entité (par exemple, un appareil). La valeur doit être une chaîne de caractères ou une chaîne de caractères avec une balise linguistique  - `hasModel[string]`: Une relation identifiant le modèle d'une entité (par exemple, un appareil). La valeur doit être une chaîne de caractères ou une chaîne de caractères avec une balise de langue  - `id[*]`: Identifiant unique de l'entité  - `isContainedInBuildingSpace[*]`: Entité utilisée pour définir les espaces physiques du bâtiment. Un espace de bâtiment contient des dispositifs ou des objets de bâtiment. (Espace Bâtiment)  - `isContainedInPhysicalObject[*]`: Tout objet qui possède une région spatiale propre.  (Définition extraite de l'ontologie DUL) (PhysicalObject)  - `isSubSystemOf[array]`: Référence au(x) système(s) dont cet objet physique fait partie  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `readOutType[string]`: Indication de la forme que prend la lecture du compteur. Dans le cas d'un compteur à cadran, il peut s'agir de plusieurs cadrans donnant une lecture cumulative et/ou d'un compteur kilométrique mécanique.  - `remoteReading[boolean]`: Indique si le compteur dispose d'une connexion pour le relevé à distance par l'intermédiaire d'un dispositif de communication (défini comme VRAI) ou non (défini comme FAUX).  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `type[string]`: Il doit être égal à `FlowMeter`  <!-- /30-PropertiesList -->  
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
FlowMeter:    
  description: A flow meter is a device that is used to measure the flow rate in a system.    
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
    readOutType:    
      description: 'Indication of the form that readout from the meter takes. In the case of a dial read out, this may comprise multiple dials that give a cumulative reading and/or a mechanical odometer'    
      type: string    
      x-ngsi:    
        type: Property    
    remoteReading:    
      description: Indicates whether the meter has a connection for remote reading through connection of a communication device (set TRUE) or not (set FALSE)    
      type: boolean    
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
      description: It must be equal to `FlowMeter`    
      enum:    
        - FlowMeter    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:FlowMeter"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/FlowMeter/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/FlowMeter/schema.json    
  x-model-tags: SAREF FlowMeter    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### FlowMeter NGSI-v2 key-values Exemple  
Voici un exemple de FlowMeter au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:FlowMeter:f1914d35-f81f-4a4f-a4e9-a6ff04daf648",  
  "type": "FlowMeter",  
  "readOutType": "reboot",  
  "remoteReading": true,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:134737db-1f4b-4ab8-a01c-4adc10903c37",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:578679ba-86dc-4cf5-ab82-3b604d81543b",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:efa37678-c954-42b7-88d9-41c05a3f48f2",  
    "urn:ngsi-ld:System:e95e02a5-aae1-4e42-b36f-79940ec5d998",  
    "urn:ngsi-ld:System:0fc941ae-0af9-4143-a381-254b0463b7f0"  
  ],  
  "hasManufacturer": "FlowMeter Company Inc.",  
  "hasModel": "FlowMeter 0.1.2",  
  "dateCreated": "2023-01-25T19:10:21Z",  
  "dateModified": "2023-01-25T23:16:49Z",  
  "source": "Import",  
  "name": "FlowMeter",  
  "alternateName": "FlowMeter type 2",  
  "description": "FlowMeter of limited FlowMeter types",  
  "dataProvider": "IFC file"  
}  
```  
</details>  
#### FlowMeter NGSI-v2 normalisé Exemple  
Voici un exemple de débitmètre au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec la norme NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:FlowMeter:838aaf6d-ea3e-4ea2-9576-0aec60a2cdfc",  
  "type": "FlowMeter",  
  "readOutType": {  
    "type": "Text",  
    "value": "Steel"  
  },  
  "remoteReading": {  
    "type": "Boolean",  
    "value": false  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:BuildingSpace:b93e69ee-2489-44be-bdb7-ee2adf46b639"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:PhysicalObject:bec8d226-aa30-4423-bc21-fb1bf38b1a6f"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:05e001ec-d22d-4338-b271-b23d88f1d447"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:e81ab268-aaf7-4d94-8416-86589d815169"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:7a83e4d7-d5af-4cdd-9549-7f9182ac0ccb"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "FlowMeter Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "FlowMeter 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T11:07:19.4425986+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T21:14:20.5601683+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "FlowMeter"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "FlowMeter type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "FlowMeter of limited FlowMeter types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### FlowMeter Valeurs clés NGSI-LD Exemple  
Voici un exemple de débitmètre au format JSON-LD sous forme de valeurs clés. Ce format est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:FlowMeter:80e2aa80-f309-4039-8a6d-e39445aa1d72",  
  "type": "FlowMeter",  
  "readOutType": "Spain",  
  "remoteReading": false,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:a8241df5-decd-47d3-83fb-23ac625a5690",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:c6fb3c72-03ea-4973-afbc-63d75c005d24",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:7f0a0811-c372-43d3-93a0-2463af245196",  
    "urn:ngsi-ld:System:55220a1b-f36b-4042-9257-2d8d390ac500",  
    "urn:ngsi-ld:System:d38d8eeb-5579-431a-b41a-f3807b340ebd"  
  ],  
  "hasManufacturer": "FlowMeter Company Inc.",  
  "hasModel": "FlowMeter 0.1.2",  
  "dateCreated": "2023-01-26T02:02:47Z",  
  "dateModified": "2023-01-26T06:34:10Z",  
  "source": "Import",  
  "name": "FlowMeter",  
  "alternateName": "FlowMeter type 2",  
  "description": "FlowMeter of limited FlowMeter types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### Débitmètre NGSI-LD normalisé Exemple  
Voici un exemple de débitmètre au format JSON-LD normalisé. Ce format est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:FlowMeter:fc7e5dc8-7e06-4327-a444-5b6832467810",  
  "type": "FlowMeter",  
  "readOutType": {  
    "type": "Property",  
    "value": "website"  
  },  
  "remoteReading": {  
    "type": "Property",  
    "value": true  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:9da65e0c-7b0c-4d62-99bc-1cb6926749e4"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:5199f09c-629d-48ca-9b21-7d3c2800f97f"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:2b39227b-b691-4558-9d43-3e5f8b7b632e"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:35f88756-6caf-44fa-becb-aff4e2b182be"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:01dd4075-26b6-4124-a486-0ee36e31dfd1"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "FlowMeter Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "FlowMeter 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T21:08:36Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-25T14:28:39Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "FlowMeter"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "FlowMeter type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "FlowMeter of limited FlowMeter types"  
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
