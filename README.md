# AI Chatbot Project

## Project Overview

This project is an NLP-based AI chatbot developed using Python and Flask. The chatbot predicts user intent from text input and generates suitable responses using a machine learning classifier.

The chatbot uses Natural Language Processing (NLP) techniques and a trained classifier to understand user messages and provide predefined retrieval-based responses.

---

# Features

* NLP-based chatbot
* Intent classification
* Retrieval-based responses
* Flask API server
* Simple web interface using HTML and CSS
* Machine learning model training
* JSON-based intent dataset

---

# Technologies Used

* Python
* Flask
* NLTK
* Scikit-learn
* HTML
* CSS
* JSON

---

# Project Structure

```text
AI-Chatbot-Project/
│
├── app.py
├── chatbot.py
├── train.py
├── intents.json
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── model.pkl
├── vectorizer.pkl
├── responses.pkl
│
├── screenshots/
│
└── demo/
```

---

# How the Project Works

1. User enters a message.
2. The chatbot preprocesses the text.
3. Text is converted into vectors using CountVectorizer.
4. The classifier predicts the intent.
5. The chatbot retrieves a suitable response.
6. Flask returns the response to the frontend.

---

# Machine Learning Classifier

The chatbot uses the Multinomial Naive Bayes classifier from Scikit-learn for intent classification.

---

# Installation Steps

## 1. Clone Repository

```bash
git clone <repository_link>
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

## 3. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 5. Train the Chatbot

```bash
python train.py
```

## 6. Run Flask Application

```bash
python app.py
```

---

# Flask API Endpoints

| Endpoint | Description              |
| -------- | ------------------------ |
| `/`      | Opens chatbot webpage    |
| `/get`   | Returns chatbot response |

---

# Screenshots

* Chatbot UI
* Flask server running
* Project structure

---

# Deliverables Checklist

| Deliverable               | Status      |
| ------------------------- | ----------- |
| Intent dataset JSON       | ✅ Completed |
| Train classifier          | ✅ Completed |
| Retrieval-based responses | ✅ Completed |
| Flask API server          | ✅ Completed |
| NLP processing            | ✅ Completed |
| Web interface             | ✅ Completed |
| Demo video/GIF            | ✅ Completed |
| GitHub repository         | ✅ Completed |

# Demo Video

https://drive.google.com/file/d/1MGobZiO3A4B3PirNgLf4POcnzLNW2HdJ/view?usp=sharing

---

# Future Improvements

* Voice assistant integration
* Database connectivity
* Better NLP models
* Multiple language support
* Deep learning chatbot

---

# Conclusion

This project demonstrates the implementation of an NLP-based AI chatbot using Python, Flask, and machine learning techniques. The chatbot predicts user intents and provides suitable responses through a web-based interface.

---

# Author

Sunil S
JNTUACEK
CSE Department
