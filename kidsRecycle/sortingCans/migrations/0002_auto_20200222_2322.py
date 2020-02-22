# Generated by Django 3.0.3 on 2020-02-22 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sortingCans', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='compost',
            name='filepath',
            field=models.CharField(default='kids-recycle/kidsRecycle/sortingCans/media/error.png', max_length=200),
        ),
        migrations.AddField(
            model_name='recycle',
            name='filepath',
            field=models.CharField(default='kids-recycle/kidsRecycle/sortingCans/media/error.png', max_length=200),
        ),
        migrations.AddField(
            model_name='trash',
            name='filepath',
            field=models.CharField(default='kids-recycle/kidsRecycle/sortingCans/media/error.png', max_length=200),
        ),
    ]
