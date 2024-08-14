
from django.contrib.postgres.search import SearchVector
from rest_framework import viewsets
from rest_framework import filters
from django.db.models import Q
from .models import Article
from .serializers import ArticleSerializer
from .utils import normalize_query


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['translations__title', 'translations__content']

    def get_queryset(self):
        queryset = super().get_queryset()
        search_param = self.request.query_params.get('search', None)
        if search_param:
            normalized_query = normalize_query(search_param)
            queryset = queryset.filter(translations__title__icontains=normalized_query) | queryset.filter(translations__content__icontains=normalized_query)
        return queryset 