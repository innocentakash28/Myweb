
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.template.context_processors import static
from django.urls import path

from Myweb import settings
from . import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signup, name='Signup'),
    path('register', views.register , name = 'register'),
path('signin', views.signin, name='Signin'),
path('login', views.login, name='login')

]