# Spider-WebDev-backend-task4
First I created a modelForm for user registration which requires username and password. The password should be re entered correctly and the captcha system is attached to it.Now the user can only view the posts.The update permission can be given in the admin panel by giving staff status for the user.

Admin can be created using the command: python manage.py createsuperuser
the username,email and password should be given.

list of server routes (it runs on port 8000) 127.0.0.1:8000/admin - displays admin page 127.0.0.1:8000/task/register-- registration page
127.0.0.1:8000/task/login--login page once logged in u'll be able to see the posts.


BUILD INSTRUCTIONS:

u can download django from this site: https://www.djangoproject.com/download/ then download the file named 'spider' in my repository and copy and paste it in the django directory in ur c:// drive then go to Windows power shell and go into the spider directory (for eg: cd C://django/spider) and run the command "python manage.py runserver" copy the link displayed in ur browser and press enter now add "/task/register" to the url to register
