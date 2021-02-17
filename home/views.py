from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from home.models import Setting, ContactForm, ContactFormMassage
from product.models import Product, Category


def index(request):
    setting = Setting.objects.get(pk=3)
    sliderdata = Product.objects.all()[:5]
    category = Category.objects.all()
    university = "Karabuk University"
    dept = "Computer Engineering"
    context = {'setting': setting,
               'sliderdata': sliderdata,
               'category': category,
               'page': 'hakkimizda'
               }
    return render(request, 'index.html', context)


def hakkimizda(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=3)
    context = {'setting': setting, 'category': category}
    return render(request, 'hakkimizda.html', context)


def referanslar(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=3)
    context = {'setting': setting,
               'category': category
               }
    return render(request, 'referanslar.html', context)


def iletisim(request):
    category = Category.objects.all()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactFormMassage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesajiniz basari ile gonderilmistir")
            return HttpResponseRedirect('/iletisim')

    setting = Setting.objects.get(pk=3)
    form = ContactForm()
    context = {'setting': setting,
                'category': category,
               'form': form}
    return render(request, 'iletisim.html', context)


def category_products(request, id, slug):
    products = Product.objects.filter(category_id=id)
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    context={ 'category': category,
              'products': products,
              'categorydata': categorydata}
    return render(request, 'products.html', context)