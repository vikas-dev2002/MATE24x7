from django.urls import path
from . import views

urlpatterns=[
    path("index/",views.index),
    path("",views.home),
    path("home/",views.home),
    path("login/",views.login),
    path("signout/",views.signout),
    path("signup/",views.signup),
    path("contact/",views.contact),
    path("plumber/",views.plumber),
    path("blog/",views.blog),
    path("team/",views.team),
    path("help/",views.help),
    path("work/",views.work), 
    path("alogin/",views.alogin),
    path("asignout/",views.asignout),
    path("pricing/",views.pricing),
    path("cart/",views.cart),
    path("showauser/",views.showauser),
]