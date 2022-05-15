from recompy import load_movie_data, FunkSVD
from pydantic import BaseModel

class UserInput(BaseModel):
    userId: int
    numOfRecommendations: int

class ResponseOutput(BaseModel):
    recommendations: list

def train_model() -> FunkSVD:
    clf = FunkSVD()
    clf.fit(load_movie_data())
    return clf

def get_voting(user_id) -> dict:
    # Returns mock data for now
    # TODO: Send request to the another endpoint
    # TODO: We should also implement eureka client to get the data from the other microservices
    return {
     '1':5,
     '2':4,
     '4':3
    }


def predict_recommendations_of_user(user_votings: dict, num_of_items: int) -> list:

    return model.get_recommendation_for_new_user(user_votings, similarity_measure = 'cosine_similarity', 
                                       howManyUsers = 1, howManyItems = num_of_items)

model = train_model()