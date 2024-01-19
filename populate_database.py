import os
import json
from pathlib import Path

import numpy as np


if __name__ == "__main__":
    base_path = Path(os.environ.get('FLASK_DATABASE_PATH', './database'))

    for i in range(20):
        dataset_path = base_path/f"dataset_{i}"
        try:
            dataset_path.mkdir()
        except FileExistsError:
            print("Directory already exists")

        data = {}

        for i in range(1000):
            data[f"experiment_{i}"] = {"x": np.arange(0,100).tolist(), "y": np.random.rand(100).tolist()}
            
        with open(dataset_path/"data.json", "w+", encoding="utf-8") as f:
            json.dump(data,f, indent=4)
