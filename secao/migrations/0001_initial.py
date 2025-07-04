# Generated by Django 5.1.7 on 2025-05-21 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Secao",
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
                ("nome", models.CharField(max_length=100)),
                ("texto_resposta", models.TextField(blank=True)),
                (
                    "tipo_entrada",
                    models.CharField(
                        choices=[("url", "URL"), ("file", "Arquivo")], max_length=10
                    ),
                ),
                ("url", models.URLField(blank=True, null=True)),
                (
                    "arquivo",
                    models.FileField(blank=True, null=True, upload_to="uploads/"),
                ),
            ],
        ),
    ]
