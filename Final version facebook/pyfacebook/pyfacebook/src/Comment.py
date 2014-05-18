#! /usr/bin/python

import facebook
import datetime

class Comment:
    """
        class Comment => object of this post represents a comment to a post
        fields:
           id
           from => dictionary representing the id and username of the person who commented
           message
           attachment => link or photo associated with the comment (dictionary)
           created_time
           like_count
           replies_count
           replies => list of comment objects which are replies to this comment
    """
    def __init__(self, icommentdoc, igraphobj):
        """
            icommentdoc => comment document
            igraphobj => graph obj
        """

        self.__id = icommentdoc.get("id") if icommentdoc.has_key("id") else None
        self.__comment_by = icommentdoc.get("from") if icommentdoc.has_key("from") else None
        self.__message = icommentdoc.get("message") if icommentdoc.has_key("message") else None
        self.__attachment = icommentdoc.get("attachment") if icommentdoc.has_key("attachment") else None
        self.__created_time = datetime.datetime.strptime(icommentdoc.get("created_time"), "%Y-%m-%dT%H:%M:%S+0000") if icommentdoc.has_key("created_time") else None
        self.__like_count = str(icommentdoc.get("like_count")) if icommentdoc.has_key("like_count") else None
        self.__replies_count = str(icommentdoc.get("comment_count")) if icommentdoc.has_key("comment_count") else None
        self.__replies = self.__gen_replies_for_comment(igraphobj)
        
    def __repr__(self):
        """ return the dictionary representation of the object as string """
        obj = {
        "id" : self.__id,
        "comment_by" : self.__comment_by,
        "message" : self.__message,
        "attachment" : self.__attachment,
        "created_time" : self.__created_time,
        "like_count" : self.__like_count,
        "replies_count" : self.__replies_count,
        "replies" : [comment for comment in self.__replies]
        }
        
        return str(obj)
    
    def get_dict_repr(self):
        """ returns dictionary representation """

        obj = {
        "id" : self.__id,
        "comment_by" : self.__comment_by,
        "message" : self.__message,
        "attachment" : self.__attachment,
        "created_time" : self.__created_time,
        "like_count" : self.__like_count,
        "replies_count" : self.__replies_count,
        }
        
        return obj

    def iterreplies(self):
        """ iterator for replies for this comment """
        for reply in self.__replies:
            yield reply
    
    def get_id(self):
        """ returns the id for the comment """
        return self.__id
    
    def get_comment_by(self):
        """ returns the dictionary contains the username and id of person commented """
        return self.__comment_by
    
    def get_message(self):
        """ returns the comment message else None"""
        return self.__message
    
    def get_attachment(self):
        """ return the attachment associated with this comment links or photo else None"""
        return self.__attachment
    
    def get_created_time(self):
        """ returns the created time for the comment """
        return self.__created_time
    
    def get_like_count(self):
        """ returns the like count for the comment """
        return self.__like_count
    
    def get_replies_count(self):
        """ returns the replies count count for the comment """
        return self.__replies_count
    
    def get_replies(self):
        """ returns the list of reply comment objects """
        return self.__replies
    
    def __gen_replies_for_comment(self, igraphobj):
        """
            generate the list of comment objects which are replies for this comment object
            if there are replies else returns an empty list
        """
        # list of reply comment objects
        replies = []
        
        # get the replies for the comment a dictionary
        reply_doc = igraphobj.get_connections(self.__id, "comments")
        
        # now generate the list of comment objects 
        reply_list = reply_doc.get("data") if reply_doc.has_key("data") else None
        
        # now generate the comment objects
        if reply_list:
            for comment_doc in reply_list:
                replies.append(Comment(comment_doc, igraphobj))
            
        #return the reply comment list
        return replies
    
if __name__ == "__main__":
    graph = facebook.GraphAPI("680614081950320|4YUxXCWj0TOAkgEADHaksv0lfs0")
    comment_id = "654448231252991_2178163"
    
    comment = Comment(graph.get_object(comment_id), graph)
    print comment