This project is a website developped with Django Framework (v.3.1) using Python language (v.3.7.6).

The name of the website is 'Purbeurre' and is intended to propose you a better aliment than the one you entered in the search field, all based on the nutriscore.

In this version, there a 5 categories of aliments : Drinks, Meats, Biscuits, Cheeses and Dessert and an amount of 468 products taken from Open Food Facts database.
You can change those parameters in populate.py file.

The visitor can save its favorite products only after being authenticated.

To install the repo on your computer you must follow these steps:
- Create a virtual environment
- Create a folder and initiate a git repo with `git init`
- Type `git remote add https://github.com/6netic/p8-purbeurre.git`
- Download the repo on your computer with `git clone https://github.com/6netic/p8-purbeurre.git`
- Install the required libraries to your virtual environment with `pip3 install -r requirements.txt`
- Install postgresql, create a database called 'purbeurre_db', a user 'p8user' with password 'p8Passw'
- To create the tables, type `python3 manage.py migrate`
- To populate the tables, type `python3 manage.py populate`
- Now you can run the local server by typing `python3 manage.py run server`
- To see the website just open a browser and type as the address : localhost:8000

