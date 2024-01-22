import json
from flask import Blueprint, render_template, current_app
import numpy as np

bp = Blueprint('results', __name__, url_prefix='/results')

@bp.route('/dataset/<name>', methods=(['GET']))
def dataview(name):
    path = current_app.config['FLASK_DATABASE_PATH'] / name / "data.json"

    with open(path,"r",encoding="utf-8") as f:
        data = json.load(f)

    return render_template("dataset.html", name=name, path=path, data=data)

@bp.route('/dataset/<name>/<experiment>', methods=(['GET']))
def figure(name,experiment):
    path = current_app.config['FLASK_DATABASE_PATH'] / name / "data.json"

    with open(path,"r",encoding="utf-8") as f:
        data = json.load(f)

    x = data[experiment]["x"]

    y = data[experiment]["y"]

    return render_template("data_table.html", data=data, name=f"{name}", x=x,y=y, figure_title=f"{name}-{experiment}",experiment=experiment)


@bp.route('/dataset/<name>/heatmap', methods=(['GET']))
def heatmap(name):
    path = current_app.config['FLASK_DATABASE_PATH'] / name / "data.json"

    with open(path,"r",encoding="utf-8") as f:
        data = json.load(f)

    x = data["experiment_0"]["x"]

    y = [i for i, k in enumerate(data)]
    z = [data[exp]["y"] for exp in data]

    return render_template("heatmap.html", name=f"{name}", x=x,y=y,z=z, figure_title=f"{name}")