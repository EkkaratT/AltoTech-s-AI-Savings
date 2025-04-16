import joblib
import os

class EnergyPredictor:
    def __init__(self):
        self.model = None

    def load_model(self, model_path="model/best_model.pkl"):
        # Load the pre-trained model
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at {model_path}")
        self.model = joblib.load(model_path)

    def predict(self, features):
        return self.model.predict(features)
