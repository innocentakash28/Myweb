
from django.http import *
from django.shortcuts import render, redirect

# Create your views here.

from Simple.models import users

def signup(request):
    return render(request, 'index.html')


def signin(request):
    return render(request, 'index1.html')


def register(request):
    if request.method == 'POST':


        name = (request.POST['name'])
        email = (request.POST['email'])
        pass1 = (request.POST['pass'])
        pass2 = (request.POST['re_pass'])
        if pass1 == pass2 :
            if len(pass1)<8:
                return HttpResponse("Password Must Be of 8 char")
            else:
                if users.objects.filter(email = email).exists():
                    print("user taken")
                    return HttpResponse("Email Already Register")
                else:
                  x = users(name=name ,email = email , password = pass1)
                  x.save()
                  return render(request, 'index1.html')
        else:
            return redirect('/')
    else:
        return redirect('/')

def login(request):
    if request.method == 'POST':
        email = (request.POST['email'])
        password = (request.POST['pass1'])

    if users.objects.filter(email=email).exists():

        if users.objects.filter(password=password).exists():
            a = users.objects.get(email = email)


            return render(request, 'index2.html', {'result':a.name})
        else:
            return HttpResponse("Incorrect Password")

    else:
        return HttpResponse("User Not Register")

