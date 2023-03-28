<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: AirToAirHeatRecovery  
=============================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/AirToAirHeatRecovery/LICENSE.md)  
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
#### AirToAirHeatRecovery NGSI-v2 Schlüsselwerte Beispiel  
Hier ist ein Beispiel für eine AirToAirHeatRecovery im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und gibt die Kontextdaten einer einzelnen Entität zurück.  
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
#### AirToAirHeatRecovery NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für eine AirToAirHeatRecovery im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-v2 kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
    "type": "Relationship",  
    "value": "urn:ngsi-ld:BuildingSpace:2058c38a-eb2e-4001-af3f-9a93effd41ac"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:PhysicalObject:ea1b1b2c-cb04-429d-bf2c-ca99e7f3f005"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:System:123d10ff-2c3a-40f4-9fd0-07851a7d7a3c"  
      },  
      {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:System:90a762d4-7eed-4d5a-8a0d-a4676773917f"  
      },  
      {  
        "type": "Relationship",  
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
#### AirToAirHeatRecovery NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für eine AirToAirHeatRecovery im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und gibt die Kontextdaten einer einzelnen Entität zurück.  
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
    "https://raw.githubusercontent.com/smart-data-models/incubated/master/SAREF/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### AirToAirHeatRecovery NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für eine AirToAirHeatRecovery im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
