# Generated by Django 5.1.5 on 2025-01-21 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe', '0003_rename_recipe_recipe_images_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directions',
            name='group_number',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='directions',
            name='number',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='group_number',
            field=models.IntegerField(default=1),
        ),
    ]
