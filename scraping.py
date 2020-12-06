from requests_html import HTMLSession
import csv
import json
from bs4 import BeautifulSoup

url = "https://www.zapimoveis.com.br/aluguel/imoveis/pa+belem/?pagina="
next_page = 1
session = HTMLSession()
r1 = session.get(url + str(next_page))
list_houses = BeautifulSoup(r1.content, 'html5lib')

list=list_houses.find("h1", class_="js-summary-title heading-regular heading-regular__bold align-left results__title").text.strip()[:-34]

for char in list:
    if char in ".":
        n = list.replace(char,'')
num = int(n)
print(num)
if num % 24 == 0:
    pag = num/24
    print(pag)
elif num % 24 != 0:
    pag = int(num/24) + 1
    print(pag)



f = open("data8.csv", "w", newline='')
    
writer = csv.writer(f)
writer.writerow(
    ["id", "Categoria", "Cidade", "Estado", "Aluguel", "Condominio", "Valor total", "IPTU", "Preço de venda", "CEP", "Bairro",
     "Rua", "Numero de fotos", "Numero", "Area", "Quartos", "Suites", "Estacionamento",
     "Banheiros", "Andar",
     "Tipo", "Data"])
for i in range(int(pag)):
    print(url+str(next_page))
  
    soup = BeautifulSoup(r1.text, 'html.parser')
    #print(soup)
    all_scripts = list_houses.findAll("script")[5].text.strip()[25:-122]
    all_scripts2 = list_houses.findAll("script")[5]
    print(all_scripts2)

    #print(list_houses)
    data = json.loads(all_scripts)

    for item in data['results']['listings']:

        aluguel = item['listing']['pricingInfo']['price']
        for char in aluguel:
            if char in "R$":
                aluguel = aluguel.replace(char, '')
        iptu = item['listing']['pricingInfo']['yearlyIptu']
        for char in iptu:
            if char in "R$":
                iptu = iptu.replace(char, '')
        if iptu == "":
            iptu = "NI"
        try:
            pics = len(item['listing']['images'])
        except Exception as error:
            pics = 0
        rua = item['listing']['address']['street']
        if rua == "":
            rua = "NI"
        estado = item['listing']['address']['stateAcronym']
        if estado == "":
            estado = "NI"
        cep = item['listing']['address']['zipCode']
        if cep == "":
            cep = "NI"
        bairro = item['listing']['address']['neighborhood']
        if bairro == "":
            bairro = "NI"
        cond = item['listing']['pricingInfo']['monthlyCondoFee']
        for char in cond:
            if char in "R$":
                cond = cond.replace(char, '')
        total = item['listing']['pricingInfo']['rentalTotalPrice']
        for char in total:
            if char in "R$":
                total = total.replace(char, '')
        if cond == "":
            cond = "NI"
            total = aluguel

        venda = item['listing']['pricingInfo']['salePrice']
        for char in venda:
            if char in "R$":
                venda = venda.replace(char, '')
        if venda == "":
            venda = "NI"
        num = item['listing']['address']['streetNumber']
        if num == "":
            num = "NI"
        try:
            area = item['listing']['usableAreas'][0]
        except Exception as error:
            area = 0
        try:
            quartos = item['listing']['bedrooms'][0]
        except Exception as error:
            quartos = 0
        try:
            suites = item['listing']['suites'][0]
        except Exception as error:
            suites = 0
        try:
            Estacionamento = item['listing']['parkingSpaces'][0]
        except Exception as error2:
            Estacionamento = 0
        try:
            banheiros = item['listing']['bathrooms'][0]
        except Exception as error2:
            banheiros = 0
        try:
            andar = item['listing']['unitFloor']
        except Exception as error2:
            andar = 0
        try:
            tipo = item['listing']['usageTypes'][0]
        except Exception as error2:
            tipo = "NAO DEFINIDO"
        writer.writerow([item['listing']['id'],
                         item['listing']['unitTypes'][0],
                         item['listing']['address']['city'],
                         estado,
                         aluguel,
                         cond,
                         total,
                         iptu,
                         venda,
                         cep,
                         bairro,
                         rua,
                         pics,
                         num,  
                         area,
                         quartos,
                         suites,  
                         Estacionamento,
                         banheiros,
                         andar,
                         tipo,
                         item['listing']['createdAt']])
    next_page += 1

