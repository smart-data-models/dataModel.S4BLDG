/* (Beta) Export of data model AudioVisualAppliance of the subject dataModel.S4BLDG for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE AudioVisualAppliance_type AS ENUM ('AudioVisualAppliance');
CREATE TABLE AudioVisualAppliance (address JSON, alternateName TEXT, areaServed TEXT, audioVolume NUMERIC, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, hasManufacturer TEXT, hasModel TEXT, isSubSystemOf JSON, mediaSource TEXT, name TEXT, owner JSON, source TEXT, type AudioVisualAppliance_type);