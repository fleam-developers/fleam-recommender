from fastapi import FastAPI
from src.recommend import predict_recommendations_of_user, get_voting, UserInput, ResponseOutput

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/recommendation",response_model=ResponseOutput)
async def recommendation(request_input: UserInput) -> ResponseOutput:
    user_id = request_input.userId
    user_votings = get_voting(user_id)
    num_of_items = request_input.numOfRecommendations
    return predict_recommendations_of_user(user_votings, num_of_items)

