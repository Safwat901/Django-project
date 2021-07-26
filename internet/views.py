
from django.shortcuts import render

from .models import internetpan



def internet_panel(request):
   internetdata=internetpan.objects.all()  

   content={'internetpan':internetdata }

   return render(request,'internet.html',content)

