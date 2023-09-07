<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : Récupération de chaleur AirToAirHeatRecovery  
=====================================================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/AirToAirHeatRecovery/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Un dispositif de récupération de chaleur air-air utilise un échangeur de chaleur à contre-courant entre le flux d'air entrant et le flux d'air sortant. Il est généralement utilisé pour transférer la chaleur de l'air chaud d'une chambre à l'air plus froid de la seconde chambre (c'est-à-dire pour récupérer la chaleur de l'air conditionné évacué et de l'air extérieur fourni à un bâtiment), ce qui permet de réaliser des économies d'énergie en réduisant les besoins de chauffage (ou de refroidissement).  
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
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `hasDefrost[boolean]`: Fonction de dégivrage ou non de l'échangeur de chaleur  - `hasManufacturer[string]`: Relation identifiant le fabricant d'une entité (par exemple, un appareil). La valeur doit être une chaîne de caractères ou une chaîne de caractères avec une balise linguistique  - `hasModel[string]`: Une relation identifiant le modèle d'une entité (par exemple, un appareil). La valeur doit être une chaîne de caractères ou une chaîne de caractères avec une balise de langue  - `heatTransferTypeEnum[string]`: Type de transfert de chaleur entre les deux flux d'air  - `id[*]`: Identifiant unique de l'entité  - `isContainedInBuildingSpace[*]`: Entité utilisée pour définir les espaces physiques du bâtiment. Un espace de bâtiment contient des dispositifs ou des objets de bâtiment. (Espace Bâtiment)  - `isContainedInPhysicalObject[*]`: Tout objet qui possède une région spatiale propre.  (Définition extraite de l'ontologie DUL) (PhysicalObject)  - `isSubSystemOf[array]`: Référence au(x) système(s) dont cet objet physique fait partie  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément  - `operationTemperatureMax[number]`: Plage de température ambiante (air, fluide) autorisée pour le fonctionnement. Généralement mesurée en degrés Kelvin (K)  - `operationTemperatureMin[number]`: Plage de température ambiante (air, fluide) autorisée pour le fonctionnement. Généralement mesurée en degrés Kelvin (K)  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `primaryAirFlowRateMax[number]`: Débit d'air primaire maximal pouvant être fourni. Généralement mesuré en m3/s  - `primaryAirFlowRateMin[number]`: Débit d'air primaire minimum pouvant être fourni. Généralement mesuré en m3/s  - `secondaryAirFlowRateMax[number]`: Débit d'air secondaire maximal pouvant être fourni. Généralement mesuré en Pascals (Pa, N/m2)  - `secondaryAirFlowRateMin[number]`: Débit d'air secondaire maximal pouvant être fourni. Généralement mesuré en Pascals (Pa, N/m2)  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `type[string]`: Il doit être égal à `AirToAirHeatRecovery`.  <!-- /30-PropertiesList -->  
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
AirToAirHeatRecovery:    
  description: 'An air-to-air heat recovery device employs a counter-flow heat exchanger between inbound and outbound air flow. It is typically used to transfer heat from warmer air in one chamber to cooler air in the second chamber (i.e., typically used to recover heat from the conditioned air being exhausted and the outside air being supplied to a building), resulting in energy savings from reduced heating (or cooling) requirements.'    
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
    hasDefrost:    
      description: Whether the heat exchanger has defrost function or not    
      type: boolean    
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
    heatTransferTypeEnum:    
      description: Type of heat transfer between the two air streams    
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
        type: Relationship    
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
        type: Relationship    
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
        description: 'The class of systems, i.e., systems virtually isolated from the environment, whose behaviour and interactions with the environment are modeled. Systems can be connected to other systems. Connected systems interact in some ways. Systems can also have subsystems. Properties of subsystems somehow contribute to the properties of the supersystem. (System)'    
        x-ngsi:    
          type: Relationship    
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
    primaryAirFlowRateMax:    
      description: Maximum primary airflow that can be delivered. Usually measured in m3/s    
      type: number    
      x-ngsi:    
        type: Property    
    primaryAirFlowRateMin:    
      description: Minimum primary airflow that can be delivered. Usually measured in m3/s    
      type: number    
      x-ngsi:    
        type: Property    
    secondaryAirFlowRateMax:    
      description: 'Maximum secondary airflow that can be delivered. Usually measured in Pascals (Pa, N/m2)'    
      type: number    
      x-ngsi:    
        type: Property    
    secondaryAirFlowRateMin:    
      description: 'Maximum secondary airflow that can be delivered. Usually measured in Pascals (Pa, N/m2)'    
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
      description: It must be equal to `AirToAirHeatRecovery`    
      enum:    
        - AirToAirHeatRecovery    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:AirToAirHeatRecovery"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/AirToAirHeatRecovery/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/AirToAirHeatRecovery/schema.json    
  x-model-tags: SAREF AirToAirHeatRecovery    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### AirToAirHeatRecovery Valeurs clés de l'INS-V2 Exemple  
Voici un exemple de récupération de chaleur AirToAirHeatRecovery au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:AirToAirHeatRecovery:8c59d316-ed05-4b56-bec3-886379421239",  
  "type": "AirToAirHeatRecovery",  
  "hasDefrost": false,  
  "heatTransferTypeEnum": "24/7",  
  "operationTemperatureMax": {  
    "unitCode": "K",  
    "observedAt": "2023-01-26T04:36:47Z",  
    "value": 0.8198825347384565  
  },  
  "operationTemperatureMin": {  
    "unitCode": "K",  
    "observedAt": "2023-01-25T14:46:06Z",  
    "value": 0.505815040579818  
  },  
  "primaryAirFlowRateMax": {  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-25T20:09:42Z",  
    "value": 0.2511282384018223  
  },  
  "primaryAirFlowRateMin": {  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-25T23:44:23Z",  
    "value": 0.8540184208518826  
  },  
  "secondaryAirFlowRateMax": {  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-26T11:38:58Z",  
    "value": 0.913617698002923  
  },  
  "secondaryAirFlowRateMin": {  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-25T17:25:01Z",  
    "value": 0.17456040773539583  
  },  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:018e6821-b097-4029-9cbb-207ae7e5ddca",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:ad795f1c-0754-4877-acc2-2dcc3b337edd",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:c92bd8da-e37f-4f64-989b-6007925a053b",  
    "urn:ngsi-ld:System:5642f604-3a36-49c3-b178-3e7b99eca071",  
    "urn:ngsi-ld:System:2f04039b-ef4e-4d61-8232-e786a220b927"  
  ],  
  "hasManufacturer": "AirToAirHeatRecovery Company Inc.",  
  "hasModel": "AirToAirHeatRecovery 0.1.2",  
  "dateCreated": "2023-01-25T18:33:19Z",  
  "dateModified": "2023-01-25T17:11:08Z",  
  "source": "Import",  
  "name": "AirToAirHeatRecovery",  
  "alternateName": "AirToAirHeatRecovery type 2",  
  "description": "AirToAirHeatRecovery of limited AirToAirHeatRecovery types",  
  "dataProvider": "IFC file"  
}  
```  
</details>  
#### AirToAirHeatRecovery NGSI-v2 normalisé Exemple  
Voici un exemple de récupération de chaleur AirToAirHeatRecovery au format JSON-LD tel que normalisé. Ce format est compatible avec la norme NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:AirToAirHeatRecovery:a732b90e-0296-47c9-ab0f-34f6de5edfb4",  
  "type": "AirToAirHeatRecovery",  
  "hasDefrost": {  
    "type": "Boolean",  
    "value": true  
  },  
  "heatTransferTypeEnum": {  
    "type": "Text",  
    "value": "Future"  
  },  
  "operationTemperatureMax": {  
    "type": "Measurement",  
    "value": {  
      "unitCode": "K",  
      "observedAt": "2023-01-26T07:59:34Z",  
      "value": 0.9053685058368695  
    }  
  },  
  "operationTemperatureMin": {  
    "type": "Measurement",  
    "value": {  
      "unitCode": "K",  
      "observedAt": "2023-01-26T08:16:23Z",  
      "value": 0.0225751895192714  
    }  
  },  
  "primaryAirFlowRateMax": {  
    "type": "Measurement",  
    "value": {  
      "unitCode": "m3/s",  
      "observedAt": "2023-01-25T19:33:24Z",  
      "value": 0.6828734611896666  
    }  
  },  
  "primaryAirFlowRateMin": {  
    "type": "Measurement",  
    "value": {  
      "unitCode": "m3/s",  
      "observedAt": "2023-01-25T22:42:55Z",  
      "value": 0.48874342661652126  
    }  
  },  
  "secondaryAirFlowRateMax": {  
    "type": "Measurement",  
    "value": {  
      "unitCode": "N/m2",  
      "observedAt": "2023-01-26T11:44:17Z",  
      "value": 0.36804021603434756  
    }  
  },  
  "secondaryAirFlowRateMin": {  
    "type": "Measurement",  
    "value": {  
      "unitCode": "N/m2",  
      "observedAt": "2023-01-26T01:16:14Z",  
      "value": 0.28401066550404996  
    }  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:BuildingSpace:2058c38a-eb2e-4001-af3f-9a93effd41ac"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:PhysicalObject:ea1b1b2c-cb04-429d-bf2c-ca99e7f3f005"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:123d10ff-2c3a-40f4-9fd0-07851a7d7a3c"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:90a762d4-7eed-4d5a-8a0d-a4676773917f"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:b9899a7a-dc77-43a1-a0df-5a4134af3004"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "AirToAirHeatRecovery Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "AirToAirHeatRecovery 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T00:34:42.9211606+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T13:58:25.8715515+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "AirToAirHeatRecovery"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "AirToAirHeatRecovery type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "AirToAirHeatRecovery of limited AirToAirHeatRecovery types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### AirToAirHeatRecovery Valeurs clés NGSI-LD Exemple  
Voici un exemple de récupération de chaleur AirToAirHeatRecovery au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:AirToAirHeatRecovery:8c59d316-ed05-4b56-bec3-886379421239",  
  "type": "AirToAirHeatRecovery",  
  "hasDefrost": false,  
  "heatTransferTypeEnum": "24/7",  
  "operationTemperatureMax": {  
    "unitCode": "K",  
    "observedAt": "2023-01-26T04:36:47Z",  
    "value": 0.8198825347384565  
  },  
  "operationTemperatureMin": {  
    "unitCode": "K",  
    "observedAt": "2023-01-25T14:46:06Z",  
    "value": 0.505815040579818  
  },  
  "primaryAirFlowRateMax": {  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-25T20:09:42Z",  
    "value": 0.2511282384018223  
  },  
  "primaryAirFlowRateMin": {  
    "unitCode": "m3/s",  
    "observedAt": "2023-01-25T23:44:23Z",  
    "value": 0.8540184208518826  
  },  
  "secondaryAirFlowRateMax": {  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-26T11:38:58Z",  
    "value": 0.913617698002923  
  },  
  "secondaryAirFlowRateMin": {  
    "unitCode": "N/m2",  
    "observedAt": "2023-01-25T17:25:01Z",  
    "value": 0.17456040773539583  
  },  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:018e6821-b097-4029-9cbb-207ae7e5ddca",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:ad795f1c-0754-4877-acc2-2dcc3b337edd",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:c92bd8da-e37f-4f64-989b-6007925a053b",  
    "urn:ngsi-ld:System:5642f604-3a36-49c3-b178-3e7b99eca071",  
    "urn:ngsi-ld:System:2f04039b-ef4e-4d61-8232-e786a220b927"  
  ],  
  "hasManufacturer": "AirToAirHeatRecovery Company Inc.",  
  "hasModel": "AirToAirHeatRecovery 0.1.2",  
  "dateCreated": "2023-01-25T18:33:19Z",  
  "dateModified": "2023-01-25T17:11:08Z",  
  "source": "Import",  
  "name": "AirToAirHeatRecovery",  
  "alternateName": "AirToAirHeatRecovery type 2",  
  "description": "AirToAirHeatRecovery of limited AirToAirHeatRecovery types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### AirToAirHeatRecovery NGSI-LD normalisé Exemple  
Voici un exemple de récupération de chaleur AirToAirHeatRecovery au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:AirToAirHeatRecovery:a8cd6aa9-dd5f-48bf-ba9f-3db11843b050",  
  "type": "AirToAirHeatRecovery",  
  "hasDefrost": {  
    "type": "Property",  
    "value": false  
  },  
  "heatTransferTypeEnum": {  
    "type": "Property",  
    "value": "Street"  
  },  
  "operationTemperatureMax": {  
    "type": "Property",  
    "value": {  
      "unitCode": "K",  
      "observedAt": "2023-01-26T02:03:09Z",  
      "value": 0.09206773488147657  
    }  
  },  
  "operationTemperatureMin": {  
    "type": "Property",  
    "value": {  
      "unitCode": "K",  
      "observedAt": "2023-01-26T09:23:23Z",  
      "value": 0.04773015112848933  
    }  
  },  
  "primaryAirFlowRateMax": {  
    "type": "Property",  
    "value": {  
      "unitCode": "m3/s",  
      "observedAt": "2023-01-25T15:19:05Z",  
      "value": 0.04143347387591234  
    }  
  },  
  "primaryAirFlowRateMin": {  
    "type": "Property",  
    "value": {  
      "unitCode": "m3/s",  
      "observedAt": "2023-01-26T00:05:48Z",  
      "value": 0.9113949488212527  
    }  
  },  
  "secondaryAirFlowRateMax": {  
    "type": "Property",  
    "value": {  
      "unitCode": "N/m2",  
      "observedAt": "2023-01-26T02:57:23Z",  
      "value": 0.391335331160202  
    }  
  },  
  "secondaryAirFlowRateMin": {  
    "type": "Property",  
    "value": {  
      "unitCode": "N/m2",  
      "observedAt": "2023-01-26T08:54:29Z",  
      "value": 0.9115616360325159  
    }  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:f9f09bbc-27ef-4bd0-991f-6dd8720f5e7b"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:79a8986d-8526-4608-b216-ea4eb2d147ac"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:fae709e8-6311-4179-acfd-7b79e92d095c"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:4c06efa1-0d47-4a8a-a38c-d0783a106972"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:a3120479-fd3a-4a34-915c-418000e05d2b"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "AirToAirHeatRecovery Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "AirToAirHeatRecovery 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-25T23:15:35Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-01-26T07:30:02Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "AirToAirHeatRecovery"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "AirToAirHeatRecovery type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "AirToAirHeatRecovery of limited AirToAirHeatRecovery types"  
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
