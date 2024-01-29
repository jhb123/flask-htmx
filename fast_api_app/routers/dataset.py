import os
from pathlib import Path
import json
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/results")

database = Path(os.environ.get("FLASK_DATABASE_PATH","./database"))
templates = Jinja2Templates(directory="./app/templates")


@router.get("/dataset/{name}", response_class=HTMLResponse)
async def dataview(request: Request, name):
    path = database / name / "data.json"


    with open(path,"r",encoding="utf-8") as f:
        data = json.load(f)

    return templates.TemplateResponse(
        request=request, name="dataset.html", context={"name": name, "path": path, "data": data}
    )

@router.get("/dataset/{name}/heatmap", response_class=HTMLResponse)
async def heatmap(request: Request, name, response_class=HTMLResponse):
    path = database / name / "data.json"

    with open(path,"r",encoding="utf-8") as f:
        data = json.load(f)

    x = data["experiment_0"]["x"]

    y = [i for i, k in enumerate(data)]
    z = [data[exp]["y"] for exp in data]

    return templates.TemplateResponse(request=request,name="heatmap.html", context={"name":f"{name}", "x": x,"y": y,"z": z, "figure_title": f"{name}"})

@router.get("/dataset/{name}/{experiment}", response_class=HTMLResponse)
async def figure(request: Request, name: str, experiment: str, response_class=HTMLResponse):
    path = database / name / "data.json"

    with open(path,"r",encoding="utf-8") as f:
        data = json.load(f)

    x = data[experiment]["x"]

    y = data[experiment]["y"]

    return templates.TemplateResponse(request=request, name="data_table.html", context={"data":data, "name":f"{name}", "x":x,"y":y, "figure_title": f"{name}-{experiment}","experiment": experiment})
