# Generated by Django 4.1.4 on 2022-12-30 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_blog_breif_info"),
    ]

    operations = [
        migrations.RenameField(
            model_name="blog",
            old_name="thubmnail",
            new_name="thumbnail",
        ),
    ]
