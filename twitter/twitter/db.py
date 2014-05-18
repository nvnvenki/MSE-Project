import pymongo
import tweepy
from user import User
import ast
import json

since_ids = {
	'ibnlive' : 411043660000555008L,
	'timesnow' : 410293389746122752L,
	'HeadlinesToday' : 407514371250610176L,
	"ndtv" : 411416094461546496L
}

def updateDb():
	user_names = ['ibnlive','timesnow','HeadlinesToday','ndtv']
	connection = pymongo.MongoClient("localhost", 27017)
	
	# create a database if not exists
	db = connection.twitter

	# crate collections for users
	# users = db.users
	users = db.users_new
	
	auth = tweepy.OAuthHandler("oURSVON6rRvw7gi3aCMNYg","lFzae5HXsGwhyqxdbKtYStzPy0IRI7oEAIoXbvDiRDI")
	auth.set_access_token("2243361606-6WHyclCNIuj2uAq6cJKZtScNI2XGDxCWANSlX64","lIDvQ8pTaJLDDyBIXWzwOAxwA0QXn9moFL6QUp7v1RytL")
	api = tweepy.API(auth)
	try:
		data_list = []
		for user_name in user_names:
			user = User(user_name,api,since_ids[user_name])
			user.update(api)
			data_list.append({'user_name': user_name,'data' : user.getUserDict()})

		users.insert(data_list)
	except:
		print "some kirick"


def getTweetsOfEachDay(tweets):

	retweet_count_dict = {}
	for tweet in tweets:
		
		if retweet_count_dict.has_key(str(tweet['created_at'].date())):
			if tweet['original_tweeter']:
				retweet_count_dict[str(tweet['created_at'].date())] = retweet_count_dict[str(tweet['created_at'].date())] + tweet['retweet_count']
		else:
			if tweet['original_tweeter']:
				retweet_count_dict[str(tweet['created_at'].date())] = 0


	return retweet_count_dict


def getDataForPlotting():
	
	connection = pymongo.MongoClient("localhost", 27017)
	db = connection.twitter
	cursor = db.users_new.find()
	
	data = []
	
	for eachObject in cursor:
		temp_dict = {}
		temp_dict['name'] = eachObject['data']['screen_name']
		retweet_count_dict = getTweetsOfEachDay(eachObject['data']['tweets'])
		temp_dict['data'] = { "retweet_count": eachObject['data']['retweet_count'] , "followers_count" :eachObject['data']['followers_count'],"tweet_count":eachObject['data']['tweet_count'] , "tweets_per_day": retweet_count_dict.values(), "dates" : retweet_count_dict.keys()}
		data.append(temp_dict)
	max_index = 0
	for i in range(len(data)):
		if len(data[i]['data']['tweets_per_day']) > len(data[max_index]['data']['tweets_per_day']):
			max_index = i

	for i in range(len(data)):
		if i != max_index:
			data[i]['data'].pop('dates')
			data[i]['dates'] = data[max_index]['data']['dates']
			data[i]['data']['tweets_per_day'].extend([0 for i in range(len(data[max_index]['data']['tweets_per_day']) - len(data[i]['data']['tweets_per_day']))])	
	
	return data

if __name__ == '__main__':
	# updateDb()
	print getDataForPlotting()
	