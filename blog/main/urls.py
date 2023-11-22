from django.urls import path
from main import views

urlpatterns = [
    path('main/', views.article_list),
    path('main/<int:pk>/', views.article_detail),
]