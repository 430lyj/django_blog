from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('<int:id>', detail, name='detail'),
    path('new/', new_with_django_form, name='new'),
    path('create/', create_with_django_form, name='create'),
    path("update/<int:id>", update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
    path('search', searchpage, name="search"),
    path('searchUniv', search_univ, name="searchUniv"),
    path('commentDelete/<int:id>', commentDelete, name="commentDelete"),
]
