# Generated by Django 5.0.2 on 2024-03-17 17:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('photos', '0002_alter_photo_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_photo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='photos.photo')),
            ],
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]