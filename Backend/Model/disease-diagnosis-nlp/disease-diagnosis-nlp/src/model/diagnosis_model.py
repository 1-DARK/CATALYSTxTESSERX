from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import numpy as np
import joblib

class DiagnosisModel:
    def __init__(self, data_path):
        self.data_path = data_path
        self.model = None
        self.vectorizer = None
        self.conditions = None

    def load_data(self):
        data = pd.read_csv(self.data_path)
        self.conditions = data['Condition'].values
        symptoms = data['Symptoms'].values
        return symptoms, self.conditions

    def preprocess_data(self, symptoms):
        # Convert symptoms to lowercase and remove any extra spaces
        symptoms = [symptom.lower().strip() for symptom in symptoms]
        return symptoms

    def train_model(self):
        symptoms, conditions = self.load_data()
        symptoms = self.preprocess_data(symptoms)

        self.vectorizer = CountVectorizer()
        X = self.vectorizer.fit_transform(symptoms)
        y = conditions

        self.model = MultinomialNB()
        self.model.fit(X, y)

    def predict(self, user_symptoms):
        user_symptoms = self.preprocess_data([user_symptoms])
        X_user = self.vectorizer.transform(user_symptoms)
        predictions = self.model.predict(X_user)
        return predictions

    def save_model(self, model_path, vectorizer_path):
        joblib.dump(self.model, model_path)
        joblib.dump(self.vectorizer, vectorizer_path)

    def load_model(self, model_path, vectorizer_path):
        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vectorizer_path)