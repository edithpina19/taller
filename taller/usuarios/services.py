# usuarios/services.py
import re

NEGOCIO = {
    "nombre": "Instalaciones Universales",
    "saludo": "Hola, soy Instalaciones Universales. ¿En qué puedo ayudarte hoy?",
    "direccion": "Plaza Cultural IRCA Jarachina Sur, San Pedro 169, Reynosa, Tamps.",
    "telefono": "899 257 1482",
    "horario": "Lunes a Sábado de 10:00 a.m. a 10:00 p.m.",
    "servicios": "Reparamos aparatos electrónicos, instalaciones, mantenimiento y servicio a domicilio."
}

CLAVES = {
    "telefono": ["telefono","teléfono","celular","numero","número","contacto","llamar","tel","whatsapp"],
    "direccion": ["direccion","dirección","ubicacion","ubicación","donde estan","ubicados","localización"],
    "horario": ["horario","hora","abren","cierran","horas","apertura","cierre"],
    "servicios": ["servicios","dedican","que hacen","qué hacen","ofrecen","instalaciones","reparan","domicilio","trabajan","funcion"]
}

def coincide(lista, texto):
    texto = texto.lower()
    return any(p in texto for p in lista)

def get_gemini_response(prompt: str) -> str:
    p = prompt.lower()

    # Saludo general
    if p in ["hola", "hi", "buenas", "qué tal", "hey"]:
        return NEGOCIO["saludo"]

    # Respuestas directas
    if coincide(CLAVES["telefono"], p):
        return f"📞 Nuestro número es: {NEGOCIO['telefono']}"

    if coincide(CLAVES["direccion"], p):
        return f"📍 Estamos ubicados en: {NEGOCIO['direccion']}"

    if coincide(CLAVES["horario"], p):
        return f"🕒 Nuestro horario es: {NEGOCIO['horario']}"

    if coincide(CLAVES["servicios"], p):
        return NEGOCIO["servicios"]

    # Respuesta general si no coincide nada
    return "Puedo ayudarte con teléfono, dirección, horario o servicios. ¿Qué deseas saber?"
