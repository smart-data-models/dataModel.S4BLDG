/* (Beta) Export of data model Tank of the subject dataModel.S4BLDG for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Tank_type AS ENUM ('Tank');
CREATE TABLE Tank (accessType text, address json, alternateName text, areaServed text, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, effectiveCapacity text, endShapeType text, firstCurvatureRadius text, hasManufacturer text, hasModel text, id text, isContainedInBuildingSpace json, isContainedInPhysicalObject json, isSubSystemOf json, location json, name text, nominalDepth text, nominalLengthOrDiameter text, nominalVolumetricCapacity text, nominalWidthOrDiameter text, numberOfSections text, operatingWeight text, owner json, patternType text, secondCurvatureRadius text, seeAlso json, source text, storageType text, type Tank_type);