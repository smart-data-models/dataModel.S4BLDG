/* (Beta) Export of data model Pump of the subject dataModel.S4BLDG for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Pump_type AS ENUM ('Pump');
CREATE TABLE Pump (address JSON, alternateName TEXT, areaServed TEXT, connectionSize NUMERIC, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, flowResistanceMax NUMERIC, flowResistanceMin NUMERIC, hasManufacturer TEXT, hasModel TEXT, isSubSystemOf JSON, name TEXT, netPositiveSuctionHead NUMERIC, nomminalRotationSpeed NUMERIC, operationTemperatureMax NUMERIC, operationTemperatureMin NUMERIC, owner JSON, pumpFlowRateMax NUMERIC, pumpFlowRateMin NUMERIC, source TEXT, type Pump_type);