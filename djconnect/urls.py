# dappx/urls.py
from django.conf.urls import url, include
from djconnect import views
from django.conf import settings
from django.conf.urls.static import static
# SET THE NAMESPACE!
app_name = 'djconnect'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^dashboard/$',views.dashboard,name='dashboard'),
    url(r'^dashboard/security/$', views.dashboard_security, name='dashboard_security'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)