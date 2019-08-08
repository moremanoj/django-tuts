* Basic requirements are Python 3.6+ 

1. create a virtual environment : ``` virtualenv env ```
2. activate a virtual environment : ``` source env/bin/activate ``` OR ``` .\env\Scripts\activate ```
3. install required pacakges of django :  ``` pip install -r requirements.txt ```
4. migrate databases command : ``` python manage.py makemigrations ``` 
    and after that ``` python manage.py migrate ```
5. add admin to access admin access  : ``` python manage.py createsuperuser ```
6. run server :  ``` python manage.py runserver ```
