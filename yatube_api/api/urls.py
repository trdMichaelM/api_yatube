from django.urls import path, include

from rest_framework import routers

from .views import GroupViewSet, PostViewSet, CommentViewSet, FollowViewSet

router = routers.DefaultRouter()
router.register(r'v1/groups', GroupViewSet)
router.register(r'v1/posts', PostViewSet)
router.register(r'v1/follow', FollowViewSet, basename='follow')
router.register(r'v1/posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
