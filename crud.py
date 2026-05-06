import core
import os
from datetime import datetime

ARCHIVO = "cgu.json"
META_CREDITOS = 12


class Estudiante:
    def __init__(self, codigo, nombre, email, password, programa):
        self.codigo = codigo
        self.nombre = nombre
        self.email = email
        self.password = password
        self.programa = programa

    def to_dict(self):
        return self.__dict__


class Programa:
    def __init__(self, id_programa, nombre, facultad):
        self.id_programa = id_programa
        self.nombre = nombre
        self.facultad = facultad

    def to_dict(self):
        return self.__dict__


class Credito:
    def __init__(self, codigo_estudiante, cantidad, mes, ano, semestre):
        self.codigo_estudiante = codigo_estudiante
        self.cantidad = cantidad
        self.mes = mes
        self.anio = ano
        self.semestre = semestre

    def to_dict(self):
        return self.__dict__


class Noticia:
    def __init__(self, id_noticia, titulo, contenido, fecha):
        self.id_noticia = id_noticia
        self.titulo = titulo
        self.contenido = contenido
        self.fecha = fecha

    def to_dict(self):
        return self.__dict__


def limpiar():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\nPresione ENTER para continuar...")


def registrar_estudiante():
    data = core.LoadInfo(ARCHIVO)

    codigo = input("Código estudiante: ")
    nombre = input("Nombre completo: ")
    email = input("Email: ")
    password = input("Contraseña: ")
    programa = input("Programa académico: ")

    estudiante = Estudiante(codigo, nombre, email, password, programa)
    data["estudiantes"].append(estudiante.to_dict())

    core.editarInfo(ARCHIVO, data)
    print("Estudiante registrado correctamente.")


def login():
    data = core.LoadInfo(ARCHIVO)

    email = input("Email: ")
    password = input("Contraseña: ")

    for estudiante in data["estudiantes"]:
        if estudiante["email"] == email and estudiante["password"] == password:
            print(f"Bienvenido/a {estudiante['nombre']}")
            return estudiante

    print("Credenciales incorrectas.")
    return None


def agregar_programa():
    data = core.LoadInfo(ARCHIVO)

    id_programa = len(data["programas"]) + 1
    nombre = input("Nombre del programa: ")
    facultad = input("Facultad: ")

    programa = Programa(id_programa, nombre, facultad)
    data["programas"].append(programa.to_dict())

    core.editarInfo(ARCHIVO, data)
    print("Programa agregado correctamente.")


def listar_programas():
    data = core.LoadInfo(ARCHIVO)

    print("\nPROGRAMAS")
    for programa in data["programas"]:
        print(f"{programa['id_programa']} - {programa['nombre']} | {programa['facultad']}")


def editar_programa():
    data = core.LoadInfo(ARCHIVO)

    listar_programas()
    id_programa = int(input("ID del programa a editar: "))

    for programa in data["programas"]:
        if programa["id_programa"] == id_programa:
            programa["nombre"] = input("Nuevo nombre: ")
            programa["facultad"] = input("Nueva facultad: ")
            core.editarInfo(ARCHIVO, data)
            print("Programa editado.")
            return

    print("Programa no encontrado.")


def eliminar_programa():
    data = core.LoadInfo(ARCHIVO)

    listar_programas()
    id_programa = int(input("ID del programa a eliminar: "))

    data["programas"] = [
        p for p in data["programas"] if p["id_programa"] != id_programa
    ]

    core.editarInfo(ARCHIVO, data)
    print("Programa eliminado.")


def agregar_credito(estudiante):
    data = core.LoadInfo(ARCHIVO)

    cantidad = int(input("Cantidad de créditos cursados: "))
    mes = int(input("Mes: "))
    anio = int(input("Año: "))
    semestre = input("Semestre, ejemplo 2026-1: ")

    credito = Credito(
        estudiante["codigo"],
        cantidad,
        mes,
        anio,
        semestre
    )

    data["creditos"].append(credito.to_dict())
    core.editarInfo(ARCHIVO, data)
    print("Crédito registrado correctamente.")


def listar_creditos(estudiante):
    data = core.LoadInfo(ARCHIVO)

    print("\nMIS CRÉDITOS CGU")
    for c in data["creditos"]:
        if c["codigo_estudiante"] == estudiante["codigo"]:
            print(
                f"{c['cantidad']} créditos | Mes: {c['mes']} | Año: {c['anio']} | "
                f"Semestre: {c['semestre']}"
            )


def total_creditos(estudiante):
    data = core.LoadInfo(ARCHIVO)

    total = sum(
        c["cantidad"]
        for c in data["creditos"]
        if c["codigo_estudiante"] == estudiante["codigo"]
    )

    print(f"Has cursado {total} créditos CGU.")
    return total


def creditos_faltantes(estudiante):
    total = total_creditos(estudiante)
    faltan = META_CREDITOS - total

    if faltan <= 0:
        print("Ya cumpliste los créditos requeridos para grado.")
    else:
        print(f"Te faltan {faltan} créditos para grado.")


def promedio_por_mes(estudiante):
    data = core.LoadInfo(ARCHIVO)
    meses = {}

    for c in data["creditos"]:
        if c["codigo_estudiante"] == estudiante["codigo"]:
            meses.setdefault(c["mes"], []).append(c["cantidad"])

    for mes, valores in meses.items():
        print(f"Mes {mes}: promedio {sum(valores) / len(valores):.2f}")


def promedio_por_ano(estudiante):
    data = core.LoadInfo(ARCHIVO)
    anos = {}

    for c in data["creditos"]:
        if c["codigo_estudiante"] == estudiante["codigo"]:
            anos.setdefault(c["ano"], []).append(c["cantidad"])

    for ano, valores in anos.items():
        print(f"Año {ano}: promedio {sum(valores) / len(valores):.2f}")


def promedio_por_semestre(estudiante):
    data = core.LoadInfo(ARCHIVO)
    semestres = {}

    for c in data["creditos"]:
        if c["codigo_estudiante"] == estudiante["codigo"]:
            semestres.setdefault(c["semestre"], []).append(c["cantidad"])

    for semestre, valores in semestres.items():
        print(f"Semestre {semestre}: promedio {sum(valores) / len(valores):.2f}")


def crear_noticia():
    data = core.LoadInfo(ARCHIVO)

    id_noticia = len(data["noticias"]) + 1
    titulo = input("Título: ")
    contenido = input("Contenido: ")
    fecha = datetime.now().strftime("%Y-%m-%d")

    noticia = Noticia(id_noticia, titulo, contenido, fecha)
    data["noticias"].append(noticia.to_dict())

    core.editarInfo(ARCHIVO, data)
    print("Noticia creada.")


def listar_noticias():
    data = core.LoadInfo(ARCHIVO)

    print("\nNOTICIAS")
    for n in data["noticias"]:
        print(f"{n['id_noticia']} - {n['titulo']} | {n['fecha']}")
        print(n["contenido"])
        print("-" * 40)


def editar_noticia():
    data = core.LoadInfo(ARCHIVO)

    listar_noticias()
    id_noticia = int(input("ID de noticia a editar: "))

    for noticia in data["noticias"]:
        if noticia["id_noticia"] == id_noticia:
            noticia["titulo"] = input("Nuevo título: ")
            noticia["contenido"] = input("Nuevo contenido: ")
            core.editarInfo(ARCHIVO, data)
            print("Noticia editada.")
            return

    print("Noticia no encontrada.")


def eliminar_noticia():
    data = core.LoadInfo(ARCHIVO)

    listar_noticias()
    id_noticia = int(input("ID de noticia a eliminar: "))

    data["noticias"] = [
        n for n in data["noticias"] if n["id_noticia"] != id_noticia
    ]

    core.editarInfo(ARCHIVO, data)
    print("Noticia eliminada.")


def suscribirse_noticias(estudiante):
    data = core.LoadInfo(ARCHIVO)

    if estudiante["codigo"] not in data["suscripciones"]:
        data["suscripciones"].append(estudiante["codigo"])
        core.editarInfo(ARCHIVO, data)
        print("Te has suscrito a las noticias.")
    else:
        print("Ya estás suscrito.")


def mantenimiento():
    data = core.LoadInfo(ARCHIVO)

    claves = ["estudiantes", "programas", "creditos", "noticias", "suscripciones"]

    for clave in claves:
        if clave not in data:
            data[clave] = []

    core.editarInfo(ARCHIVO, data)
    print("Mantenimiento realizado correctamente.")