import requests
import mysql.connector
from datetime import datetime

API_KEY = 'TU_API_KEY'
UrlLiga = 'https://api.football-data.org/v4/competitions/PD/standings'
HEADERS= {'X-AUth-Token':API_KEY}



db = mysql.connector.connect(
    host="NOMBRE_HOST",
    user="USUARIO",
    password="TU_PASS",
    database="TU_BD"
)
cursor = db.cursor()


response = requests.get(UrlLiga, headers=HEADERS)
data = response.json()


if 'matches' in data:
    lista_partidos = data['matches']
    print(f"Se tuvieron {len(lista_partidos)} partidos")

    for partido in lista_partidos:
        id = partido['id']
        jornada = partido['matchday']
        fecha_hora = partido['utcDate']
        equipo_local = partido['homeTeam']['id']
        equipo_visit = partido ['awayTeam']['id']
        goles_local = partido ['score']['fullTime']['home']
        goles_visit = partido ['score']['fullTime']['away']
        estado = partido ['status']
        
        formato_entrada = "%Y-%m-%dT%H:%M:%SZ"

        fecha_hora2 = datetime.strptime(fecha_hora,formato_entrada)

        
        sql = """
        INSERT INTO partidos(id, jornada, fecha_hora, equipoLocalID, equipoVisitanteID, golesLocal, golesVisitante, estado)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
        ON DUPLICATE KEY UPDATE
        fecha_hora=%s, golesLocal=%s,golesVisitante=%s, estado=%s 
        """

        val=(
            id , jornada , fecha_hora2, equipo_local, equipo_visit, goles_local, goles_visit,estado,


            fecha_hora2, goles_local, goles_visit,estado
        )
        
        cursor.execute(sql, val)
        print(f"Jornada procesada {jornada}")


    db.commit()
    print("La tabla de jornada fue actualizada")
else:
    print("Error al cargar la tbla de jornada", data)


cursor.close()
db.close()