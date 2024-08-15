from rest_framework import serializers
from .models import Article
from .documents import ArticleDocument
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'created_at']

class ArticleDocumentSerializer(DocumentSerializer):
    class Meta:
      document = ArticleDocument
      fields = [
            'title',
            'content',
        ] 