# Generated by Django 4.0.2 on 2022-02-25 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0002_women_user_alter_women_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='women',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]