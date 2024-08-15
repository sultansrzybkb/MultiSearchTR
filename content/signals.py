from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django_elasticsearch_dsl.registries import registry
from .models import Article

@receiver(post_save, sender=Article)
def update_document(sender, instance, **kwargs):
    print(f"Post-save signal triggered for Article ID: {instance.id}")
    for translation in instance.translations.all():
        print(f"Updating document for translation ID: {translation.id}")
        registry.update(instance)

@receiver(post_delete, sender=Article)
def delete_document(sender, instance, **kwargs):
    print(f"Post-delete signal triggered for Article ID: {instance.id}")
    for translation in instance.translations.all():
        print(f"Deleting document for translation ID: {translation.id}")
        registry.delete(instance, raise_on_error=False)