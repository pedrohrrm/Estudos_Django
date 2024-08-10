from django.urls import path
from recipes.views import home, contato, sobre

# por enquanto eu vou criar uma função e passar uma view

# HTTP Resquest

urlpatterns = [
    path('', home),
    path('contato/', contato),
    path('sobre/', sobre),
]
