import tweepy
import time
import secret
import random

consumer_key = secret.consumer_key
consumer_secret = secret.consumer_secret
access_token = secret.access_token
access_token_secret = secret.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


user = api.me()
print(user.name)
starttime = time.time()

while True:
    rand_num = random.randint(1, 48)
    api.update_with_media('Images/raccoon' + str(rand_num) + '.jpg')
    time.sleep(3600.0 - ((time.time() - starttime) % 3600.0))