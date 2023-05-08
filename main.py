import ClaseManejadorEmail

def menuOpciones():
    print("1 = Crear Cuenta")
    
    print("99 = Cerrar Programa")

if __name__ == '__main__':
    manejador = ClaseManejadorEmail.ManejadorEmail()
    
    menuOpciones()
    opcion = int(input("Que desea hacer? "))
    while opcion != 99:
        if opcion == 1:
            manejador.CrearCuenta(input("Correo a registrar\n"))
        elif opcion == 2:
            print(manejador.retornaListaConCorreosGuardados())
        menuOpciones()
        opcion = int(input("Que desea hacer? "))
        