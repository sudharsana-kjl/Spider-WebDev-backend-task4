# Spider-WebDev-backend-task4
First I created a modelForm for user registration which requires username and password. The password should be re entered correctly and the captcha system is attached to it.Now the user can only view the posts.The update permission can be given in the admin panel by giving staff status for the user.

Admin can be created using the command: python manage.py createsuperuser
the username,email and password should be given.

list of server routes (it runs on port 8000) 127.0.0.1:8000/admin - displays admin page 127.0.0.1:8000/task/register-- registration page
127.0.0.1:8000/task/login--login page once logged in u'll be able to see the posts.
If u have admin permission, u can go to 127.0.0.1:8000/task/create to add a new form. To update a post, click on it and then go to the update link which has the url 127.0.0.1:8000/task/2/edit ( if 2 is the id of the post). To delete just click on the delete link 127.0.0.1:8000/task/2/delete ( if 2 is the id of the post) given u'll be taken to the list of posts page.

when u give logout, u'll be redirected to the login page.



BUILD INSTRUCTIONS:

u can download django from this site: https://www.djangoproject.com/download/ then download the file named 'spider' in my repository and copy and paste it in the django directory in ur c:// drive then go to Windows power shell and go into the spider directory (for eg: cd C://django/spider) and run the command "python manage.py runserver" copy the link displayed in ur browser and press enter now add "/task/register" to the url to register. you can download the captcha package and install it using the instructions given here https://django-simple-captcha.readthedocs.io/en/latest/usage.html#installation


![ALT TEXT](https://github.com/sudharsana-kjl/Spider-WebDev-backend-task4/blob/master/Screenshot%20(195).png)
![ALT TEXT](https://github.com/sudharsana-kjl/Spider-WebDev-backend-task4/blob/master/Screenshot%20(196).png)
![ALT TEXT](https://github.com/sudharsana-kjl/Spider-WebDev-backend-task4/blob/master/Screenshot%20(197).png)
![ALT TEXT](https://github.com/sudharsana-kjl/Spider-WebDev-backend-task4/blob/master/Screenshot%20(198).png)
![ALT TEXT](https://github.com/sudharsana-kjl/Spider-WebDev-backend-task4/blob/master/Screenshot%20(199).png)
![ALT TEXT](https://github.com/sudharsana-kjl/Spider-WebDev-backend-task4/blob/master/Screenshot%20(200).png)
![ALT TEXT](https://github.com/sudharsana-kjl/Spider-WebDev-backend-task4/blob/master/Screenshot%20(201).png)
![ALT TEXT](https://github.com/sudharsana-kjl/Spider-WebDev-backend-task4/blob/master/Screenshot%20(202).png)
![ALT TEXT](https://github.com/sudharsana-kjl/Spider-WebDev-backend-task4/blob/master/Screenshot%20(203).png)
![ALT TEXT](https://github.com/sudharsana-kjl/Spider-WebDev-backend-task4/blob/master/Screenshot%20(204).png)
![ALT TEXT](https://github.com/sudharsana-kjl/Spider-WebDev-backend-task4/blob/master/Screenshot%20(205).png)
![ALT TEXT](https://github.com/sudharsana-kjl/Spider-WebDev-backend-task4/blob/master/Screenshot%20(206).png)
![ALT TEXT](https://github.com/sudharsana-kjl/Spider-WebDev-backend-task4/blob/master/Screenshot%20(207).png)
![ALT TEXT](https://github.com/sudharsana-kjl/Spider-WebDev-backend-task4/blob/master/Screenshot%20(208).png)
![ALT TEXT](https://github.com/sudharsana-kjl/Spider-WebDev-backend-task4/blob/master/Screenshot%20(209).png)
![ALT TEXT](https://github.com/sudharsana-kjl/Spider-WebDev-backend-task4/blob/master/Screenshot%20(210).png)
![ALT TEXT](https://github.com/sudharsana-kjl/Spider-WebDev-backend-task4/blob/master/Screenshot%20(211).png)
![ALT TEXT](https://github.com/sudharsana-kjl/Spider-WebDev-backend-task4/blob/master/Screenshot%20(212).png)
![ALT TEXT](https://github.com/sudharsana-kjl/Spider-WebDev-backend-task4/blob/master/Screenshot%20(213).png)
![ALT TEXT](https://github.com/sudharsana-kjl/Spider-WebDev-backend-task4/blob/master/Screenshot%20(214).png)
![ALT TEXT](https://github.com/sudharsana-kjl/Spider-WebDev-backend-task4/blob/master/Screenshot%20(215).png)
![ALT TEXT](https://github.com/sudharsana-kjl/Spider-WebDev-backend-task4/blob/master/Screenshot%20(216).png)
