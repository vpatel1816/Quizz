# Generated by Django 3.0.6 on 2020-05-31 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='quiz_que',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('answer1', models.CharField(max_length=50)),
                ('answer2', models.CharField(max_length=50)),
                ('answer3', models.CharField(max_length=50)),
                ('answer4', models.CharField(max_length=50)),
                ('ans', models.CharField(max_length=1)),
                ('gans', models.CharField(max_length=1)),
            ],
        ),
    ]
