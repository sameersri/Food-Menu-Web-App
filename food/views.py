from django.shortcuts import render,redirect
from food.forms import Registerform,Loginform
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ItemForm 
from .models import Item

def home_view(request):
    return render(request,'users/home.html')

def create_item(request):
    form=ItemForm()
    if request.method=="POST":
        form=ItemForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Item added successfully")
            return redirect("menu")
        messages.success(request,"Invalid credentials")
    return render(request,"users/create_item.html",{"form":form})

def update(request,id):
    item=Item.objects.get(id=id)
    form=ItemForm(request.POST,request.FILES,instance=item)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            messages.success(request,"Item added successfully")
            return redirect("menu")
        messages.error(request,"Invalid credential")
    return render(request,"users/update.html",{"form":form,"item":item})

def delete_item(request,id):
    Item.objects.get(id=id).delete()
    messages.success(request,"Item deleted successfully")
    return redirect("menu")
    


def register_view(request):
    form=Registerform()
    if request.method=="POST":
        form=Registerform(request.POST)
        print(form)
        if form.is_valid():
            confirm_password=form.cleaned_data["confirm_password"]
            user=form.save(commit=False) 
            user.set_password(confirm_password)
            user.save()
            messages.success(request,"User is created Successfully.")
            return redirect("login")
    return render(request,'register.html',{"form":form})

def login_view(request):
    form=Loginform()
    if request.method=="POST":
        form=Loginform(request.POST)
        if form.is_valid():
            identifier=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user=authenticate(request,username=identifier,password=password)

            storage = messages.get_messages(request)
            storage.used = True

            if user:
                if user.groups.filter(name="Manager").exists():
                    login(request,user)
                    request.session['role']="Manager"  
                    messages.success(request,"Logged in successfully as a Manager") 
                else:
                    login(request,user) 
                    request.session['role']="User"
                    messages.success(request,"Logged in successfully") 
                return redirect('home')
            else:
                messages.error(request,"Invalid Credentials")
                return redirect("login")
    return render(request,"login.html",{"form":form})

def about_view(request):
    return render(request,'users/about.html')

@login_required
def contact_view(request):
    return render(request,'users/contact.html')

@login_required
def menu_view(request):
    all_data=Item.objects.all()
    my_dict={"all_data":all_data}
    return render(request,'users/menu.html',my_dict)

def logout_view(request):
    logout(request)
    messages.success(request,"You have been logged out successfully.")
    return redirect('login')