#CREATE DATABASE UpcomingData;
USE UpcomingData; 
CREATE TABLE info (

	data LONGTEXT NOT NULL,
	hash VARCHAR(40) NOT NULL,
	PRIMARY KEY (hash)

);


