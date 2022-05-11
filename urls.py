from django.urls import path
from . import views
urlpatterns = [path('', views.index, name='index'),
path("aboutMe", views.aboutMe, name="aboutMe"),
path("login", views.login,name="login"),
path("javascript",views.javascript,name="javascript"),
path("gallery",views.gallery,name="gallery"),
path("contact",views.contact,name="contact")
]