"""This file create Movie object to put in the html \
file and open the browser"""
# Created by Rafael Ross.
#Importing the required classes
import media #Import Movie class
import fresh_tomatoes #Import functions to generate the html file

toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", #noga
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")


avatar = media.Movie(
    "Avatar",
    "A history of a marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", #noga
    "https://www.youtube.com/watch?v=d1_JBMrrYw8")

kingsman = media.Movie(
    "Kingsman",
    "A history of a man who was invited to become a secret spy",
    "https://upload.wikimedia.org/wikipedia/en/8/8b/Kingsman_The_Secret_Service_poster.jpg", #noga
    "https://www.youtube.com/watch?v=kl8F-8tR8to")

avengers = media.Movie(
    "The Avengers",
    "Super heroes saving the world",
    "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg", #noga
    "https://www.youtube.com/watch?v=eOrNdBpGMv8")

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