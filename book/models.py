import os
from random import randint
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

def store_book(model, filename):
    path = os.path.join("books", filename)
    return path

class Book(models.Model):

    id = models.IntegerField(_("ID"), primary_key=True)
    title = models.CharField(_("Title"),max_length=50, null=False, blank=False, unique=True)
    description = models.TextField(_("Description"), null=False, blank=False)
    book = models.FileField(_("Book File"), null=False, blank=False, upload_to=store_book)
    book_id = models.CharField(max_length=60, null=False, blank=False)

    def generate_id(self):

        rand_id = randint(1111111111, 9999999999)
        id = rand_id

        while(Book.objects.filter(id=id).exists()):

            rand_id = randint(1111111111, 9999999999)
            id = rand_id

        return id
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = self.generate_id()
            title = self.title.lower().replace(" ", "-")
            self.book_id = f'{title}-{self.id}'

        self.full_clean()

        return super().save(*args, **kwargs)
        