from rest_framework import routers

from django.contrib import admin
from django.urls import include, path

from api.views import PostViewSet, GroupViewSet, CommentViewSet
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
