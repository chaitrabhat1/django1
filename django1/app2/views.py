from django.shortcuts import render
from app1.forms import inputform
from itertools import permutations

def home(request):
    result=0
    n1=""
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            n1=data.get("input")
            result=get_permutations(n1)
            return render(request,"app2/index.html",{'param1':result, 'param2':n1, 'form':form1})
    else:
        form1=inputform()  
    return render(request,"app2/index.html",{'param1':result, 'param2':n1, 'form':form1})


def get_permutations(s):
    return [''.join(p) for p in permutations(s)]
