"""
from django.urls import path

from . import views as v

urlpatterns = [
path("<int:id>", views.index, name="index"),
path("",views.home, name="home"),
path("home/", views.home, name="home"),

path("create/",views.create, name="create"),
path("view/", views.view, name="view"),

]
"""

from django.urls import path

from . import views

urlpatterns = [
path("", views.home, name="home"),
path("view/", views.view, name="index"),
path("home/", views.home, name="home"),
path("create/", views.get_name, name="index"),
path("<int:id>", views.index, name="index"),
]