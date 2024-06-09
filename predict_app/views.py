from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .model_load import model, scaler
from .serializers import StressPredictionSerializer
import pandas as pd

# Generate feature names dynamically
feature_names = [f'p{i}' for i in range(1, 11)]

def predict_stress_levels(features_dict):
    # Convert input to DataFrame
    features_df = pd.DataFrame([features_dict], columns=feature_names)
    # Scale the features
    features_scaled = scaler.transform(features_df)
    # Predict using the model
    predictions = model.predict(features_scaled)
    # Get the index of the highest probability class
    predicted_class = predictions.argmax(axis=1)[0]
    # Map the predicted class to the corresponding stress level
    level_mapping = {0: 'Normal', 1: 'Stres ringan',
                     2: 'Stres sedang', 3: 'Stres berat', 4: 'Stres cukup berat'}
    # Convert predicted class index to stress level
    predicted_level = level_mapping[predicted_class]
    return predicted_level

class StressPredictionView(APIView):
    def post(self, request):
        serializer = StressPredictionSerializer(data=request.data)
        if serializer.is_valid():
            features_dict = serializer.validated_data
            try:
                # Predict stress level
                predicted_level = predict_stress_levels(features_dict)
                # Return the predicted level
                return Response({'predicted_level': predicted_level}, status=status.HTTP_200_OK)
            except Exception as e:
                # Handle any errors during prediction
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            # Handle invalid input data
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
