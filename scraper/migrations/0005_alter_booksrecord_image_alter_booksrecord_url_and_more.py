# Generated by Django 5.1 on 2024-09-08 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0004_alter_weburlsforscrape_web_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksrecord',
            name='image',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='booksrecord',
            name='url',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='weburlsforscrape',
            name='web_name',
            field=models.CharField(choices=[('LB', 'libertybooks.com'), ('RC', 'readings.com.pk'), ('BB', 'bookberry.com'), ('VB', 'vanguardbooks.com'), ('KN', 'kitabnow.com'), ('GB', 'globalbooks.com')], max_length=5),
        ),
    ]
