# Generated by Django 2.2.1 on 2019-07-20 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctordata',
            name='Time',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
