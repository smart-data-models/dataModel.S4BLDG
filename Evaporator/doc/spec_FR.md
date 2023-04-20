<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : Évaporateur  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Evaporator/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Un évaporateur est un dispositif dans lequel un réfrigérant liquide est vaporisé et absorbe la chaleur du fluide environnant.  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Date de création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage.  - `dateModified[string]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage.  - `description[string]`: Une description de l'article  - `evaporationCoolant[string]`: Propriété. Le fluide utilisé comme liquide de refroidissement dans l'évaporateur.  - `evaporationMediumType[string]`: Propriété. ColdLiquid : L'évaporateur utilise un fluide de type liquide pour échanger de la chaleur avec le réfrigérant. ColdAir : L'évaporateur utilise de l'air pour échanger de la chaleur avec le réfrigérant.  - `externalSurfaceArea[object]`: Propriété. Surface extérieure (primaire et secondaire). Généralement mesurée en mètre carré (m2).  - `hasManufacturer[string]`: Propriété. Une relation identifiant le fabricant d'une entité (par exemple, un appareil). La valeur doit être une chaîne de caractères ou une chaîne de caractères avec une étiquette de langue.  - `hasModel[string]`: Propriété. Une relation identifiant le modèle d'une entité (par exemple, un appareil). La valeur doit être une chaîne de caractères ou une chaîne de caractères avec une balise de langue.  - `id[*]`: Identifiant unique de l'entité  - `internalRefrigerantVolume[object]`: Propriété. Volume interne de l'évaporateur (côté réfrigérant). Généralement mesuré en mètre cube (m3).  - `internalSurfaceArea[object]`: Propriété. Surface intérieure. Généralement mesurée en mètre carré (m2).  - `internalWaterVolume[object]`: Propriété. Volume interne de l'évaporateur (côté eau). Généralement mesuré en mètre cube (m3).  - `isContainedInBuildingSpace[*]`: Relations. Entité utilisée pour définir les espaces physiques du bâtiment. Un espace de bâtiment contient des appareils ou des objets de bâtiment. (Espace Bâtiment)  - `isContainedInPhysicalObject[*]`: Relation. Tout objet qui possède une région spatiale propre.  (Définition extraite de l'ontologie DUL) (PhysicalObject)  - `isSubSystemOf[array]`: Relation. Référence à un ou plusieurs systèmes dont cet objet physique fait partie.  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément.  - `nominalHeatTransferArea[object]`: Propriété. Surface nominale de transfert de chaleur associée au coefficient nominal global de transfert de chaleur. Généralement mesurée en mètre carré (m2).  - `nominalHeatTransferCoefficient[object]`: Propriété. Coefficient nominal global de transfert de chaleur associé à la surface nominale de transfert de chaleur. Généralement mesuré en Watts/m2 Kelvin.  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `refrigerantClass[string]`: Propriété. Classe de réfrigérant utilisée par le compresseur. CFC : Chlorofluorocarbures. HCFC : Hydrochlorofluorocarbures. HFC : Hydrofluorocarbures.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `type[string]`: Propriété. Elle doit être égale à `Evaporator`.  <!-- /30-PropertiesList -->  
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
Evaporator:    
  description: An evaporator is a device in which a liquid refrigerent is vaporized and absorbs heat from the surrounding fluid.    
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
    evaporationCoolant:    
      description: Property. The fluid used for the coolant in the evaporator.    
      type: string    
      x-ngsi:    
        type: Property    
    evaporationMediumType:    
      description: 'Property. ColdLiquid: Evaporator is using liquid type of fluid to exchange heat with refrigerant. ColdAir: Evaporator is using air to exchange heat with refrigerant.'    
      type: string    
      x-ngsi:    
        type: Property    
    externalSurfaceArea:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: Property. External surface area (both primary and secondary area). Usually measured in square metre (m2).    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: &evaporator_-_properties_-_internalrefrigerantvolume_-_properties    
        observedAt:    
          description: Property. A relationship stating the timestamp of an entity (e.g. a measurement).    
          format: date-time    
          type: string    
        unitCode:    
          description: Property. A relationship identifying the unit of measure used for a certain entity.    
          type: string    
        value:    
          description: 'Property. A relationship defining the value of a certain property, e.g., energy or power. Note that, even if numeric values are expected to enable reasoning, measurement values could use other datatypes.'    
          type: number    
      title: Smart data models - Measurement schema    
      type: object    
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
      anyOf: &evaporator_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    internalRefrigerantVolume:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: Property. Internal volume of evaporator (refrigerant side). Usually measured in cubic metre (m3).    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *evaporator_-_properties_-_internalrefrigerantvolume_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    internalSurfaceArea:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: Property. Internal surface area. Usually measured in square metre (m2).    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *evaporator_-_properties_-_internalrefrigerantvolume_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    internalWaterVolume:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: Property. Internal volume of evaporator (water side). Usually measured in cubic metre (m3).    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *evaporator_-_properties_-_internalrefrigerantvolume_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    isContainedInBuildingSpace:    
      anyOf: *evaporator_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *evaporator_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *evaporator_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    nominalHeatTransferArea:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: Property. Nominal heat transfer surface area associated with nominal overall heat transfer coefficient. Usually measured in square metre (m2).    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *evaporator_-_properties_-_internalrefrigerantvolume_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    nominalHeatTransferCoefficient:    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement    
      derivedFrom: "https://saref.etsi.org/core/v3.1.1/#saref:Measurement"    
      description: Property. Nominal overall heat transfer coefficient associated with nominal heat transfer area. Usually measured in Watts/m2 Kelvin.    
      license: https://opensource.org/licenses/BSD-3-Clause    
      properties: *evaporator_-_properties_-_internalrefrigerantvolume_-_properties    
      title: Smart data models - Measurement schema    
      type: object    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *evaporator_-_properties_-_iscontainedinbuildingspace_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
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
      description: Property. It must be equal to `Evaporator`.    
      enum:    
        - Evaporator    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:Evaporator"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/Evaporator/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Evaporator/schema.json    
  x-model-tags: SAREF Evaporator    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### Evaporateur NGSI-v2 Valeurs clés Exemple  
Voici un exemple d'évaporateur au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Evaporator:052fc49c-111f-420b-a8e2-51fe3338d2b1",  
  "type": "Evaporator",  
  "evaporationCoolant": "Martinique",  
  "evaporationMediumType": "e-markets",  
  "externalSurfaceArea": {  
    "type": "Measurement",  
    "value": {  
      "unitCode": "m2",  
      "observedAt": "2023-01-25T22:25:21Z",  
      "value": 0.5908980288694448  
    }  
  },  
  "internalRefrigerantVolume": {  
    "type": "Measurement",  
    "value": {  
      "unitCode": "m3",  
      "observedAt": "2023-01-26T13:10:15Z",  
      "value": 0.6284120974003947  
    }  
  },  
  "internalSurfaceArea": {  
    "type": "Measurement",  
    "value": {  
      "unitCode": "m2",  
      "observedAt": "2023-01-26T09:19:30Z",  
      "value": 0.9343787028327242  
    }  
  },  
  "internalWaterVolume": {  
    "type": "Measurement",  
    "value": {  
      "unitCode": "m3",  
      "observedAt": "2023-01-26T05:01:07Z",  
      "value": 0.6490547902275666  
    }  
  },  
  "nominalHeatTransferArea": {  
    "type": "Measurement",  
    "value": {  
      "unitCode": "m2",  
      "observedAt": "2023-01-26T14:02:50Z",  
      "value": 0.4294965931834158  
    }  
  },  
  "nominalHeatTransferCoefficient": {  
    "type": "Measurement",  
    "value": {  
      "unitCode": "Kelvin",  
      "observedAt": "2023-01-26T09:00:31Z",  
      "value": 0.8081650097718576  
    }  
  },  
  "refrigerantClass": "Jewelery, Music & Games",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:51c0dbf1-adcc-4d2c-b3ea-90aa62cb494f",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:c5bac51f-5e2b-4152-9eb1-96959129eb27",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:67f3cbde-6a56-4f0b-9085-ddcee5f7e9fa",  
    "urn:ngsi-ld:System:3e056ae8-5498-4141-9bca-6f9b2eb03b67",  
    "urn:ngsi-ld:System:6692437c-d2c6-4ba0-9386-3a7e0f49d10d"  
  ],  
  "hasManufacturer": "Evaporator Company Inc.",  
  "hasModel": "Evaporator 0.1.2",  
  "dateCreated": "2023-01-26T00:54:03Z",  
  "dateModified": "2023-01-25T16:56:18Z",  
  "source": "Import",  
  "name": "Evaporator",  
  "alternateName": "Evaporator type 2",  
  "description": "Evaporator of limited Evaporator types",  
  "dataProvider": "IFC file"  
}  
```  
</details>  
#### Evaporateur NGSI-v2 normalisé Exemple  
Voici un exemple d'évaporateur au format JSON-LD tel que normalisé. Ce format est compatible avec l'INSG-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Evaporator:c9337df1-e99a-43a3-9f15-425e35abf54a",  
  "type": "Evaporator",  
  "evaporationCoolant": {  
    "type": "Text",  
    "value": "seamless"  
  },  
  "evaporationMediumType": {  
    "type": "Text",  
    "value": "Pike"  
  },  
  "externalSurfaceArea": {  
    "type": "Measurement",  
    "value": 0.07191726989654268  
  },  
  "internalRefrigerantVolume": {  
    "type": "Measurement",  
    "value":  0.20250063780044392  
  },  
  "internalSurfaceArea": {  
    "type": "Measurement",  
    "value":  0.33350088977343506  
  },  
  "internalWaterVolume": {  
    "type": "Measurement",  
    "value":  0.8525147046941662  
  },  
  "nominalHeatTransferArea": {  
    "type": "Measurement",  
    "value":  0.7335123054536791  
  },  
  "nominalHeatTransferCoefficient": {  
    "type": "Measurement",  
    "value":  0.23696481410868975  
  },  
  "refrigerantClass": {  
    "type": "Text",  
    "value": "Incredible"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:BuildingSpace:1d3c18d5-3c73-4b33-ac02-be885911a9c2"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URI",  
    "value": "urn:ngsi-ld:PhysicalObject:c2a99f87-20d2-4a3e-8869-9ccb703023f7"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:9905fd33-a0dd-465c-821e-7179621c4cd2"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:912b3134-8a54-4576-9e70-68f7d814a681"  
      },  
      {  
        "type": "URI",  
        "value": "urn:ngsi-ld:System:46197de5-7d87-4a26-9d32-4e62dd387c93"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Evaporator Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Evaporator 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T19:39:32.5598858+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T02:08:29.4163966+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Evaporator"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Evaporator type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Evaporator of limited Evaporator types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### Evaporateur Valeurs clés NGSI-LD Exemple  
Voici un exemple d'évaporateur au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Evaporator:052fc49c-111f-420b-a8e2-51fe3338d2b1",  
  "type": "Evaporator",  
  "evaporationCoolant": "Martinique",  
  "evaporationMediumType": "e-markets",  
  "externalSurfaceArea": 0.5908980288694448,  
  "internalRefrigerantVolume": 0.6284120974003947,  
  "internalSurfaceArea": 0.9343787028327242,  
  "internalWaterVolume": 0.6490547902275666,  
  "nominalHeatTransferArea": 0.4294965931834158,  
  "nominalHeatTransferCoefficient": 0.8081650097718576,  
  "refrigerantClass": "Jewelery, Music & Games",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:51c0dbf1-adcc-4d2c-b3ea-90aa62cb494f",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:c5bac51f-5e2b-4152-9eb1-96959129eb27",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:67f3cbde-6a56-4f0b-9085-ddcee5f7e9fa",  
    "urn:ngsi-ld:System:3e056ae8-5498-4141-9bca-6f9b2eb03b67",  
    "urn:ngsi-ld:System:6692437c-d2c6-4ba0-9386-3a7e0f49d10d"  
  ],  
  "hasManufacturer": "Evaporator Company Inc.",  
  "hasModel": "Evaporator 0.1.2",  
  "dateCreated": "2023-01-26T00:54:03Z",  
  "dateModified": "2023-01-25T16:56:18Z",  
  "source": "Import",  
  "name": "Evaporator",  
  "alternateName": "Evaporator type 2",  
  "description": "Evaporator of limited Evaporator types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### Evaporateur NGSI-LD normalisé Exemple  
Voici un exemple d'évaporateur au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Evaporator:012ce978-0915-4322-82cf-64be00f886e6",  
  "type": "Evaporator",  
  "evaporationCoolant": {  
    "type": "Property",  
    "value": "Generic"  
  },  
  "evaporationMediumType": {  
    "type": "Property",  
    "value": "ROI"  
  },  
  "externalSurfaceArea": {  
    "type": "Property",  
    "unitCode": "m2",  
    "observedAt": "2023-01-26T01:26:06Z",  
    "value": 0.40305559655625467  
  },  
  "internalRefrigerantVolume": {  
    "type": "Property",  
    "unitCode": "m3",  
    "observedAt": "2023-01-26T04:37:57Z",  
    "value": 0.9165377999786634  
  },  
  "internalSurfaceArea": {  
    "type": "Property",  
    "unitCode": "m2",  
    "observedAt": "2023-01-26T07:59:30Z",  
    "value": 0.11705017875360657  
  },  
  "internalWaterVolume": {  
    "type": "Property",  
    "unitCode": "m3",  
    "observedAt": "2023-01-26T13:18:36Z",  
    "value": 0.6445386560470906  
  },  
  "nominalHeatTransferArea": {  
    "type": "Property",  
    "unitCode": "m2",  
    "observedAt": "2023-01-25T18:46:49Z",  
    "value": 0.20771410507872068  
  },  
  "nominalHeatTransferCoefficient": {  
    "type": "Property",  
    "unitCode": "Kelvin",  
    "observedAt": "2023-01-26T11:33:53Z",  
    "value": 0.029467682176717913  
  },  
  "refrigerantClass": {  
    "type": "Property",  
    "value": "Directives"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:09942ed6-b0b8-4968-a57d-e48b8fd062f9"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:9f7d6071-a0a0-4b9d-9707-b59804cef5a8"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:cb2ff8f9-5b3a-48f2-a576-c7a632297517"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:c9865d23-d9da-47f2-875a-1f0beb5bbf09"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:18016c6a-4548-4adc-a84c-c62c94e34393"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Evaporator Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Evaporator 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-26T06:49:33Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T02:39:15Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Evaporator"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Evaporator type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Evaporator of limited Evaporator types"  
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
