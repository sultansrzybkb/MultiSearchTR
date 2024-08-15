
from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer
from content.filters import CustomSearchFilter
from content.documents import ArticleDocument
from content.filters import CustomSearchFilter
from django_elasticsearch_dsl_drf.filter_backends import FilteringFilterBackend, OrderingFilterBackend, DefaultOrderingFilterBackend, SearchFilterBackend
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.constants import SUGGESTER_COMPLETION
from .documents import ArticleDocument
from .serializers import ArticleDocumentSerializer
from django_elasticsearch_dsl_drf.filter_backends import SuggesterFilterBackend
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [CustomSearchFilter]
    search_fields = ['translations__title', 'translations__content']


class ArticleDocumentView(DocumentViewSet):
    document = ArticleDocument
    serializer_class = ArticleDocumentSerializer
    lookup_field = 'id'
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
        SuggesterFilterBackend
        
    ]
    
    
    search_fields = (
        'title',
        'content',
    )

    filter_fields = {
        'title': 'title',
        'content': 'content',
    }

 
    ordering_fields = {
        'id': 'id',
        'created_at': 'created_at',
    }

    suggester_fields = {
        'title': {
            'field': 'title.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
            ],
        },
    }
