import media
import fresh_tomatoes

# info of movies
# use media.Movie() to give movies their own custom data structure

les_miserables = media.Movie(
    "Les Miserables",
    "http://www.impawards.com/2012/posters/les_miserables_ver3_xlg.jpg",
    "https://www.youtube.com/watch?v=ebSQ7A1FCtc")

little_mermaid = media.Movie(
    "The Little Mermaid",
    "https://upload.wikimedia.org/wikipedia/en/7/75/"
    "Movie_poster_the_little_mermaid.jpg",
    "https://www.youtube.com/watch?v=ZGZX5-PAwR8")

inter_stellar = media.Movie(
    "Interstellar",
    "https://upload.wikimedia.org/wikipedia/en/b/bc/"
    "Interstellar_film_poster.jpg",
    "https://www.youtube.com/watch?v=zSWdZVtXT7E")

inception = media.Movie(
    "Inception",
    "http://www.impawards.com/2010/posters/inception.jpg",
    "https://www.youtube.com/watch?v=8hP9D6kZseM")

dunkirk = media.Movie(
    "Dunkirk",
    "https://images-na.ssl-images-amazon.com/images/"
    "M/MV5BN2YyZjQ0NTEtNzU5MS00NGZkLTg0MTEtYzJmMWY3"
    "MWRhZjM2XkEyXkFqcGdeQXVyMDA4NzMyOA@@._V1_SY1000_CR0,"
    "0,674,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=9UrQ4VvFO-c")

legend_of_1900 = media.Movie(
    "The Legend of 1900",
    "http://www.impawards.com/1999/posters/"
    "legend_of_nineteen_hundred.jpg",
    "https://www.youtube.com/watch?v=wGEoA8_CJzk")

# the data of movies
movies = [
    les_miserables,
    little_mermaid,
    inter_stellar,
    inception,
    dunkirk,
    legend_of_1900
]

# use open_movies_page function in fresh_tomatoesca
fresh_tomatoes.open_movies_page(movies)
