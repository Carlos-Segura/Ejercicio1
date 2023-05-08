from Clase_Email import Email

class ManejadorEmail():
    
    def __init__(self):
        self.__listaEmails = []
    
    def BuscarCorreo(self, correoBuscado):
        while cuenta in self.__listaEmails and cuenta.retornaEmail() != correoBuscado:
            if cuenta.Clase_Email.retornaEmail() != correoBuscado:
                print('El correo ingresado no existe...')
                cuenta = None
        return cuenta
                
    def CambiarContrasenia(self, correo):
        cuenta = self.BuscarCorreo(correo)
        if cuenta != None:
            #cuenta.setContraseña()
            cuenta.Clase_Email.setContrasenia 
                
    def CrearCuenta(self, correo):
        i = correo.find('@')
        j=-1
        result = True
        if i != -1:
            j = i+1
            while j < len(correo) and correo[j] != '.':
                j += 1
        else:
            print("Error. El correo ingresado no es valido")
            result = False
        if i != -1 and  j != -1 and j < len(correo):
            #print(f'Id: {correo[0:i]} - dominio: {correo[i+1:j]} - tipoDominio: {correo[j+1:len(correo)]}')
            self.__listaEmails.append(Email.Email(correo[0:i], correo[i+1:j], correo[j+1:len(correo)], input('Ingrese la contraseña nueva: ')))
        else:
            print("Error. El correo no es valido")
            result = False
        return result
    
    def retornaListaConCorreosGuardados(self):
        for cuenta in self.__listaEmails:
            print(cuenta.retornaEmail())
        
