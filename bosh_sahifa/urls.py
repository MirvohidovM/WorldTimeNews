from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

from .forms import Loginform
from .views import *

urlpatterns= [
    path('', views.uy, name = 'home' ),
    path('about/',  aboutus, name ='about'),
    path('accounts/login/', LoginViews.as_view(), name='login'),
    path('logout/', log_out, name='logout'),
    path('signup/', sign_up, name='signup'),
    path('contact/', views.contactus, name = 'contact'),
    #path('notFound/', views.notfound, name = 'notfound'),
    #path('index-inner/', views.inner, name = 'inner'),
    path('news/', include('yangiliklar_ilovasi.urls')),
]
