from connect import *

phones = """
CREATE TABLE IF NOT EXISTS phones (
	id INT NOT NULL AUTO_INCREMENT,
	PRIMARY KEY(id)
);
"""

pictures = """
CREATE TABLE IF NOT EXISTS pictures (
	id INT NOT NULL AUTO_INCREMENT,
	position POINT NOT NULL,
	bearing DECIMAL,
	focus DECIMAL,
    visited BOOL,
	SPATIAL INDEX(position),
	PRIMARY KEY(id)
) ENGINE = MyISAM;
"""

landmarks = """
CREATE TABLE IF NOT EXISTS landmarks (
	id INT NOT NULL AUTO_INCREMENT,
	position POINT NOT NULL,
    centCnt INT NOT NULL,
    sumLat DOUBLE,
    sumLon DOUBLE,
	SPATIAL INDEX(position),
	PRIMARY KEY(id)
) ENGINE = MyISAM;
"""

execute(phones)
execute(pictures)
execute(landmarks)
