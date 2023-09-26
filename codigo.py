#Passo a paso do projeto
#Passo 1: Entrar no sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui #para instalar, vai no seu terminal e escreva "pip install pyautogui"
import time
import pandas as pd #pip install pandas numpy openpyxl

# pyautogui.click -> clicar com o mouse
# pyoutogui.write -> escrever um texto
# pyoutogui.press-> apertar 1 tecla
# pyoutogui.hotkey -> atalho (combinação de teclas)

pyautogui.PAUSE = 0.5

# abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" #coloque seu link aqui
pyautogui.write(link)
pyautogui.press("enter")

#esperar o site carregar
time.sleep(3)

#Passo 2: Fazer login
pyautogui.click(x=1845, y=384, clicks=1) #pegue no auxiliar as coordenadas do seu mouse
pyautogui.write("seuemailaqui@gmail.com")

pyautogui.press("tab") #passar para o campo de senha
pyautogui.write("suasenhaaqui")

pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

#Passo 3: Importar a base de dados de produtos
tabela = pd.read_csv("produtos.csv")

#Passo 5: Repetir o cadastro para todos os produtos
for linha in tabela.index:

    #Passo 4: Cadastrar um produto
    pyautogui.click(x=1774, y=271, clicks=1)

    codigo = tabela.loc[linha, "codigo"]    
    
    # preencher os campos
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    
    # apertar para enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)



