from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.
def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    latest_question_list=[1,2,3,4,5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return HttpResponse(template.render(context))


def detail(request,img_id):
    return  HttpResponse("You're looking at question %s." % img_id)

def results(request, img_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % img_id)

def vote(request, img_id):
    return HttpResponse("You're voting on question %s." % img_id)