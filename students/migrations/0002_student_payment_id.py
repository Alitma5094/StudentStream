# Generated by Django 4.0.4 on 2023-06-04 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='payment_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
