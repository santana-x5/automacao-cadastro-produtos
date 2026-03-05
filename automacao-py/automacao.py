import pyautogui
import pandas
import time 

pyautogui.PAUSE = 1
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("Win")
pyautogui.write("Chrome")
time.sleep(2)
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
pyautogui.click(x=1207, y=409)
pyautogui.write("seu_email@exemplo.com")
pyautogui.press("tab")
pyautogui.write("sua_senha_segura")
pyautogui.press("tab")
pyautogui.press("enter")

tabela = pandas.read_csv("produtos.csv")
for linha in tabela.index:
   
    pyautogui.click(x=1063, y=294)   

    codigo = tabela.loc[linha, "codigo"] 

    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"] 
    
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"] 
    
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    categoria = tabela.loc[linha, "categoria"] 

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    preco_unitario = tabela.loc[linha, "preco_unitario"] 

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    custo = tabela.loc[linha, "custo"] 
    
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"] 
    
    obs = tabela.loc[linha, "obs"]
    if obs != "nan":    
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") 
    pyautogui.scroll(5000)
