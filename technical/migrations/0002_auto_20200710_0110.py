# Generated by Django 2.1.5 on 2020-07-09 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technical', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description1',
            new_name='description5',
        ),
        migrations.AddField(
            model_name='product',
            name='description6',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description7',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description8',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description9',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_made_in',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]