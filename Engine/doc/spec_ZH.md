<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：发动机  
======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.S4BLDG/blob/master/Engine/LICENSE.md)  
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
#### Engine NGSI-v2 key-values 示例  
这里是一个以JSON-LD格式作为key-values的引擎的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Engine:b52e685f-61d6-4f9a-a164-a1f41ec15fa2",  
  "type": "Engine",  
  "energySource": "Multi-tiered",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:c1248001-a5aa-4add-9063-e97f34b6f7cb",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:bc0986d8-b680-447e-ab2a-ccbc597ecbc1",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:ae40d806-ba78-4bcc-a14e-4677d11d3c2b",  
    "urn:ngsi-ld:System:4e0650bd-50ae-4e13-aa52-c0e27f453177",  
    "urn:ngsi-ld:System:49c6ed8d-a64e-4c4c-aa72-bac3cff74d9b"  
  ],  
  "hasManufacturer": "Engine Company Inc.",  
  "hasModel": "Engine 0.1.2",  
  "dateCreated": "2023-01-26T07:27:05Z",  
  "dateModified": "2023-01-26T12:13:01Z",  
  "source": "Import",  
  "name": "Engine",  
  "alternateName": "Engine type 2",  
  "description": "Engine of limited Engine types",  
  "dataProvider": "IFC file"  
}  
```  
</details>  
不提供JSON-LD格式的引擎的例子，因为它是规范化的。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
#### 引擎NGSI-LD关键值示例  
这里有一个JSON-LD格式的引擎作为key-values的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Engine:2151d525-b608-42c7-9fb7-878a90d0dc9d",  
  "type": "Engine",  
  "energySource": "Electronics & Health",  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:21ee1467-3690-4e04-9199-08647e69c7da",  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:d7215722-2428-4d4f-8554-c45675ab0585",  
  "isSubSystemOf": [  
    "urn:ngsi-ld:System:c47e92e7-3110-433c-8dfb-d0c9cf916d54",  
    "urn:ngsi-ld:System:647dbda8-86b9-4a88-8a38-1b69288bd4a4",  
    "urn:ngsi-ld:System:08b67c2e-9a32-4c99-bdb6-3a3b765ce14d"  
  ],  
  "hasManufacturer": "Engine Company Inc.",  
  "hasModel": "Engine 0.1.2",  
  "dateCreated": "2023-01-26T03:13:30Z",  
  "dateModified": "2023-01-26T14:10:51Z",  
  "source": "Import",  
  "name": "Engine",  
  "alternateName": "Engine type 2",  
  "description": "Engine of limited Engine types",  
  "dataProvider": "IFC file",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.S4BLDG/master/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
</details>  
不提供JSON-LD格式的引擎的例子，因为它是规范化的。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
