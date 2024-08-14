from rest_framework import filters
from django.db.models import Q, Func
from .utils import normalize_query

class Unaccent(Func):
    function = 'unaccent'

class CustomSearchFilter(filters.SearchFilter):
    def filter_queryset(self, request, queryset, view):
        search_param = request.query_params.get('search', None)
        if search_param:
            normalized_query = normalize_query(search_param)
            
            queryset = queryset.filter(
                Q(translations__title__unaccent__icontains=normalized_query)  |
                Q(translations__content__unaccent__icontains=normalized_query)
            )
            print()
        return queryset