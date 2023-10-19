from rest_framework import serializers
from .models import Article, Comment, Topic


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class ArticleListSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True, read_only=True)


    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'topics',)


class ArticleSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()


    def get_comments(self, obj):
        comments = obj.comment_set.all()
        return [{
            'id': comment.id,
            'content': comment.content,
        } for comment in comments]


    class Meta:
        model = Article
        fields = '__all__'

