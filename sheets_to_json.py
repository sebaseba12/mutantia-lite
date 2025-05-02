import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
import os

# Cargar variables del entorno
load_dotenv()
SHEET_ID = os.getenv("SHEET_ID")
GOOGLE_CREDENTIALS_JSON = os.getenv("GOOGLE_CREDENTIALS_JSON")

def cargar_bloques_desde_sheets():
    # Alcance para Google Sheets y Drive
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    # Convertir el JSON de las credenciales desde string
    creds_dict = json.loads(GOOGLE_CREDENTIALS_JSON)
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)

    # Abrir hoja por ID
    sheet = client.open_by_key(SHEET_ID).sheet1
    registros = sheet.get_all_records()

    print("📄 Registros leídos desde Sheets:")
    print(registros)

    bloques = []
    for fila in registros:
        bloque = {
            "contenido": fila.get("contenido", "").strip(),
            "fuente": fila.get("fuente", "").strip(),
            "fecha": fila.get("fecha", "").strip(),
            "etiquetas": fila.get("etiquetas", "").strip(),
            "nuevo": str(fila.get("nuevo", "")).lower().strip() in ["true", "sí", "si", "1"]
        }
        bloques.append(bloque)

    # Guardar bloques en archivo JSON
    with open("bloques.json", "w", encoding="utf-8") as f:
        json.dump(bloques, f, ensure_ascii=False, indent=2)

    print(f"✅ bloques.json actualizado con {len(bloques)} bloques.")

if __name__ == "__main__":
    cargar_bloques_desde_sheets()
