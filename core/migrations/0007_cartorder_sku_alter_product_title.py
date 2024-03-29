# Generated by Django 4.2.3 on 2023-08-20 22:45

from django.db import migrations, models
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_vendor_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorder',
            name='sku',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', blank=True, length=5, max_length=20, null=True, prefix='SKU'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(default='Fresh Pear', max_length=100),
        ),
    ]
