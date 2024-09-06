from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router
from config.database import engine, Base

app = FastAPI()
app.title = "My API"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)


movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
        "year": 2009,
        "rating": 7.8,
        "category": "Action",
    },
    {
        "id": 2,
        "title": "Avatar",
        "overview": "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
        "year": 2009,
        "rating": 7.8,
        "category": "Fantasy",
    },
]

@app.get('/', tags=['home'])
def message():
    return HTMLResponse(content="<h1>Hello World!!</h1>", status_code=200)

