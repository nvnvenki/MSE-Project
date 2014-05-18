#! /usr/bin/python

try:
    import facebook
except ImportError, e:
    print "error importing module in Comment"
    
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

        self.id = icommentdoc.get("id") if icommentdoc.has_key("id") else None
        self.comment_by = icommentdoc.get("from") if icommentdoc.has_key("from") else None
        self.message = icommentdoc.get("message") if icommentdoc.has_key("message") else None
        self.attachment = icommentdoc.get("attachment") if icommentdoc.has_key("attachment") else None
        self.created_time = icommentdoc.get("created_time") if icommentdoc.has_key("created_time") else None
        self.like_count = str(icommentdoc.get("like_count")) if icommentdoc.has_key("like_count") else None
        self.replies_count = str(icommentdoc.get("comment_count")) if icommentdoc.has_key("comment_count") else None
        self.replies = self.__gen_replies_for_comment(igraphobj)
        
    def __repr__(self):
        """ return the dictionary representation of the object as string """
        obj = {
        "id" : self.id,
        "comment_by" : self.comment_by,
        "message" : self.message,
        "attachment" : self.attachment,
        "created_time" : self.created_time,
        "like_count" : self.like_count,
        "replies_count" : self.replies_count,
        "replies" : [comment for comment in self.replies]
        }
        
        return str(obj)
    
    
    def iterreplies(self):
        """ iterator for replies for this comment """
        for reply in self.replies:
            yield reply
    
    def get_id(self):
        """ returns the id for the comment """
        return self.id
    
    def get_comment_by(self):
        """ returns the dictionary contains the username and id of person commented """
        return self.comment_by
    
    def get_message(self):
        """ returns the comment message else None"""
        return self.message
    
    def get_attachment(self):
        """ return the attachment associated with this comment links or photo else None"""
        return self.attachment
    
    def get_created_time(self):
        """ returns the created time for the comment """
        return self.created_time
    
    def get_like_count(self):
        """ returns the like count for the comment """
        return self.like_count
    
    def get_replies_count(self):
        """ returns the replies count count for the comment """
        return self.replies_count
    
    def get_replies(self):
        """ returns the list of reply comment objects """
        return self.replies
    
    def __gen_replies_for_comment(self, igraphobj):
        """
            generate the list of comment objects which are replies for this comment object
            if there are replies else returns an empty list
        """
        # list of reply comment objects
        replies = []
        
        # get the replies for the comment a dictionary
        reply_doc = igraphobj.get_connections(self.id, "comments")
        
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