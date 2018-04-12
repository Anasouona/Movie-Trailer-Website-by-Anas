import fresh_tomatoes
import media

Udacity = media.Movie("Udacity",
                      "Udacity is the outgrowth of free computer sciencs",
                      "https://f.top4top.net/p_825qxms91.jpg",
                      "https://youtu.be/cZUUjAz112w")
free_Tor = media.Movie("free tor", "Free Internet",
                       "https://f.top4top.net/p_825s656g1.jpg",
                       "https://youtu.be/l4lmO0CXrLw")
Raspberry_Pi3 = media.Movie("Raspberry Pi3",
                            "Raspberry Pi is a series of small",
                            "https://e.top4top.net/p_825tsn1z1.jpg",
                            "https://youtu.be/XYP__GbZgMU")

movies = [Udacity, free_Tor, Raspberry_Pi3]
fresh_tomatoes.open_movies_page(movies)
