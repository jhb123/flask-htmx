from flask import Blueprint, render_template
import numpy as np

bp = Blueprint('results', __name__, url_prefix='/results')

@bp.route('/dataset/<name>', methods=('GET', 'POST'))
def dataview(name):
    return render_template("dataset.html", name=name)

@bp.route('/dataset/<name>/<exponent>', methods=('GET', 'POST'))
def figure(name,exponent):
    x = np.linspace(-10, 10, 100)

    y = np.power(x, int(exponent))

    return render_template("figure.js", name=name, x=x.tolist(),y=y.tolist())