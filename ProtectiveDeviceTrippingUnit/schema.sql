/* (Beta) Export of data model ProtectiveDeviceTrippingUnit of the subject dataModel.S4BLDG for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE ProtectiveDeviceTrippingUnit_type AS ENUM ('ProtectiveDeviceTrippingUnit');
CREATE TABLE ProtectiveDeviceTrippingUnit (address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, hasManufacturer TEXT, hasModel TEXT, isSubSystemOf JSON, limitingTerminalSize NUMERIC, name TEXT, owner JSON, source TEXT, standard TEXT, type ProtectiveDeviceTrippingUnit_type);