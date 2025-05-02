import os
import json
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    ContextTypes, filters
)
from motor import buscar_mejor_respuesta  # Asegúrate de que motor.py tenga esta función

# Cargar variables de entorno
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola, soy MutantIA Lite. Pregúntame lo que quieras.")

# Manejo de mensajes
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje = update.message.text

    # Cargar bloques desde el archivo JSON
    with open("bloques.json", "r", encoding="utf-8") as f:
        bloques = json.load(f)

    # Obtener respuesta
    respuesta = buscar_mejor_respuesta(mensaje, bloques)
    await update.message.reply_text(respuesta)

# Crear y ejecutar app
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot en marcha...")
    app.run_polling()
