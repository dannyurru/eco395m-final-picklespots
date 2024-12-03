/*******************************************************************************
   Create Tables
********************************************************************************/

CREATE TABLE "City"
(
    "CityId" INT NOT NULL,
    "Name" VARCHAR(160) NOT NULL,
    "State" VARCHAR(160) NOT NULL,
    CONSTRAINT "PK_City" PRIMARY KEY  ("CityId")
);

CREATE TABLE "Temperature"
(
    "DataId" INT NOT NULL,
    "Date" TIMESTAMP,
    "Temp" FLOAT,
    "CityId" INT NOT NULL,
    CONSTRAINT "PK_Temperature" PRIMARY KEY ("DataId")
);

/*******************************************************************************
   Create Foreign Keys
********************************************************************************/
ALTER TABLE "Temperature" ADD CONSTRAINT "FK_TemperatureCityId"
    FOREIGN KEY ("CityId") REFERENCES "City" ("CityId") ON DELETE NO ACTION ON UPDATE NO ACTION;