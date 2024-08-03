import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class WhatsAppBot:
    def __init__(self):
        chromedriver_autoinstaller.install()
        
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def open_whatsapp_web(self):
        self.driver.get("https://web.whatsapp.com/")
        input("Escanea el código QR y presiona Enter para continuar...")

    def scrape_group_numbers(self, group_name, output_file):
        try:
            # Buscar el grupo por nombre
            search_box = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
            )
            search_box.click()
            search_box.send_keys(group_name)
            search_box.send_keys(Keys.ENTER)

            # Abrir información del grupo
            group_info_button = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//div[@title="Información del grupo"]'))
            )
            group_info_button.click()

            # Abrir lista de participantes
            participants_button = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//div[@title="Participantes"]'))
            )
            participants_button.click()

            # Esperar a que se cargue la lista de participantes
            time.sleep(2)

            participants = WebDriverWait(self.driver, 30).until(
                EC.presence_of_all_elements_located((By.XPATH, '//div[@class="_2nY1w"]'))
            )

            numbers = []
            for participant in participants:
                actions = ActionChains(self.driver)
                actions.move_to_element(participant).perform()
                participant.click()
                
                time.sleep(1)  # Espera para cargar la información del contacto

                try:
                    number_element = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//span[@class="_3C3fA"]'))
                    )
                    number = number_element.text
                    numbers.append(number)
                except Exception as e:
                    print(f"Error al obtener el número: {e}")

                self.driver.back()  # Regresar a la lista de participantes
                time.sleep(1)

            # Guardar los números en un archivo
            with open(output_file, 'w') as f:
                for number in numbers:
                    f.write(number + "\n")

            print(f"Números guardados en {output_file}")

        except Exception as e:
            print(f"Error al obtener los números del grupo: {e}")

    def quit(self):
        self.driver.quit()

if __name__ == "__main__":
    bot = WhatsAppBot()
    bot.open_whatsapp_web()
    
    group_name = "6to B 😻🤙🏼 (Errrr B)"  # Nombre del grupo
    output_file = "numeros_grupo.txt"  # Archivo donde se guardarán los números

    bot.scrape_group_numbers(group_name, output_file)
    bot.quit()
