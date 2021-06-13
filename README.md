## Introduction

This is a web application fully made with Django where you can `(login/register)` user, `(create)` categories and `(create/view/edit/delete/filter/sort/like)` articles.

## How to setup

- `git clone` repo
- Initialize a virtual environment `python -m venv venv`
- Enter virtual environment in this case venv
  - Windows: `source venv/Scripts/activate`
  - Mac/Linux: `source venv/bin/activate`
- Install packages `pip install -m requirements.txt`
- Create a .env file and include the variable `PROJECT_SECRET_KEY`, in order to generate a key you can do the following:
  - Run `python manage.py shell`
  - Inside the shell perform: `from django.core.management.utils import get_random_secret_key`
  - Then call the function `get_random_secret_key()`
  - Copy the string and place it inside the .env variable.
- Migrate the models `python manage.py migrate`
- Then runserver `python manage.py runserver`

### Optional

- To create admin user:
  - Run `python manage.py createsuperuser`
  - Enter your credentials

## How to use

- ### Web:
  - Register user, then login.
  - There is an icon in the banner to create a new article, there you have the ability to either choose a category or create one from scratch. Afterwards you can proceed with filling the rest of the article info.
  - You will be redirected to the articles page where you can view/edit any article you have permission for.
- ### API:
  There are two API paths you can use, one to create an article and one to view all published articles.
  - Login using your username and password.
  - Then use any of the following APIs:
    - Create API:
      ```
        METHOD: POST
        URL: <HOST>/articles/create_article
        BODY: {
          "title": <STR>,
          "description": <STR>,
          "category": <INT>
        }
      ```
    - List API:
      ```
        METHOD: GET
        URL: <HOST>/articles/list_articles
        BODY: {
          "status": <STR>,
          "title": <STR>,
          "description": <STR>,
          "category": <INT>
        }
      ```
