CREATE DATABASE LaLiga;

use LaLiga;


show Tables;

Create Table equipos(
id INT PRIMARY KEY, /* Se usa el id que viene de la API */
nombre VARCHAR(100) NOT NULL,
abreviatura VARCHAR(10),
estadio VARCHAR(100),
fundacion YEAR
);


select * from equipos ;


CREATE TABLE clasificacion(
posicion INT NOT NULL,
equipo_ID INT PRIMARY KEY NOT NULL,
equipo VARCHAR(50) NOT NULL,
puntos INT NOT NULL,
partidos_jugados INT NOT NULL,
goles_favor INT NOT NULL,
goles_contra INT NOT NULL,
diferencia_goles INT NOT NULL
);

select * from clasificacion;

ALTER TABLE jornadas RENAME TO clasificacion;






ALTER TABLE clasificacion
DROP COLUMN id;

ALTER TABLE clasificacion
DROP COLUMN num_jornada;

DROP TABLE clasificacion;


CREATE TABLE partidos(
id INT PRIMARY KEY,
jornada INT,
fecha_hora DATETIME,
equipoLocalID INT,
equipoVisitanteID INT,
golesLocal INT DEFAULT 0,
golesVisitante INT DEFAULT 0,
estado VARCHAR(20),

CONSTRAINT fk_local FOREIGN KEY (equipoLocalID) REFERENCES equipos(id),
CONSTRAINT fk_visitante FOREIGN KEY (equipoVisitanteiD) REFERENCES equipos(id)
);

select * from partidos;

SELECT * FROM equipos;


ALTER TABLE equipos
RENAME COLUMN equipoLocalID to Local

SELECT * FROM equipos;
SELECT COUNT(*) AS EQUIPOS FROM equipos WHERE nombre 


ALTER TABLE equipos
MODIFY COLUMN fundacion INT;

SELECT * FROM jornadas;

CREATE TABLE posiciones(
id INT 


);


show tables;

select * FROM equipos;

select * FROM clasificacion;

select * FROM partidos;




SELECT p.jornada ,
local.abreviatura AS Local ,
p.golesLocal AS GOL_F,
visita.abreviatura AS Visitante,
p.golesVisitante AS GOL_C
FROM partidos p
JOIN equipos local ON p.equipoLocalID = local.id
JOIN equipos visita ON p.equipoVisitanteID = visita.id
WHERE p.jornada BETWEEN 1 and 15
ORDER BY p.jornada;


SELECT posicion AS POS ,
equipo AS EQUIPO,
puntos AS PTOS,
partidos_jugados AS JUEGOS ,
goles_favor AS GOL_F ,
goles_contra AS GOL_C ,
diferencia_goles AS GOL_DIF
FROM clasificacion 
ORDER BY posicion;

select * FROM partidos;



