from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import MyForm
from .models import  Course

def home(request):
    return render(request,'Home.html')

def form_add(request):
    form = MyForm()
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formend')
    return render(request, 'main_form.html', {'form': form})


# AJAX
def load_Course(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).all()
    return render(request, 'Course_dropdown.html', {'courses': courses})
     # return JsonResponse(list(cities.values('id', 'name')), safe=False)


def formend(request):
    return render(request,"formend.html")
def new_page(request):
    return render(request,"new_page.html")





def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"name already exist")
                return redirect("register")
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                return  redirect("login")

        else:
            messages.info(request,"password not matching")
            return redirect("register")
    return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('new_page')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")