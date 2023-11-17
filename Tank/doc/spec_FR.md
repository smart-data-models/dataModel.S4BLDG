<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entité : Réservoir    
==================<!-- /10-Header -->    
<!-- 15-License -->    
[Licence ouverte] (https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Tank/LICENSE.md)    
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Description globale : **Une citerne est un récipient ou un conteneur dans lequel un fluide ou un gaz est stocké en vue d'une utilisation ultérieure**.    
version : 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste des propriétés    
<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.    
- `accessType[string]`: Définit les types d'accès (ou de couverture) à une citerne qui peuvent être spécifiés. Il convient de noter que les couvercles sont généralement spécifiés pour les réservoirs rectangulaires. Pour les réservoirs cylindriques, l'accès se fait normalement par un trou d'homme.  - `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse postale et qui se trouve dans la région  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La région dans laquelle se trouve la localité et qui se trouve dans le pays  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local.      
	- `postOfficeBoxNumber[string]`: Le numéro de la boîte postale pour les adresses de boîtes postales. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `effectiveCapacity[number]`: La capacité volumétrique totale effective ou réelle du réservoir. Généralement mesurée en mètre cube (m3).B3  - `endShapeType[string]`: Définit les types de formes d'extrémité qui peuvent être utilisés pour les réservoirs préformés. La convention de lecture de ces valeurs énumérées est la suivante : pour un cylindre vertical, la première valeur est la base et la seconde est le sommet ; pour un cylindre horizontal, l'ordre de lecture doit être de gauche à droite. Pour une citerne sphérique, la valeur UNSET doit être utilisée.B5  - `firstCurvatureRadius[number]`: FirstCurvatureRadius doit être défini comme la valeur du rayon de courbure de la base ou du côté gauche. Généralement mesuré en millimètres (mm)  - `hasManufacturer[string]`: Relation identifiant le fabricant d'une entité (par exemple, un appareil). La valeur doit être une chaîne de caractères ou une chaîne de caractères avec une balise linguistique  - `hasModel[string]`: Une relation identifiant le modèle d'une entité (par exemple, un appareil). La valeur doit être une chaîne de caractères ou une chaîne de caractères avec une balise de langue  - `id[*]`: Identifiant unique de l'entité  - `isContainedInBuildingSpace[*]`: Entité utilisée pour définir les espaces physiques du bâtiment. Un espace de bâtiment contient des dispositifs ou des objets de bâtiment. (Espace Bâtiment)  - `isContainedInPhysicalObject[*]`:   (Définition extraite de l'ontologie DUL) (PhysicalObject)  - `isSubSystemOf[array]`: Référence au(x) système(s) dont cet objet physique fait partie  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément  - `nominalDepth[number]`: Profondeur nominale de la citerne. Note : non requise pour un réservoir cylindrique horizontal. Généralement mesurée en millimètres (mm)  - `nominalLengthOrDiameter[number]`: La longueur nominale ou, dans le cas d'un réservoir cylindrique vertical, le diamètre nominal du réservoir. Généralement mesurée en millimètres (mm)  - `nominalVolumetricCapacity[number]`: La capacité volumétrique nominale totale du réservoir. Généralement mesurée en mètre cube (m3).  - `nominalWidthOrDiameter[number]`: La largeur nominale ou, dans le cas d'une citerne cylindrique horizontale, le diamètre nominal de la citerne. Note : Non requis pour un réservoir cylindrique vertical. Généralement mesurée en millimètres (mm)  - `numberOfSections[number]`: Nombre de sections utilisées  - `operatingWeight[number]`: Poids en ordre de marche du réservoir, y compris tout son contenu. Généralement mesuré en kilogrammes (kg) ou en grammes (g).  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `patternType[string]`: Définit les types de motifs (ou la forme d'un réservoir) qui peuvent être spécifiés  - `secondCurvatureRadius[number]`: SecondCurvatureRadius doit être défini comme la valeur du rayon de courbure supérieur ou droit. Généralement mesuré en millimètres (mm)  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `storageType[string]`: Définit la catégorie générale d'articles destinée à être stockée  - `type[string]`: Il doit être égal à `Tank`  <!-- /30-PropertiesList -->    
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
Tank:      
  description: A tank is a vessel or container in which a fluid or gas is stored for later use.      
  properties:      
    accessType:      
      description: 'Defines the types of access (or cover) to a tank that may be specified. Note that covers are generally specified for rectangular tanks. For cylindrical tanks, access will normally be via a manhole'      
      type: string      
      x-ngsi:      
        type: Property      
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
    effectiveCapacity:      
      description: The total effective or actual volumetric capacity of the tank. Usually measured in cubic metre (m3).B3      
      type: number      
      x-ngsi:      
        type: Property      
    endShapeType:      
      description: 'Defines the types of end shapes that can be used for preformed tanks. The convention for reading these enumerated values is that for a vertical cylinder, the first value is the base and the second is the top for a horizontal cylinder, the order of reading should be left to right. For a speherical tank, the value UNSET should be used.B5'      
      type: string      
      x-ngsi:      
        type: Property      
    firstCurvatureRadius:      
      description: FirstCurvatureRadius should be defined as the base or left side radius of curvature value. Usually measured in millimeters (mm)      
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
    nominalDepth:      
      description: 'The nominal depth of the tank. Note: Not required for a horizontal cylindrical tank. Usually measured in millimeters (mm)'      
      type: number      
      x-ngsi:      
        type: Property      
    nominalLengthOrDiameter:      
      description: 'The nominal length or, in the case of a vertical cylindrical tank, the nominal diameter of the tank. Usually measured in millimeters (mm)'      
      type: number      
      x-ngsi:      
        type: Property      
    nominalVolumetricCapacity:      
      description: The total nominal or design volumetric capacity of the tank. Usually measured in cubic metre (m3)      
      type: number      
      x-ngsi:      
        type: Property      
    nominalWidthOrDiameter:      
      description: 'The nominal width or, in the case of a horizontal cylindrical tank, the nominal diameter of the tank. Note: Not required for a vertical cylindrical tank. Usually measured in millimeters (mm)'      
      type: number      
      x-ngsi:      
        type: Property      
    numberOfSections:      
      description: Number of sections used      
      type: number      
      x-ngsi:      
        type: Property      
    operatingWeight:      
      description: Operating weight of the tank including all of its contents. Usually measured in kilograms (kg) or grams (g)      
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
    patternType:      
      description: Defines the types of pattern (or shape of a tank that may be specified      
      type: string      
      x-ngsi:      
        type: Property      
    secondCurvatureRadius:      
      description: SecondCurvatureRadius should be defined as the top or right side radius of curvature value. Usually measured in millimeters (mm)      
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
    storageType:      
      description: Defines the general material category intended to be stored      
      type: string      
      x-ngsi:      
        type: Property      
    type:      
      description: It must be equal to `Tank`      
      enum:      
        - Tank      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Tank"      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Tank/LICENSE.md      
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Tank/schema.json      
  x-model-tags: SAREF Tank      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Exemples de charges utiles    
#### Tank NGSI-v2 key-values Exemple    
Voici un exemple de Tank au format JSON-LD en tant que key-values. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Tank:7a5293bf-87b8-4768-8c25-56bcbfa91649",  
  "type": "Tank",  
  "accessType": "Auto Loan Account",  
  "effectiveCapacity": 0.6627329008534851,  
  "endShapeType": "Union",  
  "firstCurvatureRadius": 0.6799132713266423,  
  "nominalDepth": 0.07530609187652448,  
  "nominalLengthOrDiameter": 0.1950493997985394,  
  "nominalVolumetricCapacity": 0.6494794060427406,  
  "nominalWidthOrDiameter": 0.2734692629974923,  
  "numberOfSections": 0.3094855572354859,  
  "operatingWeight": 0.3055837938759739,  
  "patternType": "Investment Account",  
  "secondCurvatureRadius": 0.0019846058153857316,  
  "storageType": "Investor",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:ffcd7e11-7c74-45f3-8f5a-3310ababddc8",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:c2540316-a0c2-4363-93b7-e49ab5ed3b2f",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:aae7e0b6-0256-4c58-a3ee-4989bdc205da",  
    "urn:ngsi-ld:System:857551fc-8a05-4052-9269-8193f148ff2c",  
    "urn:ngsi-ld:System:e4e88c0a-d78a-4bfd-a76b-af72e518a66e"  
  ],  
  "hasManufacturer": "Tank Company Inc.",  
  "hasModel": "Tank 0.1.2",  
  "dateCreated": "2023-01-26T12:03:34Z",  
  "dateModified": "2023-01-25T16:27:50Z",  
  "source": "Import",  
  "name": "Tank",  
  "alternateName": "Tank type 2",  
  "description": "Tank of limited Tank types",  
  "dataProvider": "IFC file"  
}  
```  
</details>    
#### Réservoir NGSI-v2 normalisé Exemple    
Voici un exemple de réservoir au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec les NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Tank:dc341150-16f1-4fa1-a674-36714ed2565c",  
  "type": "Tank",  
  "accessType": {  
    "type": "Text",  
    "value": "Benin"  
  },  
  "effectiveCapacity": {  
    "type": "Number",  
    "value": 0.34988329549654584  
  },  
  "endShapeType": {  
    "type": "Text",  
    "value": "Lari"  
  },  
  "firstCurvatureRadius": {  
    "type": "Number",  
    "value": 0.9159778495815387  
  },  
  "nominalDepth": {  
    "type": "Number",  
    "value": 0.8630341610754986  
  },  
  "nominalLengthOrDiameter": {  
    "type": "Number",  
    "value": 0.8867523503955448  
  },  
  "nominalVolumetricCapacity": {  
    "type": "Number",  
    "value": 0.27704062609207425  
  },  
  "nominalWidthOrDiameter": {  
    "type": "Number",  
    "value": 0.6770082270929979  
  },  
  "numberOfSections": {  
    "type": "Number",  
    "value": 0.7169194499582789  
  },  
  "operatingWeight": {  
    "type": "Number",  
    "value": 0.23947734710245394  
  },  
  "patternType": {  
    "type": "Text",  
    "value": "Ergonomic Cotton Ball"  
  },  
  "secondCurvatureRadius": {  
    "type": "Number",  
    "value": 0.11478790270153483  
  },  
  "storageType": {  
    "type": "Text",  
    "value": "gold"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:BuildingSpace:431e892c-1029-409d-b7b8-b9cad9a0a9e5"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:PhysicalObject:fd304ea2-572f-4b66-b8ad-d9d84c870fa1"  
  },  
  "isSubSystemOf": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:System:b3336716-b468-40f1-be04-9f7ffedcc418",  
      "urn:ngsi-ld:System:05bac9cd-2c56-4046-a70a-b2415e810f43",  
      "urn:ngsi-ld:System:2344579c-27b3-4c5d-9db3-0fd9b46fb7e7"  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Tank Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Tank 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T00:00:57.3062284+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T06:50:59.7051893+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Tank"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Tank type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Tank of limited Tank types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>    
#### Tank NGSI-LD key-values Exemple    
Voici un exemple de Tank au format JSON-LD en tant que key-values. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Tank:7a5293bf-87b8-4768-8c25-56bcbfa91649",  
  "type": "Tank",  
  "accessType": "Auto Loan Account",  
  "effectiveCapacity": 0.6627329008534851,  
  "endShapeType": "Union",  
  "firstCurvatureRadius": 0.6799132713266423,  
  "nominalDepth": 0.07530609187652448,  
  "nominalLengthOrDiameter": 0.1950493997985394,  
  "nominalVolumetricCapacity": 0.6494794060427406,  
  "nominalWidthOrDiameter": 0.2734692629974923,  
  "numberOfSections": 0.3094855572354859,  
  "operatingWeight": 0.3055837938759739,  
  "patternType": "Investment Account",  
  "secondCurvatureRadius": 0.0019846058153857316,  
  "storageType": "Investor",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:ffcd7e11-7c74-45f3-8f5a-3310ababddc8",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:c2540316-a0c2-4363-93b7-e49ab5ed3b2f",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:aae7e0b6-0256-4c58-a3ee-4989bdc205da",  
    "urn:ngsi-ld:System:857551fc-8a05-4052-9269-8193f148ff2c",  
    "urn:ngsi-ld:System:e4e88c0a-d78a-4bfd-a76b-af72e518a66e"  
  ],  
  "hasManufacturer": "Tank Company Inc.",  
  "hasModel": "Tank 0.1.2",  
  "dateCreated": "2023-01-26T12:03:34Z",  
  "dateModified": "2023-01-25T16:27:50Z",  
  "source": "Import",  
  "name": "Tank",  
  "alternateName": "Tank type 2",  
  "description": "Tank of limited Tank types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>    
#### Réservoir NGSI-LD normalisé Exemple    
Voici un exemple de réservoir au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Tank:3d8b578c-7201-4bf4-bd7f-4aa1d9f5d298",  
  "type": "Tank",  
  "accessType": {  
    "type": "Property",  
    "value": "solid state"  
  },  
  "effectiveCapacity": {  
    "type": "Property",  
    "unitCode": "m3.B",  
    "observedAt": "2023-01-26T08:12:59Z",  
    "value": 0.30258616298480145  
  },  
  "endShapeType": {  
    "type": "Property",  
    "value": "Well"  
  },  
  "firstCurvatureRadius": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T08:09:31Z",  
    "value": 0.1755132773764223  
  },  
  "nominalDepth": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T09:14:29Z",  
    "value": 0.005463727391297302  
  },  
  "nominalLengthOrDiameter": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-25T17:31:47Z",  
    "value": 0.1263533877303663  
  },  
  "nominalVolumetricCapacity": {  
    "type": "Property",  
    "unitCode": "m3",  
    "observedAt": "2023-01-26T01:49:01Z",  
    "value": 0.26912875201450304  
  },  
  "nominalWidthOrDiameter": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-25T23:31:21Z",  
    "value": 0.7148569363985878  
  },  
  "numberOfSections": {  
    "type": "Property",  
    "value": 0.4947989850793809  
  },  
  "operatingWeight": {  
    "type": "Property",  
    "unitCode": "g",  
    "observedAt": "2023-01-26T07:09:35Z",  
    "value": 0.3475732824316351  
  },  
  "patternType": {  
    "type": "Property",  
    "value": "Checking Account"  
  },  
  "secondCurvatureRadius": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T05:30:46Z",  
    "value": 0.16951688752044902  
  },  
  "storageType": {  
    "type": "Property",  
    "value": "generate"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:862ca318-44c7-49b8-b0ca-74e1a829af60"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:4b8fd30b-21ae-4587-beaa-21783322f1a8"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:b8611055-a97b-4d01-8cd6-dd7f7931aa2a"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:1f9ab32d-3414-46a9-9bc9-b3f1d1b2c750"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:30979e9d-79b3-4285-ab23-addd0bdb63ef"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Tank Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Tank 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T19:22:34Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-25T19:58:46Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Tank"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Tank type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Tank of limited Tank types"  
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
