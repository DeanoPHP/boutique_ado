from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import AnonymousUser

# Create your views here.


def index(request):
    """A view to return the index page"""
    return render(request, "home/index.html")


def debug_request_view(request):
    info = {
        "method": request.method,
        "user": str(request.user),
        "is_authenticated": request.user.is_authenticated,
        "session": dict(request.session.items()),
        "GET": dict(request.GET),
        "POST": dict(request.POST),
        "FILES": {k: v.name for k, v in request.FILES.items()},
        "headers": dict(request.headers),
        "cookies": request.COOKIES,
    }
    return JsonResponse(info, json_dumps_params={"indent": 2})
