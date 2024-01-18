from flask import Blueprint, render_template

bp = Blueprint('results', __name__, url_prefix='/results')

@bp.route('/dataset/<name>', methods=('GET', 'POST'))
def dataview(name):
    return render_template("dataset.html", name=name)