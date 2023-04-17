from django.shortcuts import render
from . models import Pictures


# Create your views here.
def gallery_home(request):
    image=Pictures.objects.all()
    context={'images':image}
    return render(request,"gallery_home.html",context)