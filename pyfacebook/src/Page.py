#! /usr/bin/python

try:
    import facebook
    import Post
except ImportError, e:
    print "error importing module in Page"

class Page:
    """
        class Page => object of this class represents a page that is related to a channel
        fields:
            id
            username
            about
            description
            company_overview
            category
            genre
            schedule
            season
            talking_about_count
            likes
            link_on_facebook
            posts => list of post objects
    """
    
    def __init__(self, ipagedoc, igraphobj):
        """
            ipagedoc => represents the doc for page
            igraphobj => graph object
        """
        
        self.id = ipagedoc.get("id") if ipagedoc.has_key("id") else None
        self.username = ipagedoc.get("username") if ipagedoc.has_key("username") else None
        self.about = ipagedoc.get("about") if ipagedoc.has_key("about") else None
        self.description = ipagedoc.get("description") if ipagedoc.has_key("description") else None
        self.company_overview = ipagedoc.get("company_overview") if ipagedoc.has_key("company_overview") else None
        self.category = ipagedoc.get("category") if ipagedoc.has_key("category") else None
        self.talking_about_count = str(ipagedoc.get("talking_about_count")) if ipagedoc.has_key("talking_about_count") else None
        self.likes = str(ipagedoc.get("likes")) if ipagedoc.has_key("likes") else None
        self.link_on_facebook = ipagedoc.get("link") if ipagedoc.has_key("link") else None
        self.genre = ipagedoc.get("genre") if ipagedoc.has_key("genre") else None
        self.schedule = ipagedoc.get("schedule") if ipagedoc.has_key("schedule") else None
        self.season = ipagedoc.get("season") if ipagedoc.has_key("season") else None
        self.posts = self.__posts_in_the_page(igraphobj)
    
    def __repr__(self):
        """ return the string representation for the page object """
        obj = {
               "id" : self.id,
               "username" : self.username,
               "about" : self.about,
               "description" : self.description,
               "company_overview" : self.company_overview,
               "category" : self.category,
               "talking_about_count" : self.talking_about_count,
               "likes" : self.likes,
               "link" : self.link_on_facebook,
               "genre" : self.genre,
               "schedule" : self.schedule,
               "season" : self.season,
               "posts" : [post for post in self.posts]
        }
        
        return str(obj)
    
    
    def iterposts(self):
        """
            iterator for iterating over the posts in the page
        """
        for post in self.posts:
            yield post
        
    def get_id(self):
        """ returns the page id for the page """
        return self.id
    
    def get_username(self):
        """ returns the username for the page """
        return self.username
    
    def get_aboutinfo(self):
        """ returns the about info for the page if found else None """
        return self.about

    def get_description(self):
        """ returns the description for the page if found else None """
        return self.description
    
    def get_company_overview(self):
        """ returns the company overview for the page if found else None """
        return self.company_overview
    
    def get_category(self):
        """ returns the company category for the page if found else None """
        return self.category

    def get_talking_about_count(self):
        """ returns the talking about count for the page """
        return self.talking_about_count
    
    def get_likes(self):
        """ returns the page likes for the page """
        return self.likes

    def get_link(self):
        """ return the link of the page on facebook """
        return self.link_on_facebook
    
    def get_genre(self):
        """ return the genre of the page """
        return self.genre

    def get_schedule(self):
        """ return the schedule time for the program """
        return self.schedule
    
    def get_season(self):
        """ return the season of the program """
        return self.season
    
    def __posts_in_the_page(self, igraphobj):
        """ returns a list of posts on this page """
        
        # list for holding a list of post objects
        posts_list = []
        
        # get the posts
        postdoc = igraphobj.get_connections(self.id, "posts")
        
        # get the data
        data = postdoc.get("data") if postdoc.has_key("data") else None
        
        # generate the list of post objects
        if data:
            for post in data:
                posts_list.append(Post.Post(post, igraphobj))
        
        # return the list
        return posts_list
    
if __name__ == "__main__":
    graph = facebook.GraphAPI("680614081950320|4YUxXCWj0TOAkgEADHaksv0lfs0")
    page_id = "526242754073540"
    
    page = Page(graph.get_object(page_id), graph)
    print str(page)