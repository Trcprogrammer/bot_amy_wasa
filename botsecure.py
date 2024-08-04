import time
import os
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import json
from termcolor import colored
from art import text2art
import random
import logging
import argparse
import re

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class WhatsAppBot:
    def __init__(self, config):
        chromedriver_autoinstaller.install()

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.phone_numbers = config['phone_numbers']
        self.messages = config['messages']
        self.max_messages = config.get('max_messages', 10)
        self.short_pause = config.get('short_pause', (1, 3))
        self.long_pause = config.get('long_pause', (600, 900))

    def open_whatsapp_web(self):
        self.driver.get("https://web.whatsapp.com/")
        input(colored("Escanea el código QR y presiona Enter para continuar...", "green"))

    def check_whatsapp_logged_in(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Escribe un mensaje"]'))
            )
            logging.info("Usuario conectado a WhatsApp Web.")
            return True
        except Exception as e:
            logging.error("No se pudo verificar el estado de conexión en WhatsApp Web. Error: %s", e)
            return False

    def validate_phone_number(self, number):
        pattern = re.compile(r'^\+\d{1,3}\d{10,12}$')
        return pattern.match(number)

    def send_messages(self):
        messages_sent = 0

        for number in self.phone_numbers:
            if not self.validate_phone_number(number):
                logging.warning(f"Número de teléfono inválido: {number}. Saltando...")
                continue

            if messages_sent >= self.max_messages:
                logging.info("Pausa larga para evitar ser detectado...")
                time.sleep(random.uniform(*self.long_pause))
                messages_sent = 0

            try:
                logging.info(f"Abriendo chat con {number}...")
                self.driver.get(f"https://web.whatsapp.com/send?phone={number}")

                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Escribe un mensaje"]'))
                )

                for message in self.messages:
                    message_box = WebDriverWait(self.driver, 30).until(
                        EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Escribe un mensaje"]'))
                    )

                    message_box.send_keys(message)
                    message_box.send_keys(Keys.ENTER)

                    logging.info(f"Mensaje enviado a {number}: {message}")
                    messages_sent += 1

                    time.sleep(random.uniform(*self.short_pause))

                time.sleep(random.uniform(*self.short_pause))

            except Exception as e:
                logging.error(f"No se pudo enviar los mensajes a {number}. Error: {e}")
                self.driver.get("https://web.whatsapp.com/")

    def quit(self):
        self.driver.quit()

def load_config(file_path):
    if not os.path.exists(file_path):
        logging.error(f"El archivo {file_path} no existe.")
        return {}

    with open(file_path, 'r') as file:
        return json.load(file)

def main(config_path):
    config = load_config(config_path)

    if not config:
        logging.error("Configuración no cargada. Saliendo...")
        return

    bot = WhatsAppBot(config)

    bot.open_whatsapp_web()

    if bot.check_whatsapp_logged_in():
        bot.send_messages()

    bot.quit()

    print(colored("¡Todos los mensajes han sido enviados exitosamente! 💻", "green"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="WhatsApp Bot de Amalia")
    parser.add_argument('-c', '--config', type=str, required=True, help="Ruta al archivo de configuración JSON")
    args = parser.parse_args()

    print(colored(text2art("AMY BOT", font='small'), "green"))
    print(colored("🔥🌟 Bienvenido al WhatsApp Bot de Amalia 🌟🔥", "green"))

    main(args.config)




# {
#     "phone_numbers": ["+1234567890", "+0987654321"],
#     "messages": ["Hola, este es un mensaje de prueba.", "Este es otro mensaje de prueba."],
#     "max_messages": 10,
#     "short_pause": [1, 3],
#     "long_pause": [600, 900]
# }



# python script.py -c config.json