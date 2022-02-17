from bs4 import BeautifulSoup
import requests

# Site que será coletado
site = "http://www.pudim.com.br/"

# Coleta os dados do site
html = requests.get(site)
print(html.text)

# Site que será coletado
site = "http://www.pudim.com.br/"

# Coleta os dados do site
html = requests.get(site).content

# Formatando os dados
dados = BeautifulSoup(html, 'html.parser')
print(dados.prettify())

# Busca por tag HTML
busca_por_tag = dados.find("TAG_BUSCADA")

# Busca por id
busca_por_id = dados.find(id="ABC")

# Busca por class
busca_por_class = dados.find(class_="XYZ")

# Buscando todos os elementos
busca_tudo = dados.find_all("div")

# Site que será coletado
site = "http://www.pudim.com.br/"

# Coleta os dados do site
html = requests.get(site).content

# Formatando os dados
dados = BeautifulSoup(html, 'html.parser')

# Coletando a div que armazena o email
email = dados.find("div", class_="email")
print(email.prettify())

# Site que será coletado
site = "http://www.pudim.com.br/"

# Coleta os dados do site
html = requests.get(site).content

# Formatando os dados
dados = BeautifulSoup(html, 'html.parser')


# coletando a class email
email = dados.find("div", class_="email")

# coletando a tag dentro da div email
link = email.find("a")
print("1", link)  

# coletando apenas o texto
print("2", link.text)

# coletando o endereço do link
print("3", link.attrs['href'])
