import requests
import mysql.connector

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



# Consumir la api (Extract)
response = requests.get(UrlLiga, headers=HEADERS)
data = response.json()





if 'standings' in data:
        
        tabla_gral = data['standings'][0]['table']
        
        for fila in tabla_gral:
            posicion = fila['position']
            equipo_id = fila ['team']['id']
            nombre_equipo = fila['team']['name']

            puntos = fila['points']
            partidos_jugados = fila['playedGames']
            goles_favor = fila ['goalsFor']
            goles_contra = fila['goalsAgainst']

            diferencia_goles = goles_favor - goles_contra




            sql = """
            INSERT INTO clasificacion(posicion, equipo_ID, equipo , puntos , partidos_jugados, goles_favor,goles_contra,diferencia_goles)
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
            ON DUPLICATE KEY UPDATE
            posicion=%s, puntos=%s, partidos_jugados=%s,goles_favor=%s,goles_contra=%s,diferencia_goles=%s 
            """

            val=(
                  posicion , equipo_id, nombre_equipo, puntos, partidos_jugados,goles_favor,goles_contra,diferencia_goles,


                  posicion , puntos , partidos_jugados, goles_favor,goles_contra,diferencia_goles 

            )

            cursor.execute(sql, val)
            print(f"Equipo procesado {nombre_equipo} con posición {posicion}")


        db.commit()
        print("La tabla de posiciones fue actualizada")
else:
      print("Error al cargar la tbla de posiciones", data)


cursor.close()
db.close()


