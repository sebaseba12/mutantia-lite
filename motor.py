import re

def limpiar_texto(texto):
    """
    Convierte el texto a minúsculas y elimina signos de puntuación.
    """
    texto = texto.lower()
    texto = re.sub(r'[^\w\s]', '', texto)  # Elimina signos de puntuación
    return texto

def buscar_mejor_respuesta(pregunta, bloques):
    """
    Compara la pregunta con los bloques y devuelve el más relevante.
    """
    pregunta = limpiar_texto(pregunta)
    palabras_pregunta = set(pregunta.split())

    mejor_bloque = None
    max_coincidencias = 0

    for bloque in bloques:
        contenido = limpiar_texto(bloque.get("contenido", ""))
        palabras_bloque = set(contenido.split())
        coincidencias = palabras_pregunta & palabras_bloque  # Intersección

        if len(coincidencias) > max_coincidencias:
            mejor_bloque = bloque
            max_coincidencias = len(coincidencias)

    if not mejor_bloque:
        return "No encontré información relacionada con tu pregunta."

    respuesta = mejor_bloque["contenido"]
    if mejor_bloque.get("nuevo") is True:
        respuesta += "\n\n🆕 Este es un bloque nuevo."

    return respuesta
