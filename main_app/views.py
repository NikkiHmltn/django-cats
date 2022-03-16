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

class Cat:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

cats = [
    Cat("Mau", 5, "Female"),
    Cat("Garfield", 43, "Male"),
    Cat("Meowth", 25, "Male"),
    Cat("Salem", 500, "Male"),
]

class CatList(TemplateView):
    template_name = 'catlist.html'
    # get_context_data returns a dictionary that populates a dictionary with our data (our cats list)

    # **kwargs is a dictionary of keyword arguments. the ** sort of acts as a spread operator in that it accepts any amount of arguments into the function. this really comes in handy for when our routes start to use various params like :id

    # a keywored argument is where you provide a name to the variable as you pass it into the function. think of it similar to .map() in js where we can get the key and the value from

    # ====== Run kwarg.py for **kwargs examples ====== *

    # we need super() in order to get the context that the class based views would generate by default. This helps us call the base implementation first to get a context.

    # context = super().get_context_data(**kwargs) is literally the entire views.py classes

    #if you deep-dive under the hood of get_context_data while using a super() to do some intense wizardry and magic to grab everything on this page
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cats"] = cats
        return context
