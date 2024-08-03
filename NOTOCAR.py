import os
import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Instala automáticamente la versión correcta de chromedriver
chromedriver_autoinstaller.install()

# Configura el controlador del navegador
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

# Abre WhatsApp Web
driver.get("https://web.whatsapp.com/")

# Espera manual para escanear el código QR
input("Escanea el código QR y presiona Enter para continuar...")

# Números de teléfono y mensaje a enviar
phone_numbers = [
    '+18298811619',
    '+18498613595'
]
message = "Hola, este es un mensaje de prueba."
image_name = "azul.jpg"

def send_messages():
    for number in phone_numbers:
        try:
            print(f"Abriendo chat con {number}...")
            driver.get(f"https://web.whatsapp.com/send?phone={number}")

            # Espera a que se cargue la página de chat y el campo de mensaje esté visible
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Escribe un mensaje"]'))
            )

            # Encuentra el campo de mensaje
            message_box = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Escribe un mensaje"]'))
            )

            # Asegúrate de que el campo de mensaje esté en foco
            actions = ActionChains(driver)
            actions.move_to_element(message_box).click().perform()

            # Espera un momento para asegurarse de que el campo de mensaje esté activo
            time.sleep(1)

            # Limpia el campo de mensaje antes de enviar
            message_box.clear()

            # Escribe el mensaje letra por letra en el campo de mensaje
            for char in message:
                message_box.send_keys(char)
                time.sleep(0.1)  # Ajusta este tiempo si es necesario

            # Espera un momento para asegurarse de que el mensaje se haya escrito completo
            time.sleep(1)

            # Envía el mensaje completo con Enter
            message_box.send_keys(u'\ue007')

            print(f"Mensaje enviado a {number}")

            # Espera antes de enviar la imagen
            time.sleep(5)  # Ajusta según sea necesario

            # Envía la imagen
            try:
                # Encuentra el botón de adjuntar (clip) y haz clic en él
                attach_button = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '//div[@title="Adjuntar"]'))
                )
                attach_button.click()

                # Encuentra el input para seleccionar el archivo y envía el archivo
                file_input = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
                )
                file_input.send_keys(os.path.join(os.getcwd(), image_name))

                # Espera un momento para asegurarse de que el archivo se haya cargado
                time.sleep(10)

                # Encuentra el botón de enviar y haz clic en él
                send_image_button = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="send"]'))
                )
                send_image_button.click()

                print(f"Imagen enviada a {number}")

            except Exception as e:
                print(f"No se pudo enviar la imagen a {number}. Error: {e}")

            # Espera antes de enviar el siguiente mensaje
            time.sleep(5)  # Ajusta según sea necesario

        except Exception as e:
            print(f"No se pudo enviar el mensaje a {number}. Error: {e}")

# Ejecuta la función para enviar mensajes
send_messages()

# Cierra el navegador después de enviar todos los mensajes
driver.quit()






































import os
import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Instala automáticamente la versión correcta de chromedriver
chromedriver_autoinstaller.install()

# Configura el controlador del navegador
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

# Abre WhatsApp Web
driver.get("https://web.whatsapp.com/")

# Espera manual para escanear el código QR
input("Escanea el código QR y presiona Enter para continuar...")

# Números de teléfono y mensaje a enviar
phone_numbers = [
    '+18298811619',
    '+18498613595'
]
message = "Hola, este es un mensaje de prueba."
image_path = "hl.jpeg"  # Ruta a la imagen

def send_messages():
    for number in phone_numbers:
        try:
            print(f"Abriendo chat con {number}...")
            driver.get(f"https://web.whatsapp.com/send?phone={number}")

            # Espera a que se cargue la página de chat y el campo de mensaje esté visible
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Escribe un mensaje"]'))
            )

            # Encuentra el campo de mensaje
            message_box = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Escribe un mensaje"]'))
            )

            # Limpia el campo de mensaje antes de enviar
            message_box.clear()

            # Escribe el mensaje en el campo de mensaje
            message_box.send_keys(message)
            message_box.send_keys(u'\ue007')  # Enviar mensaje con Enter

            print(f"Mensaje enviado a {number}")

            # Espera antes de enviar la imagen
            time.sleep(5)  # Ajusta según sea necesario

            # Envía la imagen usando send_keys
            try:
                # Encuentra el área de chat para arrastrar y soltar
                chat_area = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"]'))
                )

                # Usa el input tipo archivo para enviar la imagen
                file_input = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
                )
                file_input.send_keys(os.path.abspath(image_path))

                # Espera a que se cargue la vista previa de la imagen
                WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//div[@class="_1E0yF"]'))  # Ajusta este XPath según sea necesario
                )

                # Encuentra el botón de enviar y haz clic en él
                send_image_button = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="send-light"]'))
                )
                send_image_button.click()

                print(f"Imagen enviada a {number}")

            except Exception as e:
                print(f"No se pudo enviar la imagen a {number}. Error: {e}")

            # Espera antes de enviar el siguiente mensaje
            time.sleep(5)  # Ajusta según sea necesario

        except Exception as e:
            print(f"No se pudo enviar el mensaje a {number}. Error: {e}")

# Ejecuta la función para enviar mensajes
send_messages()

# Cierra el navegador después de enviar todos los mensajes
driver.quit()
















import os
import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Instala automáticamente la versión correcta de chromedriver
chromedriver_autoinstaller.install()

# Configura el controlador del navegador
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

# Abre WhatsApp Web
driver.get("https://web.whatsapp.com/")

# Espera manual para escanear el código QR
input("Escanea el código QR y presiona Enter para continuar...")

# Números de teléfono y mensaje a enviar
phone_numbers = [
    '+18298811619',
    '+18498613595'
]
message = "Hola, este es un mensaje de prueba."
image_path = "hl.jpeg"  # Ruta a la imagen

def send_messages():
    for number in phone_numbers:
        try:
            print(f"Abriendo chat con {number}...")
            driver.get(f"https://web.whatsapp.com/send?phone={number}")

            # Espera a que se cargue la página de chat y el campo de mensaje esté visible
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Escribe un mensaje"]'))
            )

            # Encuentra el campo de mensaje
            message_box = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Escribe un mensaje"]'))
            )

            # Limpia el campo de mensaje antes de enviar
            message_box.clear()

            # Escribe el mensaje en el campo de mensaje
            message_box.send_keys(message)
            message_box.send_keys(u'\ue007')  # Enviar mensaje con Enter

            print(f"Mensaje enviado a {number}")

            # Espera antes de enviar la imagen
            time.sleep(1)  # Ajusta según sea necesario

            # Envía la imagen usando send_keys
            try:
                # Encuentra el área de chat para arrastrar y soltar
                chat_area = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"]'))
                )

                # Usa el input tipo archivo para enviar la imagen
                file_input = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
                )
                file_input.send_keys(os.path.abspath(image_path))

                # Espera a que se cargue la vista previa de la imagen
                WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//div[@class="_1E0yF"]'))  # Ajusta este XPath según sea necesario
                )

                # Encuentra el botón de enviar y haz clic en él
                # send_image_button = WebDriverWait(driver, 30).until(
                #     EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="send-light"]'))
                # )
                # send_image_button.click()
                message_box.send_keys(u'\ue007')  # Enviar imagen con Enter
                
                # Presiona Enter después de enviar la imagen para asegurarse de que se envíe
                time.sleep(1)  # Espera para asegurar que la imagen se cargue completamente
                message_box.send_keys(u'\ue007')  # Enviar la imagen con Enter

                print(f"Imagen enviada a {number}")

            except Exception as e:
                print(f"No se pudo enviar la imagen a {number}. Error: {e}")

            # Espera antes de enviar el siguiente mensaje
            time.sleep(5)  # Ajusta según sea necesario

        except Exception as e:
            print(f"No se pudo enviar el mensaje a {number}. Error: {e}")

# Ejecuta la función para enviar mensajes
send_messages()