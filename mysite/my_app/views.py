from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Member,CreateForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def Home(request):
    return render(request,'my_app/home.html',{'form':CreateForm()})

def Sighup(request):
    if request.method=='POST':
        form=CreateForm(request.POST)

        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            email=request.POST['email']

            message="welcome to the pyweek event thank you for registering for the event fvdfvdfvdvvfvdfk fvbdfjvbdfiuvdfivdoifvhofidhvoi vdfoivdfiovhdfoivhdfo fvdhiov dfvohfiodhgohfgobhfogfgoihbfg fbfdoibhdfghfgoidhfgjbfigh fbdfihidfsagak sahaldfoihgdfoighdfiofdgdfpgh bdfhboidfhbdfoihbfodihbfgoi dfbidhfboifdhbdofibdfbhdfoib"
            subject="welcome to the world of programming ,i hope your participation and suppourt for the event have a great day guys and explore through python"
            send_mail(subject,message,settings.EMAIL_HOST_USER,[email,],fail_silently=False,)


        else:
            form=CreateForm()
            return redirect('/')
    return render(request,'my_app/sighin.html',{})

def Sighin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return  HttpResponse("logging successful")
        else:
            return  HttpResponse("logging not successful")
