from django.shortcuts import render_to_response
from django.template import RequestContext

from draw.models import Lo_Result 


def home(request):
    return render_to_response('home.html',
                  {'results': Lo_Result.objects.all()},
                    RequestContext(request))
