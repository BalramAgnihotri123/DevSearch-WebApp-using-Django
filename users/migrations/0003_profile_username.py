# Generated by Django 4.1 on 2023-03-25 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_profile_bio_profile_github_link_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="username",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
