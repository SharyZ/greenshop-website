# Generated by Django 4.0.3 on 2022-03-05 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_customer_shipping_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='shipping_address',
        ),
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(blank=True, choices=[('Tashkent', 'Tashkent'), ('Samarkand', 'Samarkand'), ('Bukhara', 'Bukhara'), ('Nukus', 'Nukus')], max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='ShippingAddress',
        ),
    ]
