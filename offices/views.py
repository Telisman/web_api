from django.shortcuts import render
from django.http import JsonResponse
from .models import Offices
from .serializers import OfficesSerializers
from .forms import Office


def offices(request):
    offices = Offices.objects.all()
    serializers = OfficesSerializers(offices, many=True)
    return JsonResponse(serializers.data, safe=False)

def AddOfffice(request):
    submitted = False
    if request.method == "POST":
        form = Office(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'office.html')
        else:
            pass
    form = Office
    return render(request,"add_office.html", {'form': form})

def officesView(request):
    office = Offices.objects.all()
    context = {
        'office': office,
    }
    return render(request, "office.html", context)
