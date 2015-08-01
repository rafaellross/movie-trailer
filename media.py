    """This file create Movie class"""
# Created by Rafael Ross.

import webbrowser
class Movie():

    #Constructor for the Movie class
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        #Set the properties of the object
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self): #Function to open the browser
        webbrowser.open(self.trailer_youtube_url)
