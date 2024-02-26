from django.shortcuts import render,redirect,get_object_or_404
from todoapp.form import UserdetailForm,TaskdetailForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from todoapp.models import Ourtask
from datetime import datetime
# user import



# Create your views here.
def home(request):
    return render(request,'Main/base.html')


def login_page(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        pswd = request.POST.get('password')
        user = authenticate(request, username=username, password=pswd)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successfully')
            return redirect('home')
        else:
            messages.error(request, 'USER IS INVALID ')
            return redirect('register')
    return render(request,'user/login.html')
        
    
def register_page(request):
    form = UserdetailForm()
    if request.method == 'POST':
        form = UserdetailForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration Sucess you can login now..')
            return redirect('/login')
    return render(request,'user/register.html',{'form':form})


def logout_page(request):
    logout(request)
    messages.success(request, 'Logout Successfully')
    return redirect('home')

def createtask(request):
    
    if request.user.is_authenticated:
        form = TaskdetailForm()
        if request.method == 'POST':
            form = TaskdetailForm(request.POST)
            if form.is_valid():
                instance=form.save(commit=False)
                instance.user_id=request.user
                # instance.created_at = form.cleaned_data.get('created_at') or datetime.now()
                # instance.updated_at = form.cleaned_data.get('updated_at') or datetime.now()
                instance.save()
                messages.success(request, f'{request.user} task is created successfully')
                return redirect('taskvisible')
        return render(request,'user/createtask.html',{'form':form})
    else:
        return render(request, 'user/login.html')
        
def taskvisible(request):
    if request.user.is_authenticated:
        task= Ourtask.objects.filter(user_id=request.user)
        return render(request,'user/taskvisible.html',{'task':task})
    else:
        return render(request,'user/login.html')

def updatetask(request,pk):
    item=get_object_or_404(Ourtask,pk=pk)
    if request.method == 'POST':
        form = TaskdetailForm(request.POST, instance=item)
        if form.is_valid():
            # instance.user_id=request.user
            # form.created_at = form.cleaned_data.get('created_at') or datetime.now()
            # form.updated_at = form.cleaned_data.get('updated_at') or datetime.now()
            form.save()
            return redirect('taskvisible')
    else:
        form = TaskdetailForm(instance=item)
    return render(request,'user/createtask.html',{'form':form})

def deletepage(request,pk):
    item = get_object_or_404(Ourtask,pk=pk)
    if request.method =='POST':
        item.delete()
        return redirect('taskvisible')
    return render(request,'user/deletepage.html',{'item':item})

def viewtask(request,pk):
    item=get_object_or_404(Ourtask,pk=pk)
    return render(request,'user/viewsptask.html',{'item':item})
    

def privacy(request):
    return render(request,'user/terms.html')
    
    

def terms(request):
    return render(request, 'user/privarcy1.html')