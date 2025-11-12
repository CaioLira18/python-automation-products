import pyautogui as py
from time import sleep

# 1° - Digitar Usuário 
py.click(1237,724, duration=2)
py.write('caio')
# 2° - Digitar Senha
py.click(1229,743, duration=2)
py.write('1234')
# 3° - Clicar em Entrar
py.click(1083,787)
# 4° - Extrair cada produto:
with open('produtos.txt', 'r',) as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        #	4.1 - Clicar e Digitar Produto
        py.click(954,706, duration=2)
        py.write(produto)
        #	4.2 - Clicar e digitar quantidade
        py.click(951,734, duration=2)
        py.write(quantidade)
        #	4.3 - Clicar e digitar preço
        py.click(956,772, duration=2)
        py.write(preco)
        #	4.4 - Clicar em Registrar 
        py.click(809,969, duration=1)
        sleep(1)
