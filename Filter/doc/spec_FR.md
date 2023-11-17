<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entité : Filtre    
===============<!-- /10-Header -->    
<!-- 15-License -->    
[Licence ouverte] (https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Filter/LICENSE.md)    
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Description globale : **Un filtre est un appareil utilisé pour éliminer les particules ou les gaz des fluides et des gaz.    
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
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `finalResistance[number]`: Résistance du fluide du filtre lorsqu'il doit être remplacé (c'est-à-dire chute de pression au débit d'air maximal à travers le filtre lorsque le filtre doit être remplacé conformément à la norme ASHRAE 52.1). Généralement mesurée en Pascals (Pa, N/m2).  - `fluidFlowRateMax[number]`: Plage possible de débit de fluide pouvant être délivré. Généralement mesuré en m3/s  - `fluidFlowRateMin[number]`: Plage possible de débit de fluide pouvant être délivré. Généralement mesuré en m3/s  - `hasManufacturer[string]`: Relation identifiant le fabricant d'une entité (par exemple, un appareil). La valeur doit être une chaîne de caractères ou une chaîne de caractères avec une balise linguistique  - `hasModel[string]`: Une relation identifiant le modèle d'une entité (par exemple, un appareil). La valeur doit être une chaîne de caractères ou une chaîne de caractères avec une balise de langue  - `id[*]`: Identifiant unique de l'entité  - `initialResistance[number]`: Résistance initiale du fluide du filtre neuf (c'est-à-dire la chute de pression au débit d'air maximal à travers le filtre lorsque celui-ci est neuf, conformément à la norme ASHRAE 52.1). Habituellement mesurée en Pascals (Pa, N/m2).  - `isContainedInBuildingSpace[*]`: Entité utilisée pour définir les espaces physiques du bâtiment. Un espace de bâtiment contient des dispositifs ou des objets de bâtiment. (Espace Bâtiment)  - `isContainedInPhysicalObject[*]`: Tout objet qui possède une région spatiale propre.  (Définition extraite de l'ontologie DUL) (PhysicalObject)  - `isSubSystemOf[array]`: Référence au(x) système(s) dont cet objet physique fait partie  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément  - `nominalFilterFaceVelocity[number]`: Vitesse de la face du filtre. Généralement mesurée en m/s  - `nominalFlowRate[number]`: Débit nominal du fluide à travers le filtre. Généralement mesuré en m3/s  - `nominalMediaSurfaceVelocity[number]`: Vitesse moyenne du fluide à la surface du support. Généralement mesurée en m/s  - `nominalParticleGeometricMeanDiameter[number]`: Diamètre moyen géométrique des particules associé à l'efficacité nominale. Généralement mesuré en millimètres (mm)  - `nominalParticleGeometricStandardDeviation[number]`: Écart-type géométrique des particules associé à l'efficacité nominale.  - `nominalPressureDrop[number]`: Perte de charge totale à travers le filtre. Généralement mesurée en Pascals (Pa, N/m2)  - `operationTemperatureMax[number]`: Plage de température ambiante (air, fluide) autorisée pour le fonctionnement. Généralement mesurée en degrés Kelvin (K)  - `operationTemperatureMin[number]`: Plage de température ambiante (air, fluide) autorisée pour le fonctionnement. Généralement mesurée en degrés Kelvin (K)  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `type[string]`: Il doit être égal à `Filter`  - `weight[number]`: Le poids de l'appareil. Généralement mesuré en kilogrammes (kg) ou en grammes (g).  <!-- /30-PropertiesList -->    
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
Filter:      
  description: A filter is an apparatus used to remove particulate or gaseous matter from fluids and gases.      
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
    finalResistance:      
      description: 'Filter fluid resistance when replacement is required (i.e., Pressure drop at the maximum air flowrate across the filter when the filter needs replacement per ASHRAE Standard 52.1). Usually measured in Pascals (Pa, N/m2)'      
      type: number      
      x-ngsi:      
        type: Property      
    fluidFlowRateMax:      
      description: Possible range of fluid flowrate that can be delivered. Usually measured in m3/s      
      type: number      
      x-ngsi:      
        type: Property      
    fluidFlowRateMin:      
      description: Possible range of fluid flowrate that can be delivered. Usually measured in m3/s      
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
    initialResistance:      
      description: 'Initial new filter fluid resistance (i.e., pressure drop at the maximum air flowrate across the filter when the filter is new per ASHRAE Standard 52.1). Usually measured in Pascals (Pa, N/m2)'      
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
    nominalFilterFaceVelocity:      
      description: Filter face velocity. Usually measured in m/s      
      type: number      
      x-ngsi:      
        type: Property      
    nominalFlowRate:      
      description: Nominal fluid flow rate through the filter. Usually measured in m3/s      
      type: number      
      x-ngsi:      
        type: Property      
    nominalMediaSurfaceVelocity:      
      description: Average fluid velocity at the media surface. Usually measured in m/s      
      type: number      
      x-ngsi:      
        type: Property      
    nominalParticleGeometricMeanDiameter:      
      description: Particle geometric mean diameter associated with nominal efficiency. Usually measured in millimeters (mm)      
      type: number      
      x-ngsi:      
        type: Property      
    nominalParticleGeometricStandardDeviation:      
      description: 'Particle geometric standard deviation associated with nominal efficiency. '      
      type: number      
      x-ngsi:      
        type: Property      
    nominalPressureDrop:      
      description: 'Total pressure drop across the filter. Usually measured in Pascals (Pa, N/m2)'      
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
      description: It must be equal to `Filter`      
      enum:      
        - Filter      
      type: string      
      x-ngsi:      
        type: Property      
    weight:      
      description: The weight of the device. Usually measured in kilograms (kg) or grams (g)      
      type: number      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Filter"      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Filter/LICENSE.md      
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Filter/schema.json      
  x-model-tags: SAREF Filter      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Exemples de charges utiles    
#### Filtrer les valeurs-clés NGSI-v2 Exemple    
Voici un exemple de filtre au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Filter:cab351de-0353-4d67-ba3e-f8e496fff6ee",  
  "type": "Filter",  
  "finalResistance": 0.046716566596463616,  
  "fluidFlowRateMax": 0.5234640867427633,  
  "fluidFlowRateMin": 0.88979941896976,  
  "initialResistance": 0.9155546427779283,  
  "nominalFilterFaceVelocity": 0.6586465369680704,  
  "nominalFlowRate": 0.08419722940470808,  
  "nominalMediaSurfaceVelocity": 0.2909288017995001,  
  "nominalParticleGeometricMeanDiameter": 0.25048971083477223,  
  "nominalParticleGeometricStandardDeviation": 0.6860967233212114,  
  "nominalPressureDrop": 0.4382746309750293,  
  "operationTemperatureMax": 0.41660145070952037,  
  "operationTemperatureMin": 0.7951736951400654,  
  "weight": 0.9846229044529057,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:0f3368a3-5989-4693-b29e-37aaa17be464",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:78c5cc6c-d740-45dd-968c-43361a780e2c",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:c57a69ec-9b26-4933-b4ce-580e5edb9b72",  
    "urn:ngsi-ld:System:0132ad74-ea74-4d20-b0d0-bb4fa1a19af9",  
    "urn:ngsi-ld:System:be24c623-c5c4-4da0-b4ea-552cb1d31a71"  
  ],  
  "hasManufacturer": "Filter Company Inc.",  
  "hasModel": "Filter 0.1.2",  
  "dateCreated": "2023-01-26T06:33:09Z",  
  "dateModified": "2023-01-26T13:51:08Z",  
  "source": "Import",  
  "name": "Filter",  
  "alternateName": "Filter type 2",  
  "description": "Filter of limited Filter types",  
  "dataProvider": "IFC file"  
}  
```  
</details>    
#### Filtre NGSI-v2 normalisé Exemple    
Voici un exemple de filtre au format JSON-LD normalisé. Il est compatible avec les NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Filter:8e80455c-7f89-462c-b1f0-b84c6ac5e5cb",  
  "type": "Filter",  
  "finalResistance": {  
    "type": "Number",  
    "value": 0.25563353322549653  
  },  
  "fluidFlowRateMax": {  
    "type": "Number",  
    "value": 0.7441450852967011  
  },  
  "fluidFlowRateMin": {  
    "type": "Number",  
    "value": 0.32563792639259326  
  },  
  "initialResistance": {  
    "type": "Number",  
    "value": 0.41032135281652493  
  },  
  "nominalFilterFaceVelocity": {  
    "type": "Number",  
    "value": 0.829815297358211  
  },  
  "nominalFlowRate": {  
    "type": "Number",  
    "value": 0.569423507213339  
  },  
  "nominalMediaSurfaceVelocity": {  
    "type": "Number",  
    "value": 0.6085640129416107  
  },  
  "nominalParticleGeometricMeanDiameter": {  
    "type": "Number",  
    "value": 0.9736709365602062  
  },  
  "nominalParticleGeometricStandardDeviation": {  
    "type": "Number",  
    "value": 0.5284993250186989  
  },  
  "nominalPressureDrop": {  
    "type": "Number",  
    "value": 0.4856470985811685  
  },  
  "operationTemperatureMax": {  
    "type": "Number",  
    "value": 0.04450158146401939  
  },  
  "operationTemperatureMin": {  
    "type": "Number",  
    "value": 0.28211808830531604  
  },  
  "weight": {  
    "type": "Number",  
    "value": 0.5157014658259989  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:BuildingSpace:4468726f-7faa-4e8e-802e-337b7d4e2c38"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:PhysicalObject:a263b3b0-a5d7-4e38-a95f-75dd868ea6aa"  
  },  
  "isSubSystemOf": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:System:118a0d61-bba3-416e-a770-5ac45dfb66e7",  
      "urn:ngsi-ld:System:a7ba30cc-d8f3-423d-a1d6-284c130befee",  
      "urn:ngsi-ld:System:38485bc5-5ff4-49f1-b6fb-65b815b05795"  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Filter Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Filter 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T04:44:52.9377605+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T18:30:35.796352+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Filter"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Filter type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Filter of limited Filter types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>    
#### Filtrer les valeurs clés NGSI-LD Exemple    
Voici un exemple de filtre au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Filter:cab351de-0353-4d67-ba3e-f8e496fff6ee",  
  "type": "Filter",  
  "finalResistance": 0.046716566596463616,  
  "fluidFlowRateMax": 0.5234640867427633,  
  "fluidFlowRateMin": 0.88979941896976,  
  "initialResistance": 0.9155546427779283,  
  "nominalFilterFaceVelocity": 0.6586465369680704,  
  "nominalFlowRate": 0.08419722940470808,  
  "nominalMediaSurfaceVelocity": 0.2909288017995001,  
  "nominalParticleGeometricMeanDiameter": 0.25048971083477223,  
  "nominalParticleGeometricStandardDeviation": 0.6860967233212114,  
  "nominalPressureDrop": 0.4382746309750293,  
  "operationTemperatureMax": 0.41660145070952037,  
  "operationTemperatureMin": 0.7951736951400654,  
  "weight": 0.9846229044529057,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:0f3368a3-5989-4693-b29e-37aaa17be464",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:78c5cc6c-d740-45dd-968c-43361a780e2c",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:c57a69ec-9b26-4933-b4ce-580e5edb9b72",  
    "urn:ngsi-ld:System:0132ad74-ea74-4d20-b0d0-bb4fa1a19af9",  
    "urn:ngsi-ld:System:be24c623-c5c4-4da0-b4ea-552cb1d31a71"  
  ],  
  "hasManufacturer": "Filter Company Inc.",  
  "hasModel": "Filter 0.1.2",  
  "dateCreated": "2023-01-26T06:33:09Z",  
  "dateModified": "2023-01-26T13:51:08Z",  
  "source": "Import",  
  "name": "Filter",  
  "alternateName": "Filter type 2",  
  "description": "Filter of limited Filter types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>    
#### Filtre NGSI-LD normalisé Exemple    
Voici un exemple de filtre au format JSON-LD normalisé. Il est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Filter:fbeb6c10-5a65-4f37-b472-05630b596d96",  
  "type": "Filter",  
  "finalResistance": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-26T01:00:57Z",  
    "value": 0.5605621121413891  
  },  
  "fluidFlowRateMax": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-26T09:29:26Z",  
    "value": 0.8457030696896928  
  },  
  "fluidFlowRateMin": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-26T01:24:07Z",  
    "value": 0.4281237576056126  
  },  
  "initialResistance": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-26T13:16:00Z",  
    "value": 0.9855925634968424  
  },  
  "nominalFilterFaceVelocity": {  
    "type": "Property",  
    "unitCode": "m/s",  
    "observedAt": "2023-01-26T03:08:23Z",  
    "value": 0.6912281080254741  
  },  
  "nominalFlowRate": {  
    "type": "Property",  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-25T15:48:08Z",  
    "value": 0.022821238860702198  
  },  
  "nominalMediaSurfaceVelocity": {  
    "type": "Property",  
    "unitCode": "m/s",  
    "observedAt": "2023-01-25T22:13:37Z",  
    "value": 0.5684154129668265  
  },  
  "nominalParticleGeometricMeanDiameter": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T07:32:19Z",  
    "value": 0.229698552370729  
  },  
  "nominalParticleGeometricStandardDeviation": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T02:48:53Z",  
    "value": 0.8264025547190669  
  },  
  "nominalPressureDrop": {  
    "type": "Property",  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-25T19:24:30Z",  
    "value": 0.6662603303962529  
  },  
  "operationTemperatureMax": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-26T00:52:23Z",  
    "value": 0.8600599815414807  
  },  
  "operationTemperatureMin": {  
    "type": "Property",  
    "unitCode": "K",  
    "observedAt": "2023-01-25T18:39:35Z",  
    "value": 0.11197463391152895  
  },  
  "weight": {  
    "type": "Property",  
    "unitCode": "g",  
    "observedAt": "2023-01-26T06:38:32Z",  
    "value": 0.39067890635291025  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:3ad9289e-2153-42f6-821a-e050b0cece56"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:14828a20-966b-491d-8c5d-06e0e9323fe3"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:4f4ca1e9-532c-4518-b84b-92e00d43255a"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:4be15aec-065d-404f-aedd-e477a5a61f23"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:7e718726-9abe-49e6-ae69-96d1277a5af0"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Filter Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Filter 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T21:32:07Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-25T21:47:48Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Filter"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Filter type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Filter of limited Filter types"  
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
