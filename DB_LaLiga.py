import requests
import mysql.connector


# Creamos la congiruación de la ip, le especificamos de donde va a sacar la información 
# para que se llene la base de datos

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


#Transformamos los datos y los cargamos en la base

if 'teams' in data:
        for team in data['teams']:
            team_id = team['id']
            name = team['name']
            short_name = team['tla']
            venue = team['venue']
            founded = team['founded']



            sql = """
            INSERT INTO equipos(id, nombre, abreviatura, estadio,fundacion)
            VALUES(%s,%s,%s,%s,%s)
            ON DUPLICATE KEY UPDATE
            nombre=%s, estadio=%s
            """

            val=(team_id,name,short_name,venue,founded,name,venue)

            cursor.execute(sql, val)
            print(f"Equipo procesado {name}")



        db.commit()
        print("La carga de datos fue correcta")
else:
      print("Error al cargar los datos", data)


cursor.close()
db.close()