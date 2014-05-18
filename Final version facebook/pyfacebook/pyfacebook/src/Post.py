#! /usr/bin/python

import facebook
import Comment
import datetime

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
        
        self.__id = ipostdoc.get("id") if ipostdoc.has_key("id") else None
        self.__posted_by = ipostdoc.get("from") if ipostdoc.has_key("from") else None
        self.__story = ipostdoc.get("story") if ipostdoc.has_key("story") else None
        self.__message = ipostdoc.get("message") if ipostdoc.has_key("message") else None
        self.__message_tags = ipostdoc.get("message_tags") if ipostdoc.has_key("message_tags") else None
        self.__picture_attached = ipostdoc.get("picture") if ipostdoc.has_key("picture") else None
        self.__link_attached = ipostdoc.get("link") if ipostdoc.has_key("link") else None
        self.__link_name = ipostdoc.get("name") if ipostdoc.has_key("name") else None
        self.__link_description = ipostdoc.get("description") if ipostdoc.has_key("description") else None
        self.__source_link = ipostdoc.get("source") if ipostdoc.has_key("source") else None
        self.__type = ipostdoc.get("type") if ipostdoc.has_key("type") else None
        self.__share_count = str(ipostdoc.get("shares")) if ipostdoc.has_key("shares") else None
        self.__create_time = datetime.datetime.strptime(ipostdoc.get("created_time"), "%Y-%m-%dT%H:%M:%S+0000") if ipostdoc.has_key("created_time") else None
        self.__update_time = datetime.datetime.strptime(ipostdoc.get("updated_time"), "%Y-%m-%dT%H:%M:%S+0000") if ipostdoc.has_key("updated_time") else None
        
        self.__likes = []
        likes = ipostdoc.get("likes") if ipostdoc.has_key("likes") else None
        if likes:
            self.__likes = self.__get_peoples_liked(likes)
        
        self.__comments = []
        comments = ipostdoc.get("comments") if ipostdoc.has_key("comments") else None
        if comments:
            self.__comments = self.__comments_in_the_post(comments, igraphobj)
    
    def __repr__(self):
        """ return the string representation for the post object """
        obj = {
               "id" : self.__id,
               "posted_by" : self.__posted_by,
               "story" : self.__story,
               "message" : self.__message,
               "message_tags" : self.__message_tags,
               "picture_attached" : self.__picture_attached,
               "link_attached" : self.__link_attached,
               "link_name" : self.__link_name,
               "link_description" : self.__link_description,
               "source_link" : self.__source_link,
               "type" : self.__type,
               "share_count" : self.__share_count,
               "create_time" : self.__create_time,
               "update_time" : self.__update_time,
               "likes" : self.__likes,
               "comments" : [comment for comment in self.__comments]
        }
        
        return str(obj)

    def get_dict_repr(self):
        """ returns dictionary representation """
        obj = {
               "id" : self.__id,
               "posted_by" : self.__posted_by,
               "story" : self.__story,
               "message" : self.__message,
               "message_tags" : self.__message_tags,
               "picture_attached" : self.__picture_attached,
               "link_attached" : self.__link_attached,
               "link_name" : self.__link_name,
               "link_description" : self.__link_description,
               "source_link" : self.__source_link,
               "type" : self.__type,
               "share_count" : self.__share_count,
               "create_time" : self.__create_time,
               "update_time" : self.__update_time,
               "likes" : self.__likes,
        }
        
        return obj

    def get_comments(self):
        """returns the comments in the post"""
        return self.__comments

    def get_likes(self):
        """return list of peoples who liked post"""
        return self.__likes
        
    def iterlikes(self):
        """ iterator for likes for this post """
        for likedict in self.__likes:
            yield likedict
            
    def itercomments(self):
        """ iterator for comments in the post """
        for comment in self.__comments:
            yield comment
            
    def get_id(self):
        """ returns the id for this post """
        return self.__id
    
    def get_posted_by(self):
        """ return a dictionary containing the id and name of the person posted else None"""
        return self.__posted_by

    def get_story(self):
        """ return the story in this post else None"""
        return self.__story
    
    def get_message(self):
        """ returns the message in the post else None"""
        return self.__message
    
    def get_message_tags(self):
        """ return this list of dictionaries each representing the username and id of the people or page tagged in the post else None"""
        return self.__message_tags
    
    def get_picture_attached(self):
        """ return the link of the picture attached in this post else None"""
        return self.__picture_attached
    
    def get_link_attached(self):
        """ return the link attached in the post URL else None"""
        return self.__link_attached
    
    def get_link_name(self):
        """ return the name of the link else None"""
        return self.__link_name
    
    def get_link_description(self):
        """ return the description of the link else None"""
        return self.__link_description
    
    def get_source_link(self):
        """ return the URL (link) to the video if attached in the post else None """
        return self.__source_link
    
    def get_type(self):
        """ return the type of this post (link, photo, video) else None """
        return self.__type
    
    def get_share_count(self):
        """ returns the number of peoples who shared this post """
        return self.__share_count
    
    def get_create_time(self):
        """ returns the create time of this post as string"""
        return self.__create_time
    
    def get_updated_time(self):
        """ returns the updated time of this post (time of the last comment on this post) """
        return self.__update_time
    
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