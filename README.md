# Company Test App
### Run

1. Create virtual env:
    - to create `python -m venv venv `
    - to activate `source venv/bin/activate `
2. Install requirements - `pip install -r requirements/base.txt`
3. Run the migrations:
    - `python manage.py makemigrations`
    - `python manage.py migrate`
4. Create super user if need
   - `python manage.py createsuperuser`
4. Run app - `python manage.py runserver`
