Mkdir flask-boilerplate

Cd flask-boilerplate

Git init

cp directory of the file that is being copied(the .gitignore file) .(here)

cp directory of the file that is being copied(the setup.py file) .(here)

within setup add the code block from discord

  extras_require={
    'test': [
        'pytest',
        'coverage',
        ],
        },

virtual environment python3 -m venv venv

source venv/bin/activate

which python

python –version

(this is the normal dependencies) pip install -e .

which flask

(this is the dev dependencies) pip install -e ‘.[test]’

Which pytest

Which coverage

Echo $FLASK_APP

Echo $FLASK_ENV

export FLASK_APP=flask_boilerplate

export FLASK_ENV=development

Echo $FLASK_APP

Echo $FLASK_ENV

Git status

Mkdir flask_boilerplate

Create and open flask_boilerplate/__init__.py

	From flask import Flask


	def create_app():
		app = Flask(__init__)

		@app.route(‘/’)
		def index():
			return ‘Hello, World!’

		return app

flask run
