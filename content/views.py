
from django.contrib.postgres.search import SearchVector
from rest_framework import viewsets

from rest_framework import filters
from django.db.models import Q

from content.filters import CustomSearchFilter
from .models import Article
from .serializers import ArticleSerializer
from .utils import normalize_query


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    filter_backends = [CustomSearchFilter]
    search_fields = ['translations__title', 'translations__content']

    
    
