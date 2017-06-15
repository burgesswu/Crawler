from django.shortcuts import render

# Create your views here.
def login(request):
    context={}
    context['hello']='burgess'
    return render(request, 'login.html', context)
