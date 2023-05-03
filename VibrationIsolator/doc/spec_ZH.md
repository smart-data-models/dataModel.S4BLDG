<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：振动隔离器  
========<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/VibrationIsolator/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- 没有要求的属性  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### VibrationIsolator NGSI-v2 key-values 示例  
这里是一个以JSON-LD格式作为关键值的VibrationIsolator的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:VibrationIsolator:cd36687d-d862-4b70-b8ed-789a16b2afec",  
    "type": "VibrationIsolator",  
    "height": 0.38014362681889713,  
    "isolatorCompressibility": 0.7634523319144405,  
    "isolatorStaticDeflection": 0.7887792629834026,  
    "supportedWeightMax": 0.32346503665487614,  
    "vibrationTransmissibility": 0.0735805434874115,  
    "hasManufacturer": "VibrationIsolator Company Inc.",  
    "hasModel": "VibrationIsolator 0.1.2",  
    "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:e78215e8-4265-4a20-abd0-a19cbe803047",  
    "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:30fd3d36-dbea-4994-a312-a061f283886a",  
    "isSubSystemOf": [  
        "urn:ngsi-ld:System:a9cb3141-21d1-41f9-882d-4e7eb5ca0538",  
        "urn:ngsi-ld:System:d34a3962-d8fc-4d65-a0d8-57d881ec9279",  
        "urn:ngsi-ld:System:c23095d2-a7c8-4920-b237-e7ae47f03451"  
    ],  
    "dateCreated": "2023-01-26T13:07:56Z",  
    "dateModified": "2023-01-26T06:35:21Z",  
    "source": "Import",  
    "name": "VibrationIsolator",  
    "alternateName": "VibrationIsolator type 2",  
    "description": "VibrationIsolator of limited VibrationIsolator types",  
    "dataProvider": "IFC file"  
}  
```  
</details>  
#### VibrationIsolator NGSI-v2 normalized 示例  
下面是一个以JSON-LD格式规范化的VibrationIsolator的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:VibrationIsolator:c808c7ae-06ec-4022-8405-3a2031703303",  
  "type": "VibrationIsolator",  
  "height": {  
    "type": "Measurement",  
    "value": 0.4519574730782471  
  },  
  "isolatorCompressibility": {  
    "type": "Measurement",  
    "value": 0.11287489586954691  
  },  
  "isolatorStaticDeflection": {  
    "type": "Measurement",  
    "value": 0.44640431539803016  
  },  
  "supportedWeightMax": {  
    "type": "Measurement",  
    "value": 0.9957664703512201  
  },  
  "vibrationTransmissibility": {  
    "type": "Measurement",  
    "value": 0.045745566367183965  
  },  
  "hasManufacturer": {  
    "type": "Text",  
    "value": "VibrationIsolator Company Inc."  
  },  
  "hasModel": {  
    "type": "Text",  
    "value": "VibrationIsolator 0.1.2"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:BuildingSpace:35215bc5-6e3e-4794-ab50-6a3a56149e98"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "URL",  
    "value": "urn:ngsi-ld:PhysicalObject:e97a7737-8516-4038-b9c3-a6bc22bc3228"  
  },  
  "isSubSystemOf": {  
    "type": "array",  
    "value": [  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:4491af0e-5aaf-494e-a7c2-7d62f7e18db5"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:18b4c438-10ee-4916-9d1d-b6e4dbc3bd7f"  
      },  
      {  
        "type": "URL",  
        "value": "urn:ngsi-ld:System:541cc5f6-fade-4136-a18a-784f97ebe6c4"  
      }  
    ]  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-01-26T04:34:02.6856577+01:00"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-01-25T21:20:11.0544578+01:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Text",  
    "value": "VibrationIsolator"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "VibrationIsolator type 2"  
  },  
  "description": {  
    "type": "Text",  
    "value": "VibrationIsolator of limited VibrationIsolator types"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "IFC file"  
  }  
}  
```  
</details>  
#### VibrationIsolator NGSI-LD key-values 示例  
这里是一个以JSON-LD格式作为关键值的VibrationIsolator的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:VibrationIsolator:cd36687d-d862-4b70-b8ed-789a16b2afec",  
  "type": "VibrationIsolator",  
  "height": 0.38014362681889713,  
  "isolatorCompressibility": 0.7634523319144405,  
  "isolatorStaticDeflection": 0.7887792629834026,  
  "supportedWeightMax": 0.32346503665487614,  
  "vibrationTransmissibility": 0.0735805434874115,  
  "hasManufacturer": "VibrationIsolator Company Inc.",  
  "hasModel": "VibrationIsolator 0.1.2",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:e78215e8-4265-4a20-abd0-a19cbe803047",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:30fd3d36-dbea-4994-a312-a061f283886a",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:a9cb3141-21d1-41f9-882d-4e7eb5ca0538",  
    "urn:ngsi-ld:System:d34a3962-d8fc-4d65-a0d8-57d881ec9279",  
    "urn:ngsi-ld:System:c23095d2-a7c8-4920-b237-e7ae47f03451"  
  ],  
  "dateCreated": "2023-01-26T13:07:56Z",  
  "dateModified": "2023-01-26T06:35:21Z",  
  "source": "Import",  
  "name": "VibrationIsolator",  
  "alternateName": "VibrationIsolator type 2",  
  "description": "VibrationIsolator of limited VibrationIsolator types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
#### VibrationIsolator NGSI-LD归一化实例  
下面是一个以JSON-LD格式规范化的VibrationIsolator的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:VibrationIsolator:3fef599e-57dd-4ead-b1f1-1be1acec4ed4",  
  "type": "VibrationIsolator",  
  "height": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T00:57:35Z",  
    "value": 0.5291676326164039  
  },  
  "isolatorCompressibility": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T13:38:20Z",  
    "value": 0.0633806140666543  
  },  
  "isolatorStaticDeflection": {  
    "type": "Property",  
    "unitCode": "mm",  
    "observedAt": "2023-01-26T05:45:32Z",  
    "value": 0.7015963366033574  
  },  
  "supportedWeightMax": {  
    "type": "Property",  
    "unitCode": "g",  
    "observedAt": "2023-01-26T11:46:41Z",  
    "value": 0.22821941593534223  
  },  
  "vibrationTransmissibility": {  
    "type": "Property",  
    "unitCode": "NA",  
    "observedAt": "2023-01-26T02:32:45Z",  
    "value": 0.5811208596388945  
  },  
  "hasManufacturer": {  
    "type": "Property",  
    "value": "VibrationIsolator Company Inc."  
  },  
  "hasModel": {  
    "type": "Property",  
    "value": "VibrationIsolator 0.1.2"  
  },  
  "isContainedInBuildingSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:BuildingSpace:fd49449a-d970-42ca-b1fc-76498db2246a"  
  },  
  "isContainedInPhysicalObject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PhysicalObject:928afd04-5e3b-4626-a746-e15f82d1dd27"  
  },  
  "isSubSystemOf": [  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:ef621e1c-9c02-4f58-9460-e9792c709c3c"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:d166189e-cc79-40a9-ad8d-9874487d095f"  
    },  
    {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:System:5dface3a-d991-4c63-a878-87fc9194c2a8"  
    }  
  ],  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-01-25T22:43:59Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-01-26T12:00:10Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Import"  
  },  
  "name": {  
    "type": "Property",  
    "value": "VibrationIsolator"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "VibrationIsolator type 2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "VibrationIsolator of limited VibrationIsolator types"  
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
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
