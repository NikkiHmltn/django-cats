from django.shortcuts import render
from django.urls import reverse
# from django.views import View #this handles our requests
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse #this handles SENDING any type of response
from .models import Cat
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
        # to get the query parameter we have to acccess it in the request.GET dictionary object        
        name = self.request.GET.get("name")
        # If a query exists we will filter by name 
        if name != None:
        # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["cats"] = Cat.objects.filter(name__icontains=name)
            # We add a header context that includes the search param
            context["header"] = f"Searching for {name}"
        else:
            context["cats"] = Cat.objects.all()
            # default header for not searching 
            context["header"] = "Our Cats"
        return context

class CatCreate(CreateView):
    model = Cat
    fields = ['name', 'img', 'age', 'gender']
    template_name = "cat_create.html"
    # ===== OLD FOR INITIAL CATCREATE VIEW ===== #
    # success_url = "/cats/"
    # ===== NEW REFACTOR FOR GET SUCCESS URL REDIRECT ===== #
    def get_success_url(self):
        return reverse('cat_detail', kwargs={'pk': self.object.pk})

class CatDetail(DetailView):
    model = Cat
    template_name= "cat_detail.html"

class CatUpdate(UpdateView):
    model = Cat
    fields = ['name', 'img', 'age', 'gender']
    template_name = "cat_update.html"
    # ===== OLD FOR INITIAL CATCREATE VIEW ===== #
    # success_url = "/cats/"
    # ===== NEW REFACTOR FOR GET SUCCESS URL REDIRECT ===== #
    def get_success_url(self):
        return reverse('cat_detail', kwargs={'pk': self.object.pk})

class CatDelete(DeleteView):
    model = Cat
    template_name = "cat_delete_confirmation.html"
    success_url = "/cats/"