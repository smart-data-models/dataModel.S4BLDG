/* (Beta) Export of data model Chiller of the subject dataModel.S4BLDG for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Chiller_type AS ENUM ('Chiller');
CREATE TABLE Chiller (address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, hasManufacturer TEXT, hasModel TEXT, isSubSystemOf JSON, name TEXT, nominalCapacity NUMERIC, nominalCondensingTemperature NUMERIC, nominalEfficiency NUMERIC, nominalEvaporatingTemmperature NUMERIC, nominalHeatRejectionRate NUMERIC, nominalPowerConsumption NUMERIC, owner JSON, source TEXT, type Chiller_type);