import crud
import core
import os

ARCHIVO = "cgu.json"


def limpiar():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\nPresione ENTER para continuar...")


def menu_principal():
    while True:
        limpiar()
        print("****************************************")
        print("*  Sistema Créditos para Grado UNAB    *")
        print("*              CGU                     *")
        print("****************************************")
        print("1. Registrar estudiante")
        print("2. Login estudiante")
        print("3. Gestión de programas")
        print("4. Gestión de noticias")
        print("5. Mantenimiento")
        print("6. Salir")

        op = input("Seleccione una opción: ")

        if op == "1":
            crud.registrar_estudiante()
            pausar()

        elif op == "2":
            estudiante = crud.login()
            pausar()
            if estudiante:
                menu_estudiante(estudiante)

        elif op == "3":
            menu_programas()

        elif op == "4":
            menu_noticias()

        elif op == "5":
            crud.mantenimiento()
            pausar()

        elif op == "6":
            print("Gracias por usar CGU.")
            break

        else:
            print("Opción inválida.")
            pausar()


def menu_estudiante(estudiante):
    while True:
        limpiar()
        print("******** MENÚ ESTUDIANTE CGU ********")
        print("1. Registrar créditos CGU")
        print("2. Ver mis créditos")
        print("3. ¿Cuántos créditos he cursado?")
        print("4. Créditos faltantes para grado")
        print("5. Promedio por mes")
        print("6. Promedio por año")
        print("7. Promedio por semestre")
        print("8. Ver noticias")
        print("9. Inscribirme a noticias")
        print("10. Volver")

        op = input("Seleccione una opción: ")

        if op == "1":
            crud.agregar_credito(estudiante)
        elif op == "2":
            crud.listar_creditos(estudiante)
        elif op == "3":
            crud.total_creditos(estudiante)
        elif op == "4":
            crud.creditos_faltantes(estudiante)
        elif op == "5":
            crud.promedio_por_mes(estudiante)
        elif op == "6":
            crud.promedio_por_anio(estudiante)
        elif op == "7":
            crud.promedio_por_semestre(estudiante)
        elif op == "8":
            crud.listar_noticias()
        elif op == "9":
            crud.suscribirse_noticias(estudiante)
        elif op == "10":
            break
        else:
            print("Opción inválida.")

        pausar()


def menu_programas():
    while True:
        limpiar()
        print("******** CRUD PROGRAMAS ********")
        print("1. Agregar programa")
        print("2. Listar programas")
        print("3. Editar programa")
        print("4. Eliminar programa")
        print("5. Volver")

        op = input("Seleccione una opción: ")

        if op == "1":
            crud.agregar_programa()
        elif op == "2":
            crud.listar_programas()
        elif op == "3":
            crud.editar_programa()
        elif op == "4":
            crud.eliminar_programa()
        elif op == "5":
            break
        else:
            print("Opción inválida.")

        pausar()


def menu_noticias():
    while True:
        limpiar()
        print("******** CRUD NOTICIAS ********")
        print("1. Crear noticia")
        print("2. Listar noticias")
        print("3. Editar noticia")
        print("4. Eliminar noticia")
        print("5. Volver")

        op = input("Seleccione una opción: ")

        if op == "1":
            crud.crear_noticia()
        elif op == "2":
            crud.listar_noticias()
        elif op == "3":
            crud.editar_noticia()
        elif op == "4":
            crud.eliminar_noticia()
        elif op == "5":
            break
        else:
            print("Opción inválida.")

        pausar()


if __name__ == "__main__":
    core.crearInfo(ARCHIVO)
    menu_principal()