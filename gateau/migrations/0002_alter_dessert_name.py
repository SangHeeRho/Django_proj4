# Generated by Django 3.2.6 on 2021-08-11 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gateau', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dessert',
            name='name',
            field=models.CharField(db_index=True, max_length=50),
        ),
    ]
