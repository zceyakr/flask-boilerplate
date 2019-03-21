from flask import Flask, request, abort, make_response


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.route('/')
    def index():
        return 'Hello World!'

    @app.route('/hello')
    def hello():

        for key, value in request.args.items():
            print(f"{key}: {value}")

        name = request.args.get('name', 'World')
        return f"Hello {name}!"

    @app.route('/number/<int:n>')
    def number_route(n):
        return f"Number: {n}"

    @app.route('/method', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
    def method_route():
        return f"HTTP Method: {request.method}"

    @app.route('/status')
    def status_route():
        code = request.args.get('c', 200)
        response = make_response("", code)

        return response

    return app
