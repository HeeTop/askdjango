from django.conf.urls import url, include
from accounts import views
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.views import login,logout
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^login/$',login,name='login',kwargs={
            'template_name':'accounts/login.html',

        }),
    url(r'logout/$',logout,name='logout',kwargs={
            'next_page': reverse_lazy('home'),
        })
]