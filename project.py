import os
from flask import Flask, render_template, redirect, url_for

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return render_template('home.html')

    @app.route('/test')
    def test():
        return render_template('test.html')

    @app.route('/about')
    def about():
        return render_template('about.html')
    
    @app.route('/login')
    def login():
        return render_template('login.html')

    """ from . import db
    db.init_app(app) """
    
    return app
#flask --app project run --host=0.0.0.0 --debug