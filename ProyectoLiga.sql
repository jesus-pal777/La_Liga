CREATE DATABASE IF NOT EXISTS LaLiga;
USE LaLiga;

-- 1. Tabla de Equipos
CREATE TABLE equipos (
    id INT PRIMARY KEY, -- ID proveniente de la API 
    nombre VARCHAR(100) NOT NULL,
    abreviatura VARCHAR(10),
    estadio VARCHAR(100),
    fundacion INT
);

-- 2. Tabla de Clasificación 
CREATE TABLE clasificacion (
    posicion INT NOT NULL,
    equipo_ID INT PRIMARY KEY NOT NULL,
    equipo VARCHAR(50) NOT NULL,
    puntos INT NOT NULL,
    partidos_jugados INT NOT NULL,
    goles_favor INT NOT NULL,
    goles_contra INT NOT NULL,
    diferencia_goles INT NOT NULL
);

-- 3. Tabla de Partidos 
CREATE TABLE partidos (
    id INT PRIMARY KEY,
    jornada INT,
    fecha_hora DATETIME,
    equipoLocalID INT,
    equipoVisitanteID INT,
    golesLocal INT DEFAULT 0,
    golesVisitante INT DEFAULT 0,
    estado VARCHAR(20),
    
    -- Espeicifcamos que la llave foranea fk_local se llamara equipoLocalID y hará referencia de
    -- equipos ID, el mismo caso para equipoVisitante
    CONSTRAINT fk_local FOREIGN KEY (equipoLocalID) REFERENCES equipos(id),
    CONSTRAINT fk_visitante FOREIGN KEY (equipoVisitanteID) REFERENCES equipos(id)
);




