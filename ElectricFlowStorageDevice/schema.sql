/* (Beta) Export of data model ElectricFlowStorageDevice of the subject dataModel.S4BLDG for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE ElectricFlowStorageDevice_type AS ENUM ('ElectricFlowStorageDevice');
CREATE TABLE ElectricFlowStorageDevice (address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, hasManufacturer TEXT, hasModel TEXT, isSubSystemOf JSON, name TEXT, nominalFrequency NUMERIC, nominalSupplyVoltage NUMERIC, nominalSupplyVoltageMin NUMERIC, owner JSON, source TEXT, type ElectricFlowStorageDevice_type);