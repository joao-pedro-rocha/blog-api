from django.urls import path
from posts import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('<int:post_id>/', views.post_detail, name='post-detail'),
    path('api/list/', views.api_root),
    path('api/posts/', views.PostAPIList.as_view(), name='posts-api-list'),
    path('api/posts/<int:pk>/', views.PostAPIDetail.as_view(), name='posts-api-detail'),
    path('posts/<int:post_id>/comments/<int:comment_id>/like/', views.like, name='increment-like'),
    path('api/comments/', views.CommentAPIList.as_view(), name='comments-api-list'),
    path('api/comments/<int:pk>/', views.CommentAPIDetail.as_view(), name='posts-api-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
