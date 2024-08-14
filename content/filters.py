from rest_framework import filters
from django.db.models import Q
from .utils import normalize_query

class CustomSearchFilter(filters.SearchFilter):
    def filter_queryset(self, request, queryset, view):
        search_param = request.query_params.get('search', None)
        if search_param:
            normalized_query = normalize_query(search_param)
            normalized_query_tr = normalize_query(search_param, True)
            
            queryset = queryset.filter(
                Q(translations__title__icontains=normalized_query) | Q(translations__title__icontains=normalized_query_tr) |
                Q(translations__content__icontains=normalized_query) | Q(translations__content__icontains=normalized_query_tr)
            )
        return queryset