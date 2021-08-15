from rest_framework import routers
from bosh_sahifa import views

router = routers.DefaultRouter()
router.register('axborot', views.NewsViewSets)
router.register('kategoriya', views.CatViewSets)