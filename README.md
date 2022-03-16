# Starting Up a New Django Project with Pipenv
- Run `pipenv install django` (Note: if you get the 'command not found: pipenv' error, try to uninstall and reinstall pipenv!)
- After that, open up the virtual environment with `pipenv shell`
- `django-admin startproject <app-name-here> .` Don't forget the `.` it's very important for your file structure!
- Now we can start up our server to make sure it can run with `python3 manage.py runserver`. Assuming all is working, we should see our rocket ship! 
![django rocket ship](/images/Screen Shot 2022-03-15 at 5.53.39 PM.png)

Don't worry about the message of unapplied migrations just yet. After you confirm the server is working, we can stop the process with `control + c`. Then we can exit anytime out of our virtual envirnment with `exit`