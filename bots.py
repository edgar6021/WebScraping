import pyautogui
import time

# Abre el navegador web
pyautogui.press('win')
pyautogui.typewrite('chrome\n')
time.sleep(2)

# Navega a una página web específica
pyautogui.typewrite('https://www.google.com\n')
time.sleep(2)

# Busca un término de búsqueda en Google
pyautogui.click(100, 100)  # Hace clic en el campo de búsqueda
pyautogui.typewrite('python\n')  # Escribe "python" en el campo de búsqueda
time.sleep(2)
pyautogui.press('enter')  # Presiona la tecla "Enter" para realizar la búsqueda