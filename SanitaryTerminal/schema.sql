/* (Beta) Export of data model SanitaryTerminal of the subject dataModel.S4BLDG for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE SanitaryTerminal_type AS ENUM ('SanitaryTerminal');
CREATE TABLE SanitaryTerminal (address json, alternateName text, areaServed text, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, hasManufacturer text, hasModel text, id text, isContainedInBuildingSpace json, isContainedInPhysicalObject json, isSubSystemOf json, location json, name text, owner json, seeAlso json, source text, type SanitaryTerminal_type);