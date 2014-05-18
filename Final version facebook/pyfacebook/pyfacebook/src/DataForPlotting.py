import pymongo
import datetime
import ast
import json


def getData():
	connection = pymongo.MongoClient("localhost", 27017)
	db = connection.pyfacebook

	# task is to get the comment count for all the programs in past week
	# approach:
		# query the page collection to get the id's for all the pages

		# use the id's to find the comment count for each pages by using "path" field

	result = []

	# query page collection
	page_cursor = db.pages.find({ }, {"_id": 1, "username": 1})

	# now iterate through the cursor and find all comments belong to particular page
	for res in page_cursor:
		res_ = ast.literal_eval(json.dumps(res))

		partial_list = []

		partial_list.append(res_["username"])
		partial_list.append(db.comments.find({"path": {"$regex": res_["_id"]}}).count())

		result.append(partial_list)

	return result

if __name__ == '__main__':
	print getData()