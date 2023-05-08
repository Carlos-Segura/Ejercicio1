class Email():
  def __init__(self, idCuenta, dominio, tipoDominio, contrasenia):
    self.__idCuenta = idCuenta
    self.__dominio = dominio
    self.__tipoDominio = tipoDominio
    self.__contrasenia = contrasenia

  def __getIdCuenta(self):
    return self.__idCuenta

  def getDominio(self):
    return '@' + self.__dominio

  def __getTipoDominio(self):
    return '.' + self.__tipoDominio

  def retornaEmail(self):
    return self.__getIdCuenta() + self.getDominio() + self.__getTipoDominio()

  def __getContraseniaActual(self):
    return self.__contrasenia

  def __nuevaContrasenia():
    nuevaContrasenia = ""
    sonDistintas = True
    while sonDistintas:
      nuevaContrasenia = input("Ingrese la nueva contrasenia\n")
      copia = input("Repita la contrasenia\n")
      sonDistintas = nuevaContrasenia != copia
      if sonDistintas:
        print("Error. Las contrasenias son distintas, por favor revise.")
    return nuevaContrasenia

  def setContrasenia(self, contraseniaIngresada):
    resultadoCambio = True
    if contraseniaIngresada != self.__getContraseniaActual():
      print("Error. La contrasenia ingresada no es correcta")
      resultadoCambio = False
    else:
      self.__contrasenia = self.__nuevaContrasenia()
      print("La contrasenia se cambio con exito")
    return resultadoCambio