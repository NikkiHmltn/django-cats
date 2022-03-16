from django.shortcuts import render
# from django.views import View #this handles our requests
from django.views.generic.base import TemplateView
from django.http import HttpResponse #this handles SENDING any type of response

# Create your views here.

# ============Old========== #
# #Home extends the View class so we can render a simple response to the web
# class Home(View):
#     #this is a method that runs with a 'get' request
#     def get(self, request):
#         #we are simply returning a generic string. this acts like a 'res.send()' from express!
#         return HttpResponse("Cats Home Page!")

# ===========Rework============= #

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"
