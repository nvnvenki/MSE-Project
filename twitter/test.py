import tweepy
import json

consumer_key = "Nz0tGTqqLSJQUUkgaqwLQ"
consumer_secret = "lXlDQR2UhC0ExKPmNqcFLDnoOmYQHlkrnFX97wQk94"
access_token = "267742324-nPHpJWp5GfujTpPc9okNi6z3lVbvgGj0xb6cfybh"
access_token_secret = "AEaMLCBOoyBq4ZPIK2ri8qwWBevbwsDTs6ioXzTJlIoL6"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
print api.me().name

user = api.get_user('ibnlive')
# t = user.timeline()
t = user.home_timline()
for each in t:
	print each.text 


