"""NotesSharingProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from notes.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about',about, name='about'),
    path('',index,name='index'),
    path('contact',contact,name='contact'),
    path('userlogin',userlogin,name='userlogin'),
    path('login_admin',login_admin,name='login_admin'),
    path('signup',signup1,name='signup'),
    path('admin_home',admin_home,name='admin_home'),
    path('Logout',Logout,name='Logout'),
    path('profile',profile,name="profile"),
    path('changepassword',changepassword,name='changepassword'),
    path('editprofile',editprofile,name='editprofile'),
    path('uploadnotes',uploadnotes,name='uploadnotes'),
    path('viewmynotes',viewmynotes,name='viewmynotes'),
    path('delete_mynotes(?P<int:id>)',Delete_Mynotes,name='delete_mynotes'),
    path('viewallnotesuser',viewallnotesuser,name='viewallnotesuser'),
    path('viewsusers',viewusers,name='viewusers'),
    path('delete_user(?P<int:id>)',delete_user,name='delete_user'),
    path('viewallnotes',viewallnotes,name='viewallnotes'),
    path('assign_status(?P<int:id>)',assign_status,name='assign_status'),
    path('accepted_notes',accepted_notes,name='accepted_notes'),
    path('rejected_notes',rejected_notes,name='rejected_notes'),
    path('pending_notes',pending_notes,name='pending_notes'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
