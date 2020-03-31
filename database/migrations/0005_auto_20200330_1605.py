# Generated by Django 3.0.1 on 2020-03-30 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_auto_20200330_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_ind',
            name='Link',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='database.books'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='issues',
            name='Link',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='database.books'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book_ind',
            name='ISBN',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='issues',
            name='ISBN',
            field=models.PositiveIntegerField(),
        ),
    ]