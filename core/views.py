from django.shortcuts import redirect, render
from item.models import Item, Category
from .forms import SignUpForm
from django.contrib.auth import logout
# Create your views here, basically the html pages


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'items': items,
        'categories': categories
    })


def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index/')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('/')
