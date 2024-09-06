from typing import List
from models.movie import Movie as MovieModel
from schemas.movie import Movie

class MovieService():
    def __init__(self, repository) -> None:
        self.db = repository

    def get_movies(self):
        movies = self.db.query(MovieModel).all()
        return movies

    def get_movie(self, id: int):
        movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return movie

    def get_movies_by_category(self, category: str):
        movies = self.db.query(MovieModel).filter(MovieModel.category == category).all()
        return movies

    def create_movie(self, movie: Movie):
        new_movie = MovieModel(**movie.model_dump())
        self.db.add(new_movie)
        self.db.commit()
        return

    def update_movie(self, id: int, data: Movie):
        movie = self.get_movie(id)
        if not movie:
            return None
        movie.title = data.title
        movie.overview = data.overview
        movie.year = data.year
        movie.rating = data.rating
        movie.category = data.category
        self.db.commit()
        return movie

    def delete_movie(self, id: int):
        movie = self.get_movie(id)
        if not movie:
            return False
        self.db.delete(movie)
        self.db.commit()
        return True