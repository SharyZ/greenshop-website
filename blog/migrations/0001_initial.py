# Generated by Django 4.0.3 on 2022-03-06 10:15

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('short_description', models.TextField()),
                ('featured_image', models.ImageField(upload_to='posts/')),
                ('full_description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
