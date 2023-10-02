/* (Beta) Export of data model Interceptor of the subject dataModel.S4BLDG for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Interceptor_type AS ENUM ('Interceptor');
CREATE TABLE Interceptor (address JSON, alternateName TEXT, areaServed TEXT, coverLength NUMERIC, coverWidth NUMERIC, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, hasManufacturer TEXT, hasModel TEXT, inletConnectionSize NUMERIC, isSubSystemOf JSON, name TEXT, nominalBodyDepth NUMERIC, nominalBodyLength NUMERIC, nominalBodyWidth NUMERIC, outletConnectionSize NUMERIC, owner JSON, source TEXT, type Interceptor_type, ventilatingPipeSize NUMERIC);