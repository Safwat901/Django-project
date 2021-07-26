
from django.urls import path
from . import views



urlpatterns = [
    
    path('',views.internet_panel,name='internet'),
   
    
]