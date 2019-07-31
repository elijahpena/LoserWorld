from django.urls import path
from . import views

app_name = 'social'

urlpatterns = [
        path('', views.PostListView.as_view(), name='home'),
        path('create/', views.create_post, name='post_create'),
        path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
        ]
