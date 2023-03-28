<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: Alarm  
==============<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Alarm/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- Keine erforderlichen Eigenschaften  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### Alarm NGSI-v2 Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen Alarm im JSON-LD-Format als Schlüsselwerte. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Alarm:403ddbdf-79c0-4923-9d07-4c962837c527",  
  "type": "Alarm",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:5920683a-3228-480c-82f6-17c1cf239df4",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:58a84941-5697-4bdd-a39b-0f509d89659f",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:d2fa7d6b-adfe-4b27-a231-c5c5edb297ad",  
    "urn:ngsi-ld:System:97320977-f3bd-47f8-8945-c15e1fc0c50f",  
    "urn:ngsi-ld:System:d05a0603-3ea4-4ed8-9a3d-edac79bae877"  
  ],  
  "hasManufacturer": "Alarm Company Inc.",  
  "hasModel": "Alarm 0.1.2",  
  "dateCreated": "2023-01-26T04:02:51Z",  
  "dateModified": "2023-01-26T07:49:05Z",  
  "source": "Import",  
  "name": "Alarm",  
  "alternateName": "Alarm type 2",  
  "description": "Alarm of limited Alarm types",  
  "dataProvider": "IFC file"  
}  
```  
</details>  
#### Alarm NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen Alarm im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Alarm:8ae04687-4a9f-4cc8-acfa-2bc726781aaa",  
  "type": "Alarm",  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:BuildingSpace:db2e26a9-5f4a-4b2c-9510-e7f9e2239efa"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:PhysicalObject:1c447365-0f4e-4350-bfc7-a2974d8297dd"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:System:38982b54-aaed-4916-ad8f-fcfeccb8fe6d"  
      },  
      {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:System:d7ead903-19a3-4f08-90a8-52979e99bc2b"  
      },  
      {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:System:5baec201-65ae-41f9-b557-37bd69cd14bb"  
      }  
    ]  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "Alarm Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "Alarm 0.1.2"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-25T14:33:52.1440188+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-26T10:12:39.8292183+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Alarm"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Alarm type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Alarm of limited Alarm types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### Alarm NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen Alarm im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Alarm:5c49d555-274b-4ccd-b527-823329defc35",  
  "type": "Alarm",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:98c9f61a-d8f8-4326-b4f3-8845c97ad825",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:2651a0f9-1d1b-4204-bcfc-a55f2d51f3bd",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:8162840d-293b-4e69-a911-479d6040b540",  
    "urn:ngsi-ld:System:573efc0a-de49-43da-bed2-123de1138501",  
    "urn:ngsi-ld:System:565a39a6-eea4-4b32-8dcc-f10941da849a"  
  ],  
  "hasManufacturer": "Alarm Company Inc.",  
  "hasModel": "Alarm 0.1.2",  
  "dateCreated": "2023-01-25T17:55:12Z",  
  "dateModified": "2023-01-25T23:48:06Z",  
  "source": "Import",  
  "name": "Alarm",  
  "alternateName": "Alarm type 2",  
  "description": "Alarm of limited Alarm types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/incubated/master/SAREF/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### Alarm NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen Alarm im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Alarm:3200afb8-5a97-4a51-b454-a7bb5e7dd272",  
  "type": "Alarm",  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:ef503257-cb0f-456e-88eb-90fee65efbd1"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:c6d91273-5403-4ffb-835d-5bc5f7778667"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:9cc30a80-baee-46bf-b844-9e5bfd93373f"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:c4d6a860-5659-4a7c-a2fe-6e910f200b84"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:4c12a0b6-c61d-40ec-9545-50e88d01592e"  
    }  
  ],  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "Alarm Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "Alarm 0.1.2"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T20:04:31Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T04:48:57Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Alarm"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Alarm type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Alarm of limited Alarm types"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "IFC file"  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/incubated/master/SAREF/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
