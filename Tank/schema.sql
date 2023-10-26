/* (Beta) Export of data model Tank of the subject dataModel.S4BLDG for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Tank_type AS ENUM ('Tank');
CREATE TABLE Tank (accessType TEXT, address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, effectiveCapacity NUMERIC, endShapeType TEXT, firstCurvatureRadius NUMERIC, hasManufacturer TEXT, hasModel TEXT, id TEXT PRIMARY KEY, isSubSystemOf JSON, location JSON, name TEXT, nominalDepth NUMERIC, nominalLengthOrDiameter NUMERIC, nominalVolumetricCapacity NUMERIC, nominalWidthOrDiameter NUMERIC, numberOfSections NUMERIC, operatingWeight NUMERIC, owner JSON, patternType TEXT, secondCurvatureRadius NUMERIC, seeAlso JSON, source TEXT, storageType TEXT, type Tank_type);