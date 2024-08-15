from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from content.views import ArticleDocumentView, ArticleViewSet
router = DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'article-search', ArticleDocumentView, basename='article-search')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]