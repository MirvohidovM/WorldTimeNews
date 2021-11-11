from django.conf.urls import url
from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    #path('category/', news_views, name='news_pk'),
    #path('category/<int:pk>/', get_category, name='kategoriya'),

    path('',  cache_page(60)(YangilikViews.as_view()), name='yangiliklar'),
    path('category/<int:pk>/', KategoriyaBoyicha.as_view(), name='kategoriya'),
    path('qoshish/', YangilikYaratish.as_view(), name='qoshish'),
    path('<int:pk>/almashtirish/', YangilikAlmashtirish.as_view(), name='almashtirish'),
    path('<int:pk>/tozalash/', YangilikTozalash.as_view(), name='tozalash'),
    path('<slug:slug>/', yangilikDetali, name='oneOfNews'),
    ]
