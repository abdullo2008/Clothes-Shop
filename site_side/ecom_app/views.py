from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import ProductModel, Category
from .serializers import ProductSerializer, CategorySerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import RegisterUserForm


# API Views
class CreateListProduct(ListCreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer


class UpDelRetProduct(RetrieveUpdateDestroyAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer


class CreateListCategory(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UpDelRetCategory(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Site Views
# ---Main Part---
def index(request):
    context = {
        'categories': Category.objects.all(),
        'products': ProductModel.objects.all()
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        'categories': Category.objects.all(),
    }
    return render(request, 'about.html', context)


def single(request, id):
    products = ProductModel.objects.filter(id=id)
    context = {
        'categories': Category.objects.all(),
        'products': products
    }
    return render(request, 'single.html', context)


def single_category(request, id):
    category = get_object_or_404(Category, id=id)
    product = ProductModel.objects.all().filter(category=category)
    context = {
        'categories': Category.objects.all(),
        'products': product
    }
    return render(request, 'categories.html', context)


def search(request):
    category = Category.objects.all()
    if request.method == 'POST':
        searched = request.POST['searched']
        searched = ProductModel.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))
        if not searched:
            messages.success(request, 'That product does not exist! Please try again ')
            return render(request, 'search.html', {'categories': category})
        else:
            return render(request, 'search.html',
                          {'searched': searched,
                           'categories': category
                           })
    else:
        return render(request, 'search.html', {'categories': category})


# Category
def CategoryList(request):
    context = {
        'categories': Category.objects.all()
    }
    return render(request, 'category/list.html', context)


class CategoryAdd(CreateView):
    model = Category
    template_name = 'category/add.html'
    fields = ['name']
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class CategoryUpdate(UpdateView):
    model = Category
    template_name = 'category/update.html'
    fields = ['name']
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class CategoryDelete(DeleteView):
    model = Category
    template_name = 'category/delete.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


# Product
class ProductAdd(CreateView):
    model = ProductModel
    template_name = 'product/add.html'
    fields = ['name', 'description', 'image', 'price', 'is_sale', 'sale_price', 'quantity', 'category']
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProductUpdate(UpdateView):
    model = ProductModel
    template_name = 'product/update.html'
    fields = ['name', 'description', 'image', 'price', 'price', 'is_sale', 'sale_price', 'quantity', 'category']
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProductDelete(DeleteView):
    model = ProductModel
    template_name = 'product/delete.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


# Auth
def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration Success!!')
            return redirect('index')
    else:
        form = RegisterUserForm()
    return render(request, 'registration/signup.html', {'form': form})


def LoginPage(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        new_user = authenticate(username=username, password=password)
        if new_user is not None:
            login(request, new_user)
            messages.success(request, "Good job !!!")
            return redirect('index')
        else:
            messages.success(request, "Error !!!")
    context = {
        'categories': Category.objects.all(),
    }
    return render(request, 'registration/login.html', context)


def LogoutPage(request):
    logout(request)
    messages.success(request, "Good job !!!")
    return redirect('index')


def Users(request):
    users = User.objects.filter(is_superuser=False)
    return render(request, 'registration/users.html', {'users': users})


def user(request):
    return render(request, 'registration/user_profile.html')
