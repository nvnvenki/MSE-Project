'''
ID:
User screen name:
Text:
Created on:
Retweet Count:
Original tweeter: True/False

'''

class Tweet():
	def __init__(self, tweet):
		self.id = tweet.id
		self.user_screen_name = tweet.user.screen_name
		self.text = tweet.text
		self.created_at = tweet.created_at
		self.retweet_count = tweet.retweet_count
		self.original_tweeter = False if hasattr(tweet,"retweeted_status") else True

	def __repr__(self):
		obj = {
			"id" : self.id,
			"user_screen_name" : self.user_screen_name,
			"text" : self.text,
			"created_at" : self.created_at,
			"retweet_count" : self.retweet_count,
			"original_tweeter" : self.original_tweeter
		}
		# return "Tweet id: "+str(self.id)+"\nUser screen name: "+self.user_screen_name+"\nText: "+self.text+"\nCreated on: "+str(self.created_at)+"\nRetweet count: "+str(self.retweet_count)+"\nOriginal tweeter: "+str(self.original_tweeter)+"\n"
		return str(obj)

	def getTweetDict(self):
		obj = {
			"id" : self.id,
			"user_screen_name" : self.user_screen_name,
			"text" : self.text,
			"created_at" : self.created_at,
			"retweet_count" : self.retweet_count,
			"original_tweeter" : self.original_tweeter
		}
		return obj


if __name__ == '__main__':
	pass
		