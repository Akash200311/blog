# Generated by Django 4.1.7 on 2023-04-10 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog1", "0002_remove_template_heading"),
    ]

    operations = [
        migrations.AddField(
            model_name="template",
            name="heading",
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
