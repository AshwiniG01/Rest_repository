# Generated by Django 3.0.2 on 2020-10-27 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=50)),
                ('student_phone_no', models.IntegerField()),
                ('student_mail_id', models.CharField(max_length=50)),
                ('student_address', models.CharField(max_length=50)),
            ],
        ),
    ]