#anotar o passo a passo do  de como ira ocorrer o funionamento da automação
# passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pip install pyautogui
import pyautogui
import time 

pyautogui.PAUSE =0.5

# abrir o navegador (chrome)
pyautogui.press("Win") # Pressiona 1 tecla do teclado
pyautogui.write("chrome")# Escreve chrome  
pyautogui.press("enter")# pressiona 1 tecla enter do teclado

#entrar no site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)#Escreve link
pyautogui.press("enter") # pressiona enter

# dar uma pausa um pouco maior (3 sugundos ) 
time.sleep(3)

# passo 2:Fazer login
pyautogui.click(x=488, y=411)
pyautogui.write("testepython@gmail.com")

#escrever a senha
pyautogui.press("tab")# passa pro campo de senha
pyautogui.write("123456")

# Entra no sistema
pyautogui.click(x=684, y=578)
#pyautogui.press("enter")# esse é melhor
time.sleep(2)


# passo 3:Importar a base de dados
#pip install pandas numpy openpyxl
import pandas
tabela = pandas.read_csv("produtos.csv")

# Passo 4: Cadastrar 1 produto
# Para cada linha da minha tabela
for linha in tabela.index:
    # clicar no 1° campo
    pyautogui.click(x=559, y=292)
    #codigo do produto
    codigo=tabela.loc[linha, "codigo" ]
    pyautogui.write(tabela.loc[linha, "codigo" ])
    pyautogui.press("tab")
    #marca
    pyautogui.write(tabela.loc[linha, "marca" ])
    pyautogui.press("tab")
    #tipo
    pyautogui.write(tabela.loc[linha, "tipo" ])
    pyautogui.press("tab")
    # categoria
    pyautogui.write(tabela.loc[linha, "categoria" ])
    pyautogui.press("tab")
    # preco
    pyautogui.write(tabela.loc[linha,"preco_unitario"])
    pyautogui.press("tab")
    # custo
    pyautogui.write(tabela.loc[linha, "custo" ])
    pyautogui.press("tab")
    # obs
    pyautogui.write(tabela.loc[linha, "obs" ])
    pyautogui.press("tab")
    #enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)

# Passo 5: Repetir o processo de cadastro até acabar a base de dados