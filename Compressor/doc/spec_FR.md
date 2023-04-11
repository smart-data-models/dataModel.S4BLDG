<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : Compresseur  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Compressor/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Un compresseur est un dispositif qui comprime un fluide généralement utilisé dans un circuit de réfrigération**.  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `compressorSpeed[number]`: Propriété. Vitesse du compresseur. Généralement mesurée en cycles/s.  - `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Date de création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage.  - `dateModified[string]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage.  - `description[string]`: Une description de l'article  - `hasHotGasBypass[boolean]`: Propriété. Indique si le compresseur dispose ou non d'une dérivation des gaz chauds. TRUE = Oui, FALSE = Non.  - `hasManufacturer[string]`: Propriété. Une relation identifiant le fabricant d'une entité (par exemple, un appareil). La valeur doit être une chaîne de caractères ou une chaîne de caractères avec une étiquette de langue.  - `hasModel[string]`: Propriété. Une relation identifiant le modèle d'une entité (par exemple, un appareil). La valeur doit être une chaîne de caractères ou une chaîne de caractères avec une balise de langue.  - `id[*]`: Identifiant unique de l'entité  - `idealCapacity[number]`: Propriété. Capacité du compresseur dans des conditions idéales. Généralement mesurée en watts (W, J/s).  - `idealShaftPower[number]`: Propriété. Puissance de l'arbre du compresseur dans des conditions idéales. Généralement mesurée en watts (W, J/s).  - `impellerDiameter[number]`: Propriété. Diamètre de la roue du compresseur - utilisé pour mettre à l'échelle les performances de compresseurs géométriquement similaires. Généralement mesuré en millimètres (mm).  - `isContainedInBuildingSpace[*]`: Relations. Entité utilisée pour définir les espaces physiques du bâtiment. Un espace de bâtiment contient des appareils ou des objets de bâtiment. (Espace Bâtiment)  - `isContainedInPhysicalObject[*]`: Relation. Tout objet qui possède une région spatiale propre.  (Définition extraite de l'ontologie DUL) (PhysicalObject)  - `isSubSystemOf[array]`: Relation. Référence à un ou plusieurs systèmes dont cet objet physique fait partie.  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément.  - `nominalCapacity[number]`: Propriété. Capacité nominale. Généralement mesurée en watts (W, J/s).  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `partLoadRatioMax[number]`: Propriété. Rapport entre la charge partielle maximale et la capacité nominale.  - `partLoadRatioMin[number]`: Propriété. Rapport minimum de charge partielle en tant que fraction de la capacité nominale.  - `powerSource[string]`: Propriété. Type d'énergie qui alimente le compresseur.  - `refrigerantClass[string]`: Propriété. Classe de réfrigérant utilisée par le compresseur. CFC : Chlorofluorocarbures. HCFC : Hydrochlorofluorocarbures. HFC : Hydrofluorocarbures.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `type[string]`: Propriété. Elle doit être égale à `Compressor`.  <!-- /30-PropertiesList -->  
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
Compressor:    
  description: A compressor is a device that compresses a fluid typically used in a refrigeration circuit.    
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
    compressorSpeed:    
      description: Property. Compressor speed. Usually measured in cycles/s.    
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
    hasHotGasBypass:    
      description: 'Property. Whether or not hot gas bypass is provided for the compressor. TRUE = Yes, FALSE = No.'    
      type: boolean    
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
      anyOf: &compressor_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    idealCapacity:    
      description: 'Property. Compressor capacity under ideal conditions. Usually measured in Watts (W, J/s).'    
      type: number    
      x-ngsi:    
        type: Property    
    idealShaftPower:    
      description: 'Property. Compressor shaft power under ideal conditions. Usually measured in Watts (W, J/s).'    
      type: number    
      x-ngsi:    
        type: Property    
    impellerDiameter:    
      description: Property. Diameter of compressor impeller - used to scale performance of geometrically similar compressors. Usually measured in millimeters (mm).    
      type: number    
      x-ngsi:    
        type: Property    
    isContainedInBuildingSpace:    
      anyOf: *compressor_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *compressor_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *compressor_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    nominalCapacity:    
      description: 'Property. Nominal capacity. Usually measured in Watts (W, J/s).'    
      type: number    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *compressor_-_properties_-_iscontainedinbuildingspace_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    partLoadRatioMax:    
      description: Property. Maximum part load ratio as a fraction of nominal capacity.    
      type: number    
      x-ngsi:    
        type: Property    
    partLoadRatioMin:    
      description: Property. Minimum part load ratio as a fraction of nominal capacity.    
      type: number    
      x-ngsi:    
        type: Property    
    powerSource:    
      description: Property. Type of power driving the compressor.    
      type: string    
      x-ngsi:    
        type: Property    
    refrigerantClass:    
      description: 'Property. Refrigerant class used by the compressor. CFC: Chlorofluorocarbons. HCFC: Hydrochlorofluorocarbons. HFC: Hydrofluorocarbons.'    
      type: string    
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
    type:    
      description: Property. It must be equal to `Compressor`.    
      enum:    
        - Compressor    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Compressor"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Compressor/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Compressor/schema.json    
  x-model-tags: SAREF Compressor    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### Compressor NGSI-v2 key-values Exemple  
Voici un exemple de compresseur au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Compressor:99624683-cbb4-4bac-a458-e5bde1df9ff6",  
  "type": "Compressor",  
  "compressorSpeed": 0.679723675842234,  
  "hasHotGasBypass": true,  
  "idealCapacity": 0.7248048000316983,  
  "idealShaftPower": 0.47111429367476765,  
  "impellerDiameter": 0.8496808897888555,  
  "nominalCapacity": 0.8766392143544064,  
  "partLoadRatioMax": 0.5560596438051391,  
  "partLoadRatioMin": 0.22917332777815946,  
  "powerSource": "Practical Steel Chair",  
  "refrigerantClass": "protocol",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:9c3fb868-0647-4480-b105-2221a6cd3354",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:868ed081-1e1b-497f-a18f-11c416e2a90e",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:157c6a62-21ad-4aa4-b3d2-5a0ec1f2c667",  
    "urn:ngsi-ld:System:6fd790f8-68de-4047-a771-4b245c4aff90",  
    "urn:ngsi-ld:System:18a2426a-2c96-4064-959d-98e7aba7904d"  
  ],  
  "hasManufacturer": "Compressor Company Inc.",  
  "hasModel": "Compressor 0.1.2",  
  "dateCreated": "2023-01-26T10:11:46Z",  
  "dateModified": "2023-01-26T05:03:38Z",  
  "source": "Import",  
  "name": "Compressor",  
  "alternateName": "Compressor type 2",  
  "description": "Compressor of limited Compressor types",  
  "dataProvider": "IFC file"  
}  
```  
</details>  
#### Compresseur NGSI-v2 normalisé Exemple  
Voici un exemple de compresseur au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Compressor:5286e31e-5c79-4133-93c4-07c1f3574128",  
  "type": "Compressor",  
  "compressorSpeed": {  
    "type": "Measurement",  
    "value": 0.6951462722377054  
  },  
  "hasHotGasBypass": {  
    "type": "Boolean",  
    "value": true  
  },  
  "idealCapacity": {  
    "type": "Measurement",  
    "value": 0.3445800754974827  
  },  
  "idealShaftPower": {  
    "type": "Measurement",  
    "value": 0.8311250404203112  
  },  
  "impellerDiameter": {  
    "type": "Measurement",  
    "value": 0.868808285450986  
  },  
  "nominalCapacity": {  
    "type": "Measurement",  
    "value": 0.9287385861700207  
  },  
  "partLoadRatioMax": {  
    "type": "Measurement",  
    "value": 0.38901369640969274  
  },  
  "partLoadRatioMin": {  
    "type": "Measurement",  
    "value": 0.9657934764992187  
  },  
  "powerSource": {  
    "type": "Text",  
    "value": "bluetooth"  
  },  
  "refrigerantClass": {  
    "type": "Text",  
    "value": "Fresh"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:BuildingSpace:91df3ba9-787a-4ebb-9be6-ae4c05263de1"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:PhysicalObject:e9909895-084e-4023-9a5a-001322f825f9"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:7ebaae6c-b549-4610-8df4-9c28cebe42a9"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:cedc316a-3057-4f0b-9800-db9757c47286"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:b64d7a83-9d09-405a-82dc-e2dc92ba7ae5"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Compressor Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Compressor 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T08:32:27.8745501+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T12:23:46.0320445+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Compressor"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Compressor type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Compressor of limited Compressor types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### Compresseur Valeurs clés NGSI-LD Exemple  
Voici un exemple de compresseur au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Compressor:99624683-cbb4-4bac-a458-e5bde1df9ff6",  
  "type": "Compressor",  
  "compressorSpeed": 0.679723675842234,  
  "hasHotGasBypass": true,  
  "idealCapacity": 0.7248048000316983,  
  "idealShaftPower": 0.47111429367476765,  
  "impellerDiameter": 0.8496808897888555,  
  "nominalCapacity": 0.8766392143544064,  
  "partLoadRatioMax": 0.5560596438051391,  
  "partLoadRatioMin": 0.22917332777815946,  
  "powerSource": "Practical Steel Chair",  
  "refrigerantClass": "protocol",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:9c3fb868-0647-4480-b105-2221a6cd3354",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:868ed081-1e1b-497f-a18f-11c416e2a90e",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:157c6a62-21ad-4aa4-b3d2-5a0ec1f2c667",  
    "urn:ngsi-ld:System:6fd790f8-68de-4047-a771-4b245c4aff90",  
    "urn:ngsi-ld:System:18a2426a-2c96-4064-959d-98e7aba7904d"  
  ],  
  "hasManufacturer": "Compressor Company Inc.",  
  "hasModel": "Compressor 0.1.2",  
  "dateCreated": "2023-01-26T10:11:46Z",  
  "dateModified": "2023-01-26T05:03:38Z",  
  "source": "Import",  
  "name": "Compressor",  
  "alternateName": "Compressor type 2",  
  "description": "Compressor of limited Compressor types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### Compresseur NGSI-LD normalisé Exemple  
Voici un exemple de compresseur au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Compressor:ff065369-a64b-4950-8bcd-ea73c6f6bf34",  
  "type": "Compressor",  
  "compressorSpeed": {  
    "type": "Property",  
    "unitCode": "cycles/s",  
    "observedAt": "2023-01-26T02:36:18Z",  
    "value": 0.23988109283737147  
  },  
  "hasHotGasBypass": {  
    "type": "Property",  
    "value": true  
  },  
  "idealCapacity": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-25T18:17:55Z",  
    "value": 0.37381644415955617  
  },  
  "idealShaftPower": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-25T19:36:02Z",  
    "value": 0.7352666167757617  
  },  
  "impellerDiameter": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-25T16:56:06Z",  
    "value": 0.4819044880876878  
  },  
  "nominalCapacity": {  
    "type": "Property",  
    "unitCode": "J/s",  
    "observedAt": "2023-01-26T02:02:53Z",  
    "value": 0.42903531710900167  
  },  
  "partLoadRatioMax": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-25T20:48:37Z",  
    "value": 0.44114941929726603  
  },  
  "partLoadRatioMin": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-25T21:57:43Z",  
    "value": 0.8407270037851944  
  },  
  "powerSource": {  
    "type": "Property",  
    "value": "Mississippi"  
  },  
  "refrigerantClass": {  
    "type": "Property",  
    "value": "initiatives"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:200fbc88-04e4-4634-9ab8-31a7ffd7801a"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:6516f3b0-d423-45b0-bcfe-f5a361c118a1"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:0d189ba5-fbb5-42f9-b221-e481ed2215b3"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:682f3690-3403-45d3-8c59-d62b82b2dbb3"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:f346ab7e-bb7c-4da8-853f-f37193cfe98e"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Compressor Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Compressor 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T12:36:15Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-25T17:29:33Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Compressor"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Compressor type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Compressor of limited Compressor types"  
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
