from django.shortcuts import render
import json
# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
import json

def login(request):
    print("我们重新开始吧！")
    print("reponse type is:",request.method)
    result={}
    if request.method == "GET":
        username = request.GET.get("username")
        password = request.GET.get("password")
        result["username"]=username
        result["password"] = password
        result=json.dumps(result)
        print("username is:", username)
        return HttpResponse(result)
    else:
        return render_to_response("login.html")


