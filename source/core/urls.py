from django.urls import path

from .views import (home_page, cars_inventory, cars_featured, profile,
                    account_signup_view, account_login_view, CarDetailView, OrderDetailView, buy_car)


app_name = 'core'


urlpatterns = [

    path('', home_page, name='home-page'),
    path('browse', cars_inventory, name='browse'),
    path('browse/car/<slug:slug>', CarDetailView.as_view(), name='car_detail'),
    path('buy-car/<slug>', buy_car, name='buy-car'),
    path('browse/featured', cars_featured, name='featured'),
    path('user', profile, name='user-profile'),
    path('user/order/<slug:slug>', OrderDetailView.as_view(), name='order_detail'),
    # path('accounts/signup/', view=account_signup_view),
    # path('accounts/login/', view=account_login_view)
]
