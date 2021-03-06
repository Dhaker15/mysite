# Generated by Django 2.1.5 on 2020-07-09 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('technical', '0002_auto_20200710_0110'),
    ]

    operations = [
        migrations.CreateModel(
            name='laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('price', models.CharField(default='', max_length=50)),
                ('description_made_in', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('description2', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('description3', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('description4', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('description5', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('description6', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('description7', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('description8', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('description9', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('image', models.ImageField(default='', upload_to='uploads/products/')),
            ],
        ),
        migrations.CreateModel(
            name='laptopCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='laptop',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='technical.laptopCategory'),
        ),
    ]
