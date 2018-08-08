from django.http import HttpResponse
#
#
# def hello(request):
#     return HttpResponse("Hello world ! ")


from django.shortcuts import render


def hello(request):
    context = {}
    context['hello'] = 'Hello World!12313'
    return render(request, 'hello.html', context)