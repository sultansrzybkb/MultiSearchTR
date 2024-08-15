from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django_elasticsearch_dsl.registries import registry
from .models import Article

@receiver(post_save, sender=Article)
def update_document(sender, instance, **kwargs):
   
    for translation in instance.translations.all():
        registry.update(instance)

@receiver(post_delete, sender=Article)
def delete_document(sender, instance, **kwargs):
  
    for translation in instance.translations.all():
        registry.delete(instance, raise_on_error=False)