from rest_framework.serializers import ModelSerializer

from blog.models import Post


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'author'
        ]


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'author',
            'published_date',
            'image'

        ]
