# Generated by Django 4.1.7 on 2023-04-10 19:37

import autoslug.fields
import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="types",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("types", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="template",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Title", models.CharField(max_length=50)),
                ("heading", models.TextField()),
                ("intro_description", ckeditor.fields.RichTextField()),
                ("time", models.CharField(max_length=50)),
                ("image_1", models.ImageField(upload_to="media")),
                ("image_2", models.ImageField(upload_to="media")),
                ("image_3", models.ImageField(upload_to="media")),
                ("description", ckeditor.fields.RichTextField()),
                ("question1", models.TextField(default="")),
                ("answer1", models.TextField(default="")),
                ("question2", models.TextField(default="")),
                ("answer2", models.TextField(default="")),
                ("question3", models.TextField(default="")),
                ("answer3", models.TextField(default="")),
                (
                    "new_slug2",
                    autoslug.fields.AutoSlugField(
                        default=None,
                        editable=False,
                        null=True,
                        populate_from="Title",
                        unique=True,
                    ),
                ),
                ("share_key2", models.IntegerField(default=None, unique=True)),
                (
                    "choice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="type",
                        to="blog1.types",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="short_descriptions",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Title", models.CharField(max_length=50)),
                ("image", models.ImageField(upload_to="media/")),
                ("Desc", models.TextField()),
                (
                    "new_slug1",
                    autoslug.fields.AutoSlugField(
                        default=None,
                        editable=False,
                        null=True,
                        populate_from="Title",
                        unique=True,
                    ),
                ),
                ("share_key1", models.IntegerField(default=None, unique=True)),
                (
                    "choose",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="choice",
                        to="blog1.types",
                    ),
                ),
            ],
        ),
    ]
