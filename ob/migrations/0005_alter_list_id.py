# Generated by Django 4.0.8 on 2022-11-06 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ob', '0004_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
