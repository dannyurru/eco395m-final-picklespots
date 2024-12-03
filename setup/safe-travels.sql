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
    "Temp" FLOAT(5, 2),
    "CityId" INT NOT NULL,
    CONSTRAINT "PK_Temperature" PRIMARY KEY ("DataId")
);