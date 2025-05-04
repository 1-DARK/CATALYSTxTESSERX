import pandas as pd
import re

def load_symptoms_data(filepath):
    """Load symptoms data from a CSV file."""
    data = pd.read_csv(filepath)
    return data

def preprocess_symptoms(symptoms):
    """Preprocess the input symptoms for model compatibility."""
    # Convert to lowercase
    symptoms = symptoms.lower()
    # Remove any special characters
    symptoms = re.sub(r'[^a-zA-Z0-9\s,]', '', symptoms)
    # Split symptoms into a list
    symptoms_list = [symptom.strip() for symptom in symptoms.split(',')]
    return symptoms_list

def encode_symptoms(symptoms_list, symptoms_data):
    """Encode the symptoms into a format suitable for the model."""
    encoded = []
    for symptom in symptoms_list:
        if symptom in symptoms_data['Symptoms'].values:
            encoded.append(1)  # Symptom present
        else:
            encoded.append(0)  # Symptom not present
    return encoded