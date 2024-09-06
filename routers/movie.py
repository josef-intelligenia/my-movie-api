from fastapi import APIRouter
from fastapi import Query, Path, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from config.database import Session
from models.movie import Movie as MovieModel
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()



@movie_router.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    db = Session()
    movies = MovieService(db).get_movies()
    return JSONResponse(content=jsonable_encoder(movies), status_code=200)

@movie_router.get('/movies/{id}', tags=['movies'], response_model=Movie, status_code=200)
def get_movie(id: int = Path(le=2000, ge=1)) -> Movie:
    db = Session()
    movie = MovieService(db).get_movie(id)
    return JSONResponse(content=jsonable_encoder(movie), status_code=200) if movie else JSONResponse(content={"message": "Movie not found"}, status_code=404)

@movie_router.get('/movies/', tags=['movies'], response_model=List[Movie], status_code=200)
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)) -> List[Movie]:
    db = Session()
    movies = MovieService(db).get_movies_by_category(category)
    return JSONResponse(content=jsonable_encoder(movies), status_code=200)

@movie_router.post('/movies', tags=['movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict:
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(content={"message": "Movie created"}, status_code=201)

@movie_router.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def update_movie(id: int, data: Movie) -> dict:
    db = Session()
    movie = MovieService(db).update_movie(id, data)
    if not movie:
        return JSONResponse(content={"message": "Movie not found"}, status_code=404)
    return JSONResponse(content={"message": "Movie updated"}, status_code=200)

@movie_router.delete('/movies/{id}', tags=['movies'], status_code=204)
def delete_movie(id: int) -> None:
    db = Session()
    result = MovieService(db).delete_movie(id)
    if not result:
        raise HTTPException(detail="Movie not found", status_code=404)
    return
