from funciones import ver_credenciales,tipo_usuario
from administrador import menu_administrador
from usuario import menu_usuario

def iniciar_sesion():
    intentos=0
    while intentos<3:
        print("---LOGIN---")
        nombre =input("Ingrese su nombre de usuario: ")
        contraseña=input("Ingrese su contraseña: ")
        if ver_credenciales(nombre,contraseña):
            print("Inicio de sesion correcto")
            return nombre
        else:
            print("Usuarios o contraseñas incorrectas")
            intentos=intentos + 1
    print("Supero el numero de intentos permitidos")
    return None            

def main():
    print("---SISTEMA DE LOGIN---")
    while True:       
        nombre=iniciar_sesion() 
        if nombre is not None:
            tipo=tipo_usuario(nombre)
            if tipo =="administrador":
                menu_administrador()     
            elif tipo == "usuario":
                menu_usuario(nombre)
        else:
            break        
main()         


        