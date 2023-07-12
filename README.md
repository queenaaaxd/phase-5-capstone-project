# Phase 4, Lecture 6: Client-Server Communication

## Setup

1. Fork and then Clone this repository.

2. Make sure that you are in the correct directory (folder) that contains a `Pipfile`, then run `pipenv install` in your terminal to install the required Python libraries.

3. Now that your `pipenv` virtual environment is ready to use, enter `pipenv shell` to enter the virtual environment.

4. Run `npm install --prefix client` in your terminal to install the dependencies for the React app.

5. Enter the command `cd server` in the terminal to move into the server directory.

6. Enter the command `python app.py` in the terminal to run the Flask app (make sure that you are in the `server` directory before running this terminal command).

7. In a new terminal, run `npm start --prefix client` in your terminal to run the React app in the browser. If your browser does not automatically open the page for you, open [http://localhost:4000](http://localhost:4000) to view it in your browser.

## If you are using this lecture repository as your Phase 4 Project template

1. Make sure that you are in the root directory of this repository. You can enter the command `ls` in the terminal and if you see the `Pipfile`, `Pipfile.lock`, and `README.md` then you are in the correct directory.
2. Run `rm -rf .git` in the terminal to remove existing git configuration.
3. Run `git init` to initialize the project as a git repository.



# Set Up:
    # In Terminal, `cd` into `server` and run the following:
        # export FLASK_APP=app.py
        # export FLASK_RUN_PORT=5000
        # flask db init
        # flask db revision --autogenerate -m 'Create tables' 
        # flask db upgrade 
        # python seed.py


pip install flask-restful
pip install Flask-Cors


>>> u2 = User.query.get(8)
>>> u2.transaction_products
[<Product name=Celsius Sparklng Kiwi price=21 units=1000>]
>>> u1 = User.query.get(2)
>>> u1
{ User 2 }
>>> u1.transaction_products
[<Product name=Monster Energy + Juice price=57 units=1000>]
>>> u1.transaction_products
[<Product name=Monster Energy + Juice price=57 units=1000>]