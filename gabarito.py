
import pyautogui
import time





pyautogui.PAUSE = 1  # comando para controla a velocidade dos comandos

# Abrir o Sistema da empresa

#https: //dlp.hashtagtreinamentos.com/python/intensivao/login

#pyautogui.hotkey passa varias chaves
#pyautogui.write ler um texto
#pyautogui.press clica 


# Passo 1: Entrar no sistema da empresa 




pyautogui.press("win") # Abri a janela do windows

pyautogui.write('Chorme') # Busca o Chorme 

pyautogui.press("enter")  # Aperta o enter nele

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

pyautogui.press("enter")  # Aperta o enter nele



# pedir pro computador esperar 3 segundos

time.sleep(3)



# Passo 2: Fazer login


pyautogui.click(x=358, y=384) # clica dentro do campo email
pyautogui.write("lignelli77@gmail.com")


pyautogui.press("tab") # passa para o botão senha 
pyautogui.write("fRh5gpxq4u#Nt*y")

pyautogui.press("tab") # passa para o botão logar
pyautogui.press("enter")



# Passo 3: Importar a base de produtos pra cadastrar

# instalação da biblioteca pandas junto com o openpyxl (para ler arquivos do excel)
# criando uma variavel  tabela


import pandas as pd 

tabela = pd.read_csv('produtos.csv')


print(tabela)
    




# Passo 4: Cadastrar um produto

pyautogui.click(x=414, y=255)

# Codigo

pyautogui.write("MOLO000251")
pyautogui.press("tab") 

# Marca 

pyautogui.write("Logitech")
pyautogui.press("tab") 

#Produto

pyautogui.write("Mouse")
pyautogui.press("tab") 

#Categoria

pyautogui.write("1")
pyautogui.press("tab") 

# Preço unitario

pyautogui.write("25.95")
pyautogui.press("tab") 

# Custo do produto

pyautogui.write("6.50")
pyautogui.press("tab") 

# Observação

pyautogui.write("")
pyautogui.press("tab")
pyautogui.press("enter")










