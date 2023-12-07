from rest_framework import serializers
from main.models import User, Article, Comment, Category


class UserSerializer(serializers.ModelSerializer):
    """User serializer class"""
    class Meta:
        model = User
        fields = [
            'id', 
            'name'
        ]

class CommentSerializer(serializers.ModelSerializer):
    """Comment serializer class"""
    class Meta:
        model = Comment
        fields = [
            'id', 
            'user', 
            'text', 
            'created_at',
            'article'
        ]

class ArticleSerializer(serializers.ModelSerializer):
    """Article serializer class"""
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = [
            'id', 
            'title', 
            'text', 
            'created_at',
            'category',
            'published',
            'comments'
        ]

class CategorySerializer(serializers.ModelSerializer):
    """Category serializer class"""
    class Meta:
        model = Category
        fields = [
            'id', 
            'name',
            'description'
        ]