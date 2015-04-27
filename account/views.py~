from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from forms import MyRegistrationForm, Lo_betForm
from draw.models import Lo_Result_Phase
from models import Lo_bet

import datetime

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/account/loggedin')
    else:
        return HttpResponseRedirect('/account/invalid')

def loggedin(request):
    return render_to_response('loggedin.html',
                              RequestContext(request))

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/account/register_success')

    args = {}
    args.update(csrf(request))
    args['form'] = MyRegistrationForm()
        
    return render_to_response('register.html', args)

def register_success(request):
    return render_to_response('register_success.html')

@login_required
def bet(request):
    if request.POST:
        form = Lo_betForm(request.POST)
        if form.is_valid():
            bet_form = form.save(commit=False)
            bet_form.owner = request.user
            bet_form.phase = get_current_phase()
            bet_form.bet_date = datetime.datetime.now()
            bet_form.save()
            
            return HttpResponseRedirect('/account/bet_record')
    else:
        form = Lo_betForm()
    
    args = {}
    args.update(csrf(request))
    args['form'] = form

    return render_to_response('create_bet.html', args,
                               RequestContext(request))

@login_required
def bet_record(request):
    return render_to_response('bet_record.html',
                  {'bets': Lo_bet.objects.filter(owner = request.user)})

def get_current_phase():

    result_phase = Lo_Result_Phase.objects.get(id=1)
    
    return result_phase.cur_phase

