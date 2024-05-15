
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
dataModel = "Engine"
subject = "dataModel.S4BLDG"
energySource = "{'type': 'Property', 'value': 'clicks-and-mortar'}"
attribute = "energySource"
value = energySource
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

isContainedInBuildingSpace = "{'type': 'Relationship', 'object': 'urn:ngsi-ld:BuildingSpace:c0a71c4b-b58f-4c1d-9f45-aea4edfbf81c'}"
attribute = "isContainedInBuildingSpace"
value = isContainedInBuildingSpace
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

isContainedInPhysicalObject = "{'type': 'Relationship', 'object': 'urn:ngsi-ld:PhysicalObject:94a81a63-7fa4-4c21-a848-61673bd7f88c'}"
attribute = "isContainedInPhysicalObject"
value = isContainedInPhysicalObject
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

isSubSystemOf = [{'type': 'Relationship', 'object': 'urn:ngsi-ld:System:f31c4170-f77e-4f95-b42b-1cd21ef8e055'}, {'type': 'Relationship', 'object': 'urn:ngsi-ld:System:d45e4e4d-ed6f-485a-9cb7-9dedef98f469'}, {'type': 'Relationship', 'object': 'urn:ngsi-ld:System:34934d9a-5e85-4d2a-a629-95b645c2c89e'}]
attribute = "isSubSystemOf"
value = isSubSystemOf
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

print(" In case you have installed the orion-ld broker (see comments on the header of this program)")
print(" Execute this instruction to check that the entities has been inserted")
command = ['curl', '-X', 'GET', 'http://localhost:1026/ngsi-ld/v1/entities?local=true&limit=1000']
result = subprocess.run(command, capture_output=True, text=True)
print(result.stdout)
