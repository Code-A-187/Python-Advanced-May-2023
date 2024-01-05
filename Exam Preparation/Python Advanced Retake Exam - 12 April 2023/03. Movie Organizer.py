def movie_organizer(*args):
    movie_dict = {}
    for movies, genres in args:
        if genres not in movie_dict:
            movie_dict[genres] = []
        movie_dict[genres].append(movies)

    sorted_film_genres = sorted(movie_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ''
    for genre, movie_name in sorted_film_genres:
        sorted_movies = sorted(movie_name)
        result += f"{genre} - {len(sorted_movies)}\n"
        for name in sorted_movies:
            result += f"* {name}\n"
    return result.strip()


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")
))

