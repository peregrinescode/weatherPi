import sds011
import bme280_sensor
import mysql.connector as database
from time import sleep

connection = database.connect(
    user='pi',
    password='12345678',
    host='localhost',
    database='weather')

cursor = connection.cursor()

def add_data(ambient_temp, air_quality_pm2, air_quality_pm10, pressure, humidity):
    try:
        statement = "INSERT INTO WEATHER_MEASUREMENT (AMBIENT_TEMPERATURE, AIR_QUALITY_PM2, AIR_QUALITY_PM10, AIR_PRESSURE, HUMIDITY) VALUES (%s, %s, %s, %s, %s)"
        data = (ambient_temp, air_quality_pm2, air_quality_pm10, pressure, humidity)
        cursor.execute(statement, data)
        connection.commit()
        # print("Successfully added entry to database")
    except database.Error as e:
        # print(f"Error adding entry to database: {e}")
        pass

#def get_data():
#    try:
#      statement = "SELECT first_name, last_name FROM employees WHERE last_name=%s"
#      data = (last_name,)
#      cursor.execute(statement, data)
#      for (first_name, last_name) in cursor:
#        print(f"Successfully retrieved {first_name}, {last_name}")
#    except database.Error as e:
#      print(f"Error retrieving entry from database: {e}")

# Read SDS011 sensor
sds011.cmd_set_sleep(0)		# turn on sensor
sleep(15)			# give it 10 seconds to power on
values = sds011.cmd_query_data()
sds011.cmd_set_sleep(1)


# Read BME280 sensor
humidity, pressure, ambient_temp = bme280_sensor.read_all()

# Print data
# print("Humidity: ", humidity, ", Pressure: ", pressure, ", Temp: ", ambient_temp, ", PM2.5: ", values[0], ", PM10: ", values[1])

# Save data to DB
add_data(ambient_temp, values[0], values[1], pressure, humidity)

connection.close()
