# Generated by Django 4.2.2 on 2023-06-07 22:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_payment_id'),
        ('ranks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RankPromotion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date', models.DateField()),
                ('belt_size', models.PositiveIntegerField()),
                ('rank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ranks.rank')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student')),
            ],
        ),
    ]
