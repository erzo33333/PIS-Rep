from Classes import Product, Item, Potato, Carrot, Berry

ProductList = [{'name': "Баклажан", 'date':"01.11.2025", 'amount':135, 'calories':50},
               {'name': "Фейхоа", 'date':"01.11.2025", 'amount':3, 'calories':59},
               {'name': "Огурец", 'date':"08.11.2025", 'amount':320, 'calories':15}]

PotatoList = [{'name': "Красная картошка", 'isdirty':True, 'date':"04.09.2025", 'amount':250, 'calories':70},
              {'name': "Белая картошка", 'isdirty':False, 'date':"03.09.2025", 'amount':300, 'calories':77},
              {'name': "Синяя картошка", 'isdirty':None, 'date':"22.10.2025", 'amount':50, 'calories':80}]

CarrotList = [{'name': "Анастасия", 'length':23, 'date':"30.08.2025", 'amount':140, 'calories':40},
              {'name': "Московская Зимняя", 'length':14, 'date':"17.09.2025", 'amount':100, 'calories':39},
              {'name': "Самсон", 'length':20, 'date':"11.10.2025", 'amount':97, 'calories':42}]

BerryList = [{'name': "Арбуз", 'size':37, 'date':"07.08.2025", 'amount':104},
             {'name': "Малина", 'size':1, 'date':"24.08.2025", 'amount':22},
             {'name': "Банан", 'size':20, 'date':"29.08.2025", 'amount':95}]


def Prooduct_Parsing():
    """
    Функция разделения неклассифицированных продуктов из текстового файла и вывода их в консоль
    """
    pl = ProductList
    allProducts = []
    allProductsString = "\n  Список добавленных продуктов:"

    for product in pl:
        newobj = Product(name=product['name'], date=product['date'], amount=product['amount'], calories=product['calories'])
        allProducts.append(newobj)
        allProductsString += f"\n{newobj}"

    print(allProductsString)


def Potato_Parsing():
    """
    Функция десериализации картофеля из списка словарей в объекты и вывод их в консоль
    """
    pl = PotatoList
    allPotato = []
    allPotatoString = "\n  Список добавленной картошки:"

    for potato in pl:
        newobj = Potato(name=potato['name'], isdirty=potato['isdirty'], date=potato['date'], amount=potato['amount'], calories=potato['calories'])
        allPotato.append(newobj)
        allPotatoString += f"\n{newobj}"

    print(allPotatoString)

def Carrot_Parsing():
    """
    Функция разделения моркови из текстового файла и вывода её в консоль
    """
    cl = CarrotList
    allCarrot = []
    allCarrotString = "\n  Список добавленной моркови:"

    for carrot in cl:
        newobj = Carrot(name=carrot['name'], length=carrot['length'], date=carrot['date'], amount=carrot['amount'], calories=carrot['calories'])
        allCarrot.append(newobj)
        allCarrotString += f"\n{newobj}"

    print(allCarrotString)


def Berry_Parsing():
    """
    Функция разделения ягод из текстового файла и вывода их в консоль
    """
    bl = BerryList
    allBerry = []
    allBerryString = "\n  Список добавленных ягод:"

    for berry in bl:
        newobj = Berry(name=berry['name'], size=berry['size'], date=berry['date'], amount=berry['amount'])
        allBerry.append(newobj)
        allBerryString += f"\n{newobj}"

    print(allBerryString)

Prooduct_Parsing()
Potato_Parsing()
Carrot_Parsing()
Berry_Parsing()