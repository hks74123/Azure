# Generated by Django 4.0.3 on 2022-04-01 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0005_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Pending', 'pending'), ('Success', 'success')], default=('Pending', 'pending'), max_length=25),
        ),
    ]