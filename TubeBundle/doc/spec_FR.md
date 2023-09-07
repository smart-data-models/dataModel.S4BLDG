<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : TubeBundle  
===================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/TubeBundle/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Un faisceau de tubes est un dispositif composé de tubes et de faisceaux de tubes utilisés pour le transfert de chaleur et contenus généralement dans d'autres dispositifs de conversion d'énergie, tels qu'un refroidisseur ou un serpentin.  
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
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `foulingFactor[number]`: Facteur d'encrassement des tubes dans le faisceau de tubes. Généralement mesuré en m2 Kelvin/Watt  - `hasManufacturer[string]`: Relation identifiant le fabricant d'une entité (par exemple, un appareil). La valeur doit être une chaîne de caractères ou une chaîne de caractères avec une balise linguistique  - `hasModel[string]`: Une relation identifiant le modèle d'une entité (par exemple, un appareil). La valeur doit être une chaîne de caractères ou une chaîne de caractères avec une balise de langue  - `hasTurbulator[boolean]`: VRAI si le tube a un turbulateur, FAUX s'il n'en a pas.  - `horizontalSpacing[number]`: Espacement horizontal entre les tubes dans le faisceau de tubes. Généralement mesuré en millimètres (mm)  - `id[*]`: Identifiant unique de l'entité  - `inLineRowSpacing[number]`: Espacement des rangées de tubes en ligne. Généralement mesuré en millimètres (mm)  - `insideDiameter[number]`: Diamètre intérieur réel du tube dans le faisceau de tubes. Généralement mesuré en millimètres (mm)  - `isContainedInBuildingSpace[*]`: Entité utilisée pour définir les espaces physiques du bâtiment. Un espace de bâtiment contient des dispositifs ou des objets de bâtiment. (Espace Bâtiment)  - `isContainedInPhysicalObject[*]`: Tout objet qui possède une région spatiale propre.  (Définition extraite de l'ontologie DUL) (PhysicalObject)  - `isSubSystemOf[array]`: Référence au(x) système(s) dont cet objet physique fait partie  - `length[number]`: La longueur finie de l'appareil. Généralement mesurée en millimètres (mm)  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément  - `nominalDiameter[number]`: Diamètre nominal ou largeur des tubes dans le faisceau de tubes. Généralement mesuré en millimètres (mm)  - `numberOfCircuits[number]`: Nombre de circuits parallèles de tubes fluides  - `numberOfRows[number]`: Nombre de rangées de tubes dans l'assemblage du faisceau de tubes  - `outsideDiameter[number]`: Diamètre extérieur réel du tube dans le faisceau de tubes. Généralement mesuré en millimètres (mm)  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `staggeredRowSpacing[number]`: Espacement des rangées de tubes en quinconce. Généralement mesuré en millimètres (mm)  - `thermalConductivity[number]`: Facteur d'encrassement des tubes dans le faisceau de tubes. Généralement mesuré en m2 Kelvin/Watt  - `type[string]`: Il doit être égal à `TubeBundle`  - `verticalSpacing[number]`: Espacement vertical entre les tubes dans le faisceau de tubes, généralement mesuré en millimètres (mm).  - `volumen[number]`: Volume total de fluide dans les tubes et leurs collecteurs. Généralement mesuré en mètre cube (m3).  <!-- /30-PropertiesList -->  
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
TubeBundle:    
  description: 'A tube bundle is a device consisting of tubes and bundles of tubes used for heat transfer and contained typically within other energy conversion devices, such as a chiller or coil.'    
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
    foulingFactor:    
      description: Fouling factor of the tubes in the tube bundle. Usually measured in m2 Kelvin/Watt    
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
    hasTurbulator:    
      description: 'TRUE if the tube has a turbulator, FALSE if it does not'    
      type: boolean    
      x-ngsi:    
        type: Property    
    horizontalSpacing:    
      description: Horizontal spacing between tubes in the tube bundle. Usually measured in millimeters (mm)    
      type: number    
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
    inLineRowSpacing:    
      description: In-line tube row spacing. Usually measured in millimeters (mm)    
      type: number    
      x-ngsi:    
        type: Property    
    insideDiameter:    
      description: Actual inner diameter of the tube in the tube bundle. Usually measured in millimeters (mm)    
      type: number    
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
    length:    
      description: The finished length of the device. Usually measured in millimeters (mm)    
      type: number    
      x-ngsi:    
        type: Property    
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
    nominalDiameter:    
      description: Nominal diameter or width of the tubes in the tube bundle. Usually measured in millimeters (mm)    
      type: number    
      x-ngsi:    
        type: Property    
    numberOfCircuits:    
      description: Number of parallel fluid tube circuits    
      type: number    
      x-ngsi:    
        type: Property    
    numberOfRows:    
      description: Number of tube rows in the tube bundle assembly    
      type: number    
      x-ngsi:    
        type: Property    
    outsideDiameter:    
      description: Actual outside diameter of the tube in the tube bundle. Usually measured in millimeters (mm)    
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
    staggeredRowSpacing:    
      description: Staggered tube row spacing. Usually measured in millimeters (mm)    
      type: number    
      x-ngsi:    
        type: Property    
    thermalConductivity:    
      description: Fouling factor of the tubes in the tube bundle. Usually measured in m2 Kelvin/Watt    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: It must be equal to `TubeBundle`    
      enum:    
        - TubeBundle    
      type: string    
      x-ngsi:    
        type: Property    
    verticalSpacing:    
      description: Vertical spacing between tubes in the tube bundle.Usually measured in millimeters (mm)    
      type: number    
      x-ngsi:    
        type: Property    
    volumen:    
      description: Total volume of fluid in the tubes and their headers. Usually measured in cubic metre (m3)    
      type: number    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:TubeBundle"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/TubeBundle/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/TubeBundle/schema.json    
  x-model-tags: SAREF TubeBundle    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### TubeBundle NGSI-v2 key-values Exemple  
Voici un exemple de TubeBundle au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:TubeBundle:ce27cf16-c4dc-4b93-a7e5-021f38a5a0b8",  
    "type": "TubeBundle",  
    "foulingFactor": 0.8435912145074106,  
    "hasTurbulator": true,  
    "horizontalSpacing": 0.45432121749623355,  
    "inLineRowSpacing": 0.9076815444305774,  
    "insideDiameter": 0.9701449888350496,  
    "length": 0.38222174657550045,  
    "nominalDiameter": 0.0408320640034282,  
    "numberOfCircuits": 0.7792295738277125,  
    "numberOfRows": 0.2682132970916634,  
    "outsideDiameter": 0.7194081859650397,  
    "staggeredRowSpacing": 0.31167087959205464,  
    "thermalConductivity": 0.9198905188483331,  
    "verticalSpacing": 0.8194554788890942,  
    "volumen": 0.7779813380010603,  
    "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:a13d415e-6116-43c4-a668-24f7dbf86bc1",  
    "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:6946c181-2515-406c-82f2-6bad063d7f8b",  
    "isSubSystemOf": [  
        "urn:ngsi-ld:System:8f497d54-7104-4546-8fa1-51c409c2b446",  
        "urn:ngsi-ld:System:adfb1f0e-a324-45c4-be4c-1127ac06e4ed",  
        "urn:ngsi-ld:System:614b0bb1-d2d9-425f-a7b1-4063e2ba74fa"  
    ],  
    "hasManufacturer": "TubeBundle Company Inc.",  
    "hasModel": "TubeBundle 0.1.2",  
    "dateCreated": "2023-01-26T00:58:36Z",  
    "dateModified": "2023-01-26T10:38:11Z",  
    "source": "Import",  
    "name": "TubeBundle",  
    "alternateName": "TubeBundle type 2",  
    "description": "TubeBundle of limited TubeBundle types",  
    "dataProvider": "IFC file"  
}  
```  
</details>  
#### TubeBundle NGSI-v2 normalisé Exemple  
Voici un exemple de TubeBundle au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:TubeBundle:75ab66ce-2623-41a5-884f-ed9b90bde563",  
  "type": "TubeBundle",  
  "foulingFactor": {  
    "type": "Measurement",  
    "value": 0.10691025901902518  
  },  
  "hasTurbulator": {  
    "type": "Boolean",  
    "value": false  
  },  
  "horizontalSpacing": {  
    "type": "Measurement",  
    "value": 0.5021481278695225  
  },  
  "inLineRowSpacing": {  
    "type": "Measurement",  
    "value": 0.7015738944986649  
  },  
  "insideDiameter": {  
    "type": "Measurement",  
    "value": 0.47609748066140833  
  },  
  "length": {  
    "type": "Measurement",  
    "value": 0.6920310151935178  
  },  
  "nominalDiameter": {  
    "type": "Measurement",  
    "value": 0.7019643160884628  
  },  
  "numberOfCircuits": {  
    "type": "Float",  
    "value": 0.2146661280911759  
  },  
  "numberOfRows": {  
    "type": "Float",  
    "value": 0.7182471012018697  
  },  
  "outsideDiameter": {  
    "type": "Measurement",  
    "value": 0.41939698462727526  
  },  
  "staggeredRowSpacing": {  
    "type": "Measurement",  
    "value": 0.39127220946141616  
  },  
  "thermalConductivity": {  
    "type": "Measurement",  
    "value": 0.9507857927588059  
  },  
  "verticalSpacing": {  
    "type": "Measurement",  
    "value": 0.08491295072422345  
  },  
  "volumen": {  
    "type": "Measurement",  
    "value": 0.16253433369725145  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:BuildingSpace:e03ce9ef-23a6-4ad9-a533-a960cec73dbe"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:PhysicalObject:1c71e6d7-68ef-4a8d-9fde-985758f88344"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:c9a9c176-b562-42b7-ad80-cc8db2093faa"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:63e522a0-7de4-4bd9-9f94-094efdf565dc"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:0eebd7dc-010a-4f91-a4d1-da8b2a153b7b"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "TubeBundle Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "TubeBundle 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T11:52:01.9956382+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T07:18:26.9100211+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "TubeBundle"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "TubeBundle type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "TubeBundle of limited TubeBundle types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### TubeBundle Valeurs clés NGSI-LD Exemple  
Voici un exemple de TubeBundle au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:TubeBundle:ce27cf16-c4dc-4b93-a7e5-021f38a5a0b8",  
  "type": "TubeBundle",  
  "foulingFactor": 0.8435912145074106,  
  "hasTurbulator": true,  
  "horizontalSpacing": 0.45432121749623355,  
  "inLineRowSpacing": 0.9076815444305774,  
  "insideDiameter": 0.9701449888350496,  
  "length": 0.38222174657550045,  
  "nominalDiameter": 0.0408320640034282,  
  "numberOfCircuits": 0.7792295738277125,  
  "numberOfRows": 0.2682132970916634,  
  "outsideDiameter": 0.7194081859650397,  
  "staggeredRowSpacing": 0.31167087959205464,  
  "thermalConductivity": 0.9198905188483331,  
  "verticalSpacing": 0.8194554788890942,  
  "volumen": 0.7779813380010603,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:a13d415e-6116-43c4-a668-24f7dbf86bc1",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:6946c181-2515-406c-82f2-6bad063d7f8b",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:8f497d54-7104-4546-8fa1-51c409c2b446",  
    "urn:ngsi-ld:System:adfb1f0e-a324-45c4-be4c-1127ac06e4ed",  
    "urn:ngsi-ld:System:614b0bb1-d2d9-425f-a7b1-4063e2ba74fa"  
  ],  
  "hasManufacturer": "TubeBundle Company Inc.",  
  "hasModel": "TubeBundle 0.1.2",  
  "dateCreated": "2023-01-26T00:58:36Z",  
  "dateModified": "2023-01-26T10:38:11Z",  
  "source": "Import",  
  "name": "TubeBundle",  
  "alternateName": "TubeBundle type 2",  
  "description": "TubeBundle of limited TubeBundle types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### TubeBundle NGSI-LD normalisé Exemple  
Voici un exemple de TubeBundle au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:TubeBundle:e896fec0-f21f-4fa6-a73b-274bb42fb0fe",  
  "type": "TubeBundle",  
  "foulingFactor": {  
    "type": "Property",  
    "unitCode": "Kelvin/Watt",  
    "observedAt": "2023-01-25T15:34:45Z",  
    "value": 0.7896142805113859  
  },  
  "hasTurbulator": {  
    "type": "Property",  
    "value": false  
  },  
  "horizontalSpacing": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-25T18:38:27Z",  
    "value": 0.9299315212283089  
  },  
  "inLineRowSpacing": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T04:15:23Z",  
    "value": 0.12680136540868248  
  },  
  "insideDiameter": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T12:46:46Z",  
    "value": 0.9063711005346757  
  },  
  "length": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-25T15:58:18Z",  
    "value": 0.5121996408910179  
  },  
  "nominalDiameter": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T05:13:10Z",  
    "value": 0.8209837702761213  
  },  
  "numberOfCircuits": {  
    "type": "Property",  
    "value": 0.253153343197542  
  },  
  "numberOfRows": {  
    "type": "Property",  
    "value": 0.69547957104902  
  },  
  "outsideDiameter": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T07:32:26Z",  
    "value": 0.7479684351740756  
  },  
  "staggeredRowSpacing": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T08:06:42Z",  
    "value": 0.2757631103143954  
  },  
  "thermalConductivity": {  
    "type": "Property",  
    "unitCode": "Kelvin/Watt",  
    "observedAt": "2023-01-25T15:39:27Z",  
    "value": 0.28193770602031487  
  },  
  "verticalSpacing": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T06:27:04Z",  
    "value": 0.7886025280565963  
  },  
  "volumen": {  
    "type": "Property",  
    "unitCode": "m3",  
    "observedAt": "2023-01-26T05:29:35Z",  
    "value": 0.6238667384353597  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:4943f440-65d7-4fe4-834f-140d786124af"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:6b66c26d-c9a9-4e59-ba5f-5a17174fa9da"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:721e7dae-913a-4e6e-989b-30d545a7ec3d"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:c6a87a94-a7c7-4c31-9b33-6f3ad7861cd0"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:205f1bbb-6bff-422a-9121-4c30a002dfe3"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "TubeBundle Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "TubeBundle 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T21:28:33Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T00:41:51Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "TubeBundle"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "TubeBundle type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "TubeBundle of limited TubeBundle types"  
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
