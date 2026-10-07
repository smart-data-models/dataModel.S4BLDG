/* (Beta) Export of data model Controller of the subject dataModel.S4BLDG for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Controller_controllingProperty_type AS ENUM ('temperature', 'CO2');
CREATE TYPE Controller_type AS ENUM ('Controller');
CREATE TABLE Controller (
  "address" JSON,
  "alternateName" TEXT,
  "areaServed" TEXT,
  "controllingProperty" Controller_controllingProperty_type,
  "dataProvider" TEXT,
  "dateCreated" TIMESTAMP,
  "dateModified" TIMESTAMP,
  "description" TEXT,
  "hasManufacturer" TEXT,
  "hasModel" TEXT,
  "id" TEXT PRIMARY KEY,
  "isContainedInBuildingSpace" JSON,
  "isContainedInPhysicalObject" JSON,
  "isSubSystemOf" JSON,
  "location" JSON,
  "name" TEXT,
  "owner" JSON,
  "seeAlso" JSON,
  "source" TEXT,
  "type" Controller_type
);