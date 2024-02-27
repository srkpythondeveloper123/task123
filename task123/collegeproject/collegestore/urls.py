
from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('add/',views.form_add,name='form_add'),
    path('ajax/load-Course/',views.load_Course, name='ajax_load_Course'),
    path('new_page',views.new_page ,name='new_page'),
    path('formend',views.formend,name="formend")
]