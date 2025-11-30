# preprocessing.py
import numpy as np

class Preprocessor:
    """
    Preprocess input data for AI engine.
    Handles normalization, feature extraction, and formatting.
    """

    @staticmethod
    def normalize(data):
        """Normalize numeric data to range [0,1]."""
        data = np.array(data, dtype=float)
        return (data - np.min(data)) / (np.max(data) - np.min(data) + 1e-8)

    @staticmethod
    def extract_features(raw_input):
        """
        Example feature extraction: 
        converts text or sensor input into numerical vector.
        """
        # Dummy placeholder: length of string and ASCII sum
        if isinstance(raw_input, str):
            length = len(raw_input)
            ascii_sum = sum(ord(c) for c in raw_input)
            return np.array([length, ascii_sum], dtype=float)
        # If already numeric
        elif isinstance(raw_input, (list, np.ndarray)):
            return np.array(raw_input, dtype=float)
        else:
            raise ValueError("Unsupported input type")
