import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import json

class WhatsAppBot:
    def __init__(self, phone_numbers, messages):
        chromedriver_autoinstaller.install()
        
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.phone_numbers = phone_numbers
        self.messages = messages

    def open_whatsapp_web(self):
        self.driver.get("https://web.whatsapp.com/")
        input("Escanea el código QR y presiona Enter para continuar...")

    def send_messages(self):
        for number in self.phone_numbers:
            try:
                print(f"Abriendo chat con {number}...")
                self.driver.get(f"https://web.whatsapp.com/send?phone={number}")

                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Escribe un mensaje"]'))
                )

                for message in self.messages:
                    message_box = WebDriverWait(self.driver, 30).until(
                        EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Escribe un mensaje"]'))
                    )

                    message_box.send_keys(message)

                    if "https://www.instagram.com" in message:
                        time.sleep(6)  
                    message_box.send_keys(Keys.ENTER)

                    print(f"Mensaje enviado a {number}: {message}")

                    if "https://www.instagram.com" not in message:
                        time.sleep(1) 

                time.sleep(1)  

            except Exception as e:
                print(f"No se pudo enviar los mensajes a {number}. Error: {e}")

    def quit(self):
        self.driver.quit()

def load_phone_numbers_from_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

if __name__ == "__main__":
    phone_numbers = load_phone_numbers_from_json('phone_numbers.json')
    messages = [
        "<3 Saludos, me llamo Amalia y soy una florista de flores eternas",
        "Espero que estés bien. Descubre nuestra hermosa colección de flores frescas. Para ver más, visita nuestro perfil en Instagram: https://www.instagram.com/p/C9x02ZhvkZo/?igsh=MmhpcnEzaXV3N3N1",
        "¡Gracias por tu tiempo y que tengas un excelente día!"
    ]

    bot = WhatsAppBot(phone_numbers, messages)
    bot.open_whatsapp_web()
    bot.send_messages()
    bot.quit()
