import os
from random import randint
from uuid import uuid4

from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.


def store_book(model, filename):
    _, extension = os.path.splitext(filename)
    path = os.path.join("books", model.title, f'{model.title}.{extension}')
    return path


def store_cover(model, filename):
    _, extension = os.path.splitext(filename)
    path = os.path.join("books", model.title, f'{model.title}.{extension}')
    return path


class Book(models.Model):

    def generate_id():

        return randint(int("1"*15), int("9"*15))

    id = models.PositiveBigIntegerField(
        _("ID"), primary_key=True, default=generate_id)
    title = models.CharField(_("Title"), max_length=50,
                             null=False, blank=False, unique=True)
    description = models.TextField(
        _("Description"), null=False, blank=False)
    cover_page = models.ImageField(
        _("Cover Page"), null=False, blank=False, upload_to=store_cover)
    book = models.FileField(_("Book File"), null=False,
                            blank=False, upload_to=store_book)
    book_id = models.CharField(max_length=60, null=False, blank=False)
    price = models.FloatField(validators=[MaxValueValidator(
        1000000.0), MinValueValidator(1.0)], null=False, blank=False)

    def save(self, *args, **kwargs):
        if not self.book_id:
            title = self.title.lower().replace(" ", "-")
            self.book_id = f'{title}-{self.id}'

        self.full_clean()

        return super().save(*args, **kwargs)


class PurchasedBooks(models.Model):

    id = models.UUIDField(default=uuid4, primary_key=True)
    book = models.ForeignKey(
        to=Book, on_delete=models.CASCADE, related_name="purchases")
    user = models.ForeignKey(
        to=get_user_model(), on_delete=models.CASCADE, related_name="mybooks")

    def __str__(self):
        return f'{self.user}\'s {self.book}'
