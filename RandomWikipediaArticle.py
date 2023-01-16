#importando bibliotecas e suas respectivas funcoes

import requests
from bs4 import BeautifulSoup
import webbrowser

while True:
    #get_link funcao abaixo:
    
    url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(url.content, "html.parser")
    title = soup.find(class_="firstHeading").text

    print(f"\n\n{title} \n...Quer ler o artigo ?...\n[s]SIM\n[n]NAO\n[e]SAIR")
    ans = input("").lower()

    if ans == "s" or ans == 'S':
        url = "https://en.wikipedia.org/wiki/%s" % title
        webbrowser.open(url)
        break
    elif ans == "n" or ans == 'N':
        print("...Executando o código novamente...")
        continue
    elif ans == 'e' or ans == 'E':
        exit()
    else:
        print("...Escolha errada...")
        break