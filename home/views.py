from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from home.models import Setting


def index(request):
    setting = Setting.objects.get(pk=1)
    university = "Karabuk University"
    dept = "Computer Engineering"
    context = {'setting': setting}
    return render(request, 'index.html', context)
