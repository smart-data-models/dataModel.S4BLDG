/* (Beta) Export of data model EvaporativeCooler of the subject dataModel.S4BLDG for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE EvaporativeCooler_type AS ENUM ('EvaporativeCooler');
CREATE TABLE EvaporativeCooler (address json, alternateName text, areaServed text, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, flowArrangement text, hasManufacturer text, hasModel text, heatExchangeArea json, id text, isContainedInBuildingSpace json, isContainedInPhysicalObject json, isSubSystemOf json, location json, name text, operationTemperatureMax json, operationTemperatureMin json, owner json, seeAlso json, source text, type EvaporativeCooler_type, waterRequirement json);