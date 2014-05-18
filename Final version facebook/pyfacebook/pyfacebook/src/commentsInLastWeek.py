import pymongo
import ast
import json
import datetime

def getData():
	# finding comments per day in last week for all programs in the channel
	# returns a list of dictionary in following format
	# [
	# 	{
	# 		"page_name": "come_serial_name",
	# 		"data": {
	# 			"day" : count,
	# 			...
	# 		}
	# 	},
	# 	...
	# ]

	# connect to the database
	connection = pymongo.MongoClient("localhost", 27017)
	db = connection.pyfacebook

	today = datetime.datetime.today()

	result_list = []

	# query page collection
	page_cursor = db.pages.find({ }, {"_id": 1, "username": 1})

	for res in page_cursor:
		res_ = ast.literal_eval(json.dumps(res))

		partial_dict = {}

		partial_dict["name"]  = res_["username"]
		partial_dict["data"] = []
		
		for i in range(7, 0, -1):
			partial_dict["data"].append(db.comments.find({"created_time" : {"$gte" : datetime.datetime(today.year, today.month, today.day - i), 
			"$lt": datetime.datetime(today.year, today.month, today.day - (i - 1))}, "path": {"$regex": res_["_id"]}}).count())

		result_list.append(partial_dict)

	return result_list
if __name__ == '__main__':
	print getData()