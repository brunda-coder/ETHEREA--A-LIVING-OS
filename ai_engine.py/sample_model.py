# sample_model.py
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
from model_manager import ModelManager

class SampleAI:
    """
    Fully functional simple AI model for Etherea.
    Uses linear regression for demo.
    """

    def __init__(self):
        self.model = LinearRegression()
        self.manager = ModelManager()
        self.trained = False

    def train(self, X, y):
        """
        Train the AI model.
        """
        X = np.array(X)
        y = np.array(y)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        self.trained = True
        score = self.model.score(X_test, y_test)
        print(f"Training complete! Test R² score: {score:.4f}")

    def predict(self, features):
        """
        Predict output for given features.
        """
        if not self.trained:
            raise RuntimeError("Model not trained yet!")
        features = np.array(features)
        if features.ndim == 1:
            features = features.reshape(1, -1)
        return self.model.predict(features)

    def save(self, name="sample_ai_model"):
        if not self.trained:
            raise RuntimeError("Cannot save untrained model!")
        self.manager.save_model(self.model, name)

    def load(self, name="sample_ai_model"):
        self.model = self.manager.load_model(name)
        self.trained = True
        print(f"Model {name} loaded successfully.")
