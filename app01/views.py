from django.shortcuts import render,HttpResponse,redirect
import json
# Create your views here.


# def index(request):
#     return render(request, 'index.html')
# def index(request):
#     print(111)
#     data = {"name":'xhf','age':111}
#     response = HttpResponse(json.dumps(data))
#     response['Access-Control-Allow-Origin'] = 'http://127.0.0.1:8000'
#     return response
def index(request):
    print(111)
    data = {"name":'xhf','age':111}

    return HttpResponse('func("%s")'%data)


def add_ajax(request):
    i1 = request.GET.get("i1")
    i2 = request.GET.get("i2")
    print(i1,i2)
    ret = int(i1)+int(i2)
    return HttpResponse(ret)


def login(request):
    return render(request,"login.html")