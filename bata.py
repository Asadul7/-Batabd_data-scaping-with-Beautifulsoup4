from bs4 import BeautifulSoup
import  requests
link_list = []
for total_link in range(1,3):
    url = 'https://www.batabd.com/collections/men'+"?page="+str(total_link)
    reponses = requests.get(url)
    soup = BeautifulSoup (reponses.content,'html.parser')
    product_link = soup.find_all('div', attrs= {"class":"product-image image-swap"})

    for element in product_link:
        var = element.find('a')['href']
        link_list.append('https://www.batabd.com'+ var)

for i in link_list:
    responses2 = requests.get(i)
    soup2 = BeautifulSoup(responses2.content,'html.parser')
    bran = soup2.find('div', attrs= {'class':"vendor-product"})
    bran_full = bran.get_text().strip()
    brand = bran_full.strip().replace("\n",'').replace(" ",'')
    product_title = soup2.find("h1", attrs= {"class":"product-title"}).get_text().strip()
    code =soup2.find('div', attrs= {"class":"sku-product"}).get_text().strip().replace("\n","").replace(" ",'')
    avl = soup2.find("div", attrs= {"class":"product-inventory"})
    avl_status = avl.get_text().strip().replace("\n",'').replace(" ","")
    protype = soup2.find("div", attrs= {"class":"product-type"}).get_text().strip().replace("\n",'').replace(" ", '')
    proprice =soup2.find("span", attrs= {"class":"price on-sale"})
    price = soup2.find("div", attrs= {"class":"prices"})
    realprice = price.find("span", attrs= {"class":"price on-sale"}).get_text().strip()
    data = [i, product_title, brand, code, protype, realprice , avl_status]

    savefile = open("newfile.txt", 'a')
    savefile.write(str(data) + "\n")
    savefile.close()
