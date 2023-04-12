# Generated by Django 4.1 on 2023-04-12 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_alter_profile_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="profile_image",
            field=models.ImageField(
                blank=True,
                default="https://res.cloudinary.com/dnoomtyyx/image/upload/v1681232648/static/images/profiles/user-default.bf40b0e86c9d.png",
                null=True,
                upload_to="profiles/",
            ),
        ),
    ]
