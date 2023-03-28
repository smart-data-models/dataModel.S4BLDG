/* (Beta) Export of data model Actuator of the subject dataModel.S4BLDG for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Actuator_type AS ENUM ('Actuator');
CREATE TABLE Actuator (address json, alternateName text, areaServed text, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, failPosition text, hasManufacturer text, hasModel text, id text, isContainedInBuildingSpace json, isContainedInPhysicalObject json, isSubSystemOf json, location json, manualOverride text, name text, owner json, seeAlso json, source text, type Actuator_type);