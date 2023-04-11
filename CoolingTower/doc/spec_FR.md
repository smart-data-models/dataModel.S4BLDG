<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : Tour de refroidissement  
================================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/CoolingTower/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Une tour de refroidissement est un dispositif qui rejette la chaleur dans l'air ambiant en y faisant circuler un fluide tel que de l'eau afin de réduire sa température par évaporation partielle.  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nom alternatif pour ce poste  - `ambientDesignDryBulbTemperature[number]`: Propriété. Température ambiante du bulbe sec utilisée pour sélectionner la tour de refroidissement. Généralement mesurée en degrés Kelvin (K).  - `ambientDesignWetBulbTemperature[number]`: Propriété. Température ambiante du bulbe humide utilisée pour sélectionner la tour de refroidissement. Généralement mesurée en degrés Kelvin (K).  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `basinReserveVolume[number]`: Propriété. Volume entre les niveaux de fonctionnement et de débordement dans le bassin de la tour de refroidissement. Généralement mesuré en mètre cube (m3).  - `capacityControl[string]`: Propriété. FanCycling : Le ventilateur est activé et désactivé de manière cyclique pour contrôler le fonctionnement. TwoSpeedFan (ventilateur à deux vitesses) : le ventilateur passe de la vitesse lente à la vitesse rapide pour contrôler le fonctionnement. VariableSpeedFan (ventilateur à vitesse variable) : la vitesse du ventilateur varie pour contrôler le fonctionnement. Contrôle des amortisseurs : Les amortisseurs modulent le débit d'air pour contrôler le fonctionnement. Contrôle de la vanne de dérivation : La vanne de dérivation module le débit d'eau pour contrôler le fonctionnement. MultipleSeriesPumps : Activation/désactivation d'une pompe à séries multiples pour contrôler le fonctionnement. Pompe à deux vitesses : Passer d'une vitesse de pompe élevée à une vitesse faible pour contrôler le fonctionnement. Pompe à vitesse variable : fait varier la vitesse de la pompe pour contrôler le fonctionnement.  - `circuitType[string]`: Propriété. Circuit ouvert : expose l'eau directement à l'atmosphère de refroidissement. CloseCircuit : Le fluide est séparé de l'atmosphère par un échangeur de chaleur. Humide : Le flux d'air ou la surface d'échange de chaleur est refroidi par évaporation. Sec : Pas d'évaporation dans le flux d'air. DryWet : Combinaison d'une tour sèche et d'une tour humide.  - `controlStrategy[string]`: Propriété. FixedExitingWaterTemp : La capacité est contrôlée pour maintenir une température fixe de l'eau à la sortie. WetBulbTempReset : Le point de consigne est réinitialisé en fonction de la température du thermomètre mouillé.  - `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Date de création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage.  - `dateModified[string]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage.  - `description[string]`: Une description de l'article  - `flowArrangement[string]`: Propriété. Contre-courant : l'air et l'eau entrent dans des directions différentes. Flux croisé : les flux d'air et d'eau sont perpendiculaires. Écoulement parallèle : l'air et l'eau s'écoulent dans les mêmes directions.  - `hasManufacturer[string]`: Propriété. Une relation identifiant le fabricant d'une entité (par exemple, un appareil). La valeur doit être une chaîne de caractères ou une chaîne de caractères avec une étiquette de langue.  - `hasModel[string]`: Propriété. Une relation identifiant le modèle d'une entité (par exemple, un appareil). La valeur doit être une chaîne de caractères ou une chaîne de caractères avec une balise de langue.  - `id[*]`: Identifiant unique de l'entité  - `isContainedInBuildingSpace[*]`: Relations. Entité utilisée pour définir les espaces physiques du bâtiment. Un espace de bâtiment contient des appareils ou des objets de bâtiment. (Espace Bâtiment)  - `isContainedInPhysicalObject[*]`: Relation. Tout objet qui possède une région spatiale propre.  (Définition extraite de l'ontologie DUL) (PhysicalObject)  - `isSubSystemOf[array]`: Relation. Référence à un ou plusieurs systèmes dont cet objet physique fait partie.  - `liftElevationDifference[number]`: Propriété. Différence d'altitude entre le bassin de la tour de refroidissement et le sommet de la tour. Généralement mesurée en millimètres (mm).  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément.  - `nominalCapacity[number]`: Propriété. Capacité nominale. Généralement mesurée en watts (W, J/s).  - `numberOfCells[number]`: Propriété. Nombre de cellules dans une unité de tour de refroidissement.  - `operationTemperatureMax[number]`: Propriété. Plage de température ambiante (air, fluide) autorisée pour le fonctionnement. Généralement mesurée en degrés Kelvin (K).  - `operationTemperatureMin[number]`: Propriété. Plage de température ambiante (air, fluide) autorisée pour le fonctionnement. Généralement mesurée en degrés Kelvin (K).  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `sprayType[string]`: Propriété. SprayFilled : L'eau est pulvérisée dans le flux d'air. SplashTypeFill : l'eau tombe en cascade sur des rangées successives de barres d'éclaboussures. FilmTypeFill : l'eau s'écoule en fine couche sur des feuilles étroitement espacées.  - `type[string]`: Propriété. Elle doit être égale à `CoolingTower`.  - `waterRequirement[number]`: Propriété. Besoin en eau d'appoint. Généralement mesuré en m3/s.  <!-- /30-PropertiesList -->  
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
CoolingTower:    
  description: A cooling tower is a device which rejects heat to ambient air by circulating a fluid such as water through it to reduce its temperature by partial evaporation.    
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
    ambientDesignDryBulbTemperature:    
      description: Property. Ambient design dry bulb temperature used for selecting the cooling tower. Usually measured in degrees Kelvin (K).    
      type: number    
      x-ngsi:    
        type: Property    
    ambientDesignWetBulbTemperature:    
      description: Property. Ambient design wet bulb temperature used for selecting the cooling tower. Usually measured in degrees Kelvin (K).    
      type: number    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    basinReserveVolume:    
      description: Property. Volume between operating and overflow levels in cooling tower basin. Usually measured in cubic metre (m3).    
      type: number    
      x-ngsi:    
        type: Property    
    capacityControl:    
      description: 'Property. FanCycling: Fan is cycled on and off to control duty. TwoSpeedFan: Fan is switched between low and high speed to control duty. VariableSpeedFan: Fan speed is varied to control duty. DampersControl: Dampers modulate the air flow to control duty. BypassValveControl: Bypass valve modulates the water flow to control duty. MultipleSeriesPumps: Turn on/off multiple series pump to control duty. TwoSpeedPump: Switch between high/low pump speed to control duty. VariableSpeedPump: vary pump speed to control duty.'    
      type: string    
      x-ngsi:    
        type: Property    
    circuitType:    
      description: 'Property. OpenCircuit: Exposes water directly to the cooling atmosphere. CloseCircuit: The fluid is separated from the atmosphere by a heat exchanger. Wet: The air stream or the heat exchange surface is evaporatively cooled. Dry: No evaporation into the air stream. DryWet: A combination of a dry tower and a wet tower.'    
      type: string    
      x-ngsi:    
        type: Property    
    controlStrategy:    
      description: 'Property. FixedExitingWaterTemp: The capacity is controlled to maintain a fixed exiting water temperature. WetBulbTempReset: The set-point is reset based on the wet-bulb temperature.'    
      type: string    
      x-ngsi:    
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
    flowArrangement:    
      description: 'Property. CounterFlow: Air and water flow enter in different directions. CrossFlow: Air and water flow are perpendicular. ParallelFlow: air and water flow enter in same directions.'    
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
      anyOf: &coolingtower_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      anyOf: *coolingtower_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *coolingtower_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *coolingtower_-_properties_-_iscontainedinbuildingspace_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Relationship    
    liftElevationDifference:    
      description: Property. Elevation difference between cooling tower sump and the top of the tower. Usually measured in millimeters (mm).    
      type: number    
      x-ngsi:    
        type: Property    
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
    nominalCapacity:    
      description: 'Property. Nominal capacity. Usually measured in Watts (W, J/s).'    
      type: number    
      x-ngsi:    
        type: Property    
    numberOfCells:    
      description: Property. Number of cells in one cooling tower unit.    
      type: number    
      x-ngsi:    
        type: Property    
    operationTemperatureMax:    
      description: 'Property. Allowable operation ambient (air, fluid) temperature range. Usually measured in degrees Kelvin (K).'    
      type: number    
      x-ngsi:    
        type: Property    
    operationTemperatureMin:    
      description: 'Property. Allowable operation ambient (air, fluid) temperature range. Usually measured in degrees Kelvin (K).'    
      type: number    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *coolingtower_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    sprayType:    
      description: 'Property. SprayFilled: Water is sprayed into airflow. SplashTypeFill: water cascades over successive rows of splash bars. FilmTypeFill: water flows in a thin layer over closely spaced sheets.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: Property. It must be equal to `CoolingTower`.    
      enum:    
        - CoolingTower    
      type: string    
      x-ngsi:    
        type: Property    
    waterRequirement:    
      description: Property. Make-up water requirement. Usually measured in m3/s.    
      type: number    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:CoolingTower"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/CoolingTower/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/CoolingTower/schema.json    
  x-model-tags: SAREF CoolingTower    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### CoolingTower NGSI-v2 valeurs clés Exemple  
Voici un exemple d'une CoolingTower au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:CoolingTower:c628d24d-5b25-4b99-838e-35676956d307",  
  "type": "CoolingTower",  
  "ambientDesignDryBulbTemperature": 0.7275209381168831,  
  "ambientDesignWetBulbTemperature": 0.8419497776651206,  
  "basinReserveVolume": 0.9886525691530367,  
  "capacityControl": "Lead",  
  "circuitType": "virtual",  
  "controlStrategy": "Harbors",  
  "flowArrangement": "Extensions",  
  "liftElevationDifference": 0.9337996577856725,  
  "nominalCapacity": 0.8043496896372141,  
  "numberOfCells": 0.03361385186991317,  
  "operationTemperatureMax": 0.7125610456321683,  
  "operationTemperatureMin": 0.3015974804386986,  
  "sprayType": "programming",  
  "waterRequirement": 0.1817597423361893,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:6871b1ec-cfce-4a60-83c2-9f07b13d1703",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:e2a48930-276e-4972-9283-82fbc22faf85",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:aea47887-bc5b-47c3-aeb0-870506d76580",  
    "urn:ngsi-ld:System:2791b628-8fc1-4ec1-91a7-26efbbc892a3",  
    "urn:ngsi-ld:System:c0623c49-ae1f-4772-9323-a94078dbdb86"  
  ],  
  "hasManufacturer": "CoolingTower Company Inc.",  
  "hasModel": "CoolingTower 0.1.2",  
  "dateCreated": "2023-01-26T12:17:43Z",  
  "dateModified": "2023-01-25T16:13:00Z",  
  "source": "Import",  
  "name": "CoolingTower",  
  "alternateName": "CoolingTower type 2",  
  "description": "CoolingTower of limited CoolingTower types",  
  "dataProvider": "IFC file"  
}  
```  
</details>  
#### CoolingTower NGSI-v2 normalisé Exemple  
Voici un exemple de tour de refroidissement au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec l'INSG-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:CoolingTower:7995c5cf-c8c3-4e42-92db-6dd840796eae",  
  "type": "CoolingTower",  
  "ambientDesignDryBulbTemperature": {  
    "type": "Measurement",  
    "value": 0.36789185492213194  
  },  
  "ambientDesignWetBulbTemperature": {  
    "type": "Measurement",  
    "value": 0.1490037569659941  
  },  
  "basinReserveVolume": {  
    "type": "Measurement",  
    "value": 0.9142388286093716  
  },  
  "capacityControl": {  
    "type": "Text",  
    "value": "next-generation"  
  },  
  "circuitType": {  
    "type": "Text",  
    "value": "morph"  
  },  
  "controlStrategy": {  
    "type": "Text",  
    "value": "Concrete"  
  },  
  "flowArrangement": {  
    "type": "Text",  
    "value": "access"  
  },  
  "liftElevationDifference": {  
    "type": "Measurement",  
    "value": 0.6134421322995507  
  },  
  "nominalCapacity": {  
    "type": "Measurement",  
    "value": 0.14285208313177855  
  },  
  "numberOfCells": {  
    "type": "Float",  
    "value": 0.9307947920697038  
  },  
  "operationTemperatureMax": {  
    "type": "Measurement",  
    "value": 0.33271163839338236  
  },  
  "operationTemperatureMin": {  
    "type": "Measurement",  
    "value": 0.8346930607066967  
  },  
  "sprayType": {  
    "type": "Text",  
    "value": "synthesizing"  
  },  
  "waterRequirement": {  
    "type": "Measurement",  
    "value": 0.6749365729986966  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:BuildingSpace:e1c9dc03-9887-49df-9577-a24218339c39"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:PhysicalObject:d6e1c0cc-a656-4343-8572-21de93d365ba"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:972d1b4b-ab6d-474c-a742-c75822d6c7b8"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:8c7d509c-66b4-4504-ad2e-d7ec82146ba2"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:42d552ca-9fdd-4838-804e-41f34d6f61f7"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "CoolingTower Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "CoolingTower 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T21:28:15.4871264+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T13:03:39.0857574+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "CoolingTower"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "CoolingTower type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "CoolingTower of limited CoolingTower types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### CoolingTower Valeurs clés NGSI-LD Exemple  
Voici un exemple d'une tour de refroidissement au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:CoolingTower:c628d24d-5b25-4b99-838e-35676956d307",  
  "type": "CoolingTower",  
  "ambientDesignDryBulbTemperature": 0.7275209381168831,  
  "ambientDesignWetBulbTemperature": 0.8419497776651206,  
  "basinReserveVolume": 0.9886525691530367,  
  "capacityControl": "Lead",  
  "circuitType": "virtual",  
  "controlStrategy": "Harbors",  
  "flowArrangement": "Extensions",  
  "liftElevationDifference": 0.9337996577856725,  
  "nominalCapacity": 0.8043496896372141,  
  "numberOfCells": 0.03361385186991317,  
  "operationTemperatureMax": 0.7125610456321683,  
  "operationTemperatureMin": 0.3015974804386986,  
  "sprayType": "programming",  
  "waterRequirement": 0.1817597423361893,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:6871b1ec-cfce-4a60-83c2-9f07b13d1703",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:e2a48930-276e-4972-9283-82fbc22faf85",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:aea47887-bc5b-47c3-aeb0-870506d76580",  
    "urn:ngsi-ld:System:2791b628-8fc1-4ec1-91a7-26efbbc892a3",  
    "urn:ngsi-ld:System:c0623c49-ae1f-4772-9323-a94078dbdb86"  
  ],  
  "hasManufacturer": "CoolingTower Company Inc.",  
  "hasModel": "CoolingTower 0.1.2",  
  "dateCreated": "2023-01-26T12:17:43Z",  
  "dateModified": "2023-01-25T16:13:00Z",  
  "source": "Import",  
  "name": "CoolingTower",  
  "alternateName": "CoolingTower type 2",  
  "description": "CoolingTower of limited CoolingTower types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### CoolingTower NGSI-LD normalisé Exemple  
Voici un exemple de tour de refroidissement au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:CoolingTower:eb831bd2-82be-42c3-a0c9-a6c0a231e316",  
  "type": "CoolingTower",  
  "ambientDesignDryBulbTemperature": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T08:09:09Z",  
    "value": 0.9762464796853121  
  },  
  "ambientDesignWetBulbTemperature": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T14:29:40Z",  
    "value": 0.3062794162138128  
  },  
  "basinReserveVolume": {  
    "type": "Property",  
    "unitCode": "m3",  
    "observedAt": "2023-01-26T01:28:50Z",  
    "value": 0.9472477891325785  
  },  
  "capacityControl": {  
    "type": "Property",  
    "value": "input"  
  },  
  "circuitType": {  
    "type": "Property",  
    "value": "Mauritania"  
  },  
  "controlStrategy": {  
    "type": "Property",  
    "value": "Investor"  
  },  
  "flowArrangement": {  
    "type": "Property",  
    "value": "Direct"  
  },  
  "liftElevationDifference": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T02:02:47Z",  
    "value": 0.36539365901818843  
  },  
  "nominalCapacity": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-25T22:40:21Z",  
    "value": 0.3624642546775261  
  },  
  "numberOfCells": {  
    "type": "Property",  
    "value": 0.5588013730579288  
  },  
  "operationTemperatureMax": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T23:30:50Z",  
    "value": 0.660338038211496  
  },  
  "operationTemperatureMin": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T23:56:27Z",  
    "value": 0.0877235060077185  
  },  
  "sprayType": {  
    "type": "Property",  
    "value": "Money Market Account"  
  },  
  "waterRequirement": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-25T16:48:25Z",  
    "value": 0.40722633971933253  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:61ad4f84-a577-49d5-a088-aa301efa4ec6"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:f02a5bc4-2f87-4ff7-8dd7-fb61243128a1"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:b9323186-933c-46fd-815f-7f025b04ca80"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:1cea31ba-2978-4af2-b717-5c2a98a431b4"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:13dbe647-863b-4b1f-b10c-1737310d7c51"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "CoolingTower Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "CoolingTower 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T23:05:59Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-25T18:47:19Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "CoolingTower"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "CoolingTower type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "CoolingTower of limited CoolingTower types"  
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
