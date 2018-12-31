import conf, json, time
from boltiot import Sms, Bolt

minimum_val = 300
maximum_val = 600

mybolt= Bolt(conf.API_KEY, conf.DEVICE_ID)

sms = Sms(conf.SSID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)

while True:
    response = mybolt.analogRead('A0')
    data = json.loads(response)
    print("complete data ", data)
    print("data_val ", data['value'])
    try:
        sensor_value = int(data['value'])
        print(" sensor_val ", sensor_value)
        if sensor_value > maximum_val or sensor_value < minimum_val:
            response = sms.send_sms(" The current temp val is " +str(sensor_value))
    except Exception as e:
        print("Error", e)
    minimum_val = minimum_val -100
    time.sleep(10)
