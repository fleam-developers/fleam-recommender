from fastapi import FastAPI
from src.recommend import predict_recommendations_of_user, predict_recommendations_of_movie, get_voting, UserInput, ResponseOutput
from src.eureka import eureka_client

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/recommendation/user",response_model=ResponseOutput)
async def recommendation_user(request_input: UserInput) -> ResponseOutput:
    user_id = request_input.userId
    user_votings = get_voting(user_id)
    num_of_items = request_input.numOfRecommendations
    return predict_recommendations_of_user(user_votings, num_of_items)

@app.get("/recommendation/movie", response_model=ResponseOutput)
async def recommendation_movie(request_input: UserInput) -> ResponseOutput:
    movie_id = request_input.movieId
    return predict_recommendations_of_movie(movie_id, request_input.numOfRecommendations)

