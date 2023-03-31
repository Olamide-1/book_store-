# Generated by Django 4.1.6 on 2023-02-23 21:34

import book.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_alter_book_book_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.FloatField(default=2999, validators=[django.core.validators.MaxValueValidator(1000000.0), django.core.validators.MinValueValidator(1.0)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.IntegerField(default=book.models.Book.generate_id, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
