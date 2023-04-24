import urllib
import urllib.request

url="http://www.pudim.com.br"
try:
    print(f"Tentando acessar o site {url}")
    site=urllib.request.urlopen(url)
except:
    print("Erro ao acessar o site.")
else:
    print("Site acessado com sucesso.")
