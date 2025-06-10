from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
   #path('first/', first_view, name='first_view'),
   #path('second/', second_view, name='second_view'),

   path('', main_page, name='main_page'),
   path('catalog/', catalog_page, name='catalog'),
   path('contacts/', conatcts_page, name='contacts'),
   path('how_to_find/', how_to_find, name='how_to_find'),
   path('categories/', categories, name='categories'),
   path('cart/', cart, name='cart'),
   path('cabinet/', cabinet, name='cab'),
   path("categories/<int:id>/", category_detail, name='category_detail'),


]  

