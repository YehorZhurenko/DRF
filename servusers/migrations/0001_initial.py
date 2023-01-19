# Generated by Django 4.1.5 on 2023-01-19 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spec_type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Servuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('sname', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=30)),
                ('spec', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='servusers.spec')),
            ],
        ),
    ]
