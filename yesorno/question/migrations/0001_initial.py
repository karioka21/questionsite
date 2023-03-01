# Generated by Django 4.1.7 on 2023-03-01 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('answer_yes', models.CharField(max_length=25)),
                ('answer_no', models.CharField(max_length=25)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
