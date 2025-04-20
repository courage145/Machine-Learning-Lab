
import joblib

def load_model(model_path='price_model.pkl'):
    model = joblib.load(model_path)
    return model
