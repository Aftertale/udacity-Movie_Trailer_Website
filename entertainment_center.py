import media
import fresh_tomatoes

#dictionary to store Movie information
movie_dict = {}

toy_story = media.Movie("Toy Story",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

pulp_fiction = media.Movie("Pulp Fiction",
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

school_of_rock = media.Movie("School of Rock",
                            "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

snakes_on_a_plane = media.Movie("Snakes on a Plane",
                                "https://www.youtube.com/watch?v=vkckhcqiwM8")

django_unchained = media.Movie("Django Unchained",
                               "www.youtube.com/watch?v=eUdM9vrCbow")

princess_bride = media.Movie("The Princess Bride",
                             "www.youtube.com/watch?v=njZBYfNpWoE")

imitation_game = media.Movie("The Imitation Game",
                             "https://www.youtube.com/watch?v=S5CjKEFb-sM")

a_new_hope = media.Movie("Star Wars","https://www.youtube.com/watch?v=1g3_CFmnU7k","1977")

kiss_kiss_bang_bang = media.Movie("Kiss Kiss Bang Bang", "https://www.youtube.com/watch?v=__PnD1HWXSo")

avengers = media.Movie("The Avengers", "https://www.youtube.com/watch?v=eOrNdBpGMv8", "2012")

age_of_ultron = media.Movie("Avengers: Age of Ultron", "https://www.youtube.com/watch?v=JAUoeqvedMo")
    
unsorted_movies = [toy_story, avatar, school_of_rock, pulp_fiction, ratatouille, midnight_in_paris, snakes_on_a_plane, django_unchained, princess_bride, imitation_game, a_new_hope, kiss_kiss_bang_bang, avengers, age_of_ultron]
for movie in unsorted_movies:
    print(movie.title)
    info = movie.get_movie_info()
    movie.poster_image_url = info.get("Poster")
    movie.storyline = info.get("Plot")
    movie.genre = info.get("Genre")
    movie.cast = info.get("Actors")
    movie.year = info.get("Year")
    movie.director = info.get("Director")
    movie.rating = info.get("Rated")
movies = sorted(unsorted_movies, key=lambda movie: movie.title)


fresh_tomatoes.open_movies_page(movies)
