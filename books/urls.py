from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome),
    path('books/<int:pk>', views.books),
    path('hello/', views.hello)

]

