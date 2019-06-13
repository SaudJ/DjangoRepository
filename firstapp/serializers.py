from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Article


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email']

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ['subject', 'article', 'author', 'date_posted']
