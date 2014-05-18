#! /usr/bin/python

try:
    import Page
    import facebook
except ImportError, e:
    print "error importing module in Channel"

class Channel:
    
    """
        Channel => object of this class represents a channel
        fields:
            channel_name=> name of the channel (facebook id)
            channel_slots => dictionary representing the slot
            igraphobj => graph object
    """
    
    def __init__(self, ichannel_name, ichannel_slots, igraphobj):
        """
            ichannel_name => channel name
            ichannel_slots => channel program slots
        """
        self.channel_name = ichannel_name
        self.chennel_slots = ichannel_slots
        self.channel_program_pages = self.__gen_channel_page_objects(ichannel_slots, igraphobj)
    
    def __gen_channel_page_objects(self, ichannel_slots, igraphobj):
        """
            having taken the input of program names and their time slots
            populate the page objects for each of the program
            and return it.
            list of tuples => (time, corresponding program's page object)
        """
        channel_program_pages = []
        
        # generate the page objects for all the programs
        for time, pageid in ichannel_slots.items():
            page = Page.Page(igraphobj.get_object(pageid), igraphobj) 
            channel_program_pages.append((time, page))
        
        return channel_program_pages
    
    def iterpages(self):
        """
            returns iterator for iterating over the (time, page objects) tuple that are in this channel
        """
        for item in self.channel_program_pages:
            yield item
            
    def __repr__(self):
        """
            returns the string representation for the channel object
        """
        obj = {
               "channel_name" : self.channel_name,
               "channel_slots" : self.chennel_slots,
               "channel_program_pages" :  dict([(item[0], item[1]) for item in self.channel_program_pages])
        }
        
        return str(obj)
    
    
if __name__ == "__main__":
    graph = facebook.GraphAPI("680614081950320|4YUxXCWj0TOAkgEADHaksv0lfs0")
    channel_name = "Colors TV"
    
    channel_slots = {
                     "730" : "Colors.SasuralSimarKa"
    }
    
    channel = Channel(channel_name, channel_slots, graph)
    
    fobj = open("results.txt", "w")
    fobj.write(str(channel))
    fobj.close()
    
    print "done!"