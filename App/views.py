from django.shortcuts import render

# Create your views here.
from App.forms import *
from django.http import HttpResponse

def memory(request):
    d={'TO':Topics(),'PO':Pages(),'RO':Records()}
    if request.method=='POST':
        TDO=Topics(request.POST)
        PDO=Pages(request.POST)
        RDO=Records(request.POST)
        if TDO.is_valid() and PDO.is_valid() and RDO.is_valid():
            NST=TDO.save(commit=False)
            NST.save()
            NSP=PDO.save(commit=False)
            NSP.topic=NST
            NSP.save()
            NSR=RDO.save(commit=False)
            NSR.name=NSP
            NSR.save()
            return HttpResponse('Data Submitted Perfectly')
        else:
            return HttpResponse('Invalid details entered')
    return render(request,'memory.html',d)