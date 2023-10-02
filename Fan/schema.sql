/* (Beta) Export of data model Fan of the subject dataModel.S4BLDG for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE operationMode_type AS ENUM ('supply','exhaust');CREATE TYPE Fan_type AS ENUM ('Fan');
CREATE TABLE Fan (address JSON, alternateName TEXT, areaServed TEXT, capacityControlType TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, hasManufacturer TEXT, hasModel TEXT, isSubSystemOf JSON, motorDriveType TEXT, name TEXT, nominalAirFlowRate NUMERIC, nominalPowerRate NUMERIC, nominalRotationSpeed NUMERIC, nominalStaticPressure NUMERIC, nominalTotalPressure NUMERIC, operationMode operationMode_type, operationTemperatureMax NUMERIC, operationTemperatureMin NUMERIC, operationalRiterial NUMERIC, owner JSON, source TEXT, type Fan_type);