import email_conf, json, time
from boltiot import Email, Bolt

minimum_val = 300
maximum_val = 600

mybolt= Bolt(email_conf.API_KEY, email_conf.DEVICE_ID)

mailer = Email(email_conf.MAILGUN_API_KEY, email_conf.SANDBOX_URL, email_conf.SENDER_EMAIL, email_conf.RECIPIENT_EMAIL)

while True:
    response = mybolt.analogRead('A0')
    data = json.loads(response)
    print("complete data ", data)
    print("data_val ", data['value'])
    try:
        sensor_value = int(data['value'])
        print(" sensor_val ", sensor_value)
        print("temp ", (100*sensor_value)/1024)
        if sensor_value > maximum_val or sensor_value < minimum_val:
            response = mailer.send_email("Alert", " The current temp val is " +str(sensor_value/10.24))
    except Exception as e:
        print("Error", e)
    minimum_val = minimum_val -100
    time.sleep(10)


