from django.urls import path, include
from django.contrib.auth import views as auth_views #import this
from .views import *

urlpatterns= [
    path('', uy, name = 'home' ),
    path('innner/', inner, name = 'inner'),
    path('about/',  aboutus, name ='about'),
    path('accounts/login/', LoginViews.as_view(), name='login'),
    path('logout/', log_out, name='logout'),
    path('signup/', sign_up, name='signup'),
    path('contact/', contactus, name = 'contact'),
    path('news/', include('yangiliklar_ilovasi.urls')),
    # path('notFound/', views.notfound, name = 'notfound'),
    # path('index-inner/', views.inner, name = 'inner'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='main/password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="main/password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='main/password/password_reset_complete.html'), name='password_reset_complete'),
    path("password_reset/", password_reset_request, name="password_reset"),
]

