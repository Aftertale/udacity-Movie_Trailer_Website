import webbrowser
import re
import urllib.request
import json
        
class Movie():
    """This Class provides a way to store movie related information"""

#Initialize the class with at least one argument, arg[1] and arg[2] are optional.
    
    def __init__(self, movie_title, trailer_youtube="www.youtube.com", movie_year=""):
        self.title = movie_title
        self.year = movie_year
        self.trailer_youtube_url = trailer_youtube
        

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def get_movie_info(self):
        url = "http://www.omdbapi.com/?t=" + self.title.replace(" ", "+") + "&y=" + self.year + "&plot=full&r=json"
        req = urllib.request.urlopen(url)
        response = req.read()
        decode = response.decode(encoding='utf-8')
        movieInfo = json.loads(decode)
        return(movieInfo)
    
    #def get_you_tube_link(self):
    #    youtubeurl = "https://gdata.youtube.com/feeds/api/videos"
