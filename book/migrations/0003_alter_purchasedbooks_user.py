# Generated by Django 4.1.6 on 2023-04-09 09:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0002_purchasedbooks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasedbooks',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mybooks', to=settings.AUTH_USER_MODEL),
        ),
    ]