from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog_view),
    path('post/', views.post_view),
]