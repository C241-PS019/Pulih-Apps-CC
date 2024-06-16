from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .model_load import model, scaler
from .serializers import StressPredictionSerializer
import pandas as pd

feature_names = [f'p{i}' for i in range(1, 11)]


def predict_stress_levels(features_dict):
    features_df = pd.DataFrame([features_dict], columns=feature_names)
    features_scaled = scaler.transform(features_df)
    predictions = model.predict(features_scaled)
    predicted_class = predictions.argmax(axis=1)[0]
    level_mapping = {0: 'Normal', 1: 'Stres ringan',
                     2: 'Stres sedang', 3: 'Stres berat', 4: 'Stres cukup berat'}
    predicted_level = level_mapping[predicted_class]
    return predicted_level


class StressPredictionView(APIView):
    def post(self, request):
        serializer = StressPredictionSerializer(data=request.data)
        if serializer.is_valid():
            features_dict = serializer.validated_data
            try:
                predicted_level = predict_stress_levels(features_dict)
                return Response({'predicted_level': predicted_level}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
