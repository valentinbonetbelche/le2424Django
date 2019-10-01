# dprojx/urls.py
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from djconnect import views


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.dashboard,name='dashboard'),
    url(r'^special/',views.special,name='special'),
    url(r'^djconnect/',include('djconnect.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
url('avatar/', include('avatar.urls')),

]