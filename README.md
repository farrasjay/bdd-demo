This is a **Django** project made by **Farras Hafizhudin Indra Wijaya (2106652682)** using [`behave-django`](https://behave-django.readthedocs.io/en/stable/) with the intention of exploring and applying Behavior-Driven Development (BDD). 

## Bash Commands
```bash
# activate venv
venv\Scripts\activate.bat

# install venv's requirements
pip install -r requirements.txt

# run django's server
python manage.py runserver

# run BDD tests
python manage.py behave

# run BDD tests with HTML report
python manage.py behave --format behave_html_formatter:HTMLFormatter --outfile reports/bdd_report.html
```

## Docs

[BDD Note](https://docs.google.com/document/d/1dv9lx74oH6H0AF2nhmivQmaP4vNMXRerGyAJJPkZN8A/edit?usp=sharing) - detailed note on what i've learned from exploring and applying BDD.