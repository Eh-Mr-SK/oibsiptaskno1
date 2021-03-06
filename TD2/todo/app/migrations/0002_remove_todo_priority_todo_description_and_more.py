# Generated by Django 4.0.4 on 2022-05-28 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='priority',
        ),
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('C', 'COMPLETED'), ('P', 'PENDING')], max_length=2),
        ),
    ]
