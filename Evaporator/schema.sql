/* (Beta) Export of data model Evaporator of the subject dataModel.S4BLDG for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Evaporator_type AS ENUM ('Evaporator');
CREATE TABLE Evaporator (address json, alternateName text, areaServed text, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, evaporationCoolant text, evaporationMediumType text, externalSurfaceArea text, hasManufacturer text, hasModel text, id text, internalRefrigerantVolume text, internalSurfaceArea text, internalWaterVolume text, isContainedInBuildingSpace json, isContainedInPhysicalObject json, isSubSystemOf json, location json, name text, nominalHeatTransferArea text, nominalHeatTransferCoefficient text, owner json, refrigerantClass text, seeAlso json, source text, type Evaporator_type);