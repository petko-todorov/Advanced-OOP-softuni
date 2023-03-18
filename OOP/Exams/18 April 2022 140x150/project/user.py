from typing import List


class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked: List = []
        self.movies_owned: List[object] = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not value:
            raise ValueError("Invalid username!")

        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):
        liked_movies = []
        if self.movies_liked:
            for movie in self.movies_liked:
                liked_movies.append(movie.details())
        else:
            liked_movies = ['No movies liked.']

        owned_movies = []
        if self.movies_owned:
            for movie in self.movies_owned:
                owned_movies.append(movie.details())
        else:
            owned_movies = ["No movies owned."]

        result = [f"Username: {self.username}, Age: {self.age}", "Liked movies:",
                  '\n'.join(x for x in liked_movies),
                  "Owned movies:",
                  '\n'.join(x for x in owned_movies)]

        return '\n'.join(result)
