# Generated by Django 4.1.4 on 2022-12-29 07:04

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="content",
            field=tinymce.models.HTMLField(),
        ),
    ]
