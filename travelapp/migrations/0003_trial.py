# Generated by Django 4.1.3 on 2022-12-02 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_members'),
    ]

    operations = [
        migrations.CreateModel(
            name='trial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
    ]
