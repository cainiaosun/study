from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.


def login(request):
    if request.method == "POST":
        print("我们重新开始吧！")
        return HttpResponse("zheshi")
    else:
        print("我们重新开始吧！")
        return render_to_response("login.html")