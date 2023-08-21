"""Init database module importing all src models from modules"""
import os

ROOT_PATH = "src/modules"


def database_path(module_name):
    """Function returning models location from module param"""
    return f"{ROOT_PATH}/{module_name}/database/models"


MODULE = ""
MODEL = ""
for MODULE in os.listdir(ROOT_PATH):
    if MODULE in ("__init__.py", "__pycache__"):
        continue
    for MODEL in os.listdir(database_path(MODULE)):
        if MODEL in ("__init__.py", "__pycache__"):
            continue
        __import__(
            database_path(MODULE).replace("/", ".") + f".{MODEL[:-3]}",
            locals(),
            globals(),
        )
del MODEL
del MODULE
