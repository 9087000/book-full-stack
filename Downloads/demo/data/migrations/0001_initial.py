# Generated by Django 3.2.18 on 2023-05-04 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='projectdemo',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('roll_no', models.IntegerField(db_column='roll_no')),
                ('marks', models.IntegerField(db_column='marks')),
                ('strength', models.IntegerField(db_column='strength')),
            ],
            options={
                'db_table': 'masterdata"."projectdemo',
                'managed': False,
            },
        ),
    ]
