import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import json
from termcolor import colored
from art import text2art

class setup:
    def __init__(self, option):
        self.option = option
    
    def choose_option(self):
        print(colored(text2art("SETUP BOT", font='small'), "green"))
        print(colored('[1]: Iniciar bot', "green"))
        print(colored('[2]: Cambiar Mensajes', "green"))
        print(colored('[3]: Cambiar Números telefónicos', "green"))
        print(colored('[4]: Salir del bot', "red"))
        
        if self.option == "1":
            print(colored(text2art("AMY BOT", font='small'), "green"))
            print(colored("🔥🌟 Bienvenido al WhatsApp Bot de Amalia 🌟🔥", "green"))
            data = load_data_from_json('data.json')
            phone_numbers = data['phone_numbers']
            messages = data['messages']
            bot = WhatsAppBot(phone_numbers, messages)
            bot.open_whatsapp_web()
            bot.send_messages()
            bot.quit()
            print(colored("¡Todos los mensajes han sido enviados exitosamente! 💻", "green"))
        elif self.option == "4":
            print(colored("Saliendo del bot...", "red"))
        else:
            print(colored("Opción no válida. Intenta de nuevo.", "red"))


class WhatsAppBot:
    def __init__(self, phone_numbers, messages):
        chromedriver_autoinstaller.install()

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.add_argument("start-maximized")  # Para maximizar la ventana en Windows
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.phone_numbers = phone_numbers
        self.messages = messages

    def open_whatsapp_web(self):
        self.driver.get("https://web.whatsapp.com/")
        input(colored("Escanea el código QR y presiona Enter para continuar...", "green"))

    def send_messages(self):
        for number in self.phone_numbers:
            try:
                print(colored(f"Abriendo chat con {number}...", "cyan"))
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

                    print(colored(f"Mensaje enviado a {number}: {message}", "green"))

                    if "https://www.instagram.com" not in message:
                        time.sleep(1)

                time.sleep(1)

            except Exception as e:
                print(colored(f"No se pudieron enviar los mensajes a {number}. Error: {e}", "red"))

    def quit(self):
        self.driver.quit()


def load_data_from_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


if __name__ == "__main__":
    print(colored(text2art("SETUP BOT", font='small'), "green"))
    option = input("Elige una opción: ")
    init = setup(option)
    init.choose_option()
