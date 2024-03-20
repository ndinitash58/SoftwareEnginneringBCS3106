# Generated by Django 5.0.2 on 2024-02-20 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('picture', models.ImageField(upload_to='candidates_pictures/')),
                ('position', models.CharField(choices=[('president', 'President'), ('vice_president', 'President'), ('secretary', 'Secretary'), ('Clerk', 'Clerk')], max_length=30)),
            ],
        ),
    ]
