
from django.shortcuts import render ,redirect,get_object_or_404
from django.contrib.auth.admin import User
from .models import *
from datetime import date
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages


# Create your views here.
def about(request):
    return render(request,'about.html')

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def userlogin(request):
    error = ''
    if request.method == 'POST':
        u = request.POST['emailid']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user:
                login(request, user)
                error = 'no'
            else:
                error = 'yes'
        except:
            error = 'yes'
    d = {'error':error}
    return render(request,'login.html',d)

def login_admin(request):
    error = ''
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = 'no'
            else:
                error = 'yes'
        except:
            error = 'yes'
    d = {'error':error}
    return render(request,'login_admin.html',d)

def signup1(request):
    error = ''
    if request.method == 'POST':
        f = request.POST['firstname']
        l = request.POST['lastname']
        c = request.POST['contact']
        e = request.POST['emailid']
        p = request.POST['password']
        b = request.POST['Branch']
        r = request.POST['role']
        try:
            user = User.objects.create_user(username=e,password=p,first_name=f,last_name=l)
            signup.objects.create(user=user, contact=c, branch=b, role=r)
            error = 'no'
        except:
            error = 'yes'
    d = {'error':error}
    return render(request,'signup.html',d) 

def admin_home(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    allnotes = Notes.objects.all()
    apnotes = Notes.objects.filter(status__exact='approved')
    rnotes = Notes.objects.filter(status__exact='rejected')
    pnotes = Notes.objects.filter(status__exact='pending')
    ap = 0
    a = 0
    p = 0
    r = 0
    for i in rnotes:
        r += 1
    for i in pnotes:
        p += 1
    for i in apnotes:
        ap += 1
    for i in allnotes:
        a += 1
    d = {'a':a,'ap':ap,'p':p,'r':r}

    return render(request,'admin_home.html',d)

def Logout(request):
    logout(request)
    return redirect('index')


def profile(request): 
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    data = signup.objects.get(user=user)
    d = {
        'data': data,
        'user':user,
    }
    return render(request,'profile.html',d)

def changepassword(request): 
    if not request.user.is_authenticated:
        return redirect('login')
    error = ''
    if request.method =='POST':
        o = request.POST['old']
        n = request.POST['new']
        c = request.POST['confirm']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            error= 'no'
        else:
            error = 'yes'
    d = {'error':error}
    return render(request,'changepassword.html',d)

def editprofile(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    error = False
    user = User.objects.get(id=request.user.id)
    pro = signup.objects.get(user=user)
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        #u = request.POST['emailid']
        c = request.POST['contact']
        b = request.POST['branch']
        #pro.user.username=u
        user.first_name=f
        user.last_name=l
        pro.contact=c
        pro.branch=b
        pro.save()
        pro.user.save()
        user.save()
        error = True
    d = {'error':error,'pro':pro}
    return render(request,'editprofile.html',d)
def uploadnotes(request):
    if not request.user.is_authenticated:
        return('Login')
    error = ''
    if request.method == 'POST':
        b = request.POST['branch']
        s = request.POST['subject']
        n = request.FILES['notesfile']
        f = request.POST['filetype']
        des = request.POST['description']
        ct = User.objects.filter(username=request.user.username).first()
        try:
            Notes.objects.create(user=ct,uploadingdate=date.today(),branch=b,subject=s,notesfile=n,filetype=f,description=des,status='pending')
            error = 'no'
        except:
            error = 'yes'
    d = {'error':error}
    return render(request,'uploadnotes.html',d)

def viewmynotes(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    user = User.objects.get(id=request.user.id)
    notes = Notes.objects.filter(status__exact='pending',user=user)

    d = {'notes':notes}
    return render(request,'viewmynotes.html',d)

def Delete_Mynotes(request, id):
    if not request.user.is_authenticated:
        return redirect('Login')
    if Notes.objects.filter(id=id).exists():
        notes = Notes.objects.get(id=id)
        notes.delete()
        message1 = messages.info(request,'Notes Deleted')
        return redirect('viewallnotes')    
def viewallnotesuser(request):
    if not request.user.is_authenticated:
        redirect('Login')
    
    apnotes = Notes.objects.filter(status__exact='approved')
    d = {'apnotes':apnotes}
    return render(request,'viewallnotesuser.html',d)


def viewusers(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    user = User.objects.all()[1:]
    d = {"user":user}
    return render(request,'viewusers.html',d)

def delete_user(request,id):
    if not request.user.is_staff:
        return redirect('login_admin')
    if User.objects.filter(id=id).exists():

        user = User.objects.get(id=id)
        user.delete()
        message1 = messages.info(request,'User Deleted')
        return redirect('viewusers')

def viewallnotes(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    user = User.objects.get(id=request.user.id)
    notes = Notes.objects.all()
    d = {'notes':notes}
    return render(request,'viewallnotes.html',d)

def assign_status(request,id):
    if not request.user.is_staff:
        return redirect('login_admin')
    error = ''
    notes = Notes.objects.get(id=id)
    if request.method == 'POST':
        s = request.POST['status']
        notes.status=s
        try:
            notes.save()
            error = 'no'
            return redirect('viewallnotes')
        except:
            error = 'yes'
        
        #redirect('viewallnotes')
    d = {'error':error}
    return render(request,'assign_status.html')

def accepted_notes(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    #user = User.objects.get(id=request.user.id)
    apnotes = Notes.objects.filter(status__exact='approved')
    d = {'apnotes':apnotes}
    return render(request,'accepted_notes.html',d)
def rejected_notes(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    #user = User.objects.get(id=request.user.id)
    apnotes = Notes.objects.filter(status__exact='rejected')
    d = {'apnotes':apnotes}
    return render(request,'rejected_notes.html',d)
def pending_notes(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    #user = User.objects.get(id=request.user.id)
    apnotes = Notes.objects.filter(status__exact='pending')
    d = {'apnotes':apnotes}
    return render(request,'pending_notes.html',d)