# Generated by Django 3.0.6 on 2020-06-02 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0004_auto_20200601_0857'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='job_title',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
