# Generated by Django 3.2.12 on 2022-06-23 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0003_delete_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewimage',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.review'),
        ),
    ]
