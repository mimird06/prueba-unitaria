import os
os.system('cls')

class App:
    def CrearUsuario(self, nombre, correo):
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")
        if "@" not in correo:
            raise ValueError("El correo no es válido")
        return {"nombre": nombre, "correo": correo}

    def IniciarSesion(self, usuarios, nombre, password):
        usuario = next((u for u in usuarios if u["nombre"] == nombre and u["password"] == password), None)
        if usuario:
            return "Inicio de sesión exitoso"
        raise ValueError("Credenciales incorrectas")
