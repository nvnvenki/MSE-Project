import tweepy
from tweet import Tweet
'''
Name:
Screen name:
Retweet count:
Tweets : list of your tweets which are all objects of Tweet class
Tweet count: 
Followers count:
Since id: dont worry about this much

'''
class User():
	"""docstring for User"""
	def __init__(self, screen_name,api,since_id):
		self.screen_name = screen_name
		self.name = api.get_user(screen_name).name
		self.tweets = list()	# does not contain all the tweets of the user bcoz there is a limit to the number
								# of tweets that can be retrieved through the api
		self.retweet_count = 0	# this is the count of the number of tweets of this user that have been retweeted by others
		self.followers_count = 0
		self.tweet_count = 0	# the number of tweets archived in this object i.e in "tweets" list
		self.since_id = since_id

	def __repr__(self):
		obj = {
			"screen_name" : self.screen_name,
			"name" : self.name,
			"tweets" : [tweet for tweet in self.tweets],
			"retweet_count" : self.retweet_count,
			"followers_count" : self.followers_count,
			"tweet_count" : self.tweet_count,
			"since_id" : self.since_id
		}
		# return "User name: "+self.name+"\n"+"Screen name: "+self.screen_name+"\n"+"Followers: "+str(self.followers_count)+"\n"+"Tweets: "+str(self.tweet_count)+"\n"+"Retweets count: "+str(self.retweet_count)+"\n"
		return str(obj)
	
	def getUserDict(self):
		obj = {
			"screen_name" : self.screen_name,
			"name" : self.name,
			"tweets" : [tweet.getTweetDict() for tweet in self.tweets],
			"retweet_count" : self.retweet_count,
			"followers_count" : self.followers_count,
			"tweet_count" : self.tweet_count,
			"since_id" : self.since_id
		}
		return obj



	def update(self,api):
		twitter_user_object = api.get_user(self.screen_name) # a temporary object
		timeline = twitter_user_object.timeline(since_id=self.since_id,count=200,include_rts=1) # a temporary object
		timeline.reverse()
		
		for each_tweet in timeline:
			tweet = Tweet(each_tweet) 
			self.tweets.insert(0,tweet)

			if tweet.original_tweeter==True:
				self.retweet_count = self.retweet_count + tweet.retweet_count
			
			self.tweet_count = self.tweet_count+1
			
		self.followers_count = int(twitter_user_object.followers_count)
		self.since_id = self.tweets[0].id
 	 
if __name__ == '__main__':
	auth = tweepy.OAuthHandler("oURSVON6rRvw7gi3aCMNYg","lFzae5HXsGwhyqxdbKtYStzPy0IRI7oEAIoXbvDiRDI")
	auth.set_access_token("2243361606-6WHyclCNIuj2uAq6cJKZtScNI2XGDxCWANSlX64","lIDvQ8pTaJLDDyBIXWzwOAxwA0QXn9moFL6QUp7v1RytL")
	api = tweepy.API(auth)
	
	
	# abhi = User("kashyap2292",api,385409948256960512L)
	# abhi.update(api)
	# for everytweet in abhi.tweets:
	# 	try:
	# 		print everytweet.text
	# 		print everytweet.retweet_count
	# 		print "\n"

	# 	except Exception, e:
	# 		pass
		
	# print "total retweet count" + str(abhi.retweet_count)

	

	# venki = User("nvnvenki",api,382135610024005632L)
	# venki.update(api)

	# for everytweet in venki.tweets:
	# 	print everytweet
	# 	break

	# print venki
	channel = User("ibnlive",api,382135610024005632L)
	channel.update(api)

	print channel

	

		