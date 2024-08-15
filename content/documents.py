
from django_elasticsearch_dsl import Document,fields
from django_elasticsearch_dsl.registries import registry
from .models import Article

@registry.register_document
class ArticleDocument(Document):
    id = fields.IntegerField(attr='id')
    class Index:
        name = 'content'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = Article
        fields = ['created_at']

    title = fields.TextField(
        attr='title',
        fields={
            'raw': fields.KeywordField(),
            'suggest': fields.CompletionField(),
        }
    )
    content = fields.TextField(
        attr='content',
        fields={
            'raw': fields.KeywordField()
        }
    )
        