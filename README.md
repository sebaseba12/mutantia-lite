# MutantIA Lite

MutantIA Lite es un asistente educativo basado en Telegram que responde preguntas utilizando bloques de conocimiento almacenados en Google Sheets.

## 🚀 ¿Qué hace?

- Recibe mensajes desde Telegram.
- Busca respuestas en un archivo JSON generado desde Google Sheets.
- Devuelve la respuesta más relevante.

## 🛠️ Requisitos

- Python 3.10 o superior
- Una cuenta de Telegram con un bot
- Google Sheets con acceso API

## ⚙️ Cómo usar

1. Crea tu archivo `.env` con tu `TELEGRAM_TOKEN` y `SHEET_ID`.
2. Coloca tu `credentials.json` en la carpeta raíz.
3. Ejecuta:

```bash
python sheets_to_json.py
python main.py
