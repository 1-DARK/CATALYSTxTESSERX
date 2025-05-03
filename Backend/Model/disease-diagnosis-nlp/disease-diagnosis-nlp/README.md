# Disease Diagnosis NLP

This project is an NLP-based application designed to diagnose possible diseases based on user-provided symptoms. It utilizes a dataset of symptoms and their associated conditions to train a model that can predict diseases.

## Project Structure

```
disease-diagnosis-nlp
├── src
│   ├── app.py                # Main entry point for the application
│   ├── model
│   │   └── diagnosis_model.py # Implementation of the NLP model
│   ├── data
│   │   └── symptoms.csv       # Dataset containing conditions and symptoms
│   └── utils
│       └── preprocess.py      # Utility functions for data preprocessing
├── requirements.txt           # List of dependencies required for the project
└── README.md                  # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd disease-diagnosis-nlp
   ```

2. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python src/app.py
   ```

2. Input your symptoms when prompted. The application will analyze the symptoms and provide possible disease diagnoses.

## Functionality

- The application loads symptoms data from `symptoms.csv`.
- It preprocesses the input symptoms for better model performance.
- The NLP model predicts possible diseases based on the symptoms provided by the user.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.