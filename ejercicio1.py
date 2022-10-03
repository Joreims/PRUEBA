"""Una tienda que ofrece el servicio de recargas celular le contrata a usted para
realizar una aplicación que permita registrar las ventas de recargas hechas en
el día para lo cual se desea almacenar la siguiente: número del celular,
compañía y monto que compra. La aplicación debe tener las siguientes
opciones:
a. Agregar Recarga
b. Ver monto vendido por recargas Tigo
c. Ver monto vendido por recargas Claro
d. Ver monto del día """

from recargas import recargar as rg, listarecarga as a

def menu():
    print("1. Agregar recarga")
    print("2. Mostrar recargas por compañía")
    print("3. Ver monto del día")
    op = int(input("Escriba una opción: "))
    return op

def agregarRecarga():
    print("Recarga:")
    compañia = print("Compañía:")
    if (compañia.upper="TIGO")
        numcelu=print("Numero de celular: ")
        monto = print("Monto de la recarga")
        t=rg(numcelu,monto)
        a.agregarRecargaTIGO(t)
        print("RECARGA EN PROCESO")
        print("Recarga realizada")
        system("pause")
    elif (compañia.upper="CLARO"):
        numcelu=print("Numero de celular: ")
        monto = print("Monto de la recarga")
        t=rg(numcelu,monto)
        a.agregarRecargaCLARO(t)
        print("RECARGA EN PROCESO")
        print("Recarga realizada")
        system("pause")
def mostrarRTIGO():
        print("Monto de recarga tigos realizadas: ", recargaTIGO)
def mostrarRCLARO():
        print("Monto de recarga Claro realizada: ", recargaCLARO)

def Monto():
    MontoDIA = recargaTIGO + recargaCLARO
    print("El monto del día es: ", str(MontoDIA))

def main():
    op = menu()
    if op == 1: agregarRecarga()
    elif op == 2: menuR()
    elif op == 3: Monto()


def menuR():
    print("¿Que compañía desea ver?:")
    print("1. TIGO")
    print("2. CLARO")
    op = int(input("Escriba una opción: "))
    return op
    menuRECARGA()

def menuRECARGA():
    op = menuR()
    if op == 1: print("Monto del dia TIGO: ", str(recargaTIGO))
    elif op == 2: print("Monto del dia CLARO: ", str(recargaCLARO))
main()
