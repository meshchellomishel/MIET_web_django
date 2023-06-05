from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as dj_login
from django.contrib.auth import authenticate
from django.urls import reverse_lazy
from .models import *
import datetime
from django.core.exceptions import ObjectDoesNotExist
from .forms import RegisterUserForm

import random as rd
import os

menu = [{
    'title': "О сайте",
    'url_name': 'about'
}, {
    'title': "Обратная связь",
    'url_name': 'feedback'
}, {
    'title': "Добавить продукт",
    'url_name': 'add_page'
}]


def home(request):
    products = list(Product.objects.all())
    count_of_items = 4
    items = []
    for i in range(count_of_items):
        items += [products[i]]
    context = {
        'menu': menu,
        'title': 'Главная страница',
        'items': items,
        'request': request
    }
    return render(request, 'index.html', context=context)


def about(request):
    return render(request, 'about.html', {
        'menu': menu,
        'title': 'О сайте',
        'request': request
    })


def login(request):
    return render(request, 'registration/login.html', {
        'menu': menu,
        'title': 'Войти',
        'request': request
    })


def addpage(request):
    return render(request, 'addpage.html', {
        'menu': menu,
        'title': 'Добавить продукт',
        'request': request
    })


# def register(request):
#     return render(request, 'register.html', {'menu': menu,
#                                             'request': request})


def feedback(request):
    return render(request, 'feedback.html', {
        'menu': menu,
        'title': 'Обратная связь',
        'request': request
    })


def post(request):
    posts = product.objects.all()
    return render(request, 'post.html', {
        'menu': menu,
        'posts': posts,
        'request': request
    })


def show_post(request, post_id):
    post = get_object_or_404(Product, pk=post_id)
    context = {
        'menu': menu,
        'post': post,
        'title': post.title,
        'request': request
    }
    return render(request, 'post.html', context=context)


def user_page(request):
    return render(request, 'user_page.html', {
        'menu': menu,
        'title': 'Ваша страница',
        'request': request
    })


def card(request):
    user = request.user
    orders = Orders.objects.filter(user=user)
    products = list(map(lambda x: x.product, orders))
    counts = {products[i]: orders[i].count for i in range(len(products))}
    return render(
        request, 'card.html', {
            'menu': menu,
            'items': products,
            'counts': counts,
            'title': 'Ваша корзина',
            'request': request
        })


def del_from_card(request, post_id):
    if request.method == 'POST':
        user = request.user
        product = Product.objects.get(id=post_id)
        current_count = product.count
        current_ship = product.ship_date
        try:
            card = Orders.objects.get(user=user, product=product)
            Orders.objects.filter(user=user, product=product).delete()
            product.count += card.count
            product.save()
        except ObjectDoesNotExist:
            pass

        data = {'count': current_count,
                   'can delete': False
        }
      
        return JsonResponse(data, safe=False)
      
    return HttpResponseRedirect(reverse('card'))


def add_to_card(request, post_id):
    if request.method == 'POST':
        user = request.user
        product = Product.objects.get(id=post_id)
        current_count = product.count
        current_ship = product.ship_date
        if current_count:
            try:
                card = Orders.objects.get(user=user, product=product)
                print(card)
                current_count -= 1
                card.count += 1
                card.save()
            except ObjectDoesNotExist:
                current_count -= 1
                Orders(user=user,
                       product=product,
                       ship_date=current_ship,
                       count=1).save()
            product.count -= 1
            product.save()

            data = {'count': current_count,
                   'can delete': True}

            return JsonResponse(data, safe=False)

    return HttpResponseRedirect(reverse('post', args=[post_id]))


class Register_user(View):
    form_class = RegisterUserForm()
    template_name = 'registration/register.html'

    def get(self, request):
        context = {'form': self.form_class, 'menu': menu, 'request': request}
        return render(request, self.template_name, context)

    def post(self, request):
        form_class = RegisterUserForm(request.POST)

        print(form_class)

        if form_class.is_valid():
            form_class.save()
            username = form_class.cleaned_data.get('username')
            password = form_class.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            dj_login(request, user)
            return redirect('login')

        context = {'form': form_class, 'menu': menu, 'request': request}
        return render(request, self.template_name, context)
