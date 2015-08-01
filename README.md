# Movie Trailer

This project was created to render your favorite movies into a HTML file.

#Requirements

To make it works you shoud to download and put the 3 files below in a same folder:

- <fresh_tomatoes class="py">fresh_tomatoes.py -> This file mount the html file and has a method to open the browser</fresh_tomatoes>
- <media class="py">media.py -> This file create Movie object</media>
- <entertainment_center class="py">entertainment_center.py -> This file creates Movie objects to put in the html file and open the browser</entertainment_center>

#Usage

###Example

import media
import fresh_tomatoes

captainAmerica = media.Movie(
    "Captain America - The First Avenger",
    "The story a weak man whose is chosen to became a super soldier",
    "https://upload.wikimedia.org/wikipedia/pt/3/37/Captain_America_The_First_Avenger_poster.jpg", #noga
    "https://www.youtube.com/watch?v=JerVrbLldXw")

ironMan = media.Movie(
    "Iron Man",
    "The first chapter of the awesome Tony Stark's story. This movie \
    show the begining of Iron Man",
    "https://upload.wikimedia.org/wikipedia/pt/0/00/Iron_Man_poster.jpg", #noga
    "https://www.youtube.com/watch?v=8hYlB38asDY")

movies = [toy_story, avatar, kingsman, avengers, captainAmerica, ironMan]
fresh_tomatoes.open_movies_page(movies)

$ python entertainment_center.py