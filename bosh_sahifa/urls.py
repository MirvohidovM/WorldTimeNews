from django.urls import path, include
from django.contrib.auth import views as auth_views #import this
from bosh_sahifa import views

urlpatterns= [
    path('', views.uy, name = 'home' ),
    path('innner/', views.inner, name = 'inner'),
    path('about/',  views.aboutus, name ='about'),
    path('accounts/login/', views.LoginViews.as_view(), name='login'),
    path('logout/', views.log_out, name='logout'),
    path('signup/', views.sign_up, name='signup'),
    path('contact/', views.contactus, name = 'contact'),
    path('news/', include('yangiliklar_ilovasi.urls')),

    # path('accounts/', include('django.contrib.auth.urls')),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='main/password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="main/password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='main/password/password_reset_complete.html'), name='password_reset_complete'),
    path("password_reset/", views.password_reset_request, name="password_reset"),

    path("post/", views.PostList.as_view(), name="post"),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    # path("<slug:slug>/", views.post_detail, name="post_detail"),

    path("news_api/", views.NewsViewSets.as_view({'get': 'list'})),
    path("cat_api/", views.CatViewSets.as_view({'get': 'list'}))
]
