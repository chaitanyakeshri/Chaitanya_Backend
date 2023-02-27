from django.shortcuts import render, HttpResponse

from home.models import Contact
from django.contrib import messages


def index(request):

    return render(request, 'index.html')
    # return HttpResponse("This is the homepage")


def about(request):
    # return HttpResponse("This is the about page")
    return render(request, 'about.html')


def services(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact = Contact(name="name", email="email",
                          phone="phone")
        Contact.save()
        messages.success(request, 'Form Submitted Sucessfully')
    return render(request, 'services.html')


def login(request):

    return render(request, 'login.html')
