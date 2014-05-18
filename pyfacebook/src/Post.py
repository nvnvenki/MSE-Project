#! /usr/bin/python

try:
    import facebook
    import Comment
except ImportError, e:
    print "error importing modules in Post"
    
class Post:
    """
        class Post => object of this class represents a post on a page
        fields:
            id
            from => dictionary
            story    
            message
            message_tags => list of dictionaries
            picture_attached
            link_attached
            link_name
            link_description
            source_link
            type
            share_count
            create_time
            update_time
            comments => list of comment objects
            likes => list of dictionaries representing the username , id of the people liked the post
    """
    def __init__(self, ipostdoc, igraphobj):
        """
            ipostdoc => post document
            igraphobj => graphobj
        """
        
        self.id = ipostdoc.get("id") if ipostdoc.has_key("id") else None
        self.posted_by = ipostdoc.get("from") if ipostdoc.has_key("from") else None
        self.story = ipostdoc.get("story") if ipostdoc.has_key("story") else None
        self.message = ipostdoc.get("message") if ipostdoc.has_key("message") else None
        self.message_tags = ipostdoc.get("message_tags") if ipostdoc.has_key("message_tags") else None
        self.picture_attached = ipostdoc.get("picture") if ipostdoc.has_key("picture") else None
        self.link_attached = ipostdoc.get("link") if ipostdoc.has_key("link") else None
        self.link_name = ipostdoc.get("name") if ipostdoc.has_key("name") else None
        self.link_description = ipostdoc.get("description") if ipostdoc.has_key("description") else None
        self.source_link = ipostdoc.get("source") if ipostdoc.has_key("source") else None
        self.type = ipostdoc.get("type") if ipostdoc.has_key("type") else None
        self.share_count = str(ipostdoc.get("shares")) if ipostdoc.has_key("shares") else None
        self.create_time = ipostdoc.get("created_time") if ipostdoc.has_key("created_time") else None
        self.update_time = ipostdoc.get("updated_time") if ipostdoc.has_key("updated_time") else None
        
        self.likes = []
        likes = ipostdoc.get("likes") if ipostdoc.has_key("likes") else None
        if likes:
            self.likes = self.__get_peoples_liked(likes)
        
        self.comments = []
        comments = ipostdoc.get("comments") if ipostdoc.has_key("comments") else None
        if comments:
            self.comments = self.__comments_in_the_post(comments, igraphobj)
    
    def __repr__(self):
        """ return the string representation for the post object """
        obj = {
               "id" : self.id,
               "posted_by" : self.posted_by,
               "story" : self.story,
               "message" : self.message,
               "message_tags" : self.message_tags,
               "picture_attached" : self.picture_attached,
               "link_attached" : self.link_attached,
               "link_name" : self.link_name,
               "link_description" : self.link_description,
               "source_link" : self.source_link,
               "type" : self.type,
               "share_count" : self.share_count,
               "create_time" : self.create_time,
               "update_time" : self.update_time,
               "likes" : self.likes,
               "comments" : [comment for comment in self.comments]
        }
        
        return str(obj)

    def iterlikes(self):
        """ iterator for likes for this post """
        for likedict in self.likes:
            yield likedict
            
    def itercomments(self):
        """ iterator for comments in the post """
        for comment in self.comments:
            yield comment
            
    def get_id(self):
        """ returns the id for this post """
        return self.id
    
    def get_posted_by(self):
        """ return a dictionary containing the id and name of the person posted else None"""
        return self.posted_by

    def get_story(self):
        """ return the story in this post else None"""
        return self.story
    
    def get_message(self):
        """ returns the message in the post else None"""
        return self.message
    
    def get_message_tags(self):
        """ return this list of dictionaries each representing the username and id of the people or page tagged in the post else None"""
        return self.message_tags
    
    def get_picture_attached(self):
        """ return the link of the picture attached in this post else None"""
        return self.picture_attached
    
    def get_link_attached(self):
        """ return the link attached in the post URL else None"""
        return self.link_attached
    
    def get_link_name(self):
        """ return the name of the link else None"""
        return self.link_name
    
    def get_link_description(self):
        """ return the description of the link else None"""
        return self.link_description
    
    def get_source_link(self):
        """ return the URL (link) to the video if attached in the post else None """
        return self.source_link
    
    def get_type(self):
        """ return the type of this post (link, photo, video) else None """
        return self.type
    
    def get_share_count(self):
        """ returns the number of peoples who shared this post """
        return self.share_count
    
    def get_create_time(self):
        """ returns the create time of this post as string"""
        return self.create_time
    
    def get_updated_time(self):
        """ returns the updated time of this post (time of the last comment on this post) """
        return self.update_time
    
    def __get_peoples_liked(self, likesdoc):
        """ returns a list of dictionaries of people who liked the post """ 
        # get the list of dictionaries
        data = likesdoc.get("data") if likesdoc.has_key("data") else None
        
        #return it
        return data
            
    def __comments_in_the_post(self, commentsdoc, igraphobj):
        """
            generate the comments object for all comments in the document
            return list of comment objects
        """
        # list of comment objects
        comments = []
        
        # get the data doc => list of dictionaries
        data = commentsdoc.get("data") if commentsdoc.has_key("data") else None
        
        # generate the comment objects
        if data:
            for doc in data:
                comments.append(Comment.Comment(doc, igraphobj))
        
        # return the list
        return comments


if __name__ == "__main__":
    graph = facebook.GraphAPI("680614081950320|4YUxXCWj0TOAkgEADHaksv0lfs0")
    post_id = "31867849201_10152302337139202"
    
    post = Post(graph.get_object(post_id), graph)
    print str(post)