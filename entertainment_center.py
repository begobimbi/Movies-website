#imported file containing function open_movies_page()
import fresh_tomatoes

#using contents of python file media.py
import media

#instances of class movie containing variables. When this code runs the __init__ function gets called. Self = instance being created,in this case match_point and the rest are instance variables: 
#movie_title, movie_release_year, movie_storyline, poster_image, trailer_youtube. Variables get initialised appropriately.
match_point = media.Movie("Match Point", "2005", "Tennis instructor that falls in love but with issues", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-Qnpd7eSZ1q8bNSc0giaCR8XA96S-jbV7NKWuD8O9QNVMwzfL", "https://www.youtube.com/watch?v=wISRAOb6xm0")
isle_of_dogs = media.Movie("Isle of Dogs","2018", "Group of dogs stranded in a trash island next to Japan", "https://upload.wikimedia.org/wikipedia/en/2/23/IsleOfDogsFirstLook.jpg","https://www.youtube.com/watch?v=dt__kig8PVU")
grand_hotel_budapest = media.Movie("Hotel Budapest", "2014", "Comedy set in a hotel where a crazy murder takes place","https://upload.wikimedia.org/wikipedia/en/1/1c/The_Grand_Budapest_Hotel.png", "https://www.youtube.com/watch?v=zru-1DbbcsA")
fantastic_mr_fox = media.Movie("Fantastic Mr Fox","2009", "Film about foxes that steal food from farmers every night", "https://upload.wikimedia.org/wikipedia/en/a/af/Fantastic_mr_fox.jpg", "https://www.youtube.com/watch?v=n2igjYFojUo" )
coco = media.Movie("Coco", "2017", "Disney film about a Mexican kid that visits the land of the dead", "https://upload.wikimedia.org/wikipedia/en/9/98/Coco_%282017_film%29_poster.jpg", "https://www.youtube.com/watch?v=zNCz4mQzfEI")
slumdog_millionaire = media.Movie("Slumdog Millionaire", "2008", "Drama set in India featuring a kid that becomes a millionaire", "https://upload.wikimedia.org/wikipedia/en/9/92/Slumdog_Millionaire_poster.png", "https://www.youtube.com/watch?v=JwiU94p9XPA")

def load_movies():   
    #array of movies used as input for open_movies_page function.
    movies = [match_point, isle_of_dogs, grand_hotel_budapest, fantastic_mr_fox, coco, slumdog_millionaire]
    #function takes the list of movies as input and as output it creates a website that shows those movies. 
    fresh_tomatoes.open_movies_page(movies)

#calls the load movies function to initilise the webpage values
load_movies()
