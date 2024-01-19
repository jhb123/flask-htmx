import os
from pathlib import Path
from flask import Flask, render_template, send_from_directory, current_app


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
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

    app.config['FLASK_DATABASE_PATH'] = Path(os.environ.get('FLASK_DATABASE_PATH', '/database'))


    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def index():
        db_path = current_app.config['FLASK_DATABASE_PATH']
        # Get a list of directories using iterdir() and is_dir()
        directories_list = [entry.name for entry in db_path.iterdir() if entry.is_dir()]
        directories_paths = [entry for entry in db_path.iterdir() if entry.is_dir()]
        datasets = list(zip(directories_list, directories_paths))
        
        sorted_data = sorted(datasets, key= lambda x: int(x[0].split("_")[-1]))

        return render_template('index.html', datasets=sorted_data)

    @app.route('/static/<path:filename>')
    def static_file(filename):
        return send_from_directory('static', filename)

    from . import results
    app.register_blueprint(results.bp)

    return app