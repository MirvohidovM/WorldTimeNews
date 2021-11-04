from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions
from bosh_sahifa.forms import SignUpForm,  ContactusForm
from bosh_sahifa.models import News, Category
from bosh_sahifa.serializers import CatSer, NewsSer
from django.contrib import messages
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

def uy(request):
    news = News.objects.all()
    return render(request, 'pages/index.html', {'news': news})

def inner(request):
    return render (request, 'pages/index-inner.html', {})



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
    permission_classes = [permissions.IsAuthenticated]

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

# def contactu(request):
#     form = ContactusForm(request.POST)
#     if request.method == 'POST':
#         subject = request.POST.get('subject')
#         content = request.POST.get('content')
#         email = request.POST.get('email')
#         send_mail(subject, content, "mirshoxidmirvoxidov@gmail.com"
#                   , [email], fail_silently=False)
#         return render(request, 'pages/yubor.html', {'email': email})
#     return render(request, 'pages/contactus.html', {'form':form})

def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "main/password/password_reset_email.txt"
                    c = {
                    "email":user.email,
                    'domain':'127.0.0.1:8000',
                    'site_name': 'Website',
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "user": user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                     }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'mirshohidmirvohidov@gmail.com' , [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
                    return redirect ("/bosh-sahifa/password_reset/done/")
            messages.error(request, 'An invalid email has been entered.')
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="main/password/password_reset.html", context={"password_reset_form":password_reset_form})










