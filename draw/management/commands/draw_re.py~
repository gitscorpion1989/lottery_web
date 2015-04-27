from django.core.management.base import BaseCommand
from django.utils import timezone

from draw.models import Lo_Result, Lo_Result_Phase
from account.models import Lo_bet

import random

# constant number to give to lottery result 
RE1 = 1
RE2 = 2 
RE3 = 3
RE4 = 4
RE5 = 5
RE6 = 6

class Command(BaseCommand):
    
    
    def add_arguments(self, parser):

        parser.add_argument('--debug', action='store_true', default=False, \
                             help='give constant variable to lottery for debug')
            
    def handle(self, *args, **options):
        
        if not Lo_Result_Phase.objects.all():
            count_phase = Lo_Result_Phase(cur_phase = 1)
        else:
            count_phase = (Lo_Result_Phase.objects.all())[0]
        
        if options['debug']:

            result = Lo_Result(phase= count_phase.cur_phase, \
                           re1 =RE1, re2=RE2, re3=RE3, re4=RE4, re5=RE5, re6=RE6,
                           draw_date=timezone.now())                 
        else:       
            result = Lo_Result(phase= count_phase.cur_phase, \
                               re1 = random.randint(0,99), \
                               re2 = random.randint(0,99), \
                               re3 = random.randint(0,99), \
                               re4 = random.randint(0,99), \
                               re5 = random.randint(0,99), \
                               re6 = random.randint(0,99), \
                               draw_date=timezone.now())
        
        win_set = self.generate_result_set(result)
        winner_list = []
        # loop in current phase bets to find winner
        for bet in Lo_bet.objects.filter(phase= count_phase.cur_phase):
            if self.generate_result_set(bet) == win_set:
                winner_list.append(bet.owner.username)
                #set status in bet
                bet.bet_status = "Win!"
                bet.save()

            else:
                #set status in bet
                bet.bet_status = "Miss!"
                bet.save()       
        
        # remove duplicates and convert into string
        if winner_list:
            result.winner=', '.join(sorted(set(winner_list)))
        
        result.save()
        
        count_phase.cur_phase = count_phase.cur_phase + 1
        count_phase.save()                   

    def generate_result_set(self, result):
        
        # use set to store lottery 6 number without order
        re_set = set()
        re_set.update([result.re1, result.re2, result.re3, result.re4, result.re5, result.re6])
        return re_set 


        
