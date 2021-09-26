from django.contrib import admin
from django.urls import path,include
from.views import *

urlpatterns = [
    path('',home,name='home'),
    path('yarat/',create,name='create'),
    path('sesver/<int:id>',vote,name='vote'),
    path('netice/<int:id>',results,name='results')
]