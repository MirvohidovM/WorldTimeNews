from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from rest_framework import viewsets, permissions
from bosh_sahifa.forms import SignUpForm, NewsForm, ContactusForm, Loginform
from bosh_sahifa.models import News, Category
from bosh_sahifa.serializers import CatSer, NewsSer
from django.contrib import messages
from django.contrib.auth.models import User

def uy(request):
    news = News.objects.all()
    return render(request, 'pages/index.html', {'news': news})

def aboutus(request):
    return render(request, 'pages/aboutus.html')

class LoginViews(LoginView):
    template_name = 'pages/login.html'
    #authentication_form = Loginform



class NewsViewSets(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSer
    permission_classes = [permissions.IsAuthenticated]

class CatViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CatSer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

def log_out(request):
    logout(request)
    return redirect('login')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'pages/signUp.html', {'form': form})

def contactus(request):
    if request.method == 'POST':
        form = ContactusForm(request.POST)
        if form.is_valid():
            subject = request.POST.get('subject')
            content = request.POST.get('content')
            email = request.POST.get('email')
            mail = send_mail(subject, content, "mirshoxidmirvoxidov@gmail.com", [email], fail_silently=False)
            if mail:
                messages.success(request, 'Murojatingiz Yuborildi')
                return redirect('contact')#render(request, 'pages/yubor.html', {'email': email})
            else:
                messages.error(request, 'Yuborishdagi Hatolik')
        else:
            messages.error(request, 'Validatsiyadagi Hatolik')
    else:
        form = ContactusForm()
    return render(request, 'pages/contactus.html', {'form': form})

def contactu(request):
    form = ContactusForm(request.POST)
    if request.method == 'POST':
        subject = request.POST.get('subject')
        content = request.POST.get('content')
        email = request.POST.get('email')
        send_mail(subject, content, "mirshoxidmirvoxidov@gmail.com"
                  , [email], fail_silently=False)
        return render(request, 'pages/yubor.html', {'email': email})
    return render(request, 'pages/contactus.html', {'form':form})




