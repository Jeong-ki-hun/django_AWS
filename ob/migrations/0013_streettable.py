# Generated by Django 4.1.2 on 2022-11-10 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ob', '0012_resttable_food_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='streetTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('count', models.CharField(blank=True, max_length=255, null=True)),
                ('time', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
