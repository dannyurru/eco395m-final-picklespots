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

CREATE TABLE "Coordinates"
(
    "CityId" INT NOT NULL,
    "City" VARCHAR(160) NOT NULL,
    "Latitude" FLOAT,
    "Longitude" FLOAT,
    CONSTRAINT "PK_Coordinates" PRIMARY KEY ("CityId")
);

CREATE TABLE "Courts"
(
    "CourtId" INT NOT NULL,
    "Name" VARCHAR(160) NOT NULL,
    "CityId" INT NOT NULL,
    "NumberOfCourts" INT NOT NULL,
    "Lines" VARCHAR NOT NULL,
    "Nets" VARCHAR(160) NOT NULL,
    CONSTRAINT "PK_Courts" PRIMARY KEY ("CourtId")
);

/*******************************************************************************
   Create Foreign Keys
********************************************************************************/
ALTER TABLE "Coordinates" ADD CONSTRAINT "FK_coordinatesCityId"
    FOREIGN KEY ("CityId") REFERENCES "City" ("CityId") ON DELETE NO ACTION ON UPDATE NO ACTION;