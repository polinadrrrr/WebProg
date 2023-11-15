from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    author = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True)
    
class Tag(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True)