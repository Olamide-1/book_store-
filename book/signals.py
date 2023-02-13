from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Book

@receiver(post_delete, sender=Book)
def delete_book(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    try:
        instance.book.delete(save=False)
    except:
        pass