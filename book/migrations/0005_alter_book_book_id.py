# Generated by Django 4.1.6 on 2023-02-13 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_book_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_id',
            field=models.CharField(default='aa', max_length=60),
            preserve_default=False,
        ),
    ]