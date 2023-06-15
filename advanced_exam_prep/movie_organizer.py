def movie_organizer(*args):
    dict_genres = {}

    for movie, genre in args:
        if genre not in dict_genres:
            dict_genres[genre] = []
        dict_genres[genre].append(movie)

    sorted_dict = sorted(dict_genres.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ''

    for genre, movie_name in sorted_dict:
        sorted_movies = sorted(movie_name)
        result += f"{genre} - {len(sorted_movies)}\n"
        for name in sorted_movies:
            result += f"* {name}\n"

    return result







print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))

# print(movie_organizer(
#     ("Avatar: The Way of Water", "Action"),
#     ("House Of Gucci", "Drama"),
#     ("Top Gun", "Action"),
#     ("Ted", "Comedy"),
#     ("Duck Soup", "Comedy"),
#     ("The Dark Knight", "Action"),
#     ("A Star Is Born", "Musicals"),
#     ("The Warrior", "Action"),
#     ("Like A Boss", "Comedy"),
#     ("The Green Mile", "Drama"),
#     ("21 Jump Street", "Comedy")))
