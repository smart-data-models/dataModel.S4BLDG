<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : Pompe  
==============<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Pump/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Une pompe est un dispositif qui imprime un travail mécanique à des fluides ou à des boues pour les déplacer dans un canal ou une canalisation. Une utilisation typique d'une pompe est de faire circuler de l'eau réfrigérée ou de l'eau chaude de chauffage dans un système de distribution de services d'un bâtiment**.  
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
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `connectionSize[number]`: La taille de la connexion de la pompe. Généralement mesurée en millimètres (mm)  - `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `flowResistanceMax[number]`: Plage admissible de résistance au frottement contre laquelle le fluide est pompé. Généralement mesurée en Pascals (Pa, N/m2).  - `flowResistanceMin[number]`: Plage admissible de résistance au frottement contre laquelle le fluide est pompé. Généralement mesurée en Pascals (Pa, N/m2).  - `hasManufacturer[string]`: Relation identifiant le fabricant d'une entité (par exemple, un appareil). La valeur doit être une chaîne de caractères ou une chaîne de caractères avec une balise linguistique  - `hasModel[string]`: Une relation identifiant le modèle d'une entité (par exemple, un appareil). La valeur doit être une chaîne de caractères ou une chaîne de caractères avec une balise de langue  - `id[*]`: Identifiant unique de l'entité  - `isContainedInBuildingSpace[*]`: Entité utilisée pour définir les espaces physiques du bâtiment. Un espace de bâtiment contient des dispositifs ou des objets de bâtiment. (Espace Bâtiment)  - `isContainedInPhysicalObject[*]`: Tout objet qui possède une région spatiale propre.  (Définition extraite de l'ontologie DUL) (PhysicalObject)  - `isSubSystemOf[array]`: Référence au(x) système(s) dont cet objet physique fait partie  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément  - `netPositiveSuctionHead[number]`: Pression minimale du liquide à l'entrée de la pompe pour éviter la cavitation. Généralement mesurée en Pascals (Pa, N/m2).  - `nomminalRotationSpeed[number]`: Vitesse de rotation de la pompe dans les conditions nominales. Généralement mesurée en cycles/s  - `operationTemperatureMax[number]`: Plage de température ambiante (air, fluide) autorisée pour le fonctionnement. Généralement mesurée en degrés Kelvin (K)  - `operationTemperatureMin[number]`: Plage de température ambiante (air, fluide) autorisée pour le fonctionnement. Généralement mesurée en degrés Kelvin (K)  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `pumpFlowRateMax[number]`: Plage admissible du volume de fluide pompé par rapport à la résistance spécifiée. Généralement mesurée en kg/s  - `pumpFlowRateMin[number]`: Plage admissible du volume de fluide pompé par rapport à la résistance spécifiée. Généralement mesurée en kg/s  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `type[string]`: Il doit être égal à `Pump`  <!-- /30-PropertiesList -->  
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
Pump:    
  description: A pump is a device which imparts mechanical work on fluids or slurries to move them through a channel or pipeline. A typical use of a pump is to circulate chilled water or heating hot water in a building services distribution system.    
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
    connectionSize:    
      description: The connection size of the to and from the pump. Usually measured in millimeters (mm)    
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
    flowResistanceMax:    
      description: 'Allowable range of frictional resistance against which the fluid is being pumped. Usually measured in Pascals (Pa, N/m2)'    
      type: number    
      x-ngsi:    
        type: Property    
    flowResistanceMin:    
      description: 'Allowable range of frictional resistance against which the fluid is being pumped. Usually measured in Pascals (Pa, N/m2)'    
      type: number    
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
    netPositiveSuctionHead:    
      description: 'Minimum liquid pressure at the pump inlet to prevent cavitation. Usually measured in Pascals (Pa, N/m2)'    
      type: number    
      x-ngsi:    
        type: Property    
    nomminalRotationSpeed:    
      description: Pump rotational speed under nominal conditions. Usually measured in cycles/s    
      type: number    
      x-ngsi:    
        type: Property    
    operationTemperatureMax:    
      description: 'Allowable operation ambient (air, fluid) temperature range. Usually measured in degrees Kelvin (K)'    
      type: number    
      x-ngsi:    
        type: Property    
    operationTemperatureMin:    
      description: 'Allowable operation ambient (air, fluid) temperature range. Usually measured in degrees Kelvin (K)'    
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
    pumpFlowRateMax:    
      description: Allowable range of volume of fluid being pumped against the resistance specified. Usually measured in kg/s    
      type: number    
      x-ngsi:    
        type: Property    
    pumpFlowRateMin:    
      description: Allowable range of volume of fluid being pumped against the resistance specified. Usually measured in kg/s    
      type: number    
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
      description: It must be equal to `Pump`    
      enum:    
        - Pump    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Pump"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Pump/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Pump/schema.json    
  x-model-tags: SAREF Pump    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### Pompe NGSI-v2 valeurs-clés Exemple  
Voici un exemple de pompe au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Pump:5c6aa613-0829-405e-aeb6-ef000e26fea1",  
    "type": "Pump",  
    "connectionSize": 0.0736674796470771,  
    "flowResistanceMax": 0.5763414622833901,  
    "flowResistanceMin": 0.23194313125611832,  
    "netPositiveSuctionHead": 0.9430406136976697,  
    "nomminalRotationSpeed": 0.49997837892806263,  
    "operationTemperatureMax": 0.016630756942512148,  
    "operationTemperatureMin": 0.7235008225786019,  
    "pumpFlowRateMax": 0.2126600766557486,  
    "pumpFlowRateMin": 0.8849029838139153,  
    "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:13846972-f593-4662-96b5-92cefbbe8219",  
    "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:54ecdd7e-4ab8-4c41-b56b-47bb45c572f8",  
    "isSubSystemOf": [  
        "urn:ngsi-ld:System:092c5cb0-1b8e-4bc9-88ee-ce226a23061f",  
        "urn:ngsi-ld:System:053dc8a9-bbb7-402c-8d99-522b8626091d",  
        "urn:ngsi-ld:System:60e0c6c5-ebd6-4460-aa78-442698c8204c"  
    ],  
    "hasManufacturer": "Pump Company Inc.",  
    "hasModel": "Pump 0.1.2",  
    "dateCreated": "2023-01-26T00:41:42Z",  
    "dateModified": "2023-01-26T10:20:35Z",  
    "source": "Import",  
    "name": "Pump",  
    "alternateName": "Pump type 2",  
    "description": "Pump of limited Pump types",  
    "dataProvider": "IFC file"  
}  
```  
</details>  
#### Pompe NGSI-v2 normalisée Exemple  
Voici un exemple de pompe au format JSON-LD normalisé. Ce format est compatible avec la norme NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Pump:068a2569-0602-4845-8ed3-8ddb200bdcac",  
  "type": "Pump",  
  "connectionSize": {  
    "type": "Measurement",  
    "value": 0.8537944550916271  
  },  
  "flowResistanceMax": {  
    "type": "Measurement",  
    "value": 0.934151218696693  
  },  
  "flowResistanceMin": {  
    "type": "Measurement",  
    "value": 0.5798733223282941  
  },  
  "netPositiveSuctionHead": {  
    "type": "Measurement",  
    "value": 0.9236791362464654  
  },  
  "nomminalRotationSpeed": {  
    "type": "Measurement",  
    "value": 0.9434212309119704  
  },  
  "operationTemperatureMax": {  
    "type": "Measurement",  
    "value": 0.40126909555034673  
  },  
  "operationTemperatureMin": {  
    "type": "Measurement",  
    "value": 0.49855896547412504  
  },  
  "pumpFlowRateMax": {  
    "type": "Measurement",  
    "value": 0.8126244460338075  
  },  
  "pumpFlowRateMin": {  
    "type": "Measurement",  
    "value":  0.4387979987462379  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:BuildingSpace:30823ddd-b24b-4307-917c-72134cf789aa"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:PhysicalObject:f57afcb5-61fd-4e18-b9e0-4c246e0ed2c2"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:93229da7-6aa4-42ad-8d91-7d529267dafd"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:cd14cc46-1a6c-4058-ad6c-07b62d4944c0"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:1dcc7d2b-1886-4006-970f-4c44a5213211"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Pump Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Pump 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T09:00:15.8186104+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T18:30:43.9565309+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Pump"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Pump type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Pump of limited Pump types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### Pompe NGSI-LD valeurs clés Exemple  
Voici un exemple de pompe au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Pump:5c6aa613-0829-405e-aeb6-ef000e26fea1",  
  "type": "Pump",  
  "connectionSize": 0.0736674796470771,  
  "flowResistanceMax": 0.5763414622833901,  
  "flowResistanceMin": 0.23194313125611832,  
  "netPositiveSuctionHead": 0.9430406136976697,  
  "nomminalRotationSpeed": 0.49997837892806263,  
  "operationTemperatureMax": 0.016630756942512148,  
  "operationTemperatureMin": 0.7235008225786019,  
  "pumpFlowRateMax": 0.2126600766557486,  
  "pumpFlowRateMin": 0.8849029838139153,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:13846972-f593-4662-96b5-92cefbbe8219",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:54ecdd7e-4ab8-4c41-b56b-47bb45c572f8",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:092c5cb0-1b8e-4bc9-88ee-ce226a23061f",  
    "urn:ngsi-ld:System:053dc8a9-bbb7-402c-8d99-522b8626091d",  
    "urn:ngsi-ld:System:60e0c6c5-ebd6-4460-aa78-442698c8204c"  
  ],  
  "hasManufacturer": "Pump Company Inc.",  
  "hasModel": "Pump 0.1.2",  
  "dateCreated": "2023-01-26T00:41:42Z",  
  "dateModified": "2023-01-26T10:20:35Z",  
  "source": "Import",  
  "name": "Pump",  
  "alternateName": "Pump type 2",  
  "description": "Pump of limited Pump types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### Pompe NGSI-LD normalisée Exemple  
Voici un exemple de pompe au format JSON-LD normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Pump:7ed480ca-f64d-42fd-9d2e-a792829d1467",  
  "type": "Pump",  
  "connectionSize": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T01:56:40Z",  
    "value": 0.439871049852415  
  },  
  "flowResistanceMax": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-26T10:30:54Z",  
    "value": 0.70272326323097  
  },  
  "flowResistanceMin": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-26T11:23:10Z",  
    "value": 0.748100252355086  
  },  
  "netPositiveSuctionHead": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-25T23:42:12Z",  
    "value": 0.4372375818125598  
  },  
  "nomminalRotationSpeed": {  
    "type": "Property",  
    "unitCode": "cycles/s",  
    "observedAt": "2023-01-25T16:47:26Z",  
    "value": 0.9055473204179818  
  },  
  "operationTemperatureMax": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T23:01:07Z",  
    "value": 0.19255105886794588  
  },  
  "operationTemperatureMin": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T02:59:51Z",  
    "value": 0.014765641352581182  
  },  
  "pumpFlowRateMax": {  
    "type": "Property",  
    "unitCode": "kg/s",  
    "observedAt": "2023-01-26T10:06:49Z",  
    "value": 0.2765428009146871  
  },  
  "pumpFlowRateMin": {  
    "type": "Property",  
    "unitCode": "kg/s",  
    "observedAt": "2023-01-26T00:29:22Z",  
    "value": 0.691611788348768  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:00bec903-1682-4d39-9164-6b6635d717c7"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:cf20b915-721e-4f55-b736-af772bdc68c2"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:08e18090-a9f4-4837-a6aa-3d218b14721c"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:646f75aa-9900-4722-98ce-b3811440d0ce"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:00fb7f96-ff82-4b41-8b6e-1e3d2d8b66c3"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Pump Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Pump 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T13:30:12Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-25T15:53:32Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Pump"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Pump type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Pump of limited Pump types"  
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
