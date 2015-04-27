from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# Create your models here.

class Lo_bet(models.Model):

    # Owner
    owner = models.ForeignKey(User, blank=True, null=True)

    # Phase id
    phase = models.IntegerField()

    # time of bet
    bet_date = models.DateTimeField('time of draw lottery result')
       
    # bet is consist of 6 numbers     
    re1 = models.IntegerField(default=-1)
    re2 = models.IntegerField(default=-1)
    re3 = models.IntegerField(default=-1)
    re4 = models.IntegerField(default=-1)
    re5 = models.IntegerField(default=-1)
    re6 = models.IntegerField(default=-1)

    # status
    bet_status = models.CharField(max_length=7,
                                      default='Pending')


    def clean(self):
        if (self.re1 < 0 or self.re1 > 99) or \
           (self.re2 < 0 or self.re2 > 99) or \
           (self.re3 < 0 or self.re3 > 99) or \
           (self.re4 < 0 or self.re4 > 99) or \
           (self.re5 < 0 or self.re5 > 99) or \
           (self.re6 < 0 or self.re6 > 99):                                 
        
            raise ValidationError("bet number is invalid! It must between 0 and 99")
