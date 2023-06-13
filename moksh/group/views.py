from django.shortcuts import render
from .models import *
# Create your views here.
def groups(request):
    groups = Group.objects.all()
    print("GOt so far")
    return render(request, "group/groups.html", {
        "groups": groups
    })

def group(request, slug):
    group = Group.objects.get(slug=slug)
    messages = Message.objects.filter(group=group)
    return render(request, 'group/group.html', {
        'group': group,
        'messages': messages
    })