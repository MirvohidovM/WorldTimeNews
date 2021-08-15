from rest_framework import serializers
from bosh_sahifa.models import Category, News

class CatSer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class NewsSer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'