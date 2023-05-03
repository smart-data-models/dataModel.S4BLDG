/* (Beta) Export of data model Alarm of the subject dataModel.S4BLDG for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Alarm_type AS ENUM ('Alarm');
CREATE TABLE Alarm (address json, alternateName text, areaServed text, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, hasManufacturer text, hasModel text, id text, isContainedInBuildingSpace text, isContainedInPhysicalObject text, isSubSystemOf json, location json, name text, owner json, seeAlso json, source text, type Alarm_type);