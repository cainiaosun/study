from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
import json

# Create your views here.

def login(request):
    result={}
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        result["username"]= username
        result["password"] = password
        result=json.dumps(result)
        print(type(username))
        print(result)
        return HttpResponse(result)
    else:
        return render_to_response("login.html")