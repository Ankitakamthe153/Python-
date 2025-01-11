from django.http import HttpResponse

def index(request):
    return HttpResponse('''django codewithankita ''')

def about(request):
    return HttpResponse("about ankita")