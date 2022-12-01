from django.urls import path
from users import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('api/users/', views.UserList.as_view(), name='users-api-list'),
    path('api/users/<int:pk>/', views.UserDetail.as_view(), name='users-api-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
