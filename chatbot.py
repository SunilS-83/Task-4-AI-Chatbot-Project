import pickle
import random

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
responses = pickle.load(open("responses.pkl", "rb"))

def get_response(user_input):

    X_input = vectorizer.transform([user_input])

    tag = model.predict(X_input)[0]

    return random.choice(responses[tag])