# Generated by Django 4.0.4 on 2023-06-06 16:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('alt_name', models.CharField(blank=True, max_length=50, null=True)),
                ('order', models.PositiveSmallIntegerField()),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
