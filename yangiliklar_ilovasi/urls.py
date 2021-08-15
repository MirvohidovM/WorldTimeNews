from django.conf.urls import url
from django.urls import path



from .views import *

urlpatterns = [
    #path('category/', news_views, name='news_pk'),
    #path('category/<int:pk>/', get_category, name='kategoriya'),

    path('', YangilikViews.as_view(), name='yangiliklar'),

    path('<int:pk>/', YangilikDetali.as_view(), name='oneOfNews'),
    path('category/<int:pk>/', KategoriyaDetali.as_view(), name='kategoriya'),
    path('qoshish/', Get_name.as_view(), name='qoshish'),
    path('<int:pk>/almashtirish/', YangilikAlmashtirish.as_view(), name='almashtirish'),
    path('<int:pk>/tozalash/', YangilikTozalash.as_view(), name='tozalash'),

    ]
