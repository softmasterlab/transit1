from django.urls import path
from .views import index, add, delete

urlpatterns = [
    path('', index),
    path('add', add),
    path('del', delete),
]