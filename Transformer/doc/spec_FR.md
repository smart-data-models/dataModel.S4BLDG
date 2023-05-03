<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : Transformateur  
=======================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Transformer/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Un transformateur est un dispositif stationnaire inductif qui transfère l'énergie électrique d'un circuit à un autre.  Le transformateur est utilisé pour transformer l'énergie électrique ; la conversion des signaux électriques à d'autres fins est gérée par d'autres entités : Le contrôleur convertit les signaux arbitraires, l'appareil audiovisuel convertit les signaux pour les flux audio ou vidéo, et l'appareil de communication convertit les signaux pour les données ou d'autres usages de communication**.  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nom alternatif pour ce poste  - `apparentPowerMax[number]`: Propriété. Puissance/capacité apparente maximale en VA (voltampère). Généralement mesurée en watts (W, J/s).  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Date de création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage.  - `dateModified[string]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage.  - `description[string]`: Une description de l'article  - `hasManufacturer[string]`: Propriété. Une relation identifiant le fabricant d'une entité (par exemple, un appareil). La valeur doit être une chaîne de caractères ou une chaîne de caractères avec une étiquette de langue.  - `hasModel[string]`: Propriété. Une relation identifiant le modèle d'une entité (par exemple, un appareil). La valeur doit être une chaîne de caractères ou une chaîne de caractères avec une balise de langue.  - `id[*]`: Identifiant unique de l'entité  - `imaginaryImpedanceRatio[number]`: Propriété. Le rapport entre la partie imaginaire de l'impédance homopolaire et la partie imaginaire de l'impédance positive (c'est-à-dire la partie imaginaire de la tension de court-circuit) du transformateur. Utilisé pour les transformateurs triphasés qui comprennent un conducteur N.  - `isContainedInBuildingSpace[*]`: Relations. Entité utilisée pour définir les espaces physiques du bâtiment. Un espace de bâtiment contient des appareils ou des objets de bâtiment. (Espace Bâtiment)  - `isContainedInPhysicalObject[*]`: Relation. Tout objet qui possède une région spatiale propre.  (Définition extraite de l'ontologie DUL) (PhysicalObject)  - `isNeutralPrimaryTerminalAvailable[boolean]`: Propriété. Indique si le point neutre de l'enroulement primaire est disponible comme borne (= VRAI) ou non (= FAUX).  - `isNeutralSecondaryTerminalAvailable[boolean]`: Propriété. Indique si le point neutre de l'enroulement secondaire est disponible comme borne (= VRAI) ou non (= FAUX).  - `isSubSystemOf[array]`: Relation. Référence à un ou plusieurs systèmes dont cet objet physique fait partie.  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément.  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `primaryApparentPower[number]`: Propriété. La puissance en VA (voltampère) qui a été transformée et qui entre dans le transformateur du côté primaire. Habituellement mesurée en watts (W, J/s).  - `primaryCurrent[number]`: Propriété. Le courant qui va être transformé et qui entre dans le transformateur du côté primaire. Généralement mesuré en Ampère (A).  - `primaryFrequency[number]`: Propriété. La fréquence qui va être transformée et qui entre dans le transformateur du côté primaire. Généralement mesurée en cycles/s ou en Hertz (Hz).  - `primaryVoltage[number]`: Propriété. La tension qui va être transformée et qui entre dans le transformateur du côté primaire. Généralement mesurée en Volts (V, W/A).  - `realImpedanceRatio[number]`: Propriété. Le rapport entre la partie réelle de l'impédance homopolaire et la partie réelle de l'impédance positive (c'est-à-dire la partie réelle de la tension de court-circuit) du transformateur. Utilisé pour les transformateurs triphasés qui comprennent un conducteur N.  - `secondaryApparentPower[number]`: Propriété. La puissance en VA (voltampère) qui a été transformée et qui sort du transformateur du côté secondaire. Habituellement mesurée en watts (W, J/s).  - `secondaryCurrent[number]`: Propriété. Le courant qui a été transformé et qui sort du transformateur du côté secondaire. Généralement mesuré en Ampère (A).  - `secondaryCurrentType[string]`: Propriété. Liste des types de courant secondaire pouvant résulter de la sortie du transformateur.  - `secondaryFrequency[number]`: Propriété. La fréquence qui a été transformée et qui sort du transformateur du côté secondaire. Généralement mesurée en cycles/s ou en Hertz (Hz).  - `secondaryVoltage[number]`: Propriété. La tension qui a été transformée et qui sort du transformateur du côté secondaire. Généralement mesurée en Volts (V, W/A).  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `transformerVectorGroup[string]`: Propriété. Liste des groupes de vecteurs possibles pour le transformateur, à partir desquels la valeur requise peut être définie. Les valeurs de la liste d'énumération suivent un code international standard où la première lettre décrit la façon dont les enroulements primaires sont connectés, la deuxième lettre décrit la façon dont les enroulements secondaires sont connectés, et les chiffres décrivent la rotation des tensions et des courants du côté primaire au côté secondaire par multiples de 30 degrés. D : signifie que les enroulements sont connectés en triangle. Y : signifie que les enroulements sont connectés en étoile. Z : signifie que les enroulements sont connectés en zig-zag (une connexion de démarrage spéciale assurant une faible réactance du transformateur). La connectivité ne concerne que les transformateurs triphasés.  - `type[string]`: Propriété. Elle doit être égale à `Transformer`.  <!-- /30-PropertiesList -->  
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
Transformer:    
  description: 'A transformer is an inductive stationary device that transfers electrical energy from one circuit to another.  Transformer is used to transform electric power; conversion of electric signals for other purposes is handled at other entities: Controller converts arbitrary signals, AudioVisualAppliance converts signals for audio or video streams, and CommunicationsAppliance converts signals for data or other communications usage.'    
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
    apparentPowerMax:    
      description: 'Property. Maximum apparent power/capacity in VA (volt ampere). Usually measured in Watts (W, J/s).'    
      type: number    
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
      anyOf: &transformer_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    imaginaryImpedanceRatio:    
      description: Property. The ratio between the imaginary part of the zero sequence impedance and the imaginary part of the positive impedance (i.e. imaginary part of the short-circuit voltage) of the transformer. Used for three-phase transformer which includes a N-conductor.    
      type: number    
      x-ngsi:    
        type: Property    
    isContainedInBuildingSpace:    
      anyOf: *transformer_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *transformer_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isNeutralPrimaryTerminalAvailable:    
      description: Property. An indication of whether the neutral point of the primary winding is available as a terminal (=TRUE) or not (= FALSE).    
      type: boolean    
      x-ngsi:    
        type: Property    
    isNeutralSecondaryTerminalAvailable:    
      description: Property. An indication of whether the neutral point of the secondary winding is available as a terminal (=TRUE) or not (= FALSE).    
      type: boolean    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *transformer_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
        anyOf: *transformer_-_properties_-_iscontainedinbuildingspace_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    primaryApparentPower:    
      description: 'Property. The power in VA (volt ampere) that has been transformed and that runs into the transformer on the primary side. Usually measured in Watts (W, J/s).'    
      type: number    
      x-ngsi:    
        type: Property    
    primaryCurrent:    
      description: Property. The current that is going to be transformed and that runs into the transformer on the primary side. Usually measured in Ampere (A).    
      type: number    
      x-ngsi:    
        type: Property    
    primaryFrequency:    
      description: Property. The frequency that is going to be transformed and that runs into the transformer on the primary side. Usually measured in cycles/s or Hertz (Hz).    
      type: number    
      x-ngsi:    
        type: Property    
    primaryVoltage:    
      description: 'Property. The voltage that is going to be transformed and that runs into the transformer on the primary side. Usually measured in Volts (V, W/A).'    
      type: number    
      x-ngsi:    
        type: Property    
    realImpedanceRatio:    
      description: Property. The ratio between the real part of the zero sequence impedance and the real part of the positive impedance (i.e. real part of the short-circuit voltage) of the transformer. Used for three-phase transformer which includes a N-conductor.    
      type: number    
      x-ngsi:    
        type: Property    
    secondaryApparentPower:    
      description: 'Property. The power in VA (volt ampere) that has been transformed and is running out of the transformer on the secondary side. Usually measured in Watts (W, J/s).'    
      type: number    
      x-ngsi:    
        type: Property    
    secondaryCurrent:    
      description: Property. The current that has been transformed and is running out of the transformer on the secondary side. Usually measured in Ampere (A).    
      type: number    
      x-ngsi:    
        type: Property    
    secondaryCurrentType:    
      description: Property. A list of the secondary current types that can result from transformer output.    
      type: string    
      x-ngsi:    
        type: Property    
    secondaryFrequency:    
      description: Property. The frequency that has been transformed and is running out of the transformer on the secondary side. Usually measured in cycles/s or Hertz (Hz).    
      type: number    
      x-ngsi:    
        type: Property    
    secondaryVoltage:    
      description: 'Property. The voltage that has been transformed and is running out of the transformer on the secondary side. Usually measured in Volts (V, W/A).'    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    transformerVectorGroup:    
      description: 'Property. List of the possible vector groups for the transformer from which that required may be set. Values in the enumeration list follow a standard international code where the first letter describes how the primary windings are connected, the second letter describes how the secondary windings are connected, and the numbers describe the rotation of voltages and currents from the primary to the secondary side in multiples of 30 degrees. D: means that the windings are delta-connected. Y: means that the windings are star-connected. Z: means that the windings are zig-zag connected (a special start-connected providing low reactance of the transformer). The connectivity is only relevant for three-phase transformers.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: Property. It must be equal to `Transformer`.    
      enum:    
        - Transformer    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Transformer"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Transformer/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Transformer/schema.json    
  x-model-tags: SAREF Transformer    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### Transformateur NGSI-v2 valeurs-clés Exemple  
Voici un exemple de Transformer au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Transformer:4976b0ec-0c96-4ae1-91da-c906da8348da",  
    "type": "Transformer",  
    "apparentPowerMax": 0.17497838413457267,  
    "imaginaryImpedanceRatio": 0.5323895083879017,  
    "isNeutralPrimaryTerminalAvailable": false,  
    "isNeutralSecondaryTerminalAvailable": true,  
    "primaryApparentPower": 0.8765115449298688,  
    "primaryCurrent": 0.871670986786111,  
    "primaryFrequency": 0.141749759362659,  
    "primaryVoltage": 0.5038263292514936,  
    "realImpedanceRatio": 0.06325384828151492,  
    "secondaryApparentPower": 0.45704946090246745,  
    "secondaryCurrent": 0.4016609926228465,  
    "secondaryCurrentType": "Data",  
    "secondaryFrequency": 0.7436141485906284,  
    "secondaryVoltage": 0.4646450009162978,  
    "transformerVectorGroup": "Soft",  
    "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:51645089-5e36-4b9c-ad25-b97b58506919",  
    "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:6737e804-54ff-41c0-ba12-90dde24f3d59",  
    "isSubSystemOf": [  
        "urn:ngsi-ld:System:38dfdf15-5a41-412d-9b05-435cb7809e6f",  
        "urn:ngsi-ld:System:b7274b46-33ec-4694-8dda-999197bb58c5",  
        "urn:ngsi-ld:System:b7d5c2ce-fc23-42d0-be8f-9e56a9f3c5db"  
    ],  
    "hasManufacturer": "Transformer Company Inc.",  
    "hasModel": "Transformer 0.1.2",  
    "dateCreated": "2023-01-25T16:42:43Z",  
    "dateModified": "2023-01-26T13:53:42Z",  
    "source": "Import",  
    "name": "Transformer",  
    "alternateName": "Transformer type 2",  
    "description": "Transformer of limited Transformer types",  
    "dataProvider": "IFC file"  
}  
```  
</details>  
#### Transformateur NGSI-v2 normalisé Exemple  
Voici un exemple de transformateur au format JSON-LD tel qu'il a été normalisé. Il est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Transformer:7dc130e2-e429-4c26-b467-ec9d1f41e7b8",  
  "type": "Transformer",  
  "apparentPowerMax": {  
    "type": "Measurement",  
    "value":  0.6561932522421066  
  },  
  "imaginaryImpedanceRatio": {  
    "type": "Measurement",  
    "value": 0.7913482963385954  
  },  
  "isNeutralPrimaryTerminalAvailable": {  
    "type": "Boolean",  
    "value": true  
  },  
  "isNeutralSecondaryTerminalAvailable": {  
    "type": "Boolean",  
    "value": true  
  },  
  "primaryApparentPower": {  
    "type": "Measurement",  
    "value":  0.23470397848013025  
  },  
  "primaryCurrent": {  
    "type": "Measurement",  
    "value":  0.7245530289719985  
  },  
  "primaryFrequency": {  
    "type": "Measurement",  
    "value":  0.18927842693402908  
  },  
  "primaryVoltage": {  
    "type": "Measurement",  
    "value":  0.359590276424793  
  },  
  "realImpedanceRatio": {  
    "type": "Measurement",  
    "value":  0.6917590580595899  
  },  
  "secondaryApparentPower": {  
    "type": "Measurement",  
    "value":  0.10075664755263747  
  },  
  "secondaryCurrent": {  
    "type": "Measurement",  
    "value": 0.1458215404162363  
  },  
  "secondaryCurrentType": {  
    "type": "Text",  
    "value": "Tasty Wooden Car"  
  },  
  "secondaryFrequency": {  
    "type": "Measurement",  
    "value":  0.09146741937660052  
  },  
  "secondaryVoltage": {  
    "type": "Measurement",  
    "value": 0.31779800995261864  
  },  
  "transformerVectorGroup": {  
    "type": "Text",  
    "value": "SMS"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:BuildingSpace:16bccee7-8244-4707-8d4b-c5a06b0fee75"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:PhysicalObject:b9a1bd5e-114e-41ba-b865-25b4b4c5c3c5"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:37554df5-ec0d-4e03-8697-7d562ff2134f"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:e967a169-474b-47a0-bd0c-a76ce8a5f7be"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:49a6b09b-2301-4b6e-a167-54ee44cc83d4"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Transformer Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Transformer 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T20:08:21.2034652+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T22:13:38.7837862+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Transformer"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Transformer type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Transformer of limited Transformer types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### Transformateur Valeurs clés NGSI-LD Exemple  
Voici un exemple de Transformer au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Transformer:4976b0ec-0c96-4ae1-91da-c906da8348da",  
  "type": "Transformer",  
  "apparentPowerMax": 0.17497838413457267,  
  "imaginaryImpedanceRatio": 0.5323895083879017,  
  "isNeutralPrimaryTerminalAvailable": false,  
  "isNeutralSecondaryTerminalAvailable": true,  
  "primaryApparentPower": 0.8765115449298688,  
  "primaryCurrent": 0.871670986786111,  
  "primaryFrequency": 0.141749759362659,  
  "primaryVoltage": 0.5038263292514936,  
  "realImpedanceRatio": 0.06325384828151492,  
  "secondaryApparentPower": 0.45704946090246745,  
  "secondaryCurrent": 0.4016609926228465,  
  "secondaryCurrentType": "Data",  
  "secondaryFrequency": 0.7436141485906284,  
  "secondaryVoltage": 0.4646450009162978,  
  "transformerVectorGroup": "Soft",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:51645089-5e36-4b9c-ad25-b97b58506919",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:6737e804-54ff-41c0-ba12-90dde24f3d59",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:38dfdf15-5a41-412d-9b05-435cb7809e6f",  
    "urn:ngsi-ld:System:b7274b46-33ec-4694-8dda-999197bb58c5",  
    "urn:ngsi-ld:System:b7d5c2ce-fc23-42d0-be8f-9e56a9f3c5db"  
  ],  
  "hasManufacturer": "Transformer Company Inc.",  
  "hasModel": "Transformer 0.1.2",  
  "dateCreated": "2023-01-25T16:42:43Z",  
  "dateModified": "2023-01-26T13:53:42Z",  
  "source": "Import",  
  "name": "Transformer",  
  "alternateName": "Transformer type 2",  
  "description": "Transformer of limited Transformer types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### Transformateur NGSI-LD normalisé Exemple  
Voici un exemple de transformateur au format JSON-LD tel qu'il a été normalisé. Il est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Transformer:24b95122-4055-44dc-82ad-09a2bcda9025",  
  "type": "Transformer",  
  "apparentPowerMax": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-25T20:30:38Z",  
    "value": 0.24466523496915848  
  },  
  "imaginaryImpedanceRatio": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T00:56:06Z",  
    "value": 0.0034198103714959682  
  },  
  "isNeutralPrimaryTerminalAvailable": {  
    "type": "Property",  
    "value": false  
  },  
  "isNeutralSecondaryTerminalAvailable": {  
    "type": "Property",  
    "value": true  
  },  
  "primaryApparentPower": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-26T12:47:55Z",  
    "value": 0.9141641275735504  
  },  
  "primaryCurrent": {  
    "type": "Property",  
    "unitCode": "A",  
    "observedAt": "2023-01-26T04:09:04Z",  
    "value": 0.21921580436899846  
  },  
  "primaryFrequency": {  
    "type": "Property",  
    "unitCode": "Hz",  
    "observedAt": "2023-01-26T11:27:17Z",  
    "value": 0.8873577584995188  
  },  
  "primaryVoltage": {  
    "type": "Property",  
    "unitCode": "W/A",  
    "observedAt": "2023-01-26T07:23:40Z",  
    "value": 0.33421317836814646  
  },  
  "realImpedanceRatio": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T03:38:23Z",  
    "value": 0.6061321069719529  
  },  
  "secondaryApparentPower": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-25T19:57:55Z",  
    "value": 0.3997980055591537  
  },  
  "secondaryCurrent": {  
    "type": "Property",  
    "unitCode": "A",  
    "observedAt": "2023-01-26T13:58:27Z",  
    "value": 0.2899846616898377  
  },  
  "secondaryCurrentType": {  
    "type": "Property",  
    "value": "human-resource"  
  },  
  "secondaryFrequency": {  
    "type": "Property",  
    "unitCode": "Hz",  
    "observedAt": "2023-01-26T03:39:16Z",  
    "value": 0.06983160765779406  
  },  
  "secondaryVoltage": {  
    "type": "Property",  
    "unitCode": "W/A",  
    "observedAt": "2023-01-26T07:19:14Z",  
    "value": 0.8594539881916403  
  },  
  "transformerVectorGroup": {  
    "type": "Property",  
    "value": "digital"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:ded8c891-dfe1-4973-966c-96ab6231373d"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:aab67381-2a15-4bdc-ab0f-953b17253b8f"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:d06b6674-162c-4593-a8fd-3874ef353008"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:d0aca3bd-bf1b-4e9e-a998-a76c9b1ac7a6"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:1ab049a0-7295-4eef-82a1-0bb422132435"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Transformer Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Transformer 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T06:32:52Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T05:11:11Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Transformer"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Transformer type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Transformer of limited Transformer types"  
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
