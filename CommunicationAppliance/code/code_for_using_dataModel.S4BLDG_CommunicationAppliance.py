
#         # This code allows you to install a orion-ld broker in a linux system
#         # The manuals are here https://github.com/FIWARE/context.Orion-LD/tree/develop/doc/manuals-ld
#         
#         # INSTALL NGSI LD broker (OrionLD)
#         sudo docker pull mongo:3.6
#         sudo docker pull fiware/orion-ld
#         sudo docker network create fiware_default
#         sudo docker run -d --name=mongo-db --network=fiware_default --expose=27017 mongo:3.6 --bind_ip_all --smallfiles
#         sudo docker run -d --name fiware-orionld -h orion --network=fiware_default -p 1026:1026  fiware/orion-ld -dbhost mongo-db
#         
#         # TO RELAUNCH (only if you have already installed a broker in the same machine)
#         sudo docker stop fiware-orionld
#         sudo docker rm fiware-orionld
#         sudo docker stop mongo-db
#         sudo docker rm mongo-db
#         sudo docker network rm fiware_default
#         
#         # CHECK INSTANCES
#         # Check the broker is running
#         curl -X GET 'http://localhost:1026/version'
#         
#         # Check what entities are in the broker
#         curl -X GET http://localhost:1026/ngsi-ld/v1/entities?local=true&limit=1000
#         
#         # now the python code you can use to insert some value in the context broker according to the data model
#         
from pysmartdatamodels import pysmartdatamodels as sdm
import subprocess
serverUrl = "http://localhost:1026" # supposed that your broker is installed in localhost. Edit to match your configuration
dataModel = "CommunicationAppliance"
subject = "dataModel.S4BLDG"
isContainedInBuildingSpace = "{'type': 'Relationship', 'object': 'urn:ngsi-ld:BuildingSpace:75317891-340a-49a8-8f3e-4ec891d943c9'}"
attribute = "isContainedInBuildingSpace"
value = isContainedInBuildingSpace
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

isContainedInPhysicalObject = "{'type': 'Relationship', 'object': 'urn:ngsi-ld:PhysicalObject:34630474-4529-40d0-ad5c-367c9494694d'}"
attribute = "isContainedInPhysicalObject"
value = isContainedInPhysicalObject
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

isSubSystemOf = [{'type': 'Relationship', 'object': 'urn:ngsi-ld:System:91da2b77-a2e5-411c-be8f-f3245c2f9087'}, {'type': 'Relationship', 'object': 'urn:ngsi-ld:System:cdae1f62-b280-4e18-81de-99dc49cb9cd3'}, {'type': 'Relationship', 'object': 'urn:ngsi-ld:System:0233eb63-8b4d-4164-81e9-db4a7ba3f752'}]
attribute = "isSubSystemOf"
value = isSubSystemOf
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

hasManufacturer = "{'type': 'Property', 'value': 'CommunicationAppliance Company Inc.'}"
attribute = "hasManufacturer"
value = hasManufacturer
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

print(" In case you have installed the orion-ld broker (see comments on the header of this program)")
print(" Execute this instruction to check that the entities has been inserted")
command = ['curl', '-X', 'GET', 'http://localhost:1026/ngsi-ld/v1/entities?local=true&limit=1000']
result = subprocess.run(command, capture_output=True, text=True)
print(result.stdout)
