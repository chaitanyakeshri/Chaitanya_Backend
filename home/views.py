from django.shortcuts import render, HttpResponse

from home.models import Contact


def index(request):

    return render(request, 'index.html')
    # return HttpResponse("This is the homepage")
