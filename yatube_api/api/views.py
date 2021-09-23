from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import viewsets, permissions, filters, mixins
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Group, Post

from .serializers import (GroupSerializer, PostSerializer, CommentSerializer,
                          FollowSerializer)
from .permissions import OwnerOrReadOnly

User = get_user_model()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    pagination_class = LimitOffsetPagination
    permission_classes = (OwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    permission_classes = (OwnerOrReadOnly,)

    @property
    def __post(self):
        post_id = self.kwargs.get('post_id')
        return get_object_or_404(Post, id=post_id)

    def get_queryset(self):
        post = self.__post
        return post.comments.all()

    def perform_create(self, serializer):
        post = self.__post
        serializer.save(author=self.request.user, post=post)


class ListCreateViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    pass


class FollowViewSet(ListCreateViewSet):
    serializer_class = FollowSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        user = self.request.user
        return user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
