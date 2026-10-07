/* (Beta) Export of data model Coil of the subject dataModel.S4BLDG for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Coil_operationMode_type AS ENUM ('cooling', 'heating');
CREATE TYPE Coil_type AS ENUM ('Coil');
CREATE TABLE Coil (
  "address" JSON,
  "airFlowRateMax" NUMERIC,
  "airFlowRateMin" NUMERIC,
  "alternateName" TEXT,
  "areaServed" TEXT,
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
  "nominalLatentCapacity" NUMERIC,
  "nominalSensibleCapacity" NUMERIC,
  "nominalUa" NUMERIC,
  "operationMode" Coil_operationMode_type,
  "operationTemperatureMax" NUMERIC,
  "operationTemperatureMin" NUMERIC,
  "owner" JSON,
  "placementType" TEXT,
  "seeAlso" JSON,
  "source" TEXT,
  "type" Coil_type
);