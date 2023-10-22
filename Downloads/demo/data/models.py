from django.db import models

# Create your models here.

class projectdemo(models.Model):
    id = models.AutoField(primary_key=True,db_column='id')
    roll_no = models.FloatField(db_column='roll_no')
    marks = models.FloatField(db_column='marks')
    strength = models.FloatField(db_column='strength')

    class Meta:
        managed = False
        db_table = 'masterdata\".\"projectdemo'
