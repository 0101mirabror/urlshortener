from django.http import Http404
from django.shortcuts import render , redirect
from .forms import InputForm, ContactForm#, ReportForm
from .models import User, Report
import pyshorteners
import random
from .my_function import check_email , check_value
# Create your views here.
from django.forms import URLField, ValidationError

def validate_url(url):
    url_form_field = URLField()
    try:
        url = url_form_field.clean(url)
    except ValidationError:
        return False
    return True

def report(request):
    context = {}
    a = int(random.randint(0,9))
    b = int(random.randint(0,9))
    print(request.POST)
    if request.method == 'POST':
        data = request.POST 
        if validate_url(data.get('shorturl')):
            if check_value(int(data.get('a')), int(data.get('b')), int(data.get('captcha'))):
                print(check_value(int(data.get('a')), int(data.get('b')), int(data.get('captcha'))))
                report = Report.objects.create(
                    shorturl = data.get('shorturl'),
                    email = data.get('email'),
                    message = data.get('message')
                )
                redirect('/shorturl')
        else:
            print(False)
    else:
        print("method isn't POST")
    context['num'] = {
        'a' : a,
        'b' : b
    }
    print(context['num'])
    return  render(request, 'malicious.html', context)
    
def contact(request):
    context = {}
    form = ContactForm(request.POST or None)
    data = request.POST
    print('data:', data)
    a = int(random.randint(0,9))
    b = int(random.randint(0,9))
    context = {'form': form,
               'num': {'a': a, 'b': b}    
                    }
    if form.is_valid():
        print(form.is_valid())
        if check_value(int(data.get('a')), int(data.get('b')), int(data.get('captcha'))):
            print(check_value(int(data.get('a')), int(data.get('b')), int(data.get('captcha'))))
            data = User.objects.create(
                name = data.get('name'),
                email = data.get('email'),
                message = data.get('message')
            )
    return render(request, 'contact.html', context)


def main(request):
    context ={}
    context['form']= InputForm()
    if request.method == "GET":
        # print(request.GET.get('url'))
        if request.GET and len(request.GET.get('url')) > 0:
            print("URL", request.GET.get('url') )
            try:
                long_url =   request.GET.get('url')
                context['url'] = long_url
                type_tiny = pyshorteners.Shortener()
                context['short_url']  = type_tiny.tinyurl.short(long_url)
                print(type_tiny.tinyurl.short(long_url))
                return render(request, 'short_url.html', context)
            except Exception as e:
                print('Url is not valid')
                redirect('/shorturl')
    else:
        print(request.method, "\nNWORK")
    return  render(request,'landing_page.html', context)

def counter(request):
    context = {}
    if request.method == 'GET':
        a = int(random.randint(0, 9))
        b = int(random.randint(0, 9))
        print(request.GET)
    else:
        print(request.method)
    num = {
        'a' : a,
        'b' : b
    }
    print(num)
    return  render(request,'click_counter.html' )

# def report(request):
#     context = {}
#     # context['form'] = ReportForm()
#     a = int(random.randint(0,9))
#     b = int(random.randint(0,9))
#     print(request.GET)
     
#     context['num'] = {
#         'a' : a,
#         'b' : b
#     }
#     print(context['num'])
#     return  render(request, 'malicious.html', context)

def terms(request):
    context = {}
    return render(request, 'terms.html', context)
 
def privacy(request):
    context = {}
    return render(request, 'privacy.html', context)

 