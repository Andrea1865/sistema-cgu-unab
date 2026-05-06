import json
import os

RUTA_DATA = "data"
ARCHIVO = "cgu.json"


def asegurar_carpeta():
    if not os.path.exists(RUTA_DATA):
        os.makedirs(RUTA_DATA)


def estructura_inicial():
    return {
        "estudiantes": [],
        "programas": [],
        "creditos": [],
        "noticias": [],
        "suscripciones": []
    }


def checkFile(fileName):
    asegurar_carpeta()
    return os.path.exists(f"{RUTA_DATA}/{fileName}")


def crearInfo(fileName):
    asegurar_carpeta()
    if not checkFile(fileName):
        with open(f"{RUTA_DATA}/{fileName}", "w", encoding="utf-8") as file:
            json.dump(estructura_inicial(), file, indent=4, ensure_ascii=False)


def LoadInfo(fileName):
    crearInfo(fileName)
    with open(f"{RUTA_DATA}/{fileName}", "r", encoding="utf-8") as file:
        return json.load(file)


def editarInfo(fileName, data):
    asegurar_carpeta()
    with open(f"{RUTA_DATA}/{fileName}", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)