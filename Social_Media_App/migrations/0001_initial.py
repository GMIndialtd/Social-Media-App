# Generated by Django 5.0.6 on 2024-05-22 12:19

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="user_signup",
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
                ("fullname", models.CharField(max_length=255)),
                ("username", models.CharField(max_length=50, unique=True)),
                ("email", models.EmailField(max_length=100, unique=True)),
                ("password", models.CharField(max_length=255)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
