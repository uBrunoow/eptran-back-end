from rest_framework import serializers
from .models import News, SavedNews

class NewsReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ["id", "title", "subtitle", "first_paragraph", "second_paragraph", "third_paragraph", "fourth_paragraph", "fifth_paragraph", "image","created_at", "updated_at"]

class SavedNewsReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedNews
        fields = ["id", "user", "news", "created_at", "updated_at"]