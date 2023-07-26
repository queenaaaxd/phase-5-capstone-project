# Simply Beverages, easy peasy lemon squeezy.

## Set Up:

1. pipenv install;pipenv shell
2. npm install --prefix client
3. cd server
4. python app.py
5. npm start --prefix client

## In Terminal, `cd` into `server` and run the following:

    # export FLASK_APP=app.py
    # export FLASK_RUN_PORT=5000
    # flask db init
    # flask db revision --autogenerate -m 'Create tables'
    # flask db upgrade
    # python seed.py

pip install flask-restful
pip install Flask-Cors
