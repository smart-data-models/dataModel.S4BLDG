/* (Beta) Export of data model VibrationIsolator of the subject dataModel.S4BLDG for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE VibrationIsolator_type AS ENUM ('VibrationIsolator');
CREATE TABLE VibrationIsolator (address json, alternateName text, areaServed text, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, hasManufacturer text, hasModel text, height text, id text, isContainedInBuildingSpace json, isContainedInPhysicalObject json, isSubSystemOf json, isolatorCompressibility text, isolatorStaticDeflection text, location json, name text, owner json, seeAlso json, source text, supportedWeightMax text, type VibrationIsolator_type, vibrationTransmissibility text);