# Generated by Django 5.1 on 2024-09-07 04:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weburlsforscrape',
            name='category_name',
            field=models.CharField(default='Books', max_length=100),
        ),
        migrations.AddField(
            model_name='weburlsforscrape',
            name='url',
            field=models.TextField(default='readings.com.pk'),
        ),
        migrations.AlterField(
            model_name='weburlsforscrape',
            name='web_name',
            field=models.CharField(choices=[('KN', 'kitabnow.com'), ('VB', 'vanguardbooks.com'), ('RC', 'readings.com.pk'), ('BB', 'bookberry.com')], max_length=5),
        ),
        migrations.CreateModel(
            name='BooksRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.URLField()),
                ('url', models.URLField(unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('author', models.CharField(max_length=255)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraper.weburlsforscrape')),
            ],
        ),
    ]
