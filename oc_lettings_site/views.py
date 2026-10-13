from django.shortcuts import render
from .models import Letting, Profile


def index(request):
    """[DOCSTRING]"""
    return render(request, "index.html")


def lettings_index(request):
    """[DOCSTRING]"""
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings_index.html", context)


def letting(request, letting_id):
    """[DOCSTRING]"""
    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "letting.html", context)


def profiles_index(request):
    """[DOCSTRING]"""
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles_index.html", context)


def profile(request, username):
    """[DOCSTRING]"""
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profile.html", context)
