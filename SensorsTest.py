import Adafruit_DHT
from gpiozero import CPUTemperature
import time
import time
import board
import digitalio
pir_sensor = digitalio.DigitalInOut(board.D24)
pir_sensor.direction = digitalio.Direction.INPUT
door_sensor = digitalio.DigitalInOut(board.D22)
door_sensor.direction = digitalio.Direction.INPUT
door_sensor.pull = digitalio.Pull.UP
window_sensor = digitalio.DigitalInOut(board.D27)
window_sensor.direction = digitalio.Direction.INPUT
window_sensor.pull = digitalio.Pull.UP
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 23
while True:
 if pir_sensor.value:
  print("Movement!")
 if door_sensor.value:
  print("Door Open!")
 if window_sensor.value:
  print("Window Open!")
 time.sleep(0.5)
 cpu = CPUTemperature()
 temperature,humidity = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
 if humidity is not None and temperature is not None and cpu is not None:
  print("Temp = {0:0.1f}*C  Humidity = {1:0.1f}%".format(temperature, humidity))
  print("CPU Temperature:" , cpu.temperature)
 else:
  print("Failed to retrieve data...?")
