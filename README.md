# Starting Up a New Django Project with Pipenv
- Run `pipenv install django` (Note: if you get the 'command not found: pipenv' error, try to uninstall and reinstall pipenv!)
- After that, open up the virtual environment with `pipenv shell`
- `django-admin startproject <app-name-here> .` Don't forget the `.` it's very important for your file structure!
- Now we can start up our server to make sure it can run with `python3 manage.py runserver`. Assuming all is working, we should see our rocket ship! 
![django rocket ship](/images/rocketship.png)

Don't worry about the message of unapplied migrations just yet. After you confirm the server is working, we can stop the process with `control + c`. Then we can exit anytime out of our virtual envirnment with `exit`

# Setting Up Our Application 

- Once this is done, we need to put our application inside of our project folder with: `django-admin startapp main_app` or whatever you want to name it.
- With a bunch of new folders and py files, we need to make sure our project recognizes our application by adding it to the list of "INSTALLED_APPS" in the project's `settings.py`
- Now we set up our postgresql database in the same file, so scroll down to "DATABASES" and change it to:
```
'default': 
    {
        'ENGINE': 'django.db.backends.postgresql', #define we are using postgres
        'NAME': 'djangocats', #this is the name of our database
    }
```
- However, this doesn't create our database so we need to do that manually with `createdb djangocats` then run `python3 manage.py migrate` to apply the initial migrations! 
- Test our new changes with `python3 manage.py runserver` and voila!

## Running into some errors by now? 
- Having trouble creating a database with postgres? 
> Make sure you have started your service with `brew services start postgresql`.
- Getting an error with 'no module found named 'psycopg2'? 
> Make sure you are in your pipenv shell before installing the dependency with `pip3 install psycopg2`

# Connect Project URLs to App URLs
- Make a file in your application folder, NOT the project folder (main_app in our case here) called `urls.py`
- Inside of `main_app/urls.py` add the following: 
```
    from django.urls import path
    from . import views

    # this like app.use() in express
    urlpatterns = [

    ]
```

- Now we need to point our project urls to our app urls! Inside of our `djangocats/urls.py` (or whatever you have named your project!), lets add our url patterns for it to follow
```
    from django.contrib import admin
    from django.urls import path, include # <- you must add include to the imports. this is like our app.use! 

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main_app.urls')) # <- here is the new line to include the urls of our app
    ]
```

# Defining Our Views

- Let's set up the route for our home/landing page! I want to be able to pass in a view to the root directory of my application, so let's define that in our `main_app/urls.py` inside of our "urlpatterns" list.
```
path('', views.Home.as_view(), name="home")
```
> To break it down a little further, the url route is our root defined as an empty string, then we are reaching into our views.py, grab the Home class and render it as a view. Then we are simply giving this path/view a name called "home"

- Time to set up our first class called Home as a view! Go into `main_app/views.py` and let's add our class and import some useful tools to help us render it out. So now the views.py should look similar to this:
```
from django.shortcuts import render
from django.views import View #this handles our requests
from django.http import HttpResponse #this handles SENDING any type of response

# Create your views here.

#Home extends the View class so we can render a simple response to the web
class Home(View):
    #this is a method that runs with a 'get' request
    def get(self, request):
        #we are simply returning a generic string. this acts like a 'res.send()' from express!
        return HttpResponse("Cats Home Page!")
```

# Creating and Adding Templates to Views

- First, create a directory called `templates` inside of our `main_app` with `mkdir main_app/templates`.
- We want to render out a template that is an HTML file, so let's practice with a `home.html` so let's make that file inside of our `templates` folder we just made.
- Add a standard boilerplate and add any info you want to display inside of your home file.

