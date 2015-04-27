from django.db import models
import datetime

# Create your models here.
class Lo_Result(models.Model):

    # Phase id
    phase = models.IntegerField()

    # time of lottery draw
    draw_date = models.DateTimeField('time of draw lottery result')
       
    # result is consist of 6 numbers     
    re1 = models.IntegerField(default=-1)
    re2 = models.IntegerField(default=-1)
    re3 = models.IntegerField(default=-1)
    re4 = models.IntegerField(default=-1)
    re5 = models.IntegerField(default=-1)
    re6 = models.IntegerField(default=-1)

    # Winner
    winner = models.CharField(max_length=200, default= 'NO WINNER')
    
class Lo_Result_Phase(models.Model):
    
    #current Phase
    cur_phase = models.IntegerField(default= 1)               
