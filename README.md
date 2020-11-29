For this project number 11, I used project 10 and added some modifications to enhance functionalities.

We had to simulate a bug made in production environment, so I renamed a link in purbeurre/food/views.py.
The consequence is that the website showed an internal server error (500).

I also noticed a bug in responsive design mode where product pictures and nutriscore labels displayed didn't behave as expected when the screen shrinks.
Then I fixed it.

After that, I added two new functionalities:

- when a product is saved by an authenticated user, it becomes impossible to click on it trying saving it again.
Instead, a notification 'Enregistré' appears.

- Authenticated user can now modify his password.

To install that project locally, please refer to Project10 to get the steps one after the other.