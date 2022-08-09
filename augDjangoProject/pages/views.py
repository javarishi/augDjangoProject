from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def home_view(request):
    print(request)
    return HttpResponse("<h1> Home Page </h1>")


def contact_view(request):
    print(request)
    context = {}
    return render(request, "contactus.html", context)
    