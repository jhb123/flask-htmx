import os
from pathlib import Path
from app import create_app

if __name__ == "__main__":
    # use this to start it in debug mode
    app =  create_app()
    app.config['FLASK_DATABASE_PATH'] = Path(os.environ.get('FLASK_DATABASE_PATH', '/database'))

    app.run(host="0.0.0.0", port="5000", debug=True)