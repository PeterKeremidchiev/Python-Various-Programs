from project import Movie
from project import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        existing_user = [u for u in self.users_collection if u.username == username]
        if existing_user:
            raise Exception("User already exists!")
        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        existing_user = [u for u in self.users_collection if u.username == username]
        if not existing_user:
            raise Exception("This user does not exist!")
        if movie.owner.username != existing_user[0].username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        # if movie in self.movies_collection:
        #     raise Exception("Movie already added to the collection!")
        existing_movie = [m for m in self.movies_collection if m.title == movie.title]
        if existing_movie:
            raise Exception("Movie already added to the collection!")

        existing_user[0].movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        existing_movie = [m for m in self.movies_collection if m.title == movie.title]
        existing_user = [u for u in self.users_collection if u.username == username]

        if not existing_movie:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie.owner.username != existing_user[0].username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for key, value in kwargs.items():
            setattr(movie, key, value)

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        existing_movie = [m for m in self.movies_collection if m.title == movie.title]
        existing_user = [u for u in self.users_collection if u.username == username]

        if not existing_movie:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie.owner.username != existing_user[0].username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        existing_user[0].movies_owned.remove(movie)
        self.movies_collection.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):

        existing_user = [u for u in self.users_collection if u.username == username]
        existing_movie_liked = [m for m in existing_user[0].movies_liked if m.title == movie.title]

        if movie.owner.username == existing_user[0].username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if existing_movie_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        existing_user[0].movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        existing_user = [u for u in self.users_collection if u.username == username]
        existing_movie_liked = [m for m in existing_user[0].movies_liked if m.title == movie.title]

        if not existing_movie_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        existing_user[0].movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        sorted_movies = sorted(self.movies_collection, key=lambda m: (-m.year, m.title))

        if not sorted_movies:
            return "No movies found."
        return "\n".join([m.details() for m in sorted_movies])

    def __str__(self):
        result = ""
        if not self.users_collection:
            result = "All users: No users.\n"
        else:
            result = f"All users: {', '.join([u.username for u in self.users_collection])}\n"

        if not self.movies_collection:
            result += "All movies: No movies."
        else:
            result += f"All movies: {', '.join([m.title for m in self.movies_collection])}"

        return result

