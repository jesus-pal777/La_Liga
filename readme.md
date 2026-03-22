# La Liga - Pipeline de Datos (ETL)

Este proyecto desarrolla un pipeline de datos automatizado el cual extrae, 
processa y almacena información de la Primera División Española, mediante la conexión
de una API externa con una base de datos relacional.

## Descripción del proyecto
El objetivo del proyecto es automatizar la obtención de información básica de La Liga
(equipos, clasificación, y partidos) mediante una API esto con la finalidad de eliminar
procesos manuales o web scrapping complejo.


## Tecnologías utilizadas
* **Lenguaje:** Python 3.
* **Base de datos:** MySQL
* **Fuente de datos:** [football-data.org](https://www.football-data.org/) (API REST)
* **Librerias principales:** 
	* request Para el consumo de la API
	* mysql-connector-python Para la persistencia de datos

## Arquitectura de los datos
El esquema diseñado para el proyecto fue creado bajo el principio de integirdad referencial
el cual facilita el análisis con identificadores únicos.
* **Equipos:** Información principal (estadios, fundación, nombre)
* **Partidos:** Registro de cada jornada, reultados y estado del partido
* **Clasificación:** Tabla de posiciones con puntos, partidos jugados, goles


## Lógica del proceso 
1. Extracción. Se hace petición GET a la API para obtener objetos JSON
2. Transformación: Procesamiento de datos con Python, se limpian cadenas String y se hace
el calculo de diferencia de goles
3. Cargar de datos: Se usa comando "ON DUPLICATE KEY UPDATE" en sql para mantener la bd
actualizada sin tener duplicidad de datos.


## Estructura 
* Clasificación.py Procesa la tabla de posiciones
* Partidos.py Gestiona los resultados de las jornadas
* DB_LaLiga.py Conexión a la BD
* ProyectoLiga.sql Script con la creación de tablas y constraints
