from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from allauth.account.views import SignupView, LoginView
from .models import (Car, Order)


class AccountSignupView(SignupView):
    # Signup View extended

    # change template's name and path
    template_name = "signup.html"

    # You can also override some other methods of SignupView
    # Like below:
    # def form_valid(self, form):
    #     ...
    #
    # def get_context_data(self, **kwargs):
    #     ...


account_signup_view = AccountSignupView.as_view()


class AccountLoginView(LoginView):
    # Signup View extended

    # change template's name and path
    template_name = "login.html"

    # You can also override some other methods of SignupView
    # Like below:
    # def form_valid(self, form):
    #     ...
    #
    # def get_context_data(self, **kwargs):
    #     ...


account_login_view = AccountLoginView.as_view()


def home_page(request):
    return render(request, "index.html")


def cars_inventory(request):
    context = {
        'cars': Car.objects.all()
    }
    return render(request, "inventory.html", context)


def cars_featured(request):
    context = {
        'cars': Car.objects.filter(featured=True)
    }
    return render(request, "featured.html", context)


def auth_in(request):
    context = {
        # 'items': Item.objects.all()
    }
    return render(request, "auth.html", context)


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(OrderDetailView, self).dispatch(request, *args, **kwargs)


@login_required
def profile(request):
    context = {
        'orders': Order.objects.filter(user=request.user)
    }
    return render(request, "profile.html", context)

# class UserDetailView(DetailView):
#     model =


@login_required
def buy_car(request, slug):
    car = get_object_or_404(Car, slug=slug)
    ordered_date = timezone.now()

    order = Order.objects.create(
        user=request.user, car=car, ordered_date=ordered_date)

    return redirect("core:user-profile")


