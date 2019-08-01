from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'social'

urlpatterns = [
        path('', views.PostListView.as_view(), name='home'),
        path('post_create/', views.PostCreateView.as_view(), name='post_create'),
        path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
        path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
        path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
        path('post/<int:post_id>/comment_create/', views.CommentCreateView.as_view(), name='comment_create'),
        path('post/<int:post_id>/comment/<int:pk>/', views.CommentDetailView.as_view(), name='comment_detail'),
        path('post/<int:post_id>/comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),
        path('post/<int:post_id>/comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
        path('post/<int:post_id>/comments/', views.CommentListView.as_view(), name='comments'),
        #path('comments/', views.CommentListView.as_view(), name='comments'),
        ]
