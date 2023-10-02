/* (Beta) Export of data model AirToAirHeatRecovery of the subject dataModel.S4BLDG for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE AirToAirHeatRecovery_type AS ENUM ('AirToAirHeatRecovery');
CREATE TABLE AirToAirHeatRecovery (address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, hasDefrost BOOLEAN, hasManufacturer TEXT, hasModel TEXT, heatTransferTypeEnum TEXT, isSubSystemOf JSON, name TEXT, operationTemperatureMax NUMERIC, operationTemperatureMin NUMERIC, owner JSON, primaryAirFlowRateMax NUMERIC, primaryAirFlowRateMin NUMERIC, secondaryAirFlowRateMax NUMERIC, secondaryAirFlowRateMin NUMERIC, source TEXT, type AirToAirHeatRecovery_type);