# Generated by Django 3.1 on 2023-01-21 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servusers', '0004_auto_20230121_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servusers',
            name='spec',
            field=models.CharField(max_length=30),
        ),
        migrations.DeleteModel(
            name='Specs',
        ),
    ]
