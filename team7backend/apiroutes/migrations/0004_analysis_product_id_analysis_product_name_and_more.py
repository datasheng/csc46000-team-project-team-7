# Generated by Django 5.1.1 on 2024-12-16 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiroutes', '0003_analysis'),
    ]

    operations = [
        migrations.AddField(
            model_name='analysis',
            name='product_id',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='analysis',
            name='product_name',
            field=models.CharField(default='Samsung Galaxy S24 Ultra', max_length=255),
        ),
        migrations.AddField(
            model_name='review',
            name='product_id',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='review',
            name='product_name',
            field=models.CharField(default='Samsung Galaxy S24 Ultra', max_length=255),
        ),
    ]
