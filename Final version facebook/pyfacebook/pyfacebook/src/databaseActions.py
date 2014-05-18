import pymongo
import Channel
import facebook
import timeit

def main():
	# connect to mongoDB
	connection = pymongo.MongoClient("localhost", 27017)
	
	# create a database if not exists
	db = connection.pyfacebook

	# crate collections for pages, posts, comments
	channels = db.channels

	pages = db.pages

	posts = db.posts

	comments = db.comments

	# create a graph object
	graph = facebook.GraphAPI("680614081950320|4YUxXCWj0TOAkgEADHaksv0lfs0")
    
	channel_list = [
		Channel.Channel(
			"Colors TV",
			{
				"0700" : "Colors.Sanskaar",
				"0730" : "Colors.SasuralSimarKa",
				"0800" : "Colors.BalikaVadhu",
				"0830" : "MadhubalaEIEJ.Colors",
				"1000" : "ComedyNightsWithKapil",
				"1030" : "Colorstv.Bani",
				"1000" : "Colors.Uttaran"
			},
			graph)]

 	print "getting data done!!"

 	try:

	 	for channel in channel_list:
	 		page_list = []
			channel_dict = channel.get_dict_repr()
			channel_dict["_id"] = channel_dict["channel_name"]
			channel_dict["channel_name"] = channel_dict.pop("channel_name")
			channel_dict["path"] = None
			
			# now insert the pages in document to other collection
			for time, page in channel.get_channel_programs_pages():
				post_list = []
				page_dict = page.get_dict_repr()
				page_dict["_id"] = page_dict.pop("id")
				page_dict["path"] = "," + channel_dict["_id"] + ","
				page_dict["parent_id"] = channel_dict["_id"]
				
				#insert document into page list
				page_list.append(page_dict)

				# now insert the posts in this page
				for post in page.get_posts():
					comment_list = []
					post_dict = post.get_dict_repr()
					post_dict["_id"] = post_dict.pop("id")
					post_dict["path"] = "," + channel_dict["_id"] + "," + page_dict["_id"] + ","
					post_dict["parent_id"] = page_dict["_id"]

					# insert document into post list
					post_list.append(post_dict)

					#insert the comments on this post
					for comment in post.get_comments():
						comment_dict = comment.get_dict_repr()
						comment_dict["_id"] = comment_dict.pop("id")
						comment_dict["path"] = "," + channel_dict["_id"] + "," + page_dict["_id"] + "," + post_dict["_id"] + ","
						comment_dict["parent_id"] = post_dict["_id"]

						comment_list.append(comment_dict)

					# insert comments to collection
					if len(comment_list) != 0:
						try:
							comments.insert(comment_list, continue_on_error=True)
						except:
							print "some comment docs already exists... continuing further..."
				# insert posts into collection
				if len(post_list) != 0:
					try:
						posts.insert(post_list, continue_on_error=True)
					except:
						print "some post docs already exists... continuing further..."
			# insert pages into collection
			if len(page_list) != 0:
				try:
					pages.insert(page_list, continue_on_error=True)
				except:
					print "some page docs already exists... continuing further..."

			#insert channel into collection
			try:
				channels.insert(channel_dict, continue_on_error=True)
			except:
				print "some channel docs already exists... continuing further..."

	except pymongo.errors.DuplicateKeyError, e:
		print e
if __name__ == '__main__':
	start = timeit.timeit()
	main()
	print "elapsed: " + str(timeit.timeit() - start) + "seconds..."