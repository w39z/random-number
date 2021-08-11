import random

from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response


def auth(request):
    # if request.user.is_authenticated():
    return render(request, 'oauth.html')
    # else:
    #     return redirect('rnd')


def rnd_num():
    a = random.randint(0, 100)
    return a


class MainView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({'number': rnd_num()}, template_name='main.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def custom_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('rnd')
    else:
        return HttpResponseRedirect('login')
