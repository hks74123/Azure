# Generated by Django 4.0.3 on 2022-04-06 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0006_alter_order_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Pending', 'pending'), ('Success', 'success')], default='Pending', max_length=25),
        ),
    ]
