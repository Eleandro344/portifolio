# Generated by Django 5.1.1 on 2024-09-04 17:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projetos", "0003_projeto_imagem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projeto",
            name="imagem",
            field=models.ImageField(
                blank=True, null=True, upload_to="projetos/imagem/"
            ),
        ),
    ]
