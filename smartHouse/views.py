from django.template import RequestContext, loader
from .models import *
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse


from django.template import RequestContext
from .forms import *





def result(request):
    s=request.POST.getlist('rooms')
    rooms=room.objects.all()
    for a in rooms:
        if s.count(str(a.pk))==1:
            a.state=True
        else:
            a.state=False
        a.save()


    return HttpResponseRedirect('/smarthouse/')


# Create your views here.
def index(request):
    rooms = room.objects.all()
    return render(request,'smartHouse/index.html',{'rooms_list': rooms})

