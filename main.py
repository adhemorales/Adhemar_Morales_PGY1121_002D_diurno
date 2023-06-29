from LIBRO import *
import numpy as np
import random as rn
arreglo_libro = np.array([])
ciclo = True

def GrabarLibro(arreglo_libro):
    libro = Libro()
    c = False
    while c == False:
        c = libro.setCodigo(input("Ingrese Codigo de libro:"))
    libro.titulo = input("Ingrese Titulo del Libro:")
    libro.autor = input("Ingrese Autor:")
    c = False
    while c == False:
        try:
            c = libro.setPrecio(int(input("Ingrese precio de Libro:")))
        except BaseException as error:
            print(f"Error:{error}")
    libro.pais = input("Ingrese Pais de origen Libro:")
    c = False
    while c == False:
        c = libro.setAno_publicacion(int(input("Ingrese Año de Publicacion:")))
    return np.append(arreglo_libro, libro)



def BuscarLibro(arreglo_libro):
    codigo = input("Ingrese codigo:")
    flag = True
    for libro in arreglo_libro:
        if codigo == libro.codigo:
            flag = True
            print("Datos del libro")
            print(f"Codigo:{libro.codigo}")
            print(f"Titulo:{libro.titulo}")
            print(f"Autor:{libro.autor}")
            print(f"Pais:{libro.pais}")
            print(f"Año Publicacion:{libro.ano_publicacion}")
            print(f"Precio:{libro.precio}")
            print(f"Categoria:{libro.categoria}")
            break
    if flag == False:
        print("Codigo de Libro no existe")


def informe_pais(arreglo_libro):
    num_lista = rn.randint(1500,5000)
    print(f"Numero lista:{num_lista}")
    print("Informe por Pais")
    total = 0
    for libro in arreglo_libro:
        print(f"Codigo de Libro:{libro.codigo}")
        print(f"Titulo de Libro:{libro.titulo}")
        total += libro.precio
        print(f"Total:{libro.precio}")
        print(f"Autor:{libro.autor}")


def informe_categoria(arreglo_libro):
    num_lista = rn.randint(1500,5000)
    print(f"Numero lista:{num_lista}")
    print("Informe por Categoria")
    total = 0
    for libro in arreglo_libro:
        print(f"Codigo de Libro:{libro.codigo}")
        print(f"Titulo de Libro:{libro.titulo}")
        total += libro.precio
        print(f"Total:{libro.precio}")
        print(f"Autor:{libro.autor}")


def Imprimir_Informe(arreglo_libro):
    print("Informes")
    print("1) Informe por Pais")
    print("2) Informe por Categoria")
    print("3) Salir")
    try:
        op_informe = int(input("Seleccione (1-3): "))
        match op_informe:
            case 1:
                informe_pais(arreglo_libro)
            case 2:
                informe_categoria(arreglo_libro)
    except BaseException as error:
        print(f"Error:{error}")

def salir():
    print("Autor: Adhemar Morales")
    print("Version 1.0")

#################





while ciclo:
    print("Libreria Mayor")
    print("1) Grabar Libro")
    print("2) Buscar Libro")
    print("3) Imprimir Informes")
    print("4) Salir")
    try:
        op = int(input("Seleccione (1-4):"))
        match op:
            case 1:
                arreglo_libro = GrabarLibro(arreglo_libro)
            case 2:
                BuscarLibro(arreglo_libro)
            case 3:
                Imprimir_Informe(arreglo_libro)
            case 4:
                ciclo = salir()
    except BaseException as error:
        print(f"Error{error}")