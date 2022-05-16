# RPiSensorLogger
Repo for BME280/DHT22 sensors on RaspbeeyPi 4/400

## Requirements
Supported Sensors:
- [BME280](https://www.amazon.com/Barometric-Pressure-Atmospheric-Temperature-Navigation/dp/B09NPSNKHL/ref=sr_1_1_sspa?crid=1SGYFYXPALE8S&keywords=bme280&qid=1652660050&sprefix=bme280%2Caps%2C121&sr=8-1-spons&psc=1&smid=A39EXQOYLJ6M4Z&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFWSlhCRVBGRTdXQzMmZW5jcnlwdGVkSWQ9QTA2MDY1NTQyVVFDUlRDMlhLVUlZJmVuY3J5cHRlZEFkSWQ9QTAzOTU3NDAzN0pHMkE1Vk1WRENLJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==)
- [DHT22](https://www.amazon.com/Digital-Temperature-Humidity-Arduino-Replace/dp/B07XBVR532/ref=sr_1_1_sspa?keywords=dht22&qid=1652660255&sprefix=DHT%2Caps%2C129&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzM1pQRzdJREJFQkNWJmVuY3J5cHRlZElkPUEwNjM1NDUxMzJHNVQ0VElKMklZWCZlbmNyeXB0ZWRBZElkPUEwMDY2OTI3RDdEMkhSMEhJM1UxJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==)

Dependencies:
- libgpiod2
- RPi.bme280
- adafruit-circuitpython-dht

You can install dependencies by run setup.hs on RPis.


## Sensor RaspberryPi GPIO Connection
### BME280
- SCL -> I2C SCL
- SDA -> I2C SDA
### DHT22
- DATA -> GPIO4

Both sensors run through 3.3v. Additionally, DHT22 is connected with a 2K resistor (10K recommended).

## Usage

Start logging with command:
- python3 sensor.py [fequency]

where [fequency] is the time between each measurments.


## Log Format

Onec the logging starts, you can find a SensorLog.csv Under the same directory.<br>
Columns from left to right are:<br>
SystemTimestamp---BME280_Temperature---DHT22_Temperature---DHT22_Humidity---BME280_Pressure



   
