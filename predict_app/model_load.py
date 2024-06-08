import os
import tensorflow as tf
import joblib

def load_model():
    # Get the directory where the script is located
    app_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to the model JSON file
    model_h5_path = os.path.join(
        app_dir, 'model', 'model_tingkat_stress.h5')


    scaler_pkl_path = os.path.join(app_dir, 'model', 'scaler.pkl')
    
    # Load the model from the .h5 file
    model = tf.keras.models.load_model(model_h5_path)

    scaler = joblib.load(scaler_pkl_path)

    return model, scaler


# Load the model once when the module is imported
model, scaler = load_model()