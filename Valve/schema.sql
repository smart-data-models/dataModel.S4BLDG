/* (Beta) Export of data model Valve of the subject dataModel.S4BLDG for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Valve_type AS ENUM ('Valve');
CREATE TABLE Valve (address json, alternateName text, areaServed text, closeOffRating text, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, flowCoefficient text, hasManufacturer text, hasModel text, id text, isContainedInBuildingSpace json, isContainedInPhysicalObject json, isSubSystemOf json, location json, name text, owner json, seeAlso json, size text, source text, testPressure text, type Valve_type, valveMechanism text, valveOperation text, valvePattern text, workingPressure text);