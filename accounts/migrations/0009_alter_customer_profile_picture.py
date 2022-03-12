# Generated by Django 4.0.3 on 2022-03-12 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_customer_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_picture',
            field=models.ImageField(blank=True, default='images/default-profile-picture.svg', null=True, upload_to='profile/'),
        ),
    ]
