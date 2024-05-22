from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from coders.models import Postblog
from django.core import serializers
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from coders.admin import admin
from django.core.mail import send_mail
from django.conf import settings
from coders.forms import Postblogform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout as auth_logout
from django.contrib import messages 




admin.site.site_title='Log in page of Ninja coders'
admin.site.site_header='Ninja coders'
admin.site.index_title='Welcome of Ninja coders'

# Create your views here.
def home(request):
    post = Postblog.objects.all()[0:1]
    context = {
        'Postblog':post,
    }
    return render(request,'index.html',context)

def write(request):
    context = {'form':Postblogform}
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        
        slug = request.POST.get('title')
        # desc = request.POST.get('desc')
        form = Postblogform(request.POST)
        images = request.FILES.get('imagess')
        if form.is_valid():
            Desc = form.cleaned_data['Desc']
        write = Postblog(Title=title,author =author,image=images,Desc=Desc,slug=slug) 
        write.save()
        return redirect('/')
    return render(request,'write.html',context)

def contact(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            print(name,email,subject,message)
            subject = subject
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email,]
            send_mail(subject, f"{message}", email_from, recipient_list)
            return redirect('/')
    except Exception as e:
        print(e)
    return render(request,'contact.html')


def blogpost(request,slug):
    Post = Postblog.objects.filter(slug = slug)[0]
    context = {
        'post':Post
    }
    return render(request,'blogpost.html',context)

def delete(request,id):
    Post = Postblog.objects.get(id = id)
    Post.delete()
    return redirect('/')

def search(request):
    query = request.GET['search']
    if len(query) > 78:
        allPosts = []
    else:
        allPosts = Postblog.objects.filter(Title__icontains = query)
    params = {'allposts':allPosts,'query':query}
    return render(request,'search.html',params)

@csrf_exempt
def loadmore(request):
    offset = int(request.POST['offset'])
    limit = 2
    poststt = Postblog.objects.all()[offset:limit+offset]
    totalData = Postblog.objects.count()
    posts_json = serializers.serialize('json',poststt)
    data = {
        'posts':posts_json,
        'totalresult':totalData
    }
    return JsonResponse(data=data)

def handlelogin(request):
    if request.method =="POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        user=authenticate(request,username= username, password=pass1)
        if user is not None:
            login(request ,user)
            return redirect("home")
        else:
            return HttpResponse('invalid')
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        confirmpass = request.POST.get('confirmpass')
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        # return redirect('home')
        return redirect('/login/')
        
    return render(request,'sign_up.html')

def logout(request):
    auth_logout(request)
    return redirect('/login/')


def comment(request):
    return HttpResponse("Hello World!")