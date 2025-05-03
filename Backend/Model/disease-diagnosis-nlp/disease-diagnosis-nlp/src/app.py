from flask import Flask, request, jsonify
import pandas as pd
from model.diagnosis_model import DiagnosisModel

app = Flask(__name__)

# Load the symptoms data
symptoms_data_path = 'data/symptoms.csv'
symptoms_df = pd.read_csv(symptoms_data_path)

# Initialize the diagnosis model
diagnosis_model = DiagnosisModel(symptoms_df)

@app.route('/diagnose', methods=['POST'])
def diagnose():
    user_input = request.json.get('symptoms', '')
    if not user_input:
        return jsonify({'error': 'No symptoms provided'}), 400
    
    # Get possible diseases based on user symptoms
    possible_diseases = diagnosis_model.predict(user_input)
    
    return jsonify({'possible_diseases': possible_diseases})

if __name__ == '__main__':
    app.run(debug=True)