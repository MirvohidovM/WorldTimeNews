"""yangiliklar_loyihasi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
<<<<<<< HEAD
from yangiliklar_loyihasi.api import router
=======
from .api import router
>>>>>>> 5b1d019c1aa18587604e16e041bfa55cb0ff593b

urlpatterns = [
    url('admin/', admin.site.urls),
    url('bosh-sahifa/', include('bosh_sahifa.urls')),
    path('api/', include(router.urls)),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('captcha/', include('captcha.urls')),
<<<<<<< HEAD
    path('silk', include('silk.urls', namespace='silk')),

=======
    path('__debug__/', include(debug_toolbar.urls)),
>>>>>>> 5b1d019c1aa18587604e16e041bfa55cb0ff593b
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


