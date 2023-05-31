from django.http import HttpResponse

def Index(request):
    return HttpResponse('Hello it is run')