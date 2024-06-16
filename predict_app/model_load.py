import os
import tensorflow as tf
import joblib

def load_model():
    app_dir = os.path.dirname(os.path.abspath(__file__))
    model_h5_path = os.path.join(
        app_dir, 'model', 'model_tingkat_stress.h5')


    scaler_pkl_path = os.path.join(app_dir, 'model', 'scaler.pkl')
    
    model = tf.keras.models.load_model(model_h5_path)

    scaler = joblib.load(scaler_pkl_path)

    return model, scaler

model, scaler = load_model()