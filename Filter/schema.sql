/* (Beta) Export of data model Filter of the subject dataModel.S4BLDG for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Filter_type AS ENUM ('Filter');
CREATE TABLE Filter (address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, finalResistance NUMERIC, fluidFlowRateMax NUMERIC, fluidFlowRateMin NUMERIC, hasManufacturer TEXT, hasModel TEXT, initialResistance NUMERIC, isSubSystemOf JSON, name TEXT, nominalFilterFaceVelocity NUMERIC, nominalFlowRate NUMERIC, nominalMediaSurfaceVelocity NUMERIC, nominalParticleGeometricMeanDiameter NUMERIC, nominalParticleGeometricStandardDeviation NUMERIC, nominalPressureDrop NUMERIC, operationTemperatureMax NUMERIC, operationTemperatureMin NUMERIC, owner JSON, source TEXT, type Filter_type, weight NUMERIC);