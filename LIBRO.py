class Libro:
    codigo = ''
    titulo = ''
    autor = ''
    precio = 10000
    pais = ''
    ano_publicacion=''

    def __init__(self):
        self.codigo = "AAA-000"
        self.titulo = 'La cenicienta'
        self.autor = 'Jorge'
        self.precio= 10000
        self.pais = 'Chile'
        self.ano_publicacion = '1990'
        self.categoria = 'Accion'

    def setCodigo(self,codigo):
        if len(codigo) == 7:
            if codigo[0:3].isalpha() and codigo[3:4] == '-' and codigo[4:5].isdigit():
                self.codigo = codigo
                return True
            else:
                print("Formato Incorrecto")
                return False
        else:
            print("El largo debe ser de 6")
            return False
    def setPrecio(self,precio):
        if precio >= 10000 and precio <= 150000:
            self.precio = precio
            return True
        else:
            print("El precio debe ser entre 10000 y 150000")
            return False

    def setAno_publicacion(self,ano_publicacion):
        if ano_publicacion >=1780 and ano_publicacion <=2023:
            self.ano_publicacion = ano_publicacion
            return True
        else:
            print("El año debe estar entre 1780 y 2023")
            return False
