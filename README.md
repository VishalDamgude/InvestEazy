# InvestEazy
 Stock Investment simulator with real time data from National Stock Exchange

# Features: 

- View all stocks listed on the National Stock Exchange.
- View the top gainers and losers of today.
- Buy/Sell stocks (intraday trading available).
- Every user starts with a balance of 1 lakh Rs.
- View all of your orders.
- A portfolio which shows all your stocks, as well as the amount invested in them and the current value.
- Simplistic color coding to show which investments have been profitable.

# Screenshots:
![Alt text](./Docs/HomePage.PNG?raw=true "HomePage")

# Steps for Installation:

- Install Django (v>=3.2)
- Install nsetools and other python modules using requirements.txt file. python -m pip install -r requirements.txt
  Recommended to create python virtual environment for this project.
- Install Postgresql db server. After basic configuration, create a db called 'investdb', and a user, and grant all privileges to this user for this db. Do the necessary configs in investpro\investpro\settings.py file, DATABASES dictionary.
- Set up Redis on your machine.
- cd investpro and Run > python manage.py migrate
- Create a superuser > python manage.py createsuperuser (to access the admin panel).
- Now Run > python manage.py runserver
- Open two more terminals and navigate to investpro (the folder containing manage.py)
- In one, run > celery -A investpro worker -l info
- In the second, run > celery -A investpro beat -l info
- Access gui of application in browser using http://localhost:8000
