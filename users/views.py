from django.shortcuts import render
from django.contrib.forms import UserCreationform

def register(request):
    form = UserCreationForm()
    return render(request,'users/register',{'form':form})

