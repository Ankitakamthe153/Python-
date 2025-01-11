# i have created this file 
from django.http import HttpResponse
def index(request):
    return HttpResponse("hello")
def about(request):
    return HttpResponse("about")