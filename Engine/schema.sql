/* (Beta) Export of data model Engine of the subject dataModel.S4BLDG for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Engine_type AS ENUM ('Engine');
CREATE TABLE Engine (address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, energySource TEXT, hasManufacturer TEXT, hasModel TEXT, id TEXT PRIMARY KEY, isSubSystemOf JSON, location JSON, name TEXT, owner JSON, seeAlso JSON, source TEXT, type Engine_type);