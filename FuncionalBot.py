import os
import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
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
            message_box.send_keys(Keys.ENTER)  # Enviar mensaje con Enter

            print(f"Mensaje enviado a {number}")

            # Espera antes de enviar la imagen
            time.sleep(2)  # Espera de 2 segundos

            # Envía la imagen usando send_keys
            try:
                # Encuentra el input tipo archivo para enviar la imagen
                file_input = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
                )
                file_input.send_keys(os.path.abspath(image_path))

                # Espera a que se cargue la vista previa de la imagen
                WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/div/div/div[2]/div/div[2]/div[2]/div/div'))
                )

                # Intentar enviar la imagen usando Ctrl + Enter
                try:
                    message_box.send_keys(Keys.CONTROL + Keys.ENTER)
                    print(f"Imagen enviada a {number} usando Ctrl + Enter")
                except Exception as e:
                    print(f"No se pudo enviar la imagen con Ctrl + Enter. Error: {e}")

                # Intentar enviar la imagen haciendo clic en el botón de enviar
                try:
                    send_button = WebDriverWait(driver, 30).until(
                        EC.presence_of_element_located((By.XPATH, '//span[@data-icon="send"]'))
                    )
                    send_button.click()
                    print(f"Imagen enviada a {number} haciendo clic en el botón de enviar")
                except Exception as e:
                    print(f"No se pudo encontrar el botón de enviar. Error: {e}")

                # Intentar enviar la imagen haciendo clic en el área de chat
                try:
                    actions = ActionChains(driver)
                    actions.move_to_element(message_box).click().perform()
                    message_box.send_keys(Keys.ENTER)
                    print(f"Imagen enviada a {number} haciendo clic en el área de chat")
                except Exception as e:
                    print(f"No se pudo enviar la imagen haciendo clic en el área de chat. Error: {e}")

                # Intentar enviar la imagen usando JavaScript
                try:
                    driver.execute_script('document.querySelector("span[data-icon=\'send\']").click();')
                    print(f"Imagen enviada a {number} usando JavaScript")
                except Exception as e:
                    print(f"No se pudo enviar la imagen usando JavaScript. Error: {e}")

            except Exception as e:
                print(f"No se pudo enviar la imagen a {number}. Error: {e}")

            # Espera antes de enviar el siguiente mensaje
            time.sleep(2)  # Espera de 2 segundos

        except Exception as e:
            print(f"No se pudo enviar el mensaje a {number}. Error: {e}")

# Ejecuta la función para enviar mensajes
send_messages()

# Cierra el navegador después de enviar todos los mensajes
driver.quit()
