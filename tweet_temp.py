import tweepy, tweet_conf, json, time
from boltiot import Bolt

config = {
    "consumer_key": tweet_conf.consumer_key,
    "consumer_secret": tweet_conf.consumer_secret_key,
    "access_token": tweet_conf.access_token,
    "access_token_secret": tweet_conf.access_secret_token
}

def get_api_object(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)


mybolt = Bolt(tweet_conf.bolt_api_key, tweet_conf.device_id)

temp_threshold = 59

while True:
    response = mybolt.analogRead('A0')
    data = json.loads(response)
    print(data['value'])
    try:
        sensor_value = int(data['value'])
        if sensor_value > temp_threshold:
            print("Temperature has crossed the threshold.")
            api_object = get_api_object(config)
            tweet = "Temperature has crossed the threshold."
            status = api_object.update_status(status=tweet)
    except Exception as e:
        print("An error occurred. ",e)
    time.sleep(10)



