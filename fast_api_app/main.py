import os
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .routers import dataset

app = FastAPI()

app.include_router(dataset.router)
db_path = Path(os.environ.get("FLASK_DATABASE_PATH","./database"))
templates = Jinja2Templates(directory="./app/templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    # Get a list of directories using iterdir() and is_dir()
    directories_list = [entry.name for entry in db_path.iterdir() if entry.is_dir()]
    directories_paths = [entry for entry in db_path.iterdir() if entry.is_dir()]
    datasets = list(zip(directories_list, directories_paths))
    
    sorted_data = sorted(datasets, key= lambda x: int(x[0].split("_")[-1]))

    return templates.TemplateResponse(
        request=request, name='index.html', context={"datasets":sorted_data})