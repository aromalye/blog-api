from rest_framework import serializers
from .models import Post
from accounts.models import Account
from taggit.serializers import (TagListSerializerField, TaggitSerializer)

class AccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('username', 'id')


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    author = AccountSerializers(many=False)
    tags = TagListSerializerField()
    class Meta:
        fields = '__all__'
        model = Post