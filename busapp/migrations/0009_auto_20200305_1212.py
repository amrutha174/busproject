# Generated by Django 2.1.7 on 2020-03-05 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busapp', '0008_auto_20200305_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='welcome_form',
            name='BUSTIME',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
