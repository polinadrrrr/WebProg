from django.urls import path, include
from rest_framework import routers
from api.v1.client.views import (
    UserViewSet, 
    ArticleViewSet, 
    CommentViewSet, 
    CategoryViewSet,
    ArticleOnlyPublishedViewSet )


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'articles_published', ArticleOnlyPublishedViewSet)

urlpatterns = [
    path('', include(router.urls)),
]