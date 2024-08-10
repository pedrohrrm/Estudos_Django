from django.urls import path
from recipes.views import home

# por enquanto eu vou criar uma função e passar uma view

# HTTP Resquest

urlpatterns = [
    path('', home),

]
