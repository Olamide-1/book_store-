import os
from random import randint
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.

def store_book(model, filename):
    path = os.path.join("books", filename)
    return path

class Book(models.Model):


    def generate_id():

        return randint(int("1"*15), int("9"*15))

    id = models.IntegerField(_("ID"), primary_key=True, default=generate_id)
    title = models.CharField(_("Title"),max_length=50, null=False, blank=False, unique=True)
    description = models.TextField(_("Description"), null=False, blank=False)
    book = models.FileField(_("Book File"), null=False, blank=False, upload_to=store_book)
    book_id = models.CharField(max_length=60, null=False, blank=False)
    price = models.FloatField(validators=[MaxValueValidator(1000000.0), MinValueValidator(1.0)], null=False, blank=False)

    
    def save(self, *args, **kwargs):
        if not self.book_id:
            title = self.title.lower().replace(" ", "-")
            self.book_id = f'{title}-{self.id}'

        self.full_clean()

        return super().save(*args, **kwargs)
        