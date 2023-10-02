/* (Beta) Export of data model ElectricTimeControl of the subject dataModel.S4BLDG for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE ElectricTimeControl_type AS ENUM ('ElectricTimeControl');
CREATE TABLE ElectricTimeControl (address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, hasManufacturer TEXT, hasModel TEXT, isSubSystemOf JSON, name TEXT, owner JSON, source TEXT, type ElectricTimeControl_type);