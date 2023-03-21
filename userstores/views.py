from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from .forms import StoreForm, ProductForm
from .models import Store, Product, Profile
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def allstores(request):

    stores = Store.objects.all()

    return render(request, 'userstores/index.html',{'stores': stores})

@login_required
def userprofile(request):

    user = request.user   
    user_store = Store.objects.filter(owner = user)
    print(len(user_store))

    if len(user_store) > 0:
        user_store = user_store[0]

    productform  = ProductForm   
    if request.method == 'POST':
        if user_store:
            form= ProductForm(request.POST, request.FILES)
            if form.is_valid:
                product = form.save(commit=False)
                product.store= user_store
                product.save()
                return redirect('/profile')

            else:
                print(form.errors)
        else:
            message= 'This user does not have a store, Please create a store first'
            return  render(request,'userstores/profile.html', { 'productform': productform, 'message': message})  

    return render(request,'userstores/profile.html', { 'productform': productform, 'user_store': user_store})

@login_required
def storedetail(request, slug):

    print(slug)

    store = Store.objects.filter(slug=slug)[0]
    

    products = Product.objects.filter(store=store)

    return render(request, 'userstores/store.html', {'store': store, 'products': products})


def logout_view(request):

    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':

        form = CustomUserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            username= form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form= CustomUserCreationForm()   
    return render(request, 'userstores/authentication/register.html', {'form': form})



def login_view(request):

    if request.method == 'POST':
        username= request.POST.get('username')
        password = request.POST.get('password')
        user= authenticate(request, username= username, password= password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            message= 'Invalid credentials please try again!'
            return render(request, 'userstores/authentication/login.html', {'message': message})
    else:
        return render(request, 'userstores/authentication/login.html')