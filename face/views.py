from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import *
from fbrecog import recognize

# Create your views here.

def index(request):
    form = ImageForm()
    message = ''
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.save()
            print(img.image.path)
            path = img.image.path #Insert your image file path here
            access_token = 'EAACUSsUNYAEBAAaDD4CDoX9XtkhnzWpgqeF3WfPZBZCES1zYrjT8KhP8VFlcSeD6niLFO8VE6gLQtkMG0QvXqS9Qgbbt45tWyGkdkAcDdrKpVIuyAtO4bsTLe8mZCKQ5rtyLGshuLsefjvEfWyj6p753WAgyJkZD' #Insert your access token obtained from Graph API explorer here
            cookie = 'x-referer=eyJyIjoiL3VmaS9yZWFjdGlvbi9wcm9maWxlL2Jyb3dzZXIvP2Z0X2VudF9pZGVudGlmaWVyPTEyMTgyMDY4MDQ5NTE3NTgiLCJoIjoiL3VmaS9yZWFjdGlvbi9wcm9maWxlL2Jyb3dzZXIvP2Z0X2VudF9pZGVudGlmaWVyPTEyMTgyMDY4MDQ5NTE3NTgiLCJzIjoibSJ9; m_pixel_ratio=1; a11y=%7B%22sr%22%3A0%2C%22sr-ts%22%3A1505497970920%2C%22jk%22%3A10%2C%22jk-ts%22%3A1509997215516%2C%22kb%22%3A0%2C%22kb-ts%22%3A1505497970920%2C%22hcm%22%3A0%2C%22hcm-ts%22%3A1505497970920%7D; locale=en_GB; datr=cQWvWFDNAOOVkNay2OTzBUQf; sb=dAWvWAT1FT0zYZnOZKOejKUG; c_user=100002873509486; xs=22%3AkHZhvAQpZrS0-w%3A2%3A1518025260%3A2475%3A4199; fr=0lhUyjco07XsB1Omb.AWVXXR9uxDhSFT8KdHlA_MGWsc0.BZpmIR.EI.Fp7.0.0.Baezos.AWXr5WWJ; pl=n; dpr=0.800000011920929; act=1518027050235%2F2; presence=EDvF3EtimeF1518027124EuserFA21B02873509486A2EstateFDutF1518027124917CEchFDp_5f1B02873509486F28CC; wd=640x797' #Insert your cookie string here
            fb_dtsg = 'AQEYXpAjE-jd:AQEraNy2nfGo' #Insert the fb_dtsg parameter obtained from Form Data here.
            message=recognize(path,access_token,cookie,fb_dtsg)
            print(message)
    return render(request, 'face/index.html', {'form':form, 'message':message})
# Create your views here.
