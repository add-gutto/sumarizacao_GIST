# Generated by Django 5.1.7 on 2025-06-02 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("secao", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="secao",
            name="imagem_nuvem",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
