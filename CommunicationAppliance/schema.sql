/* (Beta) Export of data model CommunicationAppliance of the subject dataModel.S4BLDG for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE CommunicationAppliance_type AS ENUM ('CommunicationAppliance');
CREATE TABLE CommunicationAppliance (address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, hasManufacturer TEXT, hasModel TEXT, isSubSystemOf JSON, name TEXT, owner JSON, source TEXT, type CommunicationAppliance_type);