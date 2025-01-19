
import pyautogui
import time


pyautogui.PAUSE = 1  # comando para controla a velocidade dos comandos

# Abrir o Sistema  da empresa

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

tabela = pd.read_csv('products.csv')
print(tabela)



    


# Passo 4: Cadastrar um produto



for linha in tabela.index:
        
        

    pyautogui.click(x=414, y=255)

       
    #Codigo
        
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab") 

    #Marca 
        
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab") 

        # Tipo
        
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #Categoria
    
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")  
    
        
    #Preço unitário 
         
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab") 
    
    #Custo do produto
     
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab") 

    #Observação
        
    obs = str(tabela.loc[linha, "obs"]) 
    
    if obs != "nan":  
        pyautogui.write(obs)
        
    pyautogui.press("tab")
    
    
    pyautogui.press("enter") #  aperta o botao enviar
    
    # Descer para ver a tabela preenchida
    
    pyautogui.scroll(-100000)
     
     
    time.sleep(3)
    
    # numéro positivo igual a scroll para cima
    # numéro negativo igual a scroll para baixo
    
    # depois sobe para volta a preencer 

    pyautogui.scroll(100000)
3  
    
    # passo 5 : Repitir até que acabe todos os produtos









