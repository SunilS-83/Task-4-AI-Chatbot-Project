import json
import pickle

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load intents
with open("intents.json") as file:
    data = json.load(file)

training_sentences = []
training_labels = []

responses = {}

for intent in data["intents"]:

    for pattern in intent["patterns"]:
        training_sentences.append(pattern)
        training_labels.append(intent["tag"])

    responses[intent["tag"]] = intent["responses"]

# Convert words into vectors
vectorizer = CountVectorizer()

X = vectorizer.fit_transform(training_sentences)

# Train model
model = MultinomialNB()
model.fit(X, training_labels)

# Save files
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
pickle.dump(responses, open("responses.pkl", "wb"))

print("Model trained successfully!")