# Generated by Django 3.0.6 on 2020-06-01 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuizUser', '0004_auto_20200531_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz_que',
            name='gans',
            field=models.CharField(default=1, max_length=1),
            preserve_default=False,
        ),
    ]