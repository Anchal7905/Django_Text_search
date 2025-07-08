# api/serializers.py
from rest_framework import serializers

class TextSearchSerializer(serializers.Serializer):
    text = serializers.CharField()
    keyword = serializers.CharField()
