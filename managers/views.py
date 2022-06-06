from django.shortcuts import render
#from django.http import HttpResponse
from django.views.generic import View

# Create your views here.

#def index(request):
 #   return render(request,"index.html")
#def login(request):
 #   return render(request,"login.html")


class IndexView(View):
    def get(self,request):
        return render(request,"index.html")



class LoginView(View):
        def get(self,request):
            return render(request,"login.html")
        def post(self,request):
            print(request.POST.get("u_name"))
            print(request.POST.get("p_name"))
            return render(request,"login .html")




class RegView(View):
    def get(self,request):
        return render(request,"reg.html")
    def post(self,request):
        print("post here")
        print(request)
        print(request.POST)
        print(request.POST["f_name"])
        print(request.POST["l_name"])
        print(request.POST["e_name"])
        print(request.POST["m_name"])   # if we are using POST[],error will be occur for an invalid keyword (eg fn_name)

        print(request.POST.get("u_name"))     # if we are using get instead of POST[], the resulit will be none for an invali keyword
        print(request.POST.get("p_name"))
        return render(request,"reg.html")