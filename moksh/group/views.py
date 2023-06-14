from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import *
# Create your views here.
def groups(request):
    groups = UserGroup.objects.filter(user=request.user)
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

def edituser(request, slug):
    group = Group.objects.get(slug=slug)
    users = User.objects.all()

    if request.method == 'POST':
        for user in users:
            if user.username in request.POST and not UserGroup.objects.filter(user=user, group=Group.objects.get(slug=slug)).exists():
                usergroup = UserGroup(user=user, group=Group.objects.get(slug=slug))
                usergroup.save()
            else:
                if UserGroup.objects.check(user=user, group=Group.objects.get(slug=slug)):
                    usergroup = UserGroup.objects.get(user=user, group=Group.objects.get(slug=slug))
                    usergroup.delete()
        return HttpResponseRedirect(reverse("groups"))
    else:
        return render(request, "group/edituser.html", {
            "group": group,
            "users": users
        })