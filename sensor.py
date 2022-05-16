
import sys
import time

#BME280
import smbus2
import bme280

#DHT
import board
import adafruit_dht



def collect(file,fequency):
    #file I/O
    f =open(file,'w')
    f.write('time,temp_bme,temp_dht,humidity,pressure\n')
    print("Collecting")
    
    #BME
    port = 1
    address = 0x76
    bus = smbus2.SMBus(port)
    calibration_params = bme280.load_calibration_params(bus,address)
    
    #DHT
    dhtDevice = adafruit_dht.DHT22(board.D4)
    
    while True:
        try:
            bme_data = bme280.sample(bus,address,calibration_params)
            
            entry_time = time.time()
            temperature_c_bme = bme_data.temperature
            temperature_c_dht = dhtDevice.temperature
            humidity = dhtDevice.humidity
            pressure = bme_data.pressure

        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])
            time.sleep(2.0)
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error
        
        info = '{},{},{},{},{}\n'.format(entry_time,temperature_c_bme,temperature_c_dht,humidity,pressure)
        print(info)
        f.write(info)
        f.flush()
        

        time.sleep(fequency)



if __name__ == '__main__':
    #parse argument
    fequency = int(sys.argv[1])
    
    collect("SensorLog.csv",fequency)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    