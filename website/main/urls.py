from django.urls import path
from . import views
urlpatterns =[path("<int:id>",views.index,name="index"),
              path("v1",views.v1,name="page 2"),
              path("home",views.home,name="home"),
              path("",views.home,name="home")
              ]
