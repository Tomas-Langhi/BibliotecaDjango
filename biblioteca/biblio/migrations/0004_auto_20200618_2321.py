# Generated by Django 2.2 on 2020-06-18 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblio', '0003_auto_20200618_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ejemplar',
            name='libro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblio.Libro'),
        ),
    ]
