import fractal_tasks_demo
import json
from pathlib import Path


PACKAGE = "fractal_tasks_demo"
PACKAGE_DIR = Path(fractal_tasks_demo.__file__).parent
MANIFEST_FILE = PACKAGE_DIR / "__FRACTAL_MANIFEST__.json"
with MANIFEST_FILE.open("r") as f:
    MANIFEST = json.load(f)
    TASK_LIST = MANIFEST["task_list"]
