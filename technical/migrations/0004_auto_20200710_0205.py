# Generated by Django 2.1.5 on 2020-07-09 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('technical', '0003_auto_20200710_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='technical.Category'),
        ),
        migrations.DeleteModel(
            name='laptopCategory',
        ),
    ]