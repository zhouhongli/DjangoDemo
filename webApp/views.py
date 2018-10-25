from django.shortcuts import render
from webApp.models import HelloT
from django.views.decorators import csrf
 
def hello_post(request):
    ctx ={}
    if request.POST:
        #ctx['wname'] = request.POST['who']
        ctx['wname'] = 'Hello,' + HelloT.objects.get(name=request.POST['who']).title
        print(HelloT.objects.get(name=request.POST['who']).title)
    return render(request, "hello.html", ctx)
