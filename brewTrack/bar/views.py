from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Bar

def index(request):
    bar_list = Bar.objects.order_by('id')
    # template = loader.get_template('bar/index.html')
    context = {
        'bar_list': bar_list,
    }
    return render(request, 'bar/index.html', context)

def bar(request, bar_id):
    bar = get_object_or_404(Bar, pk=bar_id)
    response = "You're looking at bar %s."
    return render(request, 'bar/barhome.html', {'bar': bar})

def next(request, bar_id):
    return HttpResponse("You're look at another page for %s." % bar_id)
