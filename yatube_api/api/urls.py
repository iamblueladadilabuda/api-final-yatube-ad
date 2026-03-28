from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (PostViewSet,
                    CommentViewSet,
                    GroupViewSet, FollowViewSet)

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register('follow', FollowViewSet, basename='follow')

posts_router = DefaultRouter()
posts_router.register(r'posts/(?P<post_id>\d+)/comments',
                      CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(posts_router.urls)),
]
