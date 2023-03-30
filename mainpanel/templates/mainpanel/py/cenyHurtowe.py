import traceback
import xml.etree.ElementTree as ET
from urllib.request import urlopen
import os


class ProductElektro:
    def __init__(self):
        self.name = ''
        self.minimal_price = 0.0
        self.avg_price = 0.0
        self.last_price = 0.0
        self.pident = ''
        self.producer = ''
        self.pre = {'iaiext': 'http://www.iai-shop.com/developers/iof/extensions.phtml'}

    def load_product(self, xmlelement):
        self.name = xmlelement.find('description').find('name').text
        self.producer = xmlelement.find("producer").get("name")
        self.minimal_price = xmlelement.find('iaiext:price_minimal', self.pre).find('iaiext:site', self.pre).get('gross')
        self.pident = xmlelement.get("id")
        self.last_price = float(xmlelement.find('iaiext:last_purchase_price', self.pre).get('gross'))
        self.avg_price = float(xmlelement.find('iaiext:average_purchase_price', self.pre).get('gross'))

class Hurt:
    def __int__(self):
        self.srp = 0.0
        self.wholesale = 0.0

    def load(self, xml):
        self.id = xml.get('id')
        self.srp = float(xml.find('srp').get('gross'))
        self.wholesale = float(xml.find('price').get('gross'))


dopoprawy = []


def check_prices(elektr, hurt1, hurt2, hurt3, hurt4, hurtIRC, hurtKolba):
    for pel in elektr:
        if pel.last_price > pel.avg_price:
            for pro in hurt1:
                if pel.pident == pro.id:
                    if pro.wholesale < pel.last_price:
                        dopoprawy.append(str(pel.pident + ' : Cennik -Hurt1(' + str((100 - (pro.wholesale * 100) / pro.srp)) + ')- cena sprzedaży: ' + str(pro.wholesale) + ' | cena zakupu: ' + str(pel.last_price)))
                        # print(pel.pident + ' : Cennik -Hurt1(' + str((100 - (pro.wholesale * 100) / pro.srp)) + ')- cena sprzedaży: ' + str(pro.wholesale) + ' | cena zakupu: ' + str(pel.last_price))
                        break
            for pro in hurt2:
                if pel.pident == pro.id:
                    if pro.wholesale < pel.last_price:
                        dopoprawy.append(str(pel.pident + ' : Cennik -Hurt2(' + str((100 - (pro.wholesale * 100) / pro.srp)) + ')- cena sprzedaży: ' + str(pro.wholesale) + ' | cena zakupu: ' + str(pel.last_price)))
                        # print(pel.pident + ' : Cennik -Hurt2(' + str((100 - (pro.wholesale * 100) / pro.srp)) + ')- cena sprzedaży: ' + str(pro.wholesale) + ' | cena zakupu: ' + str(pel.last_price))
                        break
            for pro in hurt3:
                if pel.pident == pro.id:
                    if pro.wholesale < pel.last_price:
                        dopoprawy.append(str(pel.pident + ' : Cennik -Hurt3(' + str((100 - (pro.wholesale * 100) / pro.srp)) + ')- cena sprzedaży: ' + str(pro.wholesale) + ' | cena zakupu: ' + str(pel.last_price)))
                        # print(pel.pident + ' : Cennik -Hurt3(' + str((100 - (pro.wholesale * 100) / pro.srp)) + ')- cena sprzedaży: ' + str(pro.wholesale) + ' | cena zakupu: ' + str(pel.last_price))
                        break
            for pro in hurt4:
                if pel.pident == pro.id:
                    if pro.wholesale < pel.last_price:
                        dopoprawy.append(str(pel.pident + ' : Cennik -Hurt4(' + str((100 - (pro.wholesale * 100) / pro.srp)) + ')- cena sprzedaży: ' + str(pro.wholesale) + ' | cena zakupu: ' + str(pel.last_price)))
                        # print(pel.pident + ' : Cennik -Hurt4(' + str((100 - (pro.wholesale * 100) / pro.srp)) + ')- cena sprzedaży: ' + str(pro.wholesale) + ' | cena zakupu: ' + str(pel.last_price))
                        break
            for pro in hurtIRC:
                if pel.pident == pro.id:
                    if pro.wholesale < pel.last_price:
                        dopoprawy.append(str(pel.pident + ' : Cennik -HurtIRC(' + str((100 - (pro.wholesale * 100) / pro.srp)) + ')- cena sprzedaży: ' + str(pro.wholesale) + ' | cena zakupu: ' + str(pel.last_price)))
                        # print(pel.pident + ' : Cennik -HurtIRC(' + str((100 - (pro.wholesale * 100) / pro.srp)) + ')- cena sprzedaży: ' + str(pro.wholesale) + ' | cena zakupu: ' + str(pel.last_price))
                        break
            for pro in hurtKolba:
                if pel.pident == pro.id:
                    if pro.wholesale < pel.last_price:
                        dopoprawy.append(str(pel.pident + ' : Cennik -HurtKolba(' + str((100 - (pro.wholesale * 100) / pro.srp)) + ')- cena sprzedaży: ' + str(pro.wholesale) + ' | cena zakupu: ' + str(pel.last_price)))
                        # print(pel.pident + ' : Cennik -HurtKolba(' + str((100 - (pro.wholesale * 100) / pro.srp)) + ')- cena sprzedaży: ' + str(pro.wholesale) + ' | cena zakupu: ' + str(pel.last_price))
                        break
        else:
            for pro in hurt1:
                if pel.pident == pro.id:
                    if pro.wholesale < pel.avg_price:
                        dopoprawy.append(str(pel.pident + ' : Cennik -Hurt1(' + str((100 - (pro.wholesale * 100) / pro.srp)) + ')- cena sprzedaży: ' + str(pro.wholesale) + ' | cena zakupu: ' + str(pel.last_price)))
                        # print(pel.pident + ' : Cennik -Hurt1(' + str((100 - (pro.wholesale * 100) / pro.srp)) + ')- cena sprzedaży: ' + str(pro.wholesale) + ' | cena zakupu: ' + str(pel.last_price))
                        break
            for pro in hurt2:
                if pel.pident == pro.id:
                    if pro.wholesale < pel.avg_price:
                        dopoprawy.append(str(pel.pident + ' : Cennik -Hurt2(' + str((100 - (pro.wholesale * 100) / pro.srp)) + ')- cena sprzedaży: ' + str(pro.wholesale) + ' | cena zakupu: ' + str(pel.last_price)))
                        # print(pel.pident + ' : Cennik -Hurt2(' + str((100 - (pro.wholesale * 100) / pro.srp)) + ')- cena sprzedaży: ' + str(pro.wholesale) + ' | cena zakupu: ' + str(pel.last_price))
                        break
            for pro in hurt3:
                if pel.pident == pro.id:
                    if pro.wholesale < pel.avg_price:
                        dopoprawy.append(str(pel.pident + ' : Cennik -Hurt3(' + str((100 - (pro.wholesale * 100) / pro.srp)) + ')- cena sprzedaży: ' + str(pro.wholesale) + ' | cena zakupu: ' + str(pel.last_price)))
                        # print(pel.pident + ' : Cennik -Hurt3(' + str((100 - (pro.wholesale * 100) / pro.srp)) + ')- cena sprzedaży: ' + str(pro.wholesale) + ' | cena zakupu: ' + str(pel.last_price))
                        break
            for pro in hurt4:
                if pel.pident == pro.id:
                    if pro.wholesale < pel.avg_price:
                        dopoprawy.append(str(pel.pident + ' : Cennik -Hurt4(' + str((100 - (pro.wholesale * 100) / pro.srp)) + ')- cena sprzedaży: ' + str(pro.wholesale) + ' | cena zakupu: ' + str(pel.last_price)))
                        # print(pel.pident + ' : Cennik -Hurt4(' + str((100 - (pro.wholesale * 100) / pro.srp)) + ')- cena sprzedaży: ' + str(pro.wholesale) + ' | cena zakupu: ' + str(pel.last_price))
                        break
            for pro in hurtIRC:
                if pel.pident == pro.id:
                    if pro.wholesale < pel.avg_price:
                        dopoprawy.append(str(pel.pident + ' : Cennik -HurtIRC(' + str((100 - (pro.wholesale * 100) / pro.srp)) + ')- cena sprzedaży: ' + str(pro.wholesale) + ' | cena zakupu: ' + str(pel.last_price)))
                        # print(pel.pident + ' : Cennik -HurtIRC(' + str((100 - (pro.wholesale * 100) / pro.srp)) + ')- cena sprzedaży: ' + str(pro.wholesale) + ' | cena zakupu: ' + str(pel.last_price))
                        break
            for pro in hurtKolba:
                if pel.pident == pro.id:
                    if pro.wholesale < pel.avg_price:
                        dopoprawy.append(str(pel.pident + ' : Cennik -HurtKolba(' + str((100 - (pro.wholesale * 100) / pro.srp)) + ')- cena sprzedaży: ' + str(pro.wholesale) + ' | cena zakupu: ' + str(pel.last_price)))
                        # print(pel.pident + ' : Cennik -HurtKolba(' + str((100 - (pro.wholesale * 100) / pro.srp)) + ')- cena sprzedaży: ' + str(pro.wholesale) + ' | cena zakupu: ' + str(pel.last_price))
                        break

def check_discount(elektr, hurt1, hurt2, hurt3, hurt4, hurtIRC, hurtKolba):
    print('test')

elektro_products = []
hurt1pro = []
hurt2pro = []
hurt3pro = []
hurt4pro = []
hurtIRCpro = []
hurtKolbapro = []

d1 = False
elektro = None

try:
    ele = ET.parse('./elektroProducts1.xml')
    elektro = ele.getroot()
    d1 = True
except:
    print("zły plik")

if d1:
    try:
        fileHurt1 = urlopen(
            'https://b2b.elektromaniacy.pl/edi/export-offer.php?client=hurtowniknr1&language=pol&token=2b4b3a0bcebc70fa837391d&shop=3&type=light&format=xml&iof_3_0')
        datatowrite = fileHurt1.read()
        with open('hurt1.xml', 'wb') as f:
            f.write(datatowrite)

        fileHurt2 = urlopen(
            'https://b2b.elektromaniacy.pl/edi/export-offer.php?client=hurtowniknr2&language=pol&token=f5f9490bd7c74ff7140aa8f&shop=3&type=light&format=xml&iof_3_0')
        datatowrite = fileHurt2.read()
        with open('hurt2.xml', 'wb') as f:
            f.write(datatowrite)

        fileHurt3 = urlopen(
            'https://b2b.elektromaniacy.pl/edi/export-offer.php?client=hurtowniknr3&language=pol&token=88803e17c3a41c35ddcf1e2&shop=3&type=light&format=xml&iof_3_0')
        datatowrite = fileHurt3.read()
        with open('hurt3.xml', 'wb') as f:
            f.write(datatowrite)

        fileHurt4 = urlopen(
            'https://b2b.elektromaniacy.pl/edi/export-offer.php?client=huczto060922152655&language=pol&token=8b0b57936d18ef93b78d1e7&shop=3&type=light&format=xml&iof_3_0')
        datatowrite = fileHurt4.read()
        with open('hurt4.xml', 'wb') as f:
            f.write(datatowrite)

        fileHurtIRC = urlopen(
            'https://b2b.elektromaniacy.pl/edi/export-offer.php?client=hupito060922152854&language=pol&token=4859dd96f3ca5907783b14d&shop=3&type=light&format=xml&iof_3_0')
        datatowrite = fileHurtIRC.read()
        with open('hurtIRC.xml', 'wb') as f:
            f.write(datatowrite)

        fileHurtKolba = urlopen(
            'https://b2b.elektromaniacy.pl/edi/export-offer.php?client=hupito060922152854&language=pol&token=4859dd96f3ca5907783b14d&shop=3&type=light&format=xml&iof_3_0')
        datatowrite = fileHurtKolba.read()
        with open('hurtKolba.xml', 'wb') as f:
            f.write(datatowrite)

        xml1 = ET.parse("hurt1.xml")
        hurt1 = xml1.getroot()

        xml2 = ET.parse("hurt2.xml")
        hurt2 = xml2.getroot()

        xml3 = ET.parse("hurt3.xml")
        hurt3 = xml3.getroot()

        xml4 = ET.parse("hurt4.xml")
        hurt4 = xml4.getroot()

        xmlIRC = ET.parse("hurtIRC.xml")
        hurtIRC = xmlIRC.getroot()

        xmlKolba = ET.parse("hurtKolba.xml")
        hurtKolba = xmlKolba.getroot()

        for p in elektro.find("products").findall("product"):
            s = ProductElektro()
            s.load_product(p)
            elektro_products.append(s)

        for p in hurt1.find("products").findall("product"):
            s = Hurt()
            s.load(p)
            hurt1pro.append(s)

        for p in hurt2.find("products").findall("product"):
            s = Hurt()
            s.load(p)
            hurt2pro.append(s)

        for p in hurt3.find("products").findall("product"):
            s = Hurt()
            s.load(p)
            hurt3pro.append(s)

        for p in hurt4.find("products").findall("product"):
            s = Hurt()
            s.load(p)
            hurt4pro.append(s)

        for p in hurtIRC.find("products").findall("product"):
            s = Hurt()
            s.load(p)
            hurtIRCpro.append(s)

        for p in hurtKolba.find("products").findall("product"):
            s = Hurt()
            s.load(p)
            hurtKolbapro.append(s)

        check_prices(elektro_products, hurt1pro, hurt2pro, hurt3pro, hurt4pro, hurtIRCpro, hurtKolbapro)
        os.remove('./hurt1.xml')
        os.remove('./hurt2.xml')
        os.remove('./hurt3.xml')
        os.remove('./hurt4.xml')
        os.remove('./hurtIRC.xml')
        os.remove('./hurtKolba.xml')
        with open('./check_rabaty.txt', 'w') as out:
            out.write("Błędy w rabatach do poprawy:\n\n")

            for p in dopoprawy:
                out.write(p + "\n")
    except Exception:
        print(traceback.format_exc())