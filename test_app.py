import pytest
from prueba import App

@pytest.fixture
def app():
    return App()

def test_CrearUsuarioFuncional(app):
    usuario = app.CrearUsuario("Thammy", "thammy@gmail.com")
    assert usuario["nombre"] == "Thammy"
    assert usuario["correo"] == "thammy@gmail.com"

def test_CrearUsuarioVacio(app):
    with pytest.raises(ValueError, match="El nombre no puede estar vacío"):
        app.CrearUsuario("", "thammy@gmail.com")

def test_CrearCorreoInvalido(app):
    with pytest.raises(ValueError, match="El correo no es válido"):
        app.CrearUsuario("Thammy", "correo_invalido")

def test_InicioSesionFuncional(app):
    usuarios = [{"nombre": "Thammy", "password": "1234"}]
    mensaje = app.IniciarSesion(usuarios, "Thammy", "1234")
    assert mensaje == "Inicio de sesión exitoso"

def test_InicioSesionIncorrecto(app):
    usuarios = [{"nombre": "Thammy", "password": "1234"}]
    with pytest.raises(ValueError, match="Credenciales incorrectas"):
        app.IniciarSesion(usuarios, "Thammy", "wrongpass")
