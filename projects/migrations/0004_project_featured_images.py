# Generated by Django 4.1 on 2023-03-23 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0003_alter_tag_tag_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="featured_images",
            field=models.ImageField(
                blank=True, default="default.jpg", null=True, upload_to=""
            ),
        ),
    ]
