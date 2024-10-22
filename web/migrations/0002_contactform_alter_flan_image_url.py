# Generated by Django 5.1.2 on 2024-10-22 17:18

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactForm",
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
                (
                    "contact_form_uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("customer_email", models.EmailField(max_length=254)),
                ("customer_name", models.CharField(max_length=64)),
                ("message", models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name="flan",
            name="image_url",
            field=models.TextField(),
        ),
    ]
