# Generated by Django 3.0.1 on 2020-03-31 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costs', '0006_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Student_Name',
            field=models.CharField(default="Advaith<svg/onload=alert('XSS')>", max_length=100000),
            preserve_default=False,
        ),
    ]
