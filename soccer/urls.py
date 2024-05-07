from django.urls import path
from .views import index,contact,main,matches,single,blog,players
urlpatterns = [
    path('',index ,name="index"),
    path("contact/",contact,name="contact"),
    path("main/ ",main,name="main"),
    path("matches/",matches,name="matches"),
    path("single/",single,name="single"),
    path("blog/",blog,name="blog"),
    path("players/",players,name="players")

]

