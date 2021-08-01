# Generated by Django 3.2.4 on 2021-07-28 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thirdeyes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageTb',
            fields=[
                ('img_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('date_time', models.DateField()),
                ('img', models.ImageField(upload_to='images/')),
            ],
            options={
                'db_table': 'image_tb',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
