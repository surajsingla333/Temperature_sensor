# Temperature_sensor

The project is about monitoring temperature change of the surrounding. 

The temperature_monitoring devices use a linear monolithic-35(LM35) which is an IC with 3 pins sensor, output and ground.
LM35 will keep a track of the temprature of the surrounding.

The device is build so that if the temperature crosses a certain minimum or maximum threshold, then it will send an alert to the user via SMS or Email or a tweet whichever is used in the system.

These type of devices are very useful in pharmaceuticals factories where a strict monitoring of temperature is required.

Devices used :
Bolt IoT module,
LM35

Software: 
Python3,
Twilio(for SMS sending),
MailGun(for Email sending),
Tweepy(a twitter API for sending tweets)

File Description:
conf.py  email_conf.py  temp_email.py  temp_sms.py  tweet_conf.py  tweet_temp.py
"conf.py" has the configuration details for the device and twilio api.
"temp_sms.py" has the code to do the task and SMS sending.
"email_conf.py" has the configuration details for the device and mailgun api.
"temp_email.py" has the code to do the task and Email sending.
"tweet_conf.py" has the configuration details for the device and tweepy api.
"tweet_temp.py" has the code to do the task and sending tweets.
