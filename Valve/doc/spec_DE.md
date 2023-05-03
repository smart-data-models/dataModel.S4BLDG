<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: Ventil  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Valve/LICENSE.md)  
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
#### Ventil NGSI-v2 Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein Ventil im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
#### Ventil NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein Ventil im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
#### Ventil NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein Ventil im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
#### Ventil NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein Ventil im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
