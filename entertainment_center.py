import media
import fresh_tomatoes

# movies to display
matrix = media.Movie("The Matrix", "Storyline",
                        "https://www.movieposter.com/posters/archive/main/9/A70-4902",
                        "https://www.youtube.com/watch?v=m8e-FF8MsqU")

james_bond = media.Movie("James Bond", "Storyline",
                     "http://www.007museum.com/cr_poster.jpg",
                     "https://www.youtube.com/watch?v=sM8lWce5obY")

top_gun = media.Movie ("Top Gun", "Storyline",
                              "https://s-media-cache-ak0.pinimg.com/236x/b4/46/c1/b446c14a2545abcd7b12cd0429272749.jpg",
                              "https://www.youtube.com/watch?v=ioWpe3hdFH0")

back_to_the_future = media.Movie ("Back to the Future", "Storyline",
                           "https://www.movieposter.com/posters/archive/main/15/MPW-7684",
                           "https://www.youtube.com/watch?v=JWyOC4n4qSc")

indiana_jones = media.Movie ("Indiana Jones", "Storyline",
                                 "https://www.movieposter.com/posters/archive/main/157/MPW-78987",
                                 "https://www.youtube.com/watch?v=0ZOcoxjeUYo")

die_hard = media.Movie ("Die Hard", "Storyline",
                            "https://letusnerd.files.wordpress.com/2013/02/die-hard.jpg",
                            "https://www.youtube.com/watch?v=-qxBXm7ZUTM")

movies = [matrix, james_bond, top_gun, back_to_the_future, indiana_jones, die_hard]
fresh_tomatoes.open_movies_page(movies)
