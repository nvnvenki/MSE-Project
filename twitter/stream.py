from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key = "Nz0tGTqqLSJQUUkgaqwLQ"
consumer_secret = "lXlDQR2UhC0ExKPmNqcFLDnoOmYQHlkrnFX97wQk94"
access_token = "267742324-nPHpJWp5GfujTpPc9okNi6z3lVbvgGj0xb6cfybh"
access_token_secret = "AEaMLCBOoyBq4ZPIK2ri8qwWBevbwsDTs6ioXzTJlIoL6"

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
This is a basic listener that just prints received tweets to stdout.

"""
    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['cricket'])
