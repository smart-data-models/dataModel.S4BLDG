/* (Beta) Export of data model BuildingSpace of the subject dataModel.S4BLDG for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE buildingSpaceKind_type AS ENUM ('BuildingElementProxy','BuildingStorey','Column','Covering','CurtainWall','Door','OpeningElement','Plate','Railing','Roof','Site','Slab','Space','Stair','StairFlight','Storey','Wall','WallStandardCase','Window');CREATE TYPE BuildingSpace_type AS ENUM ('BuildingSpace');
CREATE TABLE BuildingSpace (address JSON, airVolume NUMERIC, alternateName TEXT, areaServed TEXT, bounds JSON, buildingSpaceKind buildingSpaceKind_type, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, name TEXT, owner JSON, source TEXT, type BuildingSpace_type);