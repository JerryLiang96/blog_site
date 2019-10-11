from rest_framework import serializers
from .models import Blog, Tag, Image, Category


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=True)
    image = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ('id', 'title', 'body', 'tag', 'image', 'modified_time')
