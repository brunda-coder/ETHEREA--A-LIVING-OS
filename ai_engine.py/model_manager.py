# model_manager.py
import os
import pickle

class ModelManager:
    """
    Handles saving, loading, and managing AI models.
    """

    def __init__(self, model_dir="models"):
        self.model_dir = model_dir
        if not os.path.exists(model_dir):
            os.makedirs(model_dir)

    def save_model(self, model, name):
        """Save model to disk."""
        path = os.path.join(self.model_dir, f"{name}.pkl")
        with open(path, "wb") as f:
            pickle.dump(model, f)
        print(f"Model saved: {path}")

    def load_model(self, name):
        """Load model from disk."""
        path = os.path.join(self.model_dir, f"{name}.pkl")
        if not os.path.exists(path):
            raise FileNotFoundError(f"Model {name} not found")
        with open(path, "rb") as f:
            model = pickle.load(f)
        return model

    def list_models(self):
        """List all saved models."""
        return [f for f in os.listdir(self.model_dir) if f.endswith(".pkl")]
