import pytest
from prueba import App

@pytest.fixture
def app():
    return App()

def test_CrearUsuarioFuncional(app):
    usuario = app.CrearUsuario("Franceily", "thammy@gmail.com")
    assert usuario["nombre"] == "Franceily"
    assert usuario["correo"] == "thammy@gmail.com"

def test_CrearUsuarioVacio(app):
    with pytest.raises(ValueError, match="El nombre no puede estar vacío"):
        app.CrearUsuario("", "thammy@gmail.com")

def test_CrearCorreoInvalido(app):
    with pytest.raises(ValueError, match="El correo no es válido"):
        app.CrearUsuario("Franceily", "correo_invalido")

def test_InicioSesionFuncional(app):
    usuarios = [{"nombre": "Franceily", "password": "1234"}]
    mensaje = app.IniciarSesion(usuarios, "Franceily", "1234")
    assert mensaje == "Inicio de sesión exitoso"

def test_InicioSesionIncorrecto(app):
    usuarios = [{"nombre": "Franceily", "password": "1234"}]
    with pytest.raises(ValueError, match="Credenciales incorrectas"):
        app.IniciarSesion(usuarios, "Franceily", "wrongpass")
