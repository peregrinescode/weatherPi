import bme280_sensor
import mysql.connector as database
from time import sleep

connection = database.connect(
    user='pi',
    password='12345678',
    host='localhost',
    database='weather')

cursor = connection.cursor()

def add_data(ambient_temp, air_quality, pressure, humidity):
    try:
        statement = "INSERT INTO WEATHER_MEASUREMENT (AMBIENT_TEMPERATURE, AIR_QUALITY, AIR_PRESSURE, HUMIDITY) VALUES (%s, %s, %s, %s)"
        data = (ambient_temp, air_quality, pressure, humidity)
        cursor.execute(statement, data)
        connection.commit()
        print("Successfully added entry to database")
    except database.Error as e:
        print(f"Error adding entry to database: {e}")

#def get_data():
#    try:
#      statement = "SELECT first_name, last_name FROM employees WHERE last_name=%s"
#      data = (last_name,)
#      cursor.execute(statement, data)
#      for (first_name, last_name) in cursor:
#        print(f"Successfully retrieved {first_name}, {last_name}")
#    except database.Error as e:
#      print(f"Error retrieving entry from database: {e}")

while True:
    humidity, pressure, ambient_temp = bme280_sensor.read_all()
    add_data(ambient_temp, "0", pressure, humidity)
    sleep(5)

connection.close()
