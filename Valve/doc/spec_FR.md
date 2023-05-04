<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : Valve  
==============<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Valve/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Une vanne est utilisée dans un système de distribution de tuyauterie de bâtiment pour contrôler ou moduler le débit du fluide.  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `closeOffRating[number]`: Propriété. Indice de fermeture. Généralement mesuré en Pascals (Pa, N/m2).  - `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Date de création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage.  - `dateModified[string]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage.  - `description[string]`: Une description de l'article  - `flowCoefficient[number]`: Propriété. Coefficient de débit (quantité de fluide qui passe à travers une vanne entièrement ouverte pour une perte de charge unitaire), généralement exprimé comme la valeur Kv ou Cv de la vanne.  - `hasManufacturer[string]`: Propriété. Une relation identifiant le fabricant d'une entité (par exemple, un appareil). La valeur doit être une chaîne de caractères ou une chaîne de caractères avec une étiquette de langue.  - `hasModel[string]`: Propriété. Une relation identifiant le modèle d'une entité (par exemple, un appareil). La valeur doit être une chaîne de caractères ou une chaîne de caractères avec une balise de langue.  - `id[*]`: Identifiant unique de l'entité  - `isContainedInBuildingSpace[*]`: Relations. Entité utilisée pour définir les espaces physiques du bâtiment. Un espace de bâtiment contient des appareils ou des objets de bâtiment. (Espace Bâtiment)  - `isContainedInPhysicalObject[*]`: Relation. Tout objet qui possède une région spatiale propre.  (Définition extraite de l'ontologie DUL) (PhysicalObject)  - `isSubSystemOf[array]`: Relation. Référence à un ou plusieurs systèmes dont cet objet physique fait partie.  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément.  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `size[number]`: Propriété. La taille de la connexion au robinet (ou à chaque connexion pour les robinets, les vannes de mélange, etc.) Généralement mesurée en millimètres (mm).  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `testPressure[number]`: Propriété. La pression maximale à laquelle la soupape a été soumise lors de l'essai. Généralement mesurée en Pascals (Pa, N/m2).  - `type[string]`: Propriété. Il doit être égal à `Valve`.  - `valveMechanism[string]`: Propriété. Le mécanisme par lequel la fonction de la vanne est réalisée où : BOULE : Vanne dont la boule est munie d'un orifice qui peut être tourné par rapport aux orifices du siège du corps. BUTTERFLY : Vanne dans laquelle un disque profilé pivote autour d'un axe diamétral. CONFIGUREDGATE : Vanne à vis dans laquelle l'opercule de fermeture est configuré de manière à permettre un contrôle plus précis des variations de pression et de débit à travers la vanne. GLAND : vanne à siège conique, dans laquelle un clapet rotatif est retenu au moyen d'un presse-étoupe et d'une garniture de presse-étoupe. GLOBE : Vanne à vis dont le corps est sphérique. BOUCHON LUBRIFIÉ : Robinet à tournant conique dans lequel un lubrifiant est injecté sous pression entre la face du tournant et le corps. AIGUILLE : Vanne destinée à réguler le débit dans ou à partir d'une conduite, dans laquelle un cône mince se déplace le long de l'axe d'écoulement pour se fermer contre un siège conique fixe. PARALLELSLIDE : Vanne à vis dont la plaque usinée glisse dans des rainures formées pour former un joint. BOUCHON : Vanne dont le bouchon peut être tourné par rapport aux orifices du siège du corps. WEDGEGATE : Vanne à vis dont la plaque en forme de coin s'insère dans des guides coniques pour former un joint d'étanchéité.  - `valveOperation[string]`: Propriété. La méthode de fonctionnement de la vanne où : POIDS LÉGER : soupape fermée par l'action d'un levier lesté qui est relâché, le poids étant normalement empêché de tomber en étant retenu par un fil, la fermeture étant normalement effectuée par l'action de la chaleur sur un lien fusible dans le fil FLOTTANT : soupape ouverte et fermée par l'action d'un flotteur qui monte et descend avec le niveau de l'eau. Le flotteur peut être une boule attachée à un levier ou à un autre mécanisme HYDRAULIQUE : Une vanne qui s'ouvre et se ferme par actionnement hydraulique LEVIER : Une vanne qui s'ouvre et se ferme par l'action d'un levier qui fait tourner l'opercule à l'intérieur de la vanne. VERROUILLAGE : Vanne dont l'ouverture et la fermeture nécessitent l'utilisation d'une clé de verrouillage spéciale, le mécanisme de fonctionnement étant protégé par un capot en fonctionnement normal. MOTORISE : Vanne ouverte et fermée par l'action d'un moteur électrique sur un actionneur PNEUMATIQUE : Vanne ouverte et fermée par actionnement pneumatique SOLENOID : Une vanne qui est normalement maintenue ouverte par un champ magnétique dans une bobine agissant sur l'opercule, mais qui se ferme immédiatement si le courant électrique générant le champ magnétique est supprimé. RESSORT : Une soupape qui est normalement maintenue en position par la pression d'un ressort sur une plaque, mais qui peut être amenée à s'ouvrir si la pression du fluide est suffisante pour surmonter la pression du ressort. THERMOSTATIQUE : Valve dont les orifices sont ouverts ou fermés pour maintenir une température prédéterminée. ROUE : Valve qui s'ouvre et se ferme sous l'action d'une roue qui déplace l'opercule à l'intérieur de la valve.  - `valvePattern[string]`: Propriété. La configuration des orifices d'une vanne en fonction soit de la trajectoire linéaire empruntée par un fluide circulant dans la vanne, soit du nombre d'orifices où : SINGLEPORT : vanne ayant un seul port d'entrée depuis le système qu'elle dessert, le port de sortie étant vers le milieu environnant. ANGLE_2_PORT : vanne dans laquelle le sens de l'écoulement est modifié de 90 degrés. STRAIGHT_2_PORT : vanne dans laquelle le débit est direct. STRAIGHT_3_PORT : Vanne à trois orifices distincts. CROSSOVER_4_PORT : Vanne à 4 orifices séparés.  - `workingPressure[number]`: Propriété. La pression de service maximale normalement attendue de la soupape. Généralement mesurée en Pascals (Pa, N/m2).  <!-- /30-PropertiesList -->  
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
Valve:    
  description: A valve is used in a building services piping distribution system to control or modulate the flow of the fluid.    
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
    closeOffRating:    
      description: 'Property. Close off rating. Usually measured in Pascals (Pa, N/m2).'    
      type: number    
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
    flowCoefficient:    
      description: 'Property. Flow coefficient (the quantity of fluid that passes through a fully open valve at unit pressure drop), typically expressed as the Kv or Cv value for the valve.'    
      type: number    
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
      anyOf: &valve_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      anyOf: *valve_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *valve_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *valve_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
        anyOf: *valve_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    size:    
      description: 'Property. The size of the connection to the valve (or to each connection for faucets, mixing valves, etc.). Usually measured in millimeters (mm).'    
      type: number    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    testPressure:    
      description: 'Property. The maximum pressure to which the valve has been subjected under test. Usually measured in Pascals (Pa, N/m2).'    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: Property. It must be equal to `Valve`.    
      enum:    
        - Valve    
      type: string    
      x-ngsi:    
        type: Property    
    valveMechanism:    
      description: 'Property. The mechanism by which the valve function is achieved where: BALL: Valve that has a ported ball that can be turned relative to the body seat ports. BUTTERFLY: Valve in which a streamlined disc pivots about a diametric axis. CONFIGUREDGATE: Screwdown valve in which the closing gate is shaped in a configured manner to have a more precise control of pressure and flow change across the valve. GLAND: Valve with a tapered seating, in which a rotatable plug is retained by means of a gland and gland packing. GLOBE: Screwdown valve that has a spherical body. LUBRICATEDPLUG: Plug valve in which a lubricant is injected under pressure between the plug face and the body. NEEDLE: Valve for regulating the flow in or from a pipe, in which a slender cone moves along the axis of flow to close against a fixed conical seat. PARALLELSLIDE: Screwdown valve that has a machined plate that slides in formed grooves to form a seal. PLUG: Valve that has a ported plug that can be turned relative to the body seat ports. WEDGEGATE: Screwdown valve that has a wedge shaped plate fitting into tapered guides to form a seal.'    
      type: string    
      x-ngsi:    
        type: Property    
    valveOperation:    
      description: 'Property. The method of valve operation where: DROPWEIGHT: A valve that is closed by the action of a weighted lever being released, the weight normally being prevented from dropping by being held by a wire, the closure normally being made by the action of heat on a fusible link in the wire FLOAT: A valve that is opened and closed by the action of a float that rises and falls with water level. The float may be a ball attached to a lever or other mechanism HYDRAULIC: A valve that is opened and closed by hydraulic actuation LEVER: A valve that is opened and closed by the action of a lever rotating the gate within the valve. LOCKSHIELD: A valve that requires the use of a special lockshield key for opening and closing, the operating mechanism being protected by a shroud during normal operation. MOTORIZED: A valve that is opened and closed by the action of an electric motor on an actuator PNEUMATIC: A valve that is opened and closed by pneumatic actuation SOLENOID: A valve that is normally held open by a magnetic field in a coil acting on the gate but that is closed immediately if the electrical current generating the magnetic field is removed. SPRING: A valve that is normally held in position by the pressure of a spring on a plate but that may be caused to open if the pressure of the fluid is sufficient to overcome the spring pressure. THERMOSTATIC: A valve in which the ports are opened or closed to maintain a required predetermined temperature. WHEEL: A valve that is opened and closed by the action of a wheel moving the gate within the valve.'    
      type: string    
      x-ngsi:    
        type: Property    
    valvePattern:    
      description: 'Property. The configuration of the ports of a valve according to either the linear route taken by a fluid flowing through the valve or by the number of ports where: SINGLEPORT: Valve that has a single entry port from the system that it serves, the exit port being to the surrounding environment. ANGLED_2_PORT: Valve in which the direction of flow is changed through 90 degrees. STRAIGHT_2_PORT: Valve in which the flow is straight through. STRAIGHT_3_PORT: Valve with three separate ports. CROSSOVER_4_PORT: Valve with 4 separate ports.'    
      type: string    
      x-ngsi:    
        type: Property    
    workingPressure:    
      description: 'Property. The normally expected maximum working pressure of the valve. Usually measured in Pascals (Pa, N/m2).'    
      type: number    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Valve"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Valve/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Valve/schema.json    
  x-model-tags: SAREF Valve    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### Valve NGSI-v2 key-values Exemple  
Voici un exemple d'une vanne au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Valve:5606802d-9bfc-41f4-b6cb-7a2dc52214ea",  
    "type": "Valve",  
    "closeOffRating": 0.9792941241344664,  
    "flowCoefficient": 0.825533650257277,  
    "size": 0.7178529493113952,  
    "testPressure": 0.9690729968605641,  
    "valveMechanism": "Greece",  
    "valveOperation": "auxiliary",  
    "valvePattern": "Consultant",  
    "workingPressure": 0.8773888966189294,  
    "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:c2e1097b-602a-49ef-b81e-73687c4868b3",  
    "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:663b3745-acf8-4b86-ab69-693afe57cf2c",  
    "isSubSystemOf": [  
        "urn:ngsi-ld:System:9ec35827-e00f-461e-8f22-5cd758f7f7f6",  
        "urn:ngsi-ld:System:aac7e87c-55fe-4c45-88aa-1cb36e3512f9",  
        "urn:ngsi-ld:System:a4adbc73-68e8-43c6-b366-adc5ffb0e4f8"  
    ],  
    "hasManufacturer": "Valve Company Inc.",  
    "hasModel": "Valve 0.1.2",  
    "dateCreated": "2023-01-25T17:39:28Z",  
    "dateModified": "2023-01-26T11:24:20Z",  
    "source": "Import",  
    "name": "Valve",  
    "alternateName": "Valve type 2",  
    "description": "Valve of limited Valve types",  
    "dataProvider": "IFC file"  
}  
```  
</details>  
#### Valve NGSI-v2 normalisée Exemple  
Voici un exemple d'une vanne au format JSON-LD normalisé. Ce format est compatible avec la norme NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Valve:5384a157-cc2a-4984-b4ed-4273d58990da",  
  "type": "Valve",  
  "closeOffRating": {  
    "type": "Measurement",  
    "value":  0.6442998208642058  
  },  
  "flowCoefficient": {  
    "type": "Measurement",  
    "value": 0.9502368316657622  
  },  
  "size": {  
    "type": "Measurement",  
    "value": 0.1757245625885473  
  },  
  "testPressure": {  
    "type": "Measurement",  
    "value":  0.3547642349477015  
  },  
  "valveMechanism": {  
    "type": "Text",  
    "value": "Comoro Franc"  
  },  
  "valveOperation": {  
    "type": "Text",  
    "value": "capacity"  
  },  
  "valvePattern": {  
    "type": "Text",  
    "value": "Regional"  
  },  
  "workingPressure": {  
    "type": "Measurement",  
    "value":  0.7616536973295315  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:BuildingSpace:4c2121a4-e126-4cee-bd63-517a31e19d0c"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:PhysicalObject:3b7bbebe-aa67-4d67-991d-8360e38cb075"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:a3691c28-c6b1-4dbd-8781-58c369f780f2"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:bd7d12e5-25ef-474b-93af-bba6ebef4782"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:0ee8b6da-5507-42c2-a80d-eaea8b13a894"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Valve Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Valve 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T15:00:30.8255456+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T14:02:17.0152497+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Valve"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Valve type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Valve of limited Valve types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### Valve NGSI-LD key-values Exemple  
Voici un exemple d'une vanne au format JSON-LD en tant que valeurs-clés. Ce format est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Valve:5606802d-9bfc-41f4-b6cb-7a2dc52214ea",  
  "type": "Valve",  
  "closeOffRating": 0.9792941241344664,  
  "flowCoefficient": 0.825533650257277,  
  "size": 0.7178529493113952,  
  "testPressure": 0.9690729968605641,  
  "valveMechanism": "Greece",  
  "valveOperation": "auxiliary",  
  "valvePattern": "Consultant",  
  "workingPressure": 0.8773888966189294,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:c2e1097b-602a-49ef-b81e-73687c4868b3",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:663b3745-acf8-4b86-ab69-693afe57cf2c",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:9ec35827-e00f-461e-8f22-5cd758f7f7f6",  
    "urn:ngsi-ld:System:aac7e87c-55fe-4c45-88aa-1cb36e3512f9",  
    "urn:ngsi-ld:System:a4adbc73-68e8-43c6-b366-adc5ffb0e4f8"  
  ],  
  "hasManufacturer": "Valve Company Inc.",  
  "hasModel": "Valve 0.1.2",  
  "dateCreated": "2023-01-25T17:39:28Z",  
  "dateModified": "2023-01-26T11:24:20Z",  
  "source": "Import",  
  "name": "Valve",  
  "alternateName": "Valve type 2",  
  "description": "Valve of limited Valve types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### Valve NGSI-LD normalisée Exemple  
Voici un exemple d'une vanne au format JSON-LD normalisé. Ce format est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Valve:ca643e8d-ccbe-4bc2-a132-c5a51578501a",  
  "type": "Valve",  
  "closeOffRating": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-25T21:38:33Z",  
    "value": 0.4968075534065832  
  },  
  "flowCoefficient": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T07:44:38Z",  
    "value": 0.3336750880832986  
  },  
  "size": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T10:49:30Z",  
    "value": 0.686759934652535  
  },  
  "testPressure": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-26T10:54:40Z",  
    "value": 0.2729778598678245  
  },  
  "valveMechanism": {  
    "type": "Property",  
    "value": "SSL"  
  },  
  "valveOperation": {  
    "type": "Property",  
    "value": "navigate"  
  },  
  "valvePattern": {  
    "type": "Property",  
    "value": "Central"  
  },  
  "workingPressure": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-26T10:53:59Z",  
    "value": 0.9890036767805558  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:ef5535ea-a226-4e13-ad18-534fe0998b5e"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:269255de-ebf6-4014-b255-7769687247ae"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:3199df5c-0c82-41fa-8c1c-450850408792"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:756104c3-38c5-400b-9598-4a604d9415e1"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:e8b9c356-91e3-4ff9-a98c-5bcae397ed67"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Valve Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Valve 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T16:14:40Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T03:09:51Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Valve"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Valve type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Valve of limited Valve types"  
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
