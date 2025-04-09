import pyautogui
import time
import pandas

# Set the delay between each action
pyautogui.PAUSE = 0.5

# Opening the website for registration
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(1)

# Registering on the website
pyautogui.click(x = 946, y = 361)
pyautogui.write("guilherme.cardoso@email.com")
pyautogui.press("tab")
pyautogui.write("123")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(1)

# Import the database
tabela = pandas.read_csv("products.csv")

# Register products
for linha in tabela.index:
    pyautogui.click(x = 956, y = 242)
    code = str(tabela.loc[linha, "codigo"])
    pyautogui.write(code)

    pyautogui.press("tab")
    brand = str(tabela.loc[linha, "marca"])
    pyautogui.write(brand)

    pyautogui.press("tab")
    type = str(tabela.loc[linha, "tipo"])
    pyautogui.write(type)

    pyautogui.press("tab")
    category = str(tabela.loc[linha, "categoria"])
    pyautogui.write(category)
    
    pyautogui.press("tab")
    price = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(price)
    
    pyautogui.press("tab")
    cost = str(tabela.loc[linha, "custo"])
    pyautogui.write(cost)

    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(1000)