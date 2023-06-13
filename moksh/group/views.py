from django.shortcuts import render
from .models import *
# Create your views here.
def groups(request):
    groups = Group.objects.all()
    return render(request, "group/groups.html", {
        "groups": groups
    })