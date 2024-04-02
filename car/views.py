from django.shortcuts import render

# Create your views here.
def engine(request):
    d={'name':'tata','manufacturedate':1999}
    return render(request,'engine.html',context=d)
