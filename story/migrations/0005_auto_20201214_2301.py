# Generated by Django 2.2 on 2020-12-14 14:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0004_auto_20201214_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]