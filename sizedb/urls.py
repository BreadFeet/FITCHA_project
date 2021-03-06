"""config URL Configuration

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

from django.contrib import admin
from django.urls import path
from sizedb import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about', views.about, name='about'),

    path('sign', views.sign, name='sign'),
    path('signupimpl', views.signupimpl, name='signupimpl'),
    path('signinimpl', views.signinimpl, name='signinimpl'),
    path('signout', views.signout, name='signout'),

    path('myinfo', views.myinfo, name='myinfo'),
    path('updateinfo', views.updateinfo, name='updateinfo'),
    path('deleteinfo', views.deleteinfo, name='deleteinfo'),

    path('recommend', views.recommend, name='recommend'),

    path('explore', views.explore, name='explore'),

    path('contact', views.contact, name='contact'),
    path('contactimpl', views.contactimpl, name='contactimpl'),
]
