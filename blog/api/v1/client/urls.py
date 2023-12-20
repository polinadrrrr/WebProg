from django.urls import path, include
from rest_framework import routers
from api.v1.client.views import  (
            UserViewSet, 
            ArticleViewSet,
            ArticleManageViewSet,
            CommentViewSet,
            CommentManageViewSet,
            CategoryViewSet,
            CategoryManageViewSet,
            ArticleOnlyPublishedViewSet,
        )


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'articles_manage', ArticleManageViewSet)
router.register(r'articles_only_published', ArticleOnlyPublishedViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'comments_manage', CommentManageViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'categories_manage', CategoryManageViewSet)


urlpatterns = [
    path('', include(router.urls)),
]