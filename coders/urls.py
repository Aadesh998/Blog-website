from django.contrib import admin
from django.urls import path
from coders import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('write/',views.write,name='write'),
    path('<slug:slug>',views.blogpost,name='blogpost'),
    path('delete/<id>/',views.delete,name='delete'),
    path('search/',views.search,name='search'),
    path('loadmore/',views.loadmore,name='loadmore'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.handlelogin,name='handlelogin'),
    path('logout/',views.logout,name='logout'),
    path('comment/',views.comment,name='comment'),
]
