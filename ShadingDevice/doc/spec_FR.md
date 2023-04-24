<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : Dispositif d'ombrage  
=============================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/ShadingDevice/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Les dispositifs d'ombrage sont des dispositifs conçus pour protéger de la lumière du soleil ou de la lumière naturelle, ou pour les dissimuler à la vue. Les dispositifs d'ombrage peuvent faire partie de la façade ou être montés à l'intérieur du bâtiment, ils peuvent être fixes ou actionnables.  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Date de création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage.  - `dateModified[string]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage.  - `description[string]`: Une description de l'article  - `hasManufacturer[string]`: Propriété. Une relation identifiant le fabricant d'une entité (par exemple, un appareil). La valeur doit être une chaîne de caractères ou une chaîne de caractères avec une étiquette de langue.  - `hasModel[string]`: Propriété. Une relation identifiant le modèle d'une entité (par exemple, un appareil). La valeur doit être une chaîne de caractères ou une chaîne de caractères avec une balise de langue.  - `id[*]`: Identifiant unique de l'entité  - `isContainedInBuildingSpace[*]`: Relations. Entité utilisée pour définir les espaces physiques du bâtiment. Un espace de bâtiment contient des appareils ou des objets de bâtiment. (Espace Bâtiment)  - `isContainedInPhysicalObject[*]`: Relation. Tout objet qui possède une région spatiale propre.  (Définition extraite de l'ontologie DUL) (PhysicalObject)  - `isExternal[boolean]`: Propriété. Indique si l'élément est conçu pour être utilisé à l'extérieur (VRAI) ou non (FAUX). Si (VRAI), il s'agit d'un élément extérieur qui donne sur l'extérieur du bâtiment.  - `isSubSystemOf[array]`: Relation. Référence à un ou plusieurs systèmes dont cet objet physique fait partie.  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `mechanicalOperated[boolean]`: Propriété. Indique si l'élément est exploité machinalement (VRAI) ou non, c'est-à-dire manuellement (FAUX).  - `name[string]`: Le nom de cet élément.  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `roughness[string]`: Propriété. Mesure des déviations verticales de la surface.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `shadingDeviceType[string]`: Propriété. Spécifie le type de dispositif d'ombrage.  - `solarReflectance[number]`: Propriété. (Rsol) : Le rapport entre le rayonnement solaire incident et le rayonnement solaire réfléchi par un système de protection solaire (également appelé _e). Notez l'équation suivante Asol + Rsol + Tsol = 1  - `solarTransmittance[number]`: Propriété. (Tsol) Rapport du rayonnement solaire incident qui traverse directement un système de protection solaire (également appelé _e). Notez l'équation suivante Asol + Rsol + Tsol = 1  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `thermalTransmittance[number]`: Propriété. Vitesse à laquelle l'énergie est transmise à travers un corps. Généralement mesuré en Watts/m2 Kelvin.  - `type[string]`: Property. Elle doit être égale à `ShadingDevice`.  - `visibleLightReflectance[number]`: Propriété. Fraction de la lumière visible réfléchie par le vitrage en incidence normale. Il s'agit d'une valeur sans unité.  - `visibleLightTransmittance[number]`: Propriété. Fraction de la lumière visible qui traverse le système d'ombrage à incidence normale. Il s'agit d'une valeur sans unité.  <!-- /30-PropertiesList -->  
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
ShadingDevice:    
  description: 'Shading devices are purpose built devices to protect from the sunlight, from natural light, or screening them from view. Shading devices can form part of the facade or can be mounted inside the building, they can be fixed or operable.'    
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
      anyOf: &shadingdevice_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
      anyOf: *shadingdevice_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. An entity used to define the physical spaces of the building. A building space contains devices or building objects. (BuildingSpace)    
      x-ngsi:    
        type: Property    
    isContainedInPhysicalObject:    
      anyOf: *shadingdevice_-_properties_-_iscontainedinbuildingspace_-_anyof    
      description: Relationship. Any Object that has a proper space region.  (Definition extracted from DUL ontology) (PhysicalObject)    
      x-ngsi:    
        type: Property    
    isExternal:    
      description: Property. Indication whether the element is designed for use in the exterior (TRUE) or not (FALSE). If (TRUE) it is an external element and faces the outside of the building.    
      type: boolean    
      x-ngsi:    
        type: Property    
    isSubSystemOf:    
      description: Relationship. A reference to a system(s) that this Physical Object is part of.    
      items:    
        anyOf: *shadingdevice_-_properties_-_iscontainedinbuildingspace_-_anyof    
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
    mechanicalOperated:    
      description: 'Property. Indication whether the element is operated machanically (TRUE) or not, i.e. manually (FALSE).'    
      type: boolean    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item.    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *shadingdevice_-_properties_-_iscontainedinbuildingspace_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    roughness:    
      description: Property. A measure of the vertical deviations of the surface.    
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
    shadingDeviceType:    
      description: Property. Specifies the type of shading device.    
      type: string    
      x-ngsi:    
        type: Property    
    solarReflectance:    
      description: 'Property. (Rsol): The ratio of incident solar radiation that is reflected by a shading system (also named _e). Note the following equation Asol + Rsol + Tsol = 1'    
      type: number    
      x-ngsi:    
        type: Property    
    solarTransmittance:    
      description: Property. (Tsol) The ratio of incident solar radiation that directly passes through a shading system (also named _e). Note the following equation Asol + Rsol + Tsol = 1    
      type: number    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    thermalTransmittance:    
      description: Property. Rate at which energy is transmitted through a body. Usually measured in Watts/m2 Kelvin.    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: Property. It must be equal to `ShadingDevice`.    
      enum:    
        - ShadingDevice    
      type: string    
      x-ngsi:    
        type: Property    
    visibleLightReflectance:    
      description: Property. Fraction of the visible light that is reflected by the glazing at normal incidence. It is a value without unit.    
      type: number    
      x-ngsi:    
        type: Property    
    visibleLightTransmittance:    
      description: Property. Fraction of the visible light that passes the shading system at normal incidence. It is a value without unit.    
      type: number    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: "https://saref.etsi.org/saref4bldg/v1.1.2/#s4bldg:ShadingDevice"    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.S4BLDG/blob/master/ShadingDevice/LICENSE.md    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/ShadingDevice/schema.json    
  x-model-tags: SAREF ShadingDevice    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### ShadingDevice Valeurs clés NGSI-v2 Exemple  
Voici un exemple d'un ShadingDevice au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:ShadingDevice:03281d48-cb47-4061-9208-b2a380b3d7cd",  
    "type": "ShadingDevice",  
    "isExternal": false,  
    "mechanicalOperated": true,  
    "roughness": "Executive",  
    "shadingDeviceType": "client-driven",  
    "solarReflectance": 0.7901767410172098,  
    "solarTransmittance": 0.5537106205704284,  
    "thermalTransmittance": 0.9786915841160174,  
    "visibleLightReflectance": 0.7194478774053882,  
    "visibleLightTransmittance": 0.8973320246848571,  
    "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:3f4442cb-0f79-4dad-81ba-69879612f561",  
    "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:de04c9b6-2d78-491f-987a-085ea71f747b",  
    "isSubSystemOf": [  
        "urn:ngsi-ld:System:fd063381-99e7-4b7d-8936-cd66932ba1e7",  
        "urn:ngsi-ld:System:5bfac8cc-a08e-4bc8-a9e8-474e8db84d73",  
        "urn:ngsi-ld:System:a4eef133-5e5d-4051-8b37-bf89e468f019"  
    ],  
    "hasManufacturer": "ShadingDevice Company Inc.",  
    "hasModel": "ShadingDevice 0.1.2",  
    "dateCreated": "2023-01-26T07:18:28Z",  
    "dateModified": "2023-01-26T08:58:08Z",  
    "source": "Import",  
    "name": "ShadingDevice",  
    "alternateName": "ShadingDevice type 2",  
    "description": "ShadingDevice of limited ShadingDevice types",  
    "dataProvider": "IFC file"  
}  
```  
</details>  
#### ShadingDevice NGSI-v2 normalisé Exemple  
Voici un exemple d'un ShadingDevice au format JSON-LD tel que normalisé. Ce format est compatible avec la norme NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ShadingDevice:b3c3bd8f-6f5a-400a-b43c-99c32bf7d036",  
  "type": "ShadingDevice",  
  "isExternal": {  
    "type": "Boolean",  
    "value": true  
  },  
  "mechanicalOperated": {  
    "type": "Boolean",  
    "value": false  
  },  
  "roughness": {  
    "type": "Text",  
    "value": "Home Loan Account"  
  },  
  "shadingDeviceType": {  
    "type": "Text",  
    "value": "program"  
  },  
  "solarReflectance": {  
    "type": "Measurement",  
    "value": 0.23462582512353236  
  },  
  "solarTransmittance": {  
    "type": "Measurement",  
    "value": 0.569468324137257  
  },  
  "thermalTransmittance": {  
    "type": "Measurement",  
    "value": 0.315308180363743  
  },  
  "visibleLightReflectance": {  
    "type": "Measurement",  
    "value": 0.6167477347282538  
  },  
  "visibleLightTransmittance": {  
    "type": "Measurement",  
    "value": 0.27849116636487137  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:BuildingSpace:6d6d4b35-2d0f-4590-bd7d-1e5cdc1d71fe"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:PhysicalObject:ff501e6f-1fbf-4dd4-9537-b3b6668f156b"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:System:6d7f1004-c306-4d6b-8b95-d661e62087df"  
      },  
      {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:System:9eedb406-9b0a-466e-99bf-d8b4721af694"  
      },  
      {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:System:c485e374-da84-4bff-8a79-7d35bdcd0dab"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "ShadingDevice Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "ShadingDevice 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T15:18:47.9518072+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T11:03:03.3618393+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "ShadingDevice"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "ShadingDevice type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "ShadingDevice of limited ShadingDevice types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### ShadingDevice Valeurs clés NGSI-LD Exemple  
Voici un exemple d'un ShadingDevice au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ShadingDevice:03281d48-cb47-4061-9208-b2a380b3d7cd",  
  "type": "ShadingDevice",  
  "isExternal": false,  
  "mechanicalOperated": true,  
  "roughness": "Executive",  
  "shadingDeviceType": "client-driven",  
  "solarReflectance": 0.7901767410172098,  
  "solarTransmittance": 0.5537106205704284,  
  "thermalTransmittance": 0.9786915841160174,  
  "visibleLightReflectance": 0.7194478774053882,  
  "visibleLightTransmittance": 0.8973320246848571,  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:3f4442cb-0f79-4dad-81ba-69879612f561",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:de04c9b6-2d78-491f-987a-085ea71f747b",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:fd063381-99e7-4b7d-8936-cd66932ba1e7",  
    "urn:ngsi-ld:System:5bfac8cc-a08e-4bc8-a9e8-474e8db84d73",  
    "urn:ngsi-ld:System:a4eef133-5e5d-4051-8b37-bf89e468f019"  
  ],  
  "hasManufacturer": "ShadingDevice Company Inc.",  
  "hasModel": "ShadingDevice 0.1.2",  
  "dateCreated": "2023-01-26T07:18:28Z",  
  "dateModified": "2023-01-26T08:58:08Z",  
  "source": "Import",  
  "name": "ShadingDevice",  
  "alternateName": "ShadingDevice type 2",  
  "description": "ShadingDevice of limited ShadingDevice types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### ShadingDevice NGSI-LD normalisé Exemple  
Voici un exemple d'un ShadingDevice au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ShadingDevice:98dd5d05-db70-4ebb-a39c-e286063cb137",  
  "type": "ShadingDevice",  
  "isExternal": {  
    "type": "Property",  
    "value": true  
  },  
  "mechanicalOperated": {  
    "type": "Property",  
    "value": true  
  },  
  "roughness": {  
    "type": "Property",  
    "value": "Practical Rubber Cheese"  
  },  
  "shadingDeviceType": {  
    "type": "Property",  
    "value": "parsing"  
  },  
  "solarReflectance": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T03:37:18Z",  
    "value": 0.378910710384914  
  },  
  "solarTransmittance": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T09:24:57Z",  
    "value": 0.9404860966072789  
  },  
  "thermalTransmittance": {  
    "type": "Property",  
    "unitCode": "Kelvin",  
    "observedAt": "2023-01-26T12:37:04Z",  
    "value": 0.471443015298326  
  },  
  "visibleLightReflectance": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T06:09:46Z",  
    "value": 0.7789148596577641  
  },  
  "visibleLightTransmittance": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T05:43:18Z",  
    "value": 0.9110422065316075  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:0bfda01f-c7bd-4db3-9a81-cfeb051cf629"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:53171831-ae73-45fa-8f15-b1c034e5b2af"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:b9d614e5-32c2-47cd-b5ba-23b2c8ed67ea"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:6048cde5-df44-4963-b770-29ace8711405"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:e2c351bf-c825-4bc9-a7ca-dc96552b8e38"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "ShadingDevice Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "ShadingDevice 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T15:37:39Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-25T17:44:25Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "ShadingDevice"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "ShadingDevice type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "ShadingDevice of limited ShadingDevice types"  
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
