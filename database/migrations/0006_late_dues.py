# Generated by Django 3.0.1 on 2020-03-31 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_auto_20200330_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='Late_dues',
            fields=[
                ('student_id', models.PositiveIntegerField()),
                ('Ind_Book_ID', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('return_date', models.DateField()),
                ('delay', models.PositiveIntegerField()),
                ('Link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Issues')),
            ],
        ),
    ]
