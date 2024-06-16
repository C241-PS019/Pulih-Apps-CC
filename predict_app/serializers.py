from rest_framework import serializers
from django.core.validators import MinValueValidator, MaxValueValidator


class StressPredictionSerializer(serializers.Serializer):
    p1 = serializers.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)])
    p2 = serializers.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)])
    p3 = serializers.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)])
    p4 = serializers.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)])
    p5 = serializers.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)])
    p6 = serializers.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)])
    p7 = serializers.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)])
    p8 = serializers.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)])
    p9 = serializers.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)])
    p10 = serializers.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)])
