# Generated by Django 4.2.7 on 2024-01-28 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Purpose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Realform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('Dob', models.DateField(max_length=40)),
                ('AGE', models.IntegerField(max_length=100)),
                ('GENDER', models.CharField(max_length=13)),
                ('PHONE_NUMBER', models.IntegerField(max_length=23)),
                ('EMAIL', models.EmailField(max_length=25)),
                ('ADDRESS', models.TextField(max_length=200)),
                ('Material', models.CharField(max_length=60)),
                ('Courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collegestore.courses')),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collegestore.department')),
                ('Purpose', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collegestore.purpose')),
            ],
        ),
        migrations.AddField(
            model_name='courses',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collegestore.department'),
        ),
    ]
