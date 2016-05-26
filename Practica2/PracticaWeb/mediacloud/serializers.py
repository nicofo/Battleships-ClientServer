from django.contrib.auth.models import User

from .models import Item, Comment
from rest_framework import serializers


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('description', 'n ame', 'type', 'price', 'img')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('pk', 'nick', 'item', 'score', 'text', 'user')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username')

