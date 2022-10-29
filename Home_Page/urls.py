from . import views
from django.urls import path

urlpatterns = [
    path('',views.home),
    path('signout',views.signout),
    path('register',views.register),
    path('payment_success',views.payment_success),
    path('login_signup',views.login_signup),
    path('cancel_reservation',views.cancel_reservation),
    path('contactus',views.contactus),
    path('subscription',views.subscription),
    path('gold_membership',views.gold_membership),

    path('vip_membership',views.vip_membership),
    path('silver_membership',views.silver_membership),
    path('your_tickets',views.your_tickets),

]
