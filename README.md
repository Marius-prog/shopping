# Contents

## shopping API

## Setup Python Virtual Environment


clone repo https://github.com/Marius-prog/shopping.git

cd shopping

python3 -m venv venv

. venv/bin/activate

pip3 install -r requirements.txt

python manage.py createsuperuser

## Running Server


Make sure to be in shopping directory.

python mange.py migrate

python mange.py runserver


## shopping API documentation

Go and check endpoints http://127.0.0.1:8000/docs/ 
