import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
import os

# Cargar variables del entorno
load_dotenv()
SHEET_ID = os.getenv("SHEET_ID")

def cargar_bloques_desde_sheets():
    # Definir el alcance de acceso a Sheets y Drive
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    # Cargar credenciales desde el archivo credentials.json
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    # Abrir la hoja de cálculo por su ID
    sheet = client.open_by_key(SHEET_ID).sheet1  # Primera pestaña

    # Leer todas las filas como diccionarios
    registros = sheet.get_all_records()
    print("📄 Registros leídos desde Sheets:")
    print(registros)  # <--- Línea agregada para depurar

    bloques = []
    for fila in registros:
        bloque = {
            "contenido": fila.get("contenido", ""),
            "fuente": fila.get("fuente", ""),
            "fecha": fila.get("fecha", ""),
            "etiquetas": fila.get("etiquetas", ""),
            "nuevo": str(fila.get("nuevo", "")).lower() == "true"
        }
        bloques.append(bloque)

    # Guardar como JSON
    with open("bloques.json", "w", encoding="utf-8") as f:
        json.dump(bloques, f, ensure_ascii=False, indent=2)

    print(f"✅ bloques.json actualizado con {len(bloques)} bloques.")

if __name__ == "__main__":
    cargar_bloques_desde_sheets()
