from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .forms import CustomerSignupForm
from .models import Customer

# Create your views here.


def signup_page(request):
    form = CustomerSignupForm()
    if request.user.is_anonymous:
        if request.method == 'POST':
            form = CustomerSignupForm(request.POST)
            if form.is_valid():
                new_customer = form.save()
                Customer.objects.create(user=new_customer)
                login(request, new_customer)
                return redirect('profile')
            else:
                messages.error(
                    request, 'An error occurred during registration')
    else:
        return redirect('profile')

    context = {
        'form': form,
    }
    template_name = 'accounts/signup.html'

    return render(request, template_name, context)


def login_page(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            try:
                customer = Customer.objects.get(username=username)
            except:
                messages.error(request, 'User does not exist')

            customer = authenticate(
                request, username=username, password=password)

            if customer is not None:
                login(request, customer)
                return redirect('profile')
            else:
                messages.error(request, 'Username OR password does not exit')
    else:
        return redirect('profile')

    context = {}
    template_name = 'accounts/login.html'

    return render(request, template_name, context)


def logout_page(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def profile_page(request):
    context = {}
    template_name = 'accounts/profile.html'

    return render(request, template_name, context)
